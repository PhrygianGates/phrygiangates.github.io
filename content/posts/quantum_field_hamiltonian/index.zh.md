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

---
当我们考虑多种粒子的局部相互作用时，同样的机制会给出总动量守恒，而不是要求每个粒子的动量分别守恒。

比如有两种粒子 \(A\) 和 \(B\)。除了各自的动能项之外，可以在哈密顿量中加入一个局部相互作用项：
\[
H=H_{\text{kinetic}}+g\int dx\,\Psi_A^\dagger(x)\Psi_B^\dagger(x)\Psi_B(x)\Psi_A(x).
\]
这里的 \(g\) 是耦合常数，表示这个相互作用的强弱。这个项实际上描述的是 \(A\) 和 \(B\) 的散射：右边的 \(\Psi_A(x)\)、\(\Psi_B(x)\) 先在同一个位置 \(x\) 湮灭一个 \(A\) 粒子和一个 \(B\) 粒子，左边的 \(\Psi_A^\dagger(x)\)、\(\Psi_B^\dagger(x)\) 再在同一个位置产生一个 \(A\) 粒子和一个 \(B\) 粒子。粒子种类没有改变，但各自的动量可以改变。

如果把这些场都展开到动量空间，会得到类似
\[
\int dp_A\,dp_B\,dq_A\,dq_B\,
a_A^\dagger(q_A)a_B^\dagger(q_B)a_B(p_B)a_A(p_A)\,
\delta(p_A+p_B-q_A-q_B).
\]
这里 \(p_A,p_B\) 是被湮灭的入射粒子的动量，\(q_A,q_B\) 是被产生的出射粒子的动量。对 \(x\) 的积分只给出总动量守恒：
\[
p_A+p_B=q_A+q_B,
\]
但并不要求 \(p_A=q_A\) 或 \(p_B=q_B\)。所以单个粒子的动量可以改变，只要前后总动量相同。这就是它被称为散射的原因。

再比如，如果我们想让哈密顿量描述一个 \(A\) 粒子变成一个 \(B\) 粒子和一个 \(C\) 粒子，就可以写下
\[
\Psi_B^\dagger(x)\Psi_C^\dagger(x)\Psi_A(x).
\]
它的作用是湮灭一个 \(A\)，并产生一个 \(B\) 和一个 \(C\)。但是哈密顿量必须是 Hermitian 的，因为它对应可观测的能量，也保证时间演化是幺正的。因此还要加上它的厄米共轭项：
\[
\Psi_A^\dagger(x)\Psi_C(x)\Psi_B(x).
\]
所以相互作用哈密顿量可以写成
\[
H_I=g\int dx\left[\Psi_B^\dagger(x)\Psi_C^\dagger(x)\Psi_A(x)+\Psi_A^\dagger(x)\Psi_C(x)\Psi_B(x)\right].
\]
第一项描述 \(A\to B+C\)，第二项描述反过来的过程 \(B+C\to A\)。

时间演化来自薛定谔方程。这里仍取 \(\hbar=1\)，如果 \(H\) 不显含时间，则
\[
|\phi(t+\epsilon)\rangle=e^{-iH\epsilon}|\phi(t)\rangle.
\]
把指数函数展开，就得到
\[
|\phi(t+\epsilon)\rangle
=\left(1-i\epsilon H-\frac{\epsilon^2}{2}H^2+\cdots\right)|\phi(t)\rangle.
\]
所以一阶项 \(-i\epsilon H|\phi(t)\rangle\) 表示哈密顿量作用一次，二阶项 \(-\epsilon^2H^2|\phi(t)\rangle/2\) 表示哈密顿量作用两次。对上面的 \(H_I\) 来说，作用一次可以给出 \(A\to B+C\) 或 \(B+C\to A\)。作用两次则可以给出 \(A\to B+C\to A\)，也可以给出 \(B+C\to A\to B+C\) 这样的过程。

这里的“一阶”和“二阶”不是说真实世界中先发生一个一阶过程，然后同时又发生一个二阶过程；它们是同一个时间演化振幅中的不同阶贡献。总振幅是这些项的叠加：
\[
\mathcal A=\mathcal A^{(1)}+\mathcal A^{(2)}+\mathcal A^{(3)}+\cdots.
\]
如果耦合常数 \(g\) 很小，一阶项通常是 \(g\) 阶，二阶项是 \(g^2\) 阶，所以可以按阶数逐步近似。图像上说 \(A\) “暂时”出现或消失，只是一种描述高阶项的方便语言；严格地说，它是时间演化算符展开中的中间态贡献。