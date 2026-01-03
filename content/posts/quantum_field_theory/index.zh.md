+++
date = '2025-12-16T22:00:00+08:00'
title = '量子场论'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

我们来聊一聊量子场论的基本设定。最常见的切入点，是先把“场”理解成一组（原则上无穷多）彼此独立的谐振子自由度，再把这套语言翻译回我们熟悉的波函数。

先从单个量子谐振子开始。它的能量本征方程写作
\[
H|\psi\rangle = E|\psi\rangle .
\]
它有一组离散的能量本征态。对谐振子而言，更方便的一组本征态是数态 \(|n\rangle\)（\(n=0,1,2,\dots\)），满足 \(H|n\rangle=E_n|n\rangle\)。我们引入湮灭算符 \(a\) 与创生算符 \(a^\dagger\)，令它们满足 \([a,a^\dagger]=1\)，并定义占据数算符 \(N=a^\dagger a\)。数态同时也是 \(N\) 的本征态：
\[
N|n\rangle = n|n\rangle .
\]
它们构成一组正交归一基，满足 \(\langle n|m\rangle=\delta_{nm}\)，并且有完备关系 \(\sum_{n=0}^{\infty}|n\rangle\langle n|=I\)。

升降算符在数态上的作用是
\[
a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,\qquad
a|n\rangle=\sqrt{n}\,|n-1\rangle .
\]

考虑多谐振子的情况（即有很多个彼此独立的谐振子自由度）。用 \(|n_1,n_2,n_3,\dots\rangle\) 表示：第 1 个谐振子的占据数为 \(n_1\)，第 2 个谐振子的占据数为 \(n_2\)，依此类推。第 \(j\) 个谐振子的创生算符 \(a_j^\dagger\) 会把 \(n_j\) 增加 1：
\[
a_j^\dagger|n_1,\dots,n_j,\dots\rangle
=\sqrt{n_j+1}\,|n_1,\dots,n_j+1,\dots\rangle ,
\]
相应地，\(a_j\) 会把 \(n_j\) 减少 1：
\[
a_j|n_1,\dots,n_j,\dots\rangle
=\sqrt{n_j}\,|n_1,\dots,n_j-1,\dots\rangle .
\]

---

在通常的量子力学里，我们常常固定粒子数来讨论。单粒子波函数是 \(\psi(x)=\langle x|\psi\rangle\)。如果粒子数固定为 \(N\)，多粒子波函数可以写作 \(\psi(x_1,x_2,\dots,x_N)=\langle x_1,x_2,\dots,x_N|\Psi\rangle\)。

如果粒子数不固定，而允许 0 粒子、1 粒子、2 粒子……这些情况同时被讨论，那么我们需要一个“总的”希尔伯特空间来容纳它们。一个很直观的做法是：选定一组完备、正交归一的单粒子基 \(\{|u_j\rangle\}\)，把每个编号 \(j\) 看成一个彼此独立的谐振子自由度；用一对升降算符 \(a_j,a_j^\dagger\) 来减少/增加这个自由度的占据数。接下来我们还会引入一个带位置标签的算符 \(\hat{\Psi}(x)\)。它的厄米共轭 \(\hat{\Psi}^\dagger(x_0)\) 作用在全零占据数的态（下面会记作 \(|0\rangle\)）上，会给出单粒子的位置本征态 \(|x_0\rangle\)：
\[
\hat{\Psi}^\dagger(x_0)\,|0\rangle = |x_0\rangle .
\]

为了把这个想法写成可计算的形式，我们先选取一组完备、正交归一的单粒子态 \(\{|u_j\rangle\}\)（\(j=1,2,\dots\)）。这里的 \(j\) 只是单粒子基向量的编号（例如动量本征态的标签），不是“粒子数”；粒子数由 \(|n\rangle\) 或 \(|n_1,n_2,\dots\rangle\) 里的 \(n,n_j\) 来表示。它们在位置表象的波函数记为
\[
u_j(x)\equiv \langle x|u_j\rangle,\qquad \langle u_j|x\rangle=u_j^*(x).
\]
并满足完备性
\[
\sum_j |u_j\rangle\langle u_j| = I
\]
（这里的 \(I\) 是单粒子希尔伯特空间上的单位算符）。

