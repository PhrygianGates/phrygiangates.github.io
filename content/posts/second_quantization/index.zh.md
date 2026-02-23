+++
date = '2026-02-23T16:00:00+08:00'
title = '二次量子化'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

我们开始于一个 setup：Hamiltonian 中的势能 \(V(x)\) 形状类似于一个对称的双势阱，有两个对称的极小值点，中间的 barrier 非常高（此处插入势能示意图）。我们来讨论这个系统的能量本征态，以及态的时间演化。

首先要 solve 定态薛定谔方程 \(H|\psi\rangle = E|\psi\rangle\) 来找能量的本征值和本征态。这里本征态在 \(x\) 表象下的投影就是波函数 \(\psi(x)=\langle x|\psi\rangle\)。

假设 \(V(x)\) 中间的 barrier 高到了无穷大，那么粒子被完全限制在左右两个势阱里，我们可以近似认为系统有左右两个局域态 \( |\psi_L\rangle\)、\( |\psi_R\rangle\)。它们对应的能量本征值应该相同，设为 \(E_0\)，也就是能量简并。

但实际不会如此：当 barrier 有限且 \(V(x)\) 对称时，能量本征态的波函数要么对称要么反对称，而上面的局域态 \( |\psi_L\rangle\)、\( |\psi_R\rangle\) 本身均不满足。于是能量本征态可以取为它们的对称/反对称组合：
\[
|\psi_1\rangle=\frac{|\psi_L\rangle+|\psi_R\rangle}{\sqrt{2}},\qquad E_1=E_0-\epsilon,
\]
\[
|\psi_2\rangle=\frac{|\psi_L\rangle-|\psi_R\rangle}{\sqrt{2}},\qquad E_2=E_0+\epsilon.
\]

对于能量本征态，它们满足如下时间演化（这里取 \(\hbar=1\)）：
\[
|\psi_n(t)\rangle=e^{-iE_n t}|\psi_n(0)\rangle.
\]

我们现在假设初始状态为 \( |\psi(0)\rangle=|\psi_L\rangle\)，即粒子在左边。注意这个不是能量本征态，但可以表达为本征态的线性组合：
\[
|\psi_L\rangle=\frac{|\psi_1\rangle+|\psi_2\rangle}{\sqrt{2}},\qquad
|\psi_R\rangle=\frac{|\psi_1\rangle-|\psi_2\rangle}{\sqrt{2}}.
\]

随时间演化，在时刻 \(t\) 有
\[
|\psi(t)\rangle=\frac{1}{\sqrt{2}}\left(e^{-iE_1 t}|\psi_1\rangle+e^{-iE_2 t}|\psi_2\rangle\right)
= e^{-iE_0 t}\left(\cos(\epsilon t)\,|\psi_L\rangle+i\sin(\epsilon t)\,|\psi_R\rangle\right).
\]

取 \(t=\pi/(2\epsilon)\)，会发现 \( |\psi(t)\rangle = i e^{-iE_0 t}|\psi_R\rangle\)，也就是（忽略整体相位）这正好对应粒子在右边。于是系统会在 \( |\psi_L\rangle\) 和 \( |\psi_R\rangle\) 这两种状态之间来回振荡。
