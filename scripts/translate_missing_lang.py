#!/usr/bin/env python3
"""
Translate posts to the missing language using Azure OpenAI.

Behavior:
- For each directory under content/posts/** containing index.md and/or index.zh.md:
  - If both exist: skip.
  - If only English exists (index.md): create index.zh.md via EN->ZH translation.
  - If only Chinese exists (index.zh.md): create index.md via ZH->EN translation.

Constraints for the model (enforced via prompt and masking):
- In front matter (TOML/YAML), translate ONLY the title value; keep all other keys/values unchanged.
- In the body, DO NOT translate anything inside math delimiters: \( ... \), \[ ... \], $$ ... $$.
- Also DO NOT translate code blocks (``` ... ```).
- Preserve Markdown structure and KaTeX delimiters verbatim.

Environment variables required for Azure OpenAI:
- AZURE_OPENAI_ENDPOINT https://llm-proxy.perflab.nvidia.com
- AZURE_OPENAI_API_KEY (your API key)
- AZURE_OPENAI_DEPLOYMENT gpt-5-20250807 (the deployment name, e.g., gpt-4o-mini) 
- Optionally: AZURE_OPENAI_API_VERSION (default: 2024-02-15-preview)

Usage:
  python scripts/translate_missing_lang.py

This script is idempotent and will skip directories that already contain both languages.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


# ------------------------------ Azure OpenAI ------------------------------

def get_azure_client():
    """Return an Azure OpenAI client instance using environment variables."""
    # The unified OpenAI SDK supports Azure via AzureOpenAI class
    try:
        from openai import AzureOpenAI  # type: ignore
    except Exception as exc:  # pragma: no cover - import-time aid
        raise RuntimeError(
            "Missing dependency: pip install openai>=1.0.0"
        ) from exc

    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT", "https://llm-proxy.perflab.nvidia.com")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2025-02-01-preview")
    if not endpoint or not api_key:
        raise RuntimeError(
            "AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY must be set as environment variables."
        )
    return AzureOpenAI(azure_endpoint=endpoint, api_key=api_key, api_version=api_version)


def chat_complete(client, model: str, system_prompt: str, user_content: str) -> str:
    """Call Azure OpenAI Chat Completions and return the text."""
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        temperature=0.1,
        top_p=1.0,
    )
    text = resp.choices[0].message.content or ""
    return text.strip()


# ------------------------------ Utilities ------------------------------

FRONT_MATTER_DELIMS = ("+++", "---")


@dataclass
class FrontMatter:
    raw: str
    title_value: str | None
    title_quote: str | None  # ' or " or None
    is_toml: bool


def split_front_matter(file_text: str) -> Tuple[FrontMatter, str]:
    """Split front matter (TOML +++ or YAML ---) from body.

    Returns (FrontMatter, body_text). If no front matter, returns empty FM.
    """
    lines = file_text.splitlines()
    if not lines:
        return FrontMatter(raw="", title_value=None, title_quote=None, is_toml=True), ""

    if lines[0].strip() not in FRONT_MATTER_DELIMS:
        # No recognizable front matter
        return FrontMatter(raw="", title_value=None, title_quote=None, is_toml=True), file_text

    delim = lines[0].strip()
    closing_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == delim:
            closing_index = i
            break
    if closing_index is None:
        # Malformed front matter; treat as body
        return FrontMatter(raw="", title_value=None, title_quote=None, is_toml=(delim == "+++")), file_text

    fm_text = "\n".join(lines[1:closing_index])
    body_text = "\n".join(lines[closing_index + 1 :])

    # Extract title line without parsing full TOML/YAML (to preserve formatting/ordering)
    # Support: title = '...' or title = "..." or title: ... (YAML)
    title_value = None
    title_quote = None
    # Try TOML pattern first
    m = re.search(r"^\s*title\s*=\s*(['\"])(.*?)\1\s*$", fm_text, flags=re.MULTILINE)
    if m:
        title_quote = m.group(1)
        title_value = m.group(2)
    else:
        # YAML pattern
        my = re.search(r"^\s*title\s*:\s*(.*)\s*$", fm_text, flags=re.MULTILINE)
        if my:
            # Capture raw (no quotes handling here)
            v = my.group(1).strip()
            # Remove surrounding quotes if any
            if (len(v) >= 2) and v[0] == v[-1] and v[0] in ('"', "'"):
                title_quote = v[0]
                v = v[1:-1]
            else:
                title_quote = '"'
            title_value = v

    return FrontMatter(raw=fm_text, title_value=title_value, title_quote=title_quote, is_toml=(delim == "+++")), body_text


PLACEHOLDER_PREFIX = "[[__PLACEHOLDER_"


def mask_segments(text: str) -> Tuple[str, Dict[str, str]]:
    """Mask code blocks and math segments with non-translatable placeholders.

    Order matters to avoid nested matches. We mask:
    1) Fenced code blocks: ``` ... ``` (greedy across lines)
    2) Math blocks: $$ ... $$
    3) LaTeX block math: \[ ... \]
    4) LaTeX inline math: \( ... \)
    """
    mapping: Dict[str, str] = {}
    out = text

    def _mask(pattern: str, s: str) -> str:
        nonlocal mapping
        idx = 0
        while True:
            m = re.search(pattern, s, flags=re.DOTALL)
            if not m:
                return s
            idx += 1
            placeholder = f"{PLACEHOLDER_PREFIX}{len(mapping)}__]]"
            mapping[placeholder] = m.group(0)
            s = s[: m.start()] + placeholder + s[m.end() :]
        # unreachable

    # Apply in order
    out = _mask(r"```[\s\S]*?```", out)
    out = _mask(r"\$\$[\s\S]*?\$\$", out)
    out = _mask(r"\\\[[\s\S]*?\\\]", out)
    out = _mask(r"\\\([\s\S]*?\\\)", out)
    return out, mapping


def restore_segments(text: str, mapping: Dict[str, str]) -> str:
    out = text
    # Replace in insertion order
    for key, value in mapping.items():
        out = out.replace(key, value)
    return out


def build_system_prompt(target_lang: str) -> str:
    direction = "English to Simplified Chinese (zh-Hans)" if target_lang == "zh" else "Chinese to English"
    return (
        "You are a precise technical translator. Translate "
        f"{direction}.\n"
        "Rules:\n"
        "- Preserve Markdown structure exactly.\n"
        "- Do NOT translate anything inside math delimiters: \\( ... \\), \\[ ... \\], $$ ... $$.\n"
        "- Do NOT translate code blocks (``` ... ```).\n"
        "- Keep KaTeX/LaTeX syntax unchanged.\n"
        "- Output ONLY the translated body text provided (no explanations).\n"
    )


def build_title_prompt(target_lang: str) -> str:
    direction = "English to Simplified Chinese (zh-Hans)" if target_lang == "zh" else "Chinese to English"
    return (
        "You translate TITLES only.\n"
        f"Translate the given title from {direction}. Output ONLY the translated title text without quotes."  # noqa: E501
    )


def translate_text(client, model: str, text: str, target_lang: str) -> str:
    masked, mapping = mask_segments(text)
    translated = chat_complete(client, model, build_system_prompt(target_lang), masked)
    return restore_segments(translated, mapping)


def translate_title(client, model: str, title: str, target_lang: str) -> str:
    return chat_complete(client, model, build_title_prompt(target_lang), title)


def reconstruct_file(fm: FrontMatter, new_title: str | None, body: str, fm_delim: str) -> str:
    # Replace title line inside fm.raw while preserving quotes and other fields
    fm_text = fm.raw
    if new_title is not None and fm.title_value is not None:
        q = fm.title_quote or '"'
        # Replace only the first title occurrence to be safe
        pattern = re.compile(r"^(\s*title\s*=\s*)['\"].*?['\"](\s*)$", re.MULTILINE)
        if pattern.search(fm_text):
            fm_text = pattern.sub(rf"\1{q}{new_title}{q}\2", fm_text, count=1)
        else:
            # YAML style fallback
            pattern_yaml = re.compile(r"^(\s*title\s*:\s*).*$", re.MULTILINE)
            fm_text = pattern_yaml.sub(rf"\1{new_title}", fm_text, count=1)

    return f"{fm_delim}\n{fm_text}\n{fm_delim}\n\n{body.strip()}\n"


def process_directory(client, model: str, dir_path: Path) -> None:
    files = {p.name: p for p in dir_path.glob("index*.md")}
    has_en = "index.md" in files
    has_zh = "index.zh.md" in files

    if has_en and has_zh:
        print(f"SKIP (both present): {dir_path}")
        return
    if not has_en and not has_zh:
        return

    if has_en:
        src = files["index.md"]
        target_lang = "zh"
        dest = dir_path / "index.zh.md"
        fm_delim = "+++"
    else:
        src = files["index.zh.md"]
        target_lang = "en"
        dest = dir_path / "index.md"
        fm_delim = "+++"

    text = src.read_text(encoding="utf-8")
    # Determine front matter delimiter (first line)
    first_line = text.splitlines()[0] if text else ""
    if first_line.strip() in FRONT_MATTER_DELIMS:
        fm_delim = first_line.strip()

    fm, body = split_front_matter(text)

    # Translate title (only value) and body separately
    new_title = translate_title(client, model, fm.title_value or "", target_lang) if fm.title_value else None
    translated_body = translate_text(client, model, body, target_lang)

    new_file_text = reconstruct_file(fm, new_title, translated_body, fm_delim=fm_delim)

    dest.write_text(new_file_text, encoding="utf-8")
    print(f"WROTE: {dest}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate posts to the missing language using Azure OpenAI")
    parser.add_argument("--content-root", default=str(Path(__file__).resolve().parents[1] / "content" / "posts"),
                        help="Root directory of posts (default: content/posts)")
    parser.add_argument("--only", default=None, help="Process only this single post directory name (slug)")
    parser.add_argument("--model", default=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-5-20250807"),
                        help="Azure OpenAI deployment name to use")
    args = parser.parse_args()

    posts_dir = Path(args.content_root)
    if not posts_dir.exists():
        print(f"Directory not found: {posts_dir}", file=sys.stderr)
        sys.exit(1)

    client = get_azure_client()

    # Iterate only immediate child directories of posts (each post bundle)
    for entry in sorted(posts_dir.iterdir()):
        if not entry.is_dir():
            continue
        if args.only and entry.name != args.only:
            continue
        process_directory(client, args.model, entry)


if __name__ == "__main__":
    main()


