+++
date = '2026-06-18T19:46:22+08:00'
title = '费米子与狄拉克方程'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

对 boson 来说，如果一个粒子在位置 \(x\)，另一个粒子在位置 \(y\)，那么交换这两个位置标签不会改变态：
\[
|x,y\rangle=|y,x\rangle.
\]
这里先把 \(x,y\) 理解成 position label，也就是一个粒子在 \(x\)，另一个粒子在 \(y\)。

从量子场论的角度看，这两个态可以由 creation field operator 作用在真空态上得到：
\[
|x,y\rangle=\Psi^\dagger(x)\Psi^\dagger(y)|0\rangle,
\]
\[
|y,x\rangle=\Psi^\dagger(y)\Psi^\dagger(x)|0\rangle.
\]
对 boson 来说，creation field operators commute with each other：
\[
[\Psi^\dagger(x),\Psi^\dagger(y)]=0.
\]
因此
\[
\Psi^\dagger(x)\Psi^\dagger(y)|0\rangle
=\Psi^\dagger(y)\Psi^\dagger(x)|0\rangle,
\]
也就是
\[
|x,y\rangle=|y,x\rangle.
\]

对 fermion 来说，交换两个相同费米子会多出一个负号：
\[
|x,y\rangle=-|y,x\rangle.
\]
在 field operator 的语言里，这来自 fermion creation field operators 的 anti-commutation relation：
\[
\{\Psi^\dagger(x),\Psi^\dagger(y)\}=0.
\]
也就是说
\[
\Psi^\dagger(x)\Psi^\dagger(y)
=-\Psi^\dagger(y)\Psi^\dagger(x).
\]
所以
\[
|x,y\rangle
=\Psi^\dagger(x)\Psi^\dagger(y)|0\rangle
=-\Psi^\dagger(y)\Psi^\dagger(x)|0\rangle
=-|y,x\rangle.
\]

如果令 \(y=x\)，就得到
\[
|x,x\rangle=-|x,x\rangle.
\]
因此
\[
|x,x\rangle=0.
\]
这说明两个相同 fermion 不能占据同一个完整的单粒子态。这里如果只写 position label \(x\)，实际上是把自旋等其它标签省略了；真正被排除的是所有量子数都相同的状态。

creation operator 和 annihilation operator 在 boson 与 fermion 的情形中也有不同。

先看一个 boson mode。它的 annihilation operator 和 creation operator 记作 \(a\) 与 \(a^\dagger\)，满足
\[
[a,a^\dagger]=1.
\]
交换顺序以后，
\[
[a^\dagger,a]=-1.
\]
所以在 boson 的代数里，\(a\) 和 \(a^\dagger\) 是可以区分的：commutator 的顺序变了，符号也会变。

物理图像上，一个 boson mode 的 occupation number 可以是
\[
n=0,1,2,3,\dots
\]
creation operator 让它在 ladder 上往上走：
\[
a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,
\]
annihilation operator 让它往下走：
\[
a|n\rangle=\sqrt n\,|n-1\rangle.
\]
这个 ladder 本身并不对称：往上可以一直到 infinity，往下只能到 \(0\)。当已经在 \(n=0\) 的真空态时，
\[
a|0\rangle=0.
\]

fermion 的单个 mode 则只有两个 occupation states：
\[
n=0,\qquad n=1.
\]
也就是说，这个 mode 要么是 empty，要么是 filled。对应的 creation 和 annihilation operators 满足
\[
\{a,a^\dagger\}=aa^\dagger+a^\dagger a=1,
\]
并且
\[
\{a,a\}=0,\qquad \{a^\dagger,a^\dagger\}=0.
\]
特别地，
\[
(a^\dagger)^2=0.
\]
这表示同一个 fermion mode 不能被 creation operator 作用两次。

在 occupation number basis 里，这些算符的作用是
\[
a^\dagger|0\rangle=|1\rangle,\qquad a^\dagger|1\rangle=0,
\]
\[
a|1\rangle=|0\rangle,\qquad a|0\rangle=0.
\]
creation operator 在 filled state 上给出 \(0\)，annihilation operator 在 empty state 上给出 \(0\)。因此 fermion 的单个 mode 只有
\[
|0\rangle \leftrightarrow |1\rangle
\]
这两个状态，empty 和 filled 在结构上比 boson 的无限 ladder 更对称。
