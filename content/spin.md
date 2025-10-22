+++
date = '2025-10-22T18:00:00+08:00'
katex = true
title = 'Spin'
tags = ['Advanced Quantum Mechanics']
+++

对于一维谐振子问题，其哈密顿量可以表示为 \(H = \frac{p^2}{2} + \frac{1}{2}\omega^2 x^2\)。我们的目标是求解其能量本征方程 \(H\varphi = E\varphi\)。为了用一种更简洁的代数方法求解，我们引入一对阶梯算符，定义为：
\[
a^{\pm} = \frac{p \pm i\omega x}{\sqrt{2\omega}}
\]
其中 \(a^+\) 通常被称为创生算符 \(a^\dagger\)，而 \(a^-\) 被称为湮灭算符 \(a\)。通过这些算符，我们可以将哈密顿量表达成一个更简洁的形式。我们定义粒子数算符为 \(N = a^\dagger a\)。经过推导可以发现，哈密顿量与粒子数算符的关系为：
\[
H = \omega \left(N + \frac{1}{2}\right)
\]
这个形式极大地简化了问题的求解过程。

---

直接求解谐振子的薛定谔方程是一个二阶常微分方程，过程较为繁琐。狄拉克发明了一种更深刻的代数方法，其核心思想是尝试对哈密顿算符 \(H\) 进行“因式分解”。哈密顿量 \(H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2\) 在自然单位制（令 \(m=1, \hbar=1\)）下为 \(H = \frac{p^2}{2} + \frac{1}{2}\omega^2 x^2\)，这个形式很像平方和 \(A^2+B^2\)。虽然在量子力学中位置算符 \(x\) 和动量算符 \(p\) 不对易（\([x, p] = i\)），不能像普通数字一样直接分解，但这个思路启发我们去构造一对互为厄米共轭的算符 \(a\) 和 \(a^\dagger\)，使得 \(H\) 能用它们的乘积 \(a^\dagger a\) 来简洁地表达。这对算符就是我们之前引入的升降算符。

我们来计算一下 \(a^\dagger a\) 的具体形式，其中 \(a^\dagger = a^+\) 而 \(a = a^-\)：
\[
\begin{aligned}
a^\dagger a &= \left( \frac{p + i\omega x}{\sqrt{2\omega}} \right) \left( \frac{p - i\omega x}{\sqrt{2\omega}} \right) \\
&= \frac{1}{2\omega} (p + i\omega x)(p - i\omega x) \\
&= \frac{1}{2\omega} (p^2 - i\omega px + i\omega xp + \omega^2 x^2) \\
&= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - i\omega(px - xp))
\end{aligned}
\]
利用对易关系 \([p, x] = -i\)，即 \(px - xp = -i\)，代入上式得到：
\[
\begin{aligned}
a^\dagger a &= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - i\omega(-i)) \\
&= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - \omega) \\
&= \frac{p^2 + \omega^2 x^2}{2\omega} - \frac{1}{2}
\end{aligned}
\]
由此我们得到 \(a^\dagger a = \frac{H}{\omega} - \frac{1}{2}\)，整理后便获得了哈密顿量的简洁形式 \(H = \omega (a^\dagger a + \frac{1}{2})\)。若定义粒子数算符 \(N = a^\dagger a\)，则 \(H = \omega(N + \frac{1}{2})\)。这个代数形式非常强大，可以直接导出量子谐振子的所有核心物理结论。

