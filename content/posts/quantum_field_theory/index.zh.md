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

相比于量子力学研究固定粒子数的情况，二次量子化的要点是：把 0 粒子、1 粒子、2 粒子等不同粒子数的状态统一放进同一个“总空间”，也就是福克空间；然后用创生/湮灭算符在这个空间里增减粒子数。为此我们引入场算符（算符值场）\(\hat{\Psi}(x)\)：它把位置 \(x\) 作为标记，对应一个作用在福克空间上的算符。\(\hat{\Psi}(x_0)\) 是一个算符，而它的厄米共轭 \(\hat{\Psi}^\dagger(x_0)\) 直观上应该能在位置 \(x_0\) 处“创造”一个粒子；对真空态 \(|0\rangle\) 作用时，它给出一个单粒子位置本征态 \(|x_0\rangle\)：
\[
\hat{\Psi}^\dagger(x_0)\,|0\rangle = |x_0\rangle .
\]

为了把这个想法写成可计算的形式，我们先选取一组完备、正交归一的单粒子态 \(\{|j\rangle\}\)（\(j=1,2,\dots\)）。这里的 \(j\) 只是单粒子基向量的编号（例如动量本征态的标签），不是“粒子数”；粒子数由 \(|n\rangle\) 或 \(|n_1,n_2,\dots\rangle\) 里的 \(n,n_j\) 来表示。它们在位置表象的波函数记为
\[
\psi_j(x)\equiv \langle x|j\rangle,\qquad \langle j|x\rangle=\psi_j^*(x).
\]
并满足完备性
\[
\sum_j |j\rangle\langle j| = I
\]
（这里的 \(I\) 是单粒子希尔伯特空间上的单位算符）。

这里说的“模式”，指的就是：一旦选定了单粒子基 \(\{|j\rangle\}\)，每一个编号 \(j\) 就对应一个独立的单粒子自由度（一个“基方向”）。在二次量子化里，我们允许很多个玻色子占据同一个单粒子态 \(|j\rangle\)，于是用占据数 \(n_j\) 来记录“有多少个粒子在这个模式里”。

接着在福克空间中，对每个单粒子模式 \(j\)（也就是我们选定的那组单粒子基 \(|j\rangle\) 的编号）引入一对玻色子的湮灭/创生算符 \(a_j, a_j^\dagger\)，满足
\[
[a_j,a_k^\dagger]=\delta_{jk},\qquad [a_j,a_k]=0,\qquad [a_j^\dagger,a_k^\dagger]=0.
\]
并在占有数基底（用每个模式的粒子数 \(n_j\) 来标记的基底；可以把它理解为“对每个模式各自取一个数态 \(|n_j\rangle\)，再把所有模式的数态并排写在一起”）
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
真空态（0 粒子态，也就是所有模式占据数都为 0）定义为
\[
|0\rangle \equiv |0,0,0,\dots\rangle.
\]
于是“一粒子处于模式 \(j\)”的态是
\[
a_j^\dagger|0\rangle = |0,\dots,1_j,\dots\rangle \equiv |j\rangle.
\]
这里最后一个等号就是把福克空间的一粒子子空间（粒子数为 1 的那部分）与单粒子希尔伯特空间做识别：一粒子子空间中的基向量 \(a_j^\dagger|0\rangle\) 对应单粒子态 \(|j\rangle\)。在这个约定下，我们可以用同一个记号 \(|j\rangle\) 来写这两件事。

现在定义场算符为
\[
\hat{\Psi}(x)=\sum_j a_j\,\psi_j(x)=\sum_j a_j\langle x|j\rangle,
\qquad
\hat{\Psi}^\dagger(x)=\sum_j a_j^\dagger\,\psi_j^*(x)=\sum_j a_j^\dagger\langle j|x\rangle.
\]

用这个展开，我们可以验证上面的“创生”性质。对真空态作用：
\[
\hat{\Psi}^\dagger(x_0)|0\rangle
=\sum_j a_j^\dagger\,\langle j|x_0\rangle\,|0\rangle
=\sum_j \langle j|x_0\rangle\,(a_j^\dagger|0\rangle).
\]
而在一粒子子空间里，可以把 \(|j\rangle\) 与 \(a_j^\dagger|0\rangle\) 对应起来，于是
\[
\hat{\Psi}^\dagger(x_0)|0\rangle
=\sum_j \langle j|x_0\rangle\,|j\rangle .
\]
另一方面，由完备关系 \(\sum_j|j\rangle\langle j|=I\) 立刻得到
\[
|x_0\rangle = \sum_j |j\rangle\langle j|x_0\rangle
= \sum_j \langle j|x_0\rangle\,|j\rangle .
\]
两式相同，因此 \(\hat{\Psi}^\dagger(x_0)|0\rangle=|x_0\rangle\) 成立。

顺便说一句，这套定义也能把“一粒子态”和“波函数”的对应关系写得非常直接。任取一个一粒子态
\[
|\psi\rangle=\sum_j c_j\,a_j^\dagger|0\rangle,
\]
由于在一粒子子空间里 \(a_j^\dagger|0\rangle\equiv |j\rangle\)，它在位置表象的波函数就是
\[
\psi(x)=\langle x|\psi\rangle=\sum_j c_j\,\langle x|j\rangle=\sum_j c_j\,\psi_j(x).
\]
把 \(\hat{\Psi}(x)\) 作用到这个一粒子态上，会得到对应的振幅并把系统送回真空：
\[
\hat{\Psi}(x)|\psi\rangle
=\sum_j c_j\,\psi_j(x)\,|0\rangle
=\psi(x)\,|0\rangle.
\]