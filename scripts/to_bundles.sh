#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/Users/zhichengx/Development/phrygiangates.github.io"
CONTENT_DIR="$REPO_DIR/content"

# 只处理 content 顶层的 .md 文件，排除 index.md
find "$CONTENT_DIR" -maxdepth 1 -type f -name '*.md' ! -name 'index.md' -print0 |
while IFS= read -r -d '' file; do
  base="$(basename "$file")"          # e.g. spin.md
  name="${base%.*}"                   # e.g. spin
  dest_dir="$CONTENT_DIR/$name"
  dest_file="$dest_dir/index.md"

  # 若目标已存在 index.md，则跳过
  if [ -e "$dest_file" ]; then
    echo "Skip: $base -> $name/index.md already exists"
    continue
  fi

  mkdir -p "$dest_dir"

  # 若在 git 仓库内，优先用 git mv 保留历史
  if command -v git >/dev/null 2>&1 && git -C "$REPO_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    rel_src="${file#"$REPO_DIR/"}"
    rel_dest="${dest_file#"$REPO_DIR/"}"
    git -C "$REPO_DIR" mv "$rel_src" "$rel_dest"
  else
    mv "$file" "$dest_file"
  fi

  echo "Moved: $base -> $name/index.md"
done