首先，体系的能量是量子化的。由于 \(H\) 和 \(N\) 仅相差常数，它们拥有共同的本征态。若 \(|n\rangle\) 是 \(N\) 的一个本征态，其本征值为 \(n\)，即 \(N|n\rangle = n|n\rangle\)，那么作用哈密顿算符会得到 \(H|n\rangle = \omega(N+\frac{1}{2})|n\rangle = \omega(n+\frac{1}{2})|n\rangle\)。这意味着体系的能量只能取一系列离散值：
\[ E_n = \omega\left(n + \frac{1}{2}\right) \]
其次，算符 \(a^\dagger\) 和 \(a\) 扮演了能量阶梯的“梯子”角色。为了证明这一点，我们首先计算它们与哈密顿量的对易关系。利用 \([x, p] = i\)，我们可以得到 \([a, a^\dagger] = 1\)。由此可得：
\[ [H, a] = [\omega(a^\dagger a + 1/2), a] = \omega[a^\dagger a, a] = -\omega a \]
\[ [H, a^\dagger] = [\omega(a^\dagger a + 1/2), a^\dagger] = \omega[a^\dagger a, a^\dagger] = \omega a^\dagger \]
现在，我们将 \(H\) 作用在 \(a|n\rangle\) 上，其中 \(|n\rangle\) 是能量为 \(E_n\) 的本征态：
\[ H(a|n\rangle) = (aH + [H, a])|n\rangle = aE_n|n\rangle - \omega a|n\rangle = (E_n - \omega)(a|n\rangle) \]
这表明 \(a|n\rangle\) 是一个新的能量本征态，其能量比 \(E_n\) 恰好少了一个量子 \(\omega\)。因此，\(a\) 作用在态 \(|n\rangle\) 上会得到一个对应于 \(n-1\) 的新状态，故被称为湮灭算符。同理，我们可以证明 \(a^\dagger\) 的作用：
\[ H(a^\dagger|n\rangle) = (a^\dagger H + [H, a^\dagger])|n\rangle = a^\dagger E_n|n\rangle + \omega a^\dagger|n\rangle = (E_n + \omega)(a^\dagger|n\rangle) \]
这表明 \(a^\dagger|n\rangle\) 的能量为 \(E_n + \omega\)，所以 \(a^\dagger\) 被称为创生算符。它们分别使能量本征值减小或增加一个单位 \(\omega\)。

另外，由于体系能量不能无限降低（\(H\) 是正定的），必须存在一个能量最低的基态，记为 \(|0\rangle\)。湮灭算符作用于基态不能再降低其能量，因此必然有 \(a|0\rangle = 0\)。此时，粒子数算符的本征值为 \(n=0\)，对应的基态能量为 \(E_0 = \omega(0 + \frac{1}{2}) = \frac{\omega}{2}\)。这个著名的“零点能”是量子效应的直接体现。

最后，所有激发态都可以由基态通过创生算符生成。从基态 \(|0\rangle\) 出发，不断使用创生算符 \(a^\dagger\)，就可以像爬梯子一样得到所有的激发态：
\[ |n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}} |0\rangle \]

表达式中的分母 \(\sqrt{n!}\) 是归一化常数。它的作用是确保态矢量 \(|n\rangle\) 的长度为1，即 \(\langle n|n\rangle = 1\)，这是量子力学中概率诠释的基本要求。如果我们从基态 \(|0\rangle\) （假设已归一化）出发，每次应用创生算符 \(a^\dagger\) 都会改变态矢量的长度。例如，未归一化的 \(a^\dagger|0\rangle\) 态的内积（模方）为 \(\langle 0| a a^\dagger |0\rangle = \langle 0| (a^\dagger a + 1) |0\rangle = 1\)。而未归一化的 \((a^\dagger)^2|0\rangle\) 态的内积是 \(\langle 0| a^2 (a^\dagger)^2 |0\rangle = 2\)。可以归纳出，\((a^\dagger)^n|0\rangle\) 的模方是 \(n!\)。因此，为了使最终的 \(|n\rangle\) 态满足归一化条件 \(\langle n|n\rangle=1\)，我们需要将其除以 \(\sqrt{n!}\)。

这表明所有能态构成了一个以 \(\omega\) 为间隔的等距能谱。这个图像也是量子场论中“粒子”概念的来源，每一次 \(a^\dagger\) 的作用，都相当于在场中“创生”了一个能量为 \(\omega\) 的量子。




