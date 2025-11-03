+++
date = '2025-11-03T12:00:00+08:00'
title = 'Thoughts on Do Business'
tags = ['Random Thoughts']
categories = ["Finance"]
+++

This morning at work I wanted to listen to an audiobook, so I searched online and found this [【“Madness and Civilization” Michel Foucault【Audiobook | Synchronized Original Text】】](https://www.bilibili.com/video/BV1vYMxzNELd/?share_source=copy_web&vd_source=f2844617a59fe50f738536977e8c51b8)

I think he did it very well. For books related to sociology and philosophy, just reading often feels tedious and leads to abandoning the book; just listening often makes you forget the context, zone out, and lose the thread. Books like these are best suited to audiobooks with synchronized original text. So I started thinking about how he made such an audiobook, what AI tools he used, and how he aligned the text and audio exactly, and I rummaged through r/localllama for a long time. Open-source solutions are usually very complex: first convert the e-book into audio and time-stamped subtitles, then synchronize the subtitles with the audio and play them together to make a video.

I stared at the audiobook video this uploader made for quite a while and felt something was off. It didn’t look at all like it was made with the above pipeline. The scrolling and highlighting of subtitles is clearly very difficult; if he did it himself, he probably wouldn’t choose such a high-difficulty production method, but would instead make the kind of video that just plays ass or srt subtitles burned in.

Then I asked AI how to achieve simultaneous playback of text and audio when making an audiobook, and I traced it to Speechify. I tried it, and Speechify’s effect is exactly the same as in this uploader’s video—it all clicked. In fact, I’d known about Speechify for a long time; I just never thought of using it to make videos like this.

Speechify’s annual fee is about 1,000 RMB. This uploader, who makes philosophy-related audiobook videos, has about 20,000 followers; I estimate the probability that his monthly income from Bilibili exceeds 100 RMB is quite high, which can readily cover Speechify’s cost. And in fact, I think he barely needs to do anything (other than opening a small window on his computer and recording the screen) to make money. Yet at the start I was actually thinking about how to build an entire complex toolchain just to earn this money.

I think this is a very real story—about how to make money.
