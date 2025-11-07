+++
date = '2025-11-07T23:00:00+08:00'
title = 'Automated Transcription and Translation'
tags = ['AI']
categories = ["Technology"]
+++

Today, on a whim, I wanted to study various courses in English, like biology and geography. There are quite a few The Great Courses offerings on Bilibili, but based on my previous viewing experience, these courses often use a lot of terminology; just listening—even with English subtitles—I still can’t fully understand them. So I figured I’d add bilingual Chinese–English subtitles to these course videos and then watch them.

The technical plan is straightforward: use `yutto` to download videos from Bilibili, `ffmpeg` to extract audio from the videos, `whisper.cpp` to transcribe the audio into SRT subtitles (by the way, I’m using Apple M3 Silicon), and finally use the DeepSeek API to translate the SRT subtitles.

After implementing it, I found a few issues, essentially all caused by LLM hallucinations.

1.  Whisper’s transcription sometimes produces repeated, meaningless sentences, even when the audio is very clear. This may be related to the audio sampling format, such as the number of channels, sample rate, etc. I’m using the `large-v3` model, but I’ve heard the `v2` model might be more stable in such cases.
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

2.  To let DeepSeek leverage context, I chose to “feed” it multiple lines of subtitles at once, hoping it would translate them line by line according to the input format and keep the number of output lines aligned with the input. However, at least in my experience, DeepSeek finds it hard to do this perfectly. Later, I forced it to output JSON format and add line numbers, and found that this can make the total number of translated lines equal the total number of input lines, but it still can’t guarantee a one-to-one correspondence—misalignments sometimes occur. I initially input 50 lines at a time, but found that once misaligned, a long stretch of the video would have mismatched bilingual subtitles, which was unpleasant to watch. So I reduced the batch size to 10 lines at a time; this way, even if misalignment occurs, the error won’t persist for too long.

Overall, DeepSeek’s performance on the translation part was better than I expected, and the error rate is perfectly acceptable. The main issue lies in the transcription, whose instability was somewhat unexpected.
