+++
date = '2025-11-07T23:00:00+08:00'
title = '自动化语音转录与翻译'
tags = ['AI']
categories = ["Technology"]
+++

今天心血来潮，想用英语学习各种各样的课程，比如生物、地理这些。Bilibili 上有不少 The Great Courses 的课程，但我之前的观看体验是，这些课程里经常用到很多术语，直接听，哪怕配有英语字幕，也还是不能完全听懂。所以，我就想给这些课程视频配上中英文字幕再看。

技术方案很直接：用 `yutto` 从 B 站上下载视频，`ffmpeg` 从视频中提取音频，`whisper.cpp` 从音频转录生成 SRT 字幕（顺便提一下，我用的是 Apple M3 Silicon），最后用 DeepSeek API 翻译 SRT 字幕。

实现后发现了一些问题，本质上都是大模型的幻觉导致的。

1.  Whisper 转录有时会出现重复的无意义语句，即使音频很清晰。这可能和音频的采样格式有关，比如声道数、采样率等。我用的是 `large-v3` 模型，但听说 `v2` 模型在这种情况下可能表现得更稳定一些。
    ```
    272
    00:23:23,360 --> 00:23:27,420
    Now the caldera has a crater at the bottom of the volcano. Now the caldera has a crater

    273
    00:23:27,420 --> 00:23:31,580
    at the bottom of the volcano. Now the caldera has a crater at the bottom of the volcano.

    274
    00:23:31,580 --> 00:23:35,180
    Now the caldera has a crater at the bottom of the volcano. Now the caldera has a crater

    275
    00:23:35,180 --> 00:23:37,440
    at the bottom of the volcano. Now the caldera has a crater at the bottom of the volcano.
    ```

2.  为了让 DeepSeek 能结合上下文进行分析，我选择将多行字幕一同“喂”给它，希望它能根据输入格式，一行一行地翻译出来，并且输出的行数能与输入对齐。然而，至少 DeepSeek 很难完美做到这一点。后来，我强制它输出 JSON 格式，并为每行编号，发现这样可以让翻译结果的总行数与输入总行数相等，但仍然无法保证每行都一一对应，有时会出现错位。我一开始一次性输入 50 行，但发现一旦错位，就会导致很长一段视频的中英文字幕对不上，看着很难受。所以，我把批处理大小调整为一次 10 行，这样即使出现错位，错误也不会持续太久。

总的来说，翻译部分用 DeepSeek 的效果比我想象的要好，错误率完全可以接受。主要问题是在转录的时候，其不稳定性有些出乎意料。