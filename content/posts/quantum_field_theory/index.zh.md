+++
date = '2025-12-16T22:00:00+08:00'
title = '量子场论'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

我们来聊一聊量子场论的 setup。最常见的切入点，是先把“场”理解成一组无穷多的谐振子（或模），再把这套语言翻译回我们熟悉的波函数。

先从单个量子谐振子开始。它的能量本征方程写作
\[
H|\psi\rangle = E|\psi\rangle .
\]
它有一组离散的能量本征态。对谐振子而言，更方便的一组本征态是数态（Fock 态）\(|n\rangle\)（\(n=0,1,2,\dots\)），满足 \(H|n\rangle=E_n|n\rangle\)。我们引入湮灭算符 \(a\) 与创生算符 \(a^\dagger\)，令它们满足 \([a,a^\dagger]=1\)，并定义占据数算符 \(N=a^\dagger a\)。数态同时也是 \(N\) 的本征态：
\[
N|n\rangle = n|n\rangle .
\]
它们构成一组正交归一基，满足 \(\langle n|m\rangle=\delta_{nm}\)，并且有完备关系 \(\sum_{n=0}^{\infty}|n\rangle\langle n|=I\)。

升降算符在数态上的作用是
\[
a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,\qquad
a|n\rangle=\sqrt{n}\,|n-1\rangle .
\]

考虑多谐振子的情况（也可以理解为许多“模”）。用 \(|n_1,n_2,n_3,\dots\rangle\) 表示：第 1 个模的占据数为 \(n_1\)，第 2 个模的占据数为 \(n_2\)，依此类推。第 \(j\) 个模的创生算符 \(a_j^\dagger\) 会把 \(n_j\) 增加 1：
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

相比于量子力学研究固定粒子数的情况，量子场论（更准确地说，二次量子化）的动机之一是粒子数可能改变，因此需要一个能在不同粒子数子空间之间来回跳转的语言。为此我们引入算符值场 \(\hat{\Psi}(x)\)：它把位置 \(x\) 作为标记，返回一个作用在 Fock 空间上的算符。\(\hat{\Psi}(x_0)\) 是一个算符，而它的厄米共轭 \(\hat{\Psi}^\dagger(x_0)\) 直观上应该能在位置 \(x_0\) 处“创造”一个粒子；对真空态 \(|0\rangle\) 作用时，它给出一个单粒子位置本征态 \(|x_0\rangle\)：
\[
\hat{\Psi}^\dagger(x_0)\,|0\rangle = |x_0\rangle .
\]

为了把这个想法写成可计算的形式，选取单粒子 Hilbert 空间中的一组正交归一基 \(\{|j\rangle\}\)，并记它们的位置表象为 \(\phi_j(x)=\langle x|j\rangle\)。在 Fock 空间里，令 \(a_j^\dagger\) 表示“在单粒子态 \(|j\rangle\) 上增加一个粒子”的创生算符（相应地 \(a_j\) 湮灭该模的一个粒子），满足 \([a_j,a_k^\dagger]=\delta_{jk}\)。则场算符可以展开为
\[
\hat{\Psi}(x)=\sum_j a_j\,\langle x|j\rangle=\sum_j a_j\,\phi_j(x),\qquad
\hat{\Psi}^\dagger(x)=\sum_j a_j^\dagger\,\langle j|x\rangle=\sum_j a_j^\dagger\,\phi_j^*(x).
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