接着，对每个编号 \(j\)（也就是我们选定的那组单粒子基 \(|u_j\rangle\) 的编号）引入一对湮灭/创生算符 \(a_j, a_j^\dagger\)。你可以把它们理解为“第 \(j\) 个谐振子”的升降算符：第 \(j\) 个谐振子的占据数（激发数）记作 \(n_j\)。这些算符满足
\[
[a_j,a_k^\dagger]=\delta_{jk},\qquad [a_j,a_k]=0,\qquad [a_j^\dagger,a_k^\dagger]=0.
\]
这组对易关系保证：对每个固定的 \(j\)，\(\{a_j,a_j^\dagger\}\) 的代数结构与单个谐振子的升降算符相同，因此会自然出现数态以及 \(\sqrt{n_j}\) 这样的系数。我们用占据数基底（用每个谐振子的占据数 \(n_j\) 来标记的基底）
\[
|n_1,n_2,\dots\rangle
\]
上定义它们的作用：
\[
a_j|n_1,\dots,n_j,\dots\rangle=\sqrt{n_j}\,|n_1,\dots,n_j-1,\dots\rangle,
\]
\[
a_j^\dagger|n_1,\dots,n_j,\dots\rangle=\sqrt{n_j+1}\,|n_1,\dots,n_j+1,\dots\rangle.
\]
全零占据数的态（也就是所有谐振子的占据数都为 0）定义为
\[
|0\rangle \equiv |0,0,0,\dots\rangle.
\]
于是“只有第 \(j\) 个谐振子的占据数为 1，其它都为 0”的态是
\[
a_j^\dagger|0\rangle = |0,\dots,1_j,\dots\rangle \equiv |1_j\rangle.
\]
这里的 \(|1_j\rangle\) 表示“只有第 \(j\) 个谐振子被激发一次”的态。只看总占据数为 1 的那一部分状态，它与单粒子希尔伯特空间自然对应：在这个对应下，\(|1_j\rangle\) 与单粒子态 \(|u_j\rangle\) 一一对应。

现在定义这组带位置标签的算符为
\[
\hat{\Psi}(x)=\sum_j a_j\,u_j(x)=\sum_j a_j\langle x|u_j\rangle,
\qquad
\hat{\Psi}^\dagger(x)=\sum_j a_j^\dagger\,u_j^*(x)=\sum_j a_j^\dagger\langle u_j|x\rangle.
\]

用这个展开，我们可以验证上面的性质。对 \(|0\rangle\) 作用：
\[
\hat{\Psi}^\dagger(x_0)|0\rangle
\;=\sum_j a_j^\dagger\,\langle u_j|x_0\rangle\,|0\rangle
\;=\sum_j \langle u_j|x_0\rangle\,(a_j^\dagger|0\rangle)
\;=\sum_j \langle u_j|x_0\rangle\,|1_j\rangle .
\]
另一方面，由完备关系 \(\sum_j|u_j\rangle\langle u_j|=I\)（这是单粒子空间里的等式）立刻得到
\[
|x_0\rangle = \sum_j |u_j\rangle\langle u_j|x_0\rangle
= \sum_j \langle u_j|x_0\rangle\,|u_j\rangle .
\]
将单粒子态 \(|u_j\rangle\) 与“总占据数为 1”的态 \(|1_j\rangle\) 做上面的一一对应识别后，两式逐项相同，因此 \(\hat{\Psi}^\dagger(x_0)|0\rangle=|x_0\rangle\) 成立。
顺便说一句，这套定义也能把“一粒子态”和“波函数”的对应关系写得非常直接。任取一个一粒子态
\[
|\psi\rangle=\sum_j c_j\,a_j^\dagger|0\rangle=\sum_j c_j\,|1_j\rangle,
\]
由于在“总占据数为 1”的那一部分里 \(a_j^\dagger|0\rangle\equiv |1_j\rangle\)，并且 \(|1_j\rangle\) 与单粒子态 \(|u_j\rangle\) 对应，它在位置表象的波函数就是
\[
\psi(x)=\langle x|\psi\rangle=\sum_j c_j\,\langle x|u_j\rangle=\sum_j c_j\,u_j(x).
\]
把 \(\hat{\Psi}(x)\) 作用到这个一粒子态上，会得到对应的振幅并把系统送回真空：
\[
\hat{\Psi}(x)|\psi\rangle
=\sum_j c_j\,u_j(x)\,|0\rangle
=\psi(x)\,|0\rangle.
\]
