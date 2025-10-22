+++
date = '2025-10-22T18:00:00+08:00'
katex = true
title = 'Spin'
tags = ['Advanced Quantum Mechanics']
+++ 

考虑一维谐振子，其哈密顿量为
\[
H = \frac{p^2}{2} + \frac{1}{2}\omega^2 x^2
\]
我们要求解的本征方程为 $H\varphi = E\varphi$。

引入阶梯算符（升降算符）$a^\pm$，定义为
\[
a^{\pm} = \frac{p \pm i\omega x}{\sqrt{2\omega}}
\]
进一步定义数算符 $N$：
\[
N = a^+ a^- = \frac{p^2 + \omega^2 x^2}{2\omega}
\]
则哈密顿量可以写成非常简单的形式：
\[
H = \omega \left(N + \frac{1}{2}\right)
\]

---

我将在这里为你展开讲解这部分内容。

### 为什么引入 $a^{\pm}$ (阶梯算符)？

直接解谐振子的薛定谔方程是一个二阶常微分方程，虽然可以解，但过程比较繁琐。狄拉克发明了一种更简洁、也更深刻的代数方法，其核心思想就是尝试对哈密顿算符 $H$ 进行“因式分解”。

我们知道哈密顿量 $H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2$。为了方便计算，我们常常使用自然单位制，令 $m=1, \hbar=1$，就像你的笔记里一样，此时 $H = \frac{p^2}{2} + \frac{1}{2}\omega^2 x^2$。

这个形式很像平方和 $A^2+B^2$。对于普通数字，我们可以在复数域里将其分解为 $(A-iB)(A+iB)$。但是，在量子力学中 $x$ (位置) 和 $p$ (动量) 是算符，并且它们不对易：$[x, p] = i\hbar = i$。因此我们不能直接像数字一样分解。

然而，这个思路启发我们去构造一对互为厄米共轭的算符 $a$ 和 $a^\dagger$，使得 $H$ 能够用它们的乘积 $a^\dagger a$ 来简洁地表达。这对算符就是你笔记中的 $a^{\pm}$，通常被称为 **升降算符** 或 **阶梯算符**。

### $a^{\pm}$ 的推导和哈密顿量

你的笔记中定义了：
\[
a^{\pm} = \frac{p \pm i\omega x}{\sqrt{2\omega}}
\]
我们通常把 $a^-$ 记为湮灭算符 $a$，把 $a^+$ 记为创生算符 $a^\dagger$。

现在我们来计算一下它们的乘积 $a^\dagger a$：
\[
\begin{aligned}
a^\dagger a &= \left( \frac{p + i\omega x}{\sqrt{2\omega}} \right) \left( \frac{p - i\omega x}{\sqrt{2\omega}} \right) \\
&= \frac{1}{2\omega} (p + i\omega x)(p - i\omega x) \\
&= \frac{1}{2\omega} (p^2 - i\omega px + i\omega xp + \omega^2 x^2) \\
&= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - i\omega(px - xp))
\end{aligned}
\]
这里要用到 $p$ 和 $x$ 的对易关系：$[p, x] = -i\hbar = -i$。所以 $px - xp = -i$。
将这个关系代入上式：
\[
\begin{aligned}
a^\dagger a &= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - i\omega(-i)) \\
&= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - \omega) \\
&= \frac{p^2 + \omega^2 x^2}{2\omega} - \frac{1}{2}
\end{aligned}
\]
我们又知道哈密顿量 $H = \frac{p^2}{2} + \frac{\omega^2 x^2}{2} = \omega \left(\frac{p^2 + \omega^2 x^2}{2\omega}\right)$。
所以，我们可以得到 $a^\dagger a$ 和 $H$ 的关系：
\[
a^\dagger a = \frac{H}{\omega} - \frac{1}{2}
\]
整理一下，就得到了哈密顿量的简洁形式：
\[
H = \omega (a^\dagger a + \frac{1}{2})
\]
我们定义 **粒子数算符** $N = a^\dagger a$。所以：
\[
H = \omega(N + \frac{1}{2})
\]
**这里需要注意**：你笔记中的 `N=a^+ a^- = (p^2+omg^2x^2)/2omg` 这一步是不太精确的，它忽略了 $p$ 和 $x$ 不对易而产生的 $-\frac{1}{2}$ 修正项。正确的关系是 $N = \frac{p^2 + \omega^2 x^2}{2\omega} - \frac{1}{2}$。不过最终 $H=\omega(N+1/2)$ 的结论是完全正确的。

### 主要结论与推论

这个代数形式非常强大，可以帮助我们直接得到量子谐振子的所有核心物理结论：

1.  **能量本征值是量子化的**：
    因为 $H$ 和 $N$ 之间只差常数，它们有共同的本征态。假设 $|n\rangle$ 是 $N$ 的一个本征态，其本征值为 $n$，即 $N|n\rangle = n|n\rangle$。
    那么 $H|n\rangle = \omega(N+\frac{1}{2})|n\rangle = \omega(n+\frac{1}{2})|n\rangle$。
    这意味着，体系的能量是量子化的，只能取一系列离散值：
    \[ E_n = \omega(n + \frac{1}{2}) \]

2.  **$a^\dagger$ 和 $a$ 是能量阶梯的“梯子”**：
    通过计算可以发现 $a$ 和 $a^\dagger$ 分别能让能量本征值减小或增加一个单位 $\omega$。
    *   $a$ 作用在态 $|n\rangle$ 上，会得到一个对应于 $n-1$ 的新状态。因此 $a$ 叫做**湮灭算符**。
    *   $a^\dagger$ 作用在态 $|n\rangle$ 上，会得到一个对应于 $n+1$ 的新状态。因此 $a^\dagger$ 叫做**创生算符**。

3.  **存在能量最低的基态**：
    由于体系能量不能无限降低 ($H$ 是正定的)，所以必须存在一个最低的能态，我们称之为基态 $|0\rangle$。对它使用湮灭算符 $a$ 不能再降低能量了，所以必然有：
    \[ a|0\rangle = 0 \]
    此时，粒子数算符的本征值 $n=0$。所以基态能量为：
    \[ E_0 = \omega(0 + \frac{1}{2}) = \frac{\omega}{2} \]
    这个 $E_0$ 就是著名的**零点能**，是量子效应的直接体现。

4.  **所有激发态都可以由基态生成**：
    从基态 $|0\rangle$ 出发，不断使用创生算符 $a^\dagger$，就可以像爬梯子一样得到所有的激发态：
    \[ |n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}} |0\rangle \]
    这表明所有能态构成了一个以 $\omega$ 为间隔的、等间距的能谱。这也是量子场论中“粒子”概念的来源，每一次 $a^\dagger$ 的作用，都相当于在场中“创生”了一个能量为 $\omega$ 的量子。




