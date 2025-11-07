+++
date = '2025-11-03T12:00:00+08:00'
title = 'Thoughts on Doing Business'
tags = ['Random Thoughts']
categories = ["Finance"]
+++

This morning at work I wanted to listen to an audiobook, so I searched online and found this [【"Madness and Civilization" Michel Foucault【Audiobook | Synchronized Text】】](https://www.bilibili.com/video/BV1vYMxzNELd/?share_source=copy_web&vd_source=f2844617a59fe50f738536977e8c51b8)

I think what he’s done is very appropriate. For sociology- and philosophy-related books, just reading often feels dull and leads to giving up; just listening often means forgetting the context, zoning out, and not knowing what’s being said. These kinds of books are best suited for audiobooks with synchronized text. So I started thinking: how did he make an audiobook like this? What AI tools did he use? How did he align the text and audio precisely? I dug through r/localllama for quite a while. Open-source solutions are usually very complicated: first convert the ebook into audio and timestamped subtitles, then synchronize the subtitles with the audio to produce a video.

I stared at this uploader’s audiobook video for a long time and felt something was off. It doesn’t look at all like it was made with the pipeline above. The scrolling and highlighting of the subtitles are clearly very difficult; if he had done it himself, he probably wouldn’t have chosen such a high-difficulty production method, but would have gone with a video that simply plays ASS or SRT subtitles burned in.

I asked AI again how to achieve simultaneous playback of text and audio when making an audiobook, tracked down Speechify, tried it, and found Speechify’s effect was identical to the uploader’s video—it suddenly clicked. In fact, I already knew about Speechify; I just never thought of using it to make videos like this.

Speechify costs about 1,000 RMB per year. This uploader has around 20,000 followers from making philosophy audiobooks; I estimate there’s a high probability his monthly income from Bilibili exceeds 100 RMB, which can easily cover Speechify’s cost. And in reality, I think he hardly needs to do anything (other than opening a small window on his computer and recording the screen) to make money. Yet at the outset I was actually thinking about how to build an entire complex toolchain just to earn this money.

How did he discover this business opportunity? My guess is that he himself needed audiobooks to better understand these difficult philosophy books, and after using Speechify to read, he realized this was something many people needed, so he went with the flow and turned it into videos and posted them online.

My current side hustle is actually being approached from the same angle; the takeaway for me is to estimate the time cost and see whether there’s a more direct way to implement it.
