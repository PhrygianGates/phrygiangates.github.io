+++
date = '2026-04-30T22:30:00+08:00'
title = '量子场哈密顿量'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

我们给一个哈密顿量：
\[
H=\int dx\left[\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}\right)\Psi(x)+V(x)\Psi^\dagger(x)\Psi(x)\right].
\]
这里取 \(\hbar=1\)。第一项是动能项，因为单粒子量子力学中 \(\hat p^2/(2m)\) 在位置表象里对应 \(-\nabla^2/(2m)\)。第二项是势能项，其中 \(\Psi^\dagger(x)\Psi(x)\) 是位置 \(x\) 处的粒子数密度，所以 \(V(x)\Psi^\dagger(x)\Psi(x)\) 表示在 \(x\) 处的势能密度。如果取 \(V(x)=mc^2\)，它就是给每个粒子加上一份静止能；这里仍然没有粒子之间的相互作用力。

根据上一篇文章，在一维情况下有
\[
\Psi(x)=\int \frac{dp}{\sqrt{2\pi}}\,a(p)e^{ipx},\qquad
\Psi^\dagger(x)=\int \frac{dq}{\sqrt{2\pi}}\,a^\dagger(q)e^{-iqx}.
\]
这里 \(a(p)\) 是湮灭一个动量为 \(p\) 的粒子的算符，\(a^\dagger(q)\) 是产生一个动量为 \(q\) 的粒子的算符。先看势能项里出现的粒子数密度积分：
\[
\int dx\,\Psi^\dagger(x)\Psi(x)
=\int dx\int \frac{dq}{\sqrt{2\pi}}\int \frac{dp}{\sqrt{2\pi}}\,
a^\dagger(q)a(p)e^{i(p-q)x}.
\]
整理得到
\[
\int dx\,\Psi^\dagger(x)\Psi(x)
=\int dp\,dq\,a^\dagger(q)a(p)\left[\frac{1}{2\pi}\int dx\,e^{i(p-q)x}\right].
\]
方括号里的积分就是 Dirac delta 函数：
\[
\frac{1}{2\pi}\int dx\,e^{i(p-q)x}=\delta(p-q).
\]
直观地说，当 \(p\neq q\) 时，指数因子随 \(x\) 振荡，正负部分相互抵消；当 \(p=q\) 时，指数因子等于 1，对全空间积分发散。Dirac delta 函数正是把这两种性质合在一起的对象：它只在 \(p=q\) 处有贡献，并且在积分中要求令 \(p=q\)。因此
\[
\int dx\,\Psi^\dagger(x)\Psi(x)
=\int dp\,dq\,a^\dagger(q)a(p)\delta(p-q)
=\int dp\,a^\dagger(p)a(p).
\]
算符 \(a^\dagger(p)a(p)\) 的作用是先湮灭一个动量为 \(p\) 的粒子，再产生一个同样动量为 \(p\) 的粒子，所以它实际上是在数动量为 \(p\) 的粒子数。由此可以看出，当这一项作用在某个态上时，它不会改变粒子的动量；如果 \(V(x)\) 是常数，那么这一项只给每个粒子加上同样的能量，也不会改变总动量。

再看第一项，也就是动能项：
\[
\int dx\,\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}\right)\Psi(x).
\]
把 \(\Psi(x)\) 展开成动量模式以后，\(-\nabla^2/(2m)\) 只作用在 \(e^{ipx}\) 上，并给出因子 \(p^2/(2m)\)：
\[
-\frac{\nabla^2}{2m}e^{ipx}=\frac{p^2}{2m}e^{ipx}.
\]
因此同样会出现对 \(x\) 的积分：
\[
\frac{1}{2\pi}\int dx\,e^{i(p-q)x}=\delta(p-q),
\]
于是动能项变成
\[
\int dx\,\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}\right)\Psi(x)
=\int dp\,\frac{p^2}{2m}a^\dagger(p)a(p).
\]
这说明动能项只是数出每个动量 \(p\) 上有多少粒子，并给它们各自乘上能量 \(p^2/(2m)\)，但不会把动量为 \(p\) 的粒子变成另一个动量的粒子。

所以在 \(V(x)\) 取常数，例如 \(V(x)=mc^2\) 的情况下，整个哈密顿量可以写成
\[
H=\int dp\left(\frac{p^2}{2m}+mc^2\right)a^\dagger(p)a(p).
\]
如果我们把这个 \(H\) 作用于一个有确定总动量的态，它只会改变这个态的相位或能量权重，不会改变它的总动量。这就是在这个自由粒子系统中动量守恒的意思。若 \(V(x)\) 不是常数，而是真的依赖位置，则空间平移对称性被外势破坏，动量一般就不再守恒。
