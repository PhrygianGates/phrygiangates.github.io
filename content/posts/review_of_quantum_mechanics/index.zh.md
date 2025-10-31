+++
date = '2025-06-26T22:40:00+08:00'
title = '量子力学综述'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

在量子力学中，物理系统的状态由一个态矢量描述，使用狄拉克的括号记号（bra-ket）记作 \(|\psi\rangle\)。这些态矢量是称为希尔伯特空间的复向量空间中的元素。

给定两个态矢量 \(|\psi\rangle\) 和 \(|\phi\rangle\)，它们的内积是一个复数，记为 \(\langle\phi|\psi\rangle\)。如果两个不同状态的内积为零，即 \(\langle\phi|\psi\rangle = 0\)，则称这些状态正交，表示完全独立的物理情形。

可以测量的物理量，如位置、动量和能量，称为可观测量。在量子力学中，可观测量由厄米算符表示。算符 \(A\) 若等于其自身的共轭转置 \(A = A^\dagger\)，则为厄米的。厄米算符的一个关键性质是其本征值总是实数，这是必要的，因为它们对应物理测量的结果。

当测量一个可观测量 \(A\) 时，唯一可能的结果是该算符的本征值。本征方程为：
$$
A |\alpha\rangle = \alpha |\alpha\rangle
$$
其中，\(\alpha\) 是一个本征值，\(|\alpha\rangle\) 是对应的本征矢。如果我们对 \(A\) 进行测量并得到结果 \(\alpha\)，系统的状态将坍缩到相应的本征态 \(|\alpha\rangle\)。

为了描述空间中的粒子，我们常在位置基底中工作。基底矢量记作 \(|x\rangle\)，表示具有确定位置 \(x\) 的状态。态矢量 \(|\psi\rangle\) 在该基底中的表象是波函数 \(\psi(x)\)，其由内积定义：
$$
\psi(x) = \langle x|\psi\rangle
$$

---

记号 \(\langle x|\psi\rangle\) 可能令人困惑。将其与熟悉的离散向量空间（如三维欧几里得空间）类比会有所帮助。

**在离散基底中：**

设想一个标准的三维向量 \(\vec{V}\)。我们可以在一个基底中表示它，该基底是一组三个正交的单位矢量 \(B = \{\hat{e}_1, \hat{e}_2, \hat{e}_3\}\)（例如 \(\hat{i}, \hat{j}, \hat{k}\)）。
*   基底是完整集合 \(B\)。
*   基底矢量是该集合中的一个成员，例如 \(\hat{e}_1\)。其中的 `1` 是一个离散指标。
*   要找到 \(\vec{V}\) 沿 \(\hat{e}_1\) 方向的分量，我们取点积（即内积）：\(V_1 = \hat{e}_1 \cdot \vec{V}\)。
*   该向量可以通过对其分量求和来重建：\(\vec{V} = V_1 \hat{e}_1 + V_2 \hat{e}_2 + V_3 \hat{e}_3 = \sum_{i=1}^3 (\hat{e}_i \cdot \vec{V}) \hat{e}_i\)。

**在连续的位置基底中：**

