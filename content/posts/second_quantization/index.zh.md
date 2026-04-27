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

---
我们回到基本的量子力学：给定态 \( |\psi\rangle\)，在 \(x\) 表象与动量 \(p\) 表象下的波函数分别是 \(\psi(x)=\langle x|\psi\rangle\) 与 \(\tilde\psi(p)=\langle p|\psi\rangle\)。它们可以通过傅里叶变换连接（继续取 \(\hbar=1\)）：
\[
\tilde\psi(p)=\int \frac{dx}{\sqrt{2\pi}}\,e^{-ipx}\psi(x),\qquad
\psi(x)=\int \frac{dp}{\sqrt{2\pi}}\,e^{ipx}\tilde\psi(p).
\]

现在考虑二次量子化的场景。湮灭场算符可以在一组完备的单粒子正交基 \(\{\psi_i(x)\}\) 上展开：
\[
\Psi^-(x)=\sum_i a_i^-\,\psi_i(x).
\]
这里 \(\psi_i(x)\) 可以取为单粒子哈密顿量的能量本征态，而 \(a_i^-\) 的意思是把第 \(i\) 个模（可以类比为第 \(i\) 个谐振子）里的粒子数降低 1。

对于自由粒子 \(H=\hat p^{\,2}/(2m)\)，在一维 \(x\) 空间里定态方程的解可以写成平面波的线性组合 \(Ae^{ikx}+Be^{-ikx}\)，并且 \(E=k^2/(2m)\)。在 \(\hbar=1\) 的约定下 \(p=k\)，所以 \(e^{ipx}\) 就是动量本征态在位置表象下的波函数。由于 \(p\) 是连续的，把求和改成积分，就得到
\[
\Psi^-(x)=\int \frac{dp}{\sqrt{2\pi}}\,a^-(p)\,e^{ipx},
\]
其中 \(a^-(p)\) 的意思是湮灭一个动量为 \(p\) 的粒子。为了和上面的形式对应，也可以把它写成一对互逆的傅里叶变换：
\[
a^-(p)=\int \frac{dx}{\sqrt{2\pi}}\,e^{-ipx}\Psi^-(x).
\]

形式上这就是傅里叶变换，而这也符合直觉：\(\Psi^-(x)\) 的含义是在位置 \(x\) 处湮灭一个粒子；\(\Psi^+(x)\) 和 \(a^+(p)\) 也有类似的关系（它们分别是上述算符的共轭）。

---
对于这些产生湮灭算符，我们已经知道它们满足
\[
[a_i^-,a_j^+]=\delta_{ij},\qquad [a_i^-,a_j^-]=0,\qquad [a_i^+,a_j^+]=0.
\]
也就是说，唯一非零的对易关系来自同一个模的湮灭算符和产生算符；所有产生算符之间彼此对易，所有湮灭算符之间也彼此对易。

把场算符 \(\Psi^-(x)\)、\(\Psi^+(x)\) 用这些 \(a_i^-\)、\(a_i^+\) 展开，再代入上面的对易关系，就可以推出位置空间里的场算符满足
\[
[\Psi^-(x),\Psi^+(y)]=\delta(x-y),
\]
同时
\[
[\Psi^-(x),\Psi^-(y)]=0,\qquad [\Psi^+(x),\Psi^+(y)]=0.
\]

这里要注意，\(\Psi^+(x)\) 与 \(\Psi^-(x)\) 本身是 complex 的，它们不是 Hermitian 算符，因此单独看并不是 observables。不过这一点本身不是最重要的，因为可以通过取实部、虚部，或者取适当的线性组合来构造 Hermitian 的可观测量。

我们可以回忆一下其他不对易的算符。最标准的例子是位置和动量，它们满足 \([X,P]=i\hbar\)。不对易的物理意义是：这两个量不能被同时精确测量；换句话说，对其中一个量的测量会影响另一个量。

回到上面的场算符例子，如果 \(x\neq y\)，那么 \(\delta(x-y)=0\)。这说明在不同空间点上的场算符彼此对易，因此在点 \(A\) 测量场，不会影响到点 \(B\) 处场的测量。