量子力学使用相同的逻辑，但基底是无限、连续的。
*   基底是所有位置本征矢的无限集合，即对每个可能的 \(x\) 值都有 \( \{ |x\rangle \} \)。
*   基底矢量是该集合中的一个成员 \(|x\rangle\)。位置 \(x\) 本身充当连续指标。因此，\(|2\rangle\) 和 \(|3.14\rangle\) 是该无限集合中的两个不同基底矢量。
*   表达式 \(\langle x|\psi\rangle\) 的意思是“将态矢量 \(|\psi\rangle\) 与由 x 标引的特定基底矢量取内积”。
*   结果是一个复数 \(\psi(x)\)，它是 \(|\psi\rangle\) 沿该基底矢量 \(|x\rangle\) 的分量。对所有 \(x\) 的这些分量的集合构成了波函数。
*   态矢量可以通过对连续基底“求和”（积分）来重建：\(|\psi\rangle = \int dx' |x'⟩⟨x'|ψ⟩\)。

因此，当我们写下 \(\psi(x) = \langle x|\psi\rangle\) 时，我们实际上是在问：“量子态 \(|\psi\rangle\) 在希尔伯特空间中对应确定位置 \(x\) 的特定方向上的投影是多少？”

波函数 \(\psi(x)\) 为我们提供了一个以位置为变量描述量子态的连续函数。

波函数的物理意义与在某一位置找到粒子的概率相关。根据波恩规则，在位置 \(x\) 处找到粒子的概率密度由波函数的绝对值平方给出：
$$
p(x) = |\psi(x)|^2 = \psi^*(x)\psi(x)
$$
其中 \(\psi^*(x)\) 是 \(\psi(x)\) 的复共轭。

---

正如态矢量可以在某个基底中表示，算符也可以。算符所呈现的形式取决于你选择工作的基底。

#### 位置算符
在位置基底中最简单的算符是位置算符 \(\hat{x}\)。当从位置基底来观察它对态矢量 \(|\psi\rangle\) 的作用时，就是用位置 \(x\) 相乘：
$$
\langle x | \hat{x} | \psi \rangle = x \langle x | \psi \rangle = x \psi(x)
$$
因此，在位置表象中，\(\hat{x}\) 算符就是“乘以 \(x\)”。

#### 动量算符
动量算符 \(\hat{p}\) 的表象较为非平凡。在位置基底中，\(\hat{p}\) 的作用是一个微分算符：
$$
\langle x | \hat{p} | \psi \rangle = -i\hbar \frac{\partial}{\partial x} \psi(x)
$$
这是量子力学的一个基本公设。它建立了动量与波函数空间变化之间的深刻联系。具有高动量的状态，其波函数作为位置的函数会非常快速地振荡。

我们可以据此求出具有确定动量 \langle p \rangle 的状态的波函数。这样的状态是动量算符的本征矢，满足 \(\hat{p}|p\rangle = p|p\rangle\)。将其写到位置基底中，得到其波函数 \(\psi_p(x) = \langle x|p\rangle\) 的微分方程（将 \(|p\rangle\) 类比为前一式中的 \(|\psi\rangle\)）：
$$
-i\hbar \frac{\partial}{\partial x} \psi_p(x) = \langle x | \hat{p} | p \rangle = p \langle x | p \rangle = p \, \psi_p(x)
$$
其解是平面波：
$$
\psi_p(x) = A e^{ipx/\hbar}
$$
这表明具有确定动量的状态是一种具有单一、恒定波长并遍布整个空间的波。

---
量子态的时间演化由一个幺正算符支配。让我们用 \(|\psi(t_0)\rangle\) 表示系统在时间 \(t_0\) 的状态。在稍后的时间 \(t_0+t\)，状态将变为 \(|\psi(t_0+t)\rangle\)，其变换由时间演化算符 \(U(t)\) 给出：
\[
|\psi(t_0+t)\rangle = U(t) |\psi(t_0)\rangle
\]
量子力学的一个基本公设是：在时间演化过程中，两个状态之间的内积保持不变。这是因为在某种状态下找到粒子的总概率必须始终为 1，这意味着态矢量的范数被守恒。如果我们有两个状态 \(|\psi\rangle\) 和 \(|\phi\rangle\)，则它们的内积 \(\langle\phi|\psi\rangle\) 必须随时间保持不变。
\[
\langle\phi(t_0+t)|\psi(t_0+t)\rangle = \langle\phi(t_0)|\psi(t_0)\rangle
\]
代入时间演化算符：
\[
\langle\phi(t_0)|U^\dagger(t)U(t)|\psi(t_0)\rangle = \langle\phi(t_0)|\psi(t_0)\rangle
\]
由于这对任意一对状态都必须成立，算符 \(U(t)\) 必须是幺正的：
\[
U^\dagger(t)U(t) = I
\]

现在，让我们考虑一个由微小量 \(\epsilon\) 引起的无穷小时间演化。在 \(t=0\) 时刻，没有演化，因此 \(U(0)=I\)。对于一个很小的 \(\epsilon\)，我们可以将时间演化算符写成：
\[
U(\epsilon) \approx I + \epsilon G
\]
其中 \(G\) 称为时间平移的生成元。该算符的伴随为：
\[
U^\dagger(\epsilon) \approx I + \epsilon G^\dagger
\]
应用幺正条件 \(U^\dagger(\epsilon)U(\epsilon) = I\)：
\[
(I + \epsilon G^\dagger)(I + \epsilon G) = I
\]
展开并保留 \(\epsilon\) 的一阶项：
\[
I + \epsilon G + \epsilon G^\dagger + O(\epsilon^2) = I
\]
这意味着生成元 \(G\) 必须是反厄米的：
\[
G + G^\dagger = 0
\]

任何反厄米算符都可以写成一个虚数乘以一个厄米算符。我们定义一个厄米算符 \(H\) 使得：
\[
G = -\frac{i}{\hbar} H
\]
这里，\(\hbar\) 是约化普朗克常数，引入它是为了使 \(H\) 具有能量的量纲。算符 \(H\) 为厄米（\(H=H^\dagger\)）与 \(G\) 为反厄米是一致的。这个厄米算符 \(H\) 即哈密顿算符，对应系统总能量这一可观测量。量子力学中的所有可观测量都由厄米算符表示。

因此，无穷小时间演化算符为：
\[
U(\epsilon) = I - \frac{i\epsilon}{\hbar} H
\]

---

#### 关于为何可观测量为厄米的说明

量子力学的一个基本公设是：所有可观测量（如位置、动量和能量）都由厄米算符表示。这并非任意选择；这是为了使数学框架与物理现实相一致。主要有两个原因：

1.  测量结果必须是实数：当我们测量一个物理量时，结果总是实数（例如 3 米，-1.5 焦耳）。厄米算符的一个重要数学性质是其本征值总为实数。由于量子测量的可能结果是相应算符的本征值，这一性质确保我们的测量理论预测总是实数，如同它们必须的那样。

2.  状态的正交性：对应不同本征值的厄米算符的本征态彼此正交。这对测量至关重要。如果我们测量一个可观测量并得到某个具体数值，系统状态会“坍缩”到相应的本征态。正交性保证这些可能的结果态彼此分明、相互独立。在一次测量得到本征值 \(\alpha_1\) 之后，系统处于状态 \(|\alpha_1\rangle\)，而立即测得不同数值 \(\alpha_2\) 的概率为零，因为 \(\langle\alpha_2|\alpha_1\rangle = 0\)。这保证了我们的测量毫不含糊。

---

我们先前得到，对于无穷小时间步长 \(\epsilon\)，时间演化算符为：
\[
U(\epsilon) = I - \frac{i\epsilon}{\hbar} H
\]
要得到有限时间区间 \(t\) 的算符，我们可以将该区间分为 \(N\) 个小步，其中 \(t = N\epsilon\)。总的演化是这些小演化的乘积：
\[
U(t) = \lim_{N\to\infty} \left(I - \frac{i\epsilon}{\hbar} H\right)^N = \lim_{N\to\infty} \left(I - \frac{it}{N\hbar} H\right)^N
\]
该极限就是指数函数的定义，由此得到有限时间演化算符：
\[
U(t) = e^{-iHt/\hbar}
\]
#### 时间依赖的薛定谔方程
让我们回到无穷小形式，以推导态矢量的运动方程。我们有：
\[
|\psi(t+\epsilon)\rangle = U(\epsilon)|\psi(t)\rangle = \left(I - \frac{i\epsilon}{\hbar} H\right)|\psi(t)\rangle
\]
重排得：
\[
\frac{|\psi(t+\epsilon)\rangle - |\psi(t)\rangle}{\epsilon} = -\frac{i}{\hbar} H |\psi(t)\rangle
\]
当取极限 \(\epsilon \to 0\) 时，左侧成为导数的定义，得到时间依赖的薛定谔方程：
\[
i\hbar \frac{\partial}{\partial t}|\psi(t)\rangle = H|\psi(t)\rangle
\]
这是量子动力学的核心方程，描述系统的态矢量如何随时间变化。

#### 时间无关的薛定谔方程
一个特殊但非常重要的情形是考虑具有确定能量的状态。这些是哈密顿算符的本征态，我们记为 \(|E\rangle\)。它们满足本征值方程：
\[
H|E\rangle = E|E\rangle
\]
这被称为时间无关的薛定谔方程。

之所以称为“时间无关”，是因为它的解是物理性质随时间不变的状态，称为定态。我们来看看原因。如果取一个具有确定能量的状态 \(|\psi(0)\rangle = |E\rangle\)，其时间演化为：
\[
|\psi(t)\rangle = U(t)|E\rangle = e^{-iHt/\hbar}|E\rangle
\]
由于 \(|E\rangle\) 是 \(H\) 的本征态，我们可以用其本征值 \(E\) 替换 \(H\)：
\[
|\psi(t)\rangle = e^{-iEt/\hbar}|E\rangle
\]
态矢量 \(|E\rangle\) 只获得一个随时间变化的相位因子。当我们计算概率密度（或任何其他可观测量）时，这个相位因子会相消。例如：
\[
|\langle x|\psi(t)\rangle|^2 = |e^{-iEt/\hbar}\langle x|E\rangle|^2 = |e^{-iEt/\hbar}|^2 |\langle x|E\rangle|^2 = |\psi_E(x)|^2
\]
概率分布在时间上保持不变。因此，时间无关的薛定谔方程用于为给定系统找到一组稳定的定态及其对应的能量。

---

物理中的对称性是一种使物理定律保持不变的变换。在量子力学中，这有一个深刻的结果：对于系统的每一个连续对称性，都存在一个对应的守恒量。这就是诺特定理的量子力学版本。

让我们考虑由幺正算符 \(V\) 表示的一个变换。该算符作用于态矢量 \(|\psi\rangle\)，产生变换后的状态 \(|\psi'\rangle = V|\psi\rangle\)。

为了使 \(V\) 成为动力学的对称性，系统的时间演化对于原始状态和变换后的状态必须相同。如果状态 \(|\psi_1\rangle\) 在时间 \(t_1\) 演化到时间 \(t_2\) 的状态 \(|\psi_2\rangle\)，则变换后的状态 \(V|\psi_1\rangle\) 必须在相同的时间区间内演化到 \(V|\psi_2\rangle\)。

令 \(U(t_2-t_1)\) 为时间演化算符。原始状态的演化为：
\[ |\psi_2\rangle = U(t_2-t_1) |\psi_1\rangle \]
变换后状态的演化必须为：
\[ V|\psi_2\rangle = U(t_2-t_1) (V|\psi_1\rangle) \]
将第一式代入第二式得到：
\[ V(U(t_2-t_1)|\psi_1\rangle) = U(t_2-t_1)V|\psi_1\rangle \]
由于这对任意状态 \(|\psi_1\rangle\) 都必须成立，这意味着对称算符 \(V\) 必须与时间演化算符 \(U(t)\) 对易：
\[ [V, U(t)] = VU(t) - U(t)V = 0 \]

这是一个变换成为对称性的普遍条件。现在，让我们看看这对哈密顿算符意味着什么。我们知道 \(U(t) = e^{-iHt/\hbar}\)。要使 \(V\) 与 \(U(t)\) 对易，它必须与 \(H\) 对易。通过考虑一个无穷小时间步长 \(\epsilon\) 可以看出：
\[ U(\epsilon) = I - \frac{i\epsilon}{\hbar} H \]
对易关系变为：
\[ V\left(I - \frac{i\epsilon}{\hbar} H\right) = \left(I - \frac{i\epsilon}{\hbar} H\right)V \]
展开两侧：
\[ V - \frac{i\epsilon}{\hbar} VH = V - \frac{i\epsilon}{\hbar} HV \]
这化简为 \(VH = HV\)，即：
\[ [V, H] = 0 \]

#### 从对称性到可观测量的守恒定律

条件 \([V, H] = 0\) 表明对称算符与哈密顿算符对易。但这如何引出诸如能量或动量这样的可测量量的守恒定律？关键在于将注意力从变换算符 \(V\) 转移到它的生成元上。

物理中的守恒定律适用于可观测量——由厄米算符表示的量，其本征值是我们在实验中测得的实数。
*   对称算符 \(V\)（例如有限旋转）是幺正的，但通常不是厄米的。若 \([V,H]=0\)，其期望值 \(\langle V \rangle\) 被守恒，但这个数值并不对应标准的物理可观测量。
*   连续对称性的生成元 \(G\) 是一个厄米算符，因此它代表一个物理可观测量。

这就是我们建立这种联系的原因：系统的对称性（由 \(V\) 表示）意味着存在一个守恒的可观测量（由 \(G\) 表示）。陈述 \(\frac{d}{dt}\langle G \rangle = 0\) 即我们所要的守恒定律。

下面用最重要的例子来说明。

#### 例子：空间平移与动量守恒
考虑一个在空间平移下具有对称性的系统。这意味着支配该系统的物理定律在各处都相同；例如，势能是常数 \(V(x) = V_0\)。

由算符 \(T(\vec{a})\) 执行沿向量 \(\vec{a}\) 的平移。当该算符作用于波函数时，它会平移其自变量：
\[ T(\vec{a}) \psi(\vec{x}) = \psi(\vec{x}-\vec{a}) \]
让我们通过考虑沿 x 轴的一个无穷小平移 \(T(\delta x)\) 来找到这一变换的生成元。我们可以对平移后的波函数进行泰勒展开：
\[ \psi(x-\delta x, y, z) \approx \psi(x, y, z) - \delta x \frac{\partial}{\partial x} \psi(x, y, z) \]
回忆动量算符的 x 分量是 \(\hat{p}_x = -i\hbar \frac{\partial}{\partial x}\)，这意味着 \(\frac{\partial}{\partial x} = \frac{i}{\hbar}\hat{p}_x\)。将其代入：
\[ T(\delta x)\psi(\vec{x}) \approx \psi(\vec{x}) - \delta x \left(\frac{i}{\hbar}\hat{p}_x\right) \psi(\vec{x}) = \left(I - \frac{i}{\hbar} \delta x \hat{p}_x\right) \psi(\vec{x}) \]
这表明对于无穷小平移，其算符为 \(T(\delta x) \approx I - \frac{i}{\hbar} \delta x \hat{p}_x\)。将其推广到有限平移 \(a\)，得到指数形式：
\[ T(a) = e^{-ia\hat{p}_x/\hbar} \]
这揭示了动量算符 \(\hat{p}\) 是空间平移的生成元。

如果哈密顿算符在平移下不变，那么 \([T(a), H] = 0\)，这意味着生成元也与哈密顿算符对易：
\[ [\hat{p}, H] = 0 \]
按照我们对一般生成元 \(G\) 的推导，这立刻意味着动量的期望值被守恒：\(\frac{d}{dt}\langle \hat{p} \rangle = 0\)。

#### 例子：旋转不变性与角动量守恒
现在考虑一个在旋转下具有对称性的系统，例如处于中心势 \(V(r) = V(|\vec{r}|)\) 的原子。

物理系统绕轴 \(\hat{n}\) 旋转角度 \(\theta\) 的操作由算符 \(R(\hat{n}, \theta)\) 执行。当该算符作用于波函数时，它将坐标系按相反方向旋转：
\[ R(\hat{n}, \theta) \psi(\vec{r}) = \psi(R^{-1}(\hat{n}, \theta)\vec{r}) \]
让我们通过考虑绕 z 轴的一个无穷小角度 \(\delta\phi\) 的旋转来找到生成元。逆旋转将坐标变换为：
*   \(x' = x \cos(-\delta\phi) - y \sin(-\delta\phi) \approx x + y\delta\phi\)
*   \(y' = x \sin(-\delta\phi) + y \cos(-\delta\phi) \approx y - x\delta\phi\)
*   \(z' = z\)

将其应用于波函数并进行泰勒展开：
\[ R(\hat{z}, \delta\phi)\psi(x,y,z) = \psi(x+y\delta\phi, y-x\delta\phi, z) \approx \psi(x,y,z) + y\delta\phi \frac{\partial\psi}{\partial x} - x\delta\phi \frac{\partial\psi}{\partial y} \]
\[ R(\hat{z}, \delta\phi)\psi \approx \left( I + \delta\phi \left(y\frac{\partial}{\partial x} - x\frac{\partial}{\partial y}\right) \right) \psi \]
我们识别出角动量算符的 z 分量：\(\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x = -i\hbar\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right) = i\hbar\left(y\frac{\partial}{\partial x} - x\frac{\partial}{\partial y}\right)\)。
这意味着 \(\left(y\frac{\partial}{\partial x} - x\frac{\partial}{\partial y}\right) = \frac{-i}{\hbar}\hat{L}_z\)。将其代入：
\[ R(\hat{z}, \delta\phi)\psi \approx \left( I + \delta\phi \left(\frac{-i}{\hbar}\hat{L}_z\right) \right)\psi = \left( I - \frac{i}{\hbar} \delta\phi \hat{L}_z \right)\psi \]
因此有限旋转的算符为：
\[ R(\hat{z}, \theta) = e^{-i\theta\hat{L}_z/\hbar} \]
这表明角动量算符 \(\hat{L}\) 是旋转的生成元。

如果哈密顿算符具有旋转不变性，则 \([R, H] = 0\)，这意味着 \([\hat{L}, H] = 0\)。这将导致角动量守恒：\(\frac{d}{dt}\langle \hat{L} \rangle = 0\)。

物理中的许多对称性是连续的，意味着它们可以由无穷小变换构建。例如空间平移、旋转以及时间平移本身。一个依赖参数 \(\lambda\) 的连续幺正对称算符 \(V(\lambda)\) 可以用一个称为对称性的生成元的厄米算符 \(G\) 来表示：
\[ V(\lambda) = e^{i\lambda G} \]
对于带有小参数 \(\delta\lambda\) 的无穷小变换，该算符近似为：
\[ V(\delta\lambda) \approx I + i\delta\lambda G \]
如果 \(V\) 是一种对称性，则对任意 \(\lambda\) 有 \([V(\lambda), H] = 0\)。这意味着生成元 \(G\) 也必须与哈密顿算符对易：
\[ [G, H] = 0 \]
这是一个关键结果。它告诉我们，对称性的生成元所对应的可观测量是一个守恒量。为此，让我们考察 \(G\) 的期望值 \(\langle G \rangle\) 的时间演化。使用薛定谔方程：
\[ \frac{d}{dt}\langle G \rangle = \frac{d}{dt}\langle\psi(t)|G|\psi(t)\rangle \]
状态的时间导数由 \(\frac{\partial}{\partial t}|\psi(t)\rangle = -\frac{i}{\hbar}H|\psi(t)\rangle\) 给出，而对应的 bra 为 \(\frac{\partial}{\partial t}\langle\psi(t)| = \frac{i}{\hbar}\langle\psi(t)|H\)。应用乘积法则：
\[ \frac{d}{dt}\langle G \rangle = \left(\frac{d}{dt}\langle\psi(t)|\right)G|\psi(t)\rangle + \langle\psi(t)|G\left(\frac{d}{dt}|\psi(t)\rangle\right) \]
\[ \frac{d}{dt}\langle G \rangle = \left(\frac{i}{\hbar}\langle\psi(t)|H\right)G|\psi(t)\rangle + \langle\psi(t)|G\left(-\frac{i}{\hbar}H|\psi(t)\rangle\right) \]
\[ \frac{d}{dt}\langle G \rangle = \frac{i}{\hbar}\left(\langle\psi(t)|HG|\psi(t)\rangle - \langle\psi(t)|GH|\psi(t)\rangle\right) \]
\[ \frac{d}{dt}\langle G \rangle = \frac{i}{\hbar}\langle\psi(t)|[H, G]|\psi(t)\rangle \]
由于 \([G, H] = 0\)，可得 \([H, G] = 0\)。因此：
\[ \frac{d}{dt}\langle G \rangle = 0 \]
\(G\) 的期望值随时间保持不变。这就是诺特定理的要旨：如果一个系统具有连续对称性，那么就存在一个对应的可观测量（该对称性的生成元），其期望值被守恒。

下面是一些关键例子：
*   时间平移不变性：生成元是哈密顿算符 \(H\) 本身。若 \(H\) 不显式依赖时间，系统在时间平移下具有对称性，能量（\(H\) 的期望值）被守恒。
*   空间平移不变性：生成元是动量算符 \(\hat{p}\)。如果系统在空间平移下具有对称性（即势是均匀的），则动量被守恒。
*   旋转不变性：生成元是角动量算符 \(\hat{L}\)。如果系统在旋转下具有对称性（例如中心势），则角动量被守恒。

---
