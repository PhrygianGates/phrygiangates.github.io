+++
date = '2025-06-05T21:24:00+08:00'
title = '伊辛模型'
tags = ['Statistical Mechanics']
categories = ["Physics"]
+++

遵循 Susskind 的 Statistical Mechanics 课程，第 9 讲。

伊辛模型中单个自旋的能量为：

\[E = -J\sigma\]

其中：
- \(E\) 是该自旋的能量
- \(J\) 是耦合常数（相互作用强度）
- \(\sigma\) 是自旋取值，可以是 +1（自旋向上）或 -1（自旋向下）

聚焦于单个自旋。
它的配分函数 \(Z\)，对两个构型求和（\(\sigma = +1, \sigma = -1\)），为：
\[
Z = \sum_{\sigma \in \{+1, -1\}} e^{-\beta(-J\sigma)} = \sum_{\sigma \in \{+1, -1\}} e^{\beta J\sigma} = e^{\beta J(+1)} + e^{\beta J(-1)} = e^{\beta J} + e^{-\beta J} = 2 \cosh(\beta J)
\]

（对于由 \(N\) 个独立、无相互作用的自旋组成的系统，总配分函数的对数是可加的：\(\ln Z_{total} = N \ln Z\)。）

让我们计算该自旋的平均能量 \(\langle E \rangle\)：
平均能量由 \(\langle E \rangle = -\frac{1}{Z} \frac{\partial Z}{\partial \beta}\) 给出。
由于 \(Z = 2 \cosh(\beta J)\)，它对 \(\beta\) 的导数为 \(\frac{\partial Z}{\partial \beta} = 2J \sinh(\beta J)\)。
将这些代入关于 \(\langle E \rangle\) 的表达式中：
\[
\langle E \rangle = -\frac{2J \sinh(\beta J)}{2 \cosh(\beta J)} = -J \frac{\sinh(\beta J)}{\cosh(\beta J)} = -J \tanh(\beta J)
\]

平均自旋 \(\langle \sigma \rangle\) 为：
\[ \langle \sigma \rangle = \frac{1}{Z} \sum_{\sigma \in \{+1, -1\}} \sigma e^{\beta J\sigma} = \tanh(\beta J) \]

---

现在考虑由 \(N\) 个自旋组成的一维（1D）链。这就是一维伊辛模型。
在只考虑最近邻相互作用的假设下，系统的能量为：
\[ E = -J \sum_{i=1}^{N-1} \sigma_i \sigma_{i+1} \]
这里我们假设是一个开链，含有 \(N\) 个自旋和 \(N-1\) 条键（相互作用）。对于闭链（周期性边界条件），求和通常到 \(N\)，并且有 \(\sigma_{N+1} = \sigma_1\)。我们将在本计算中专注于开链。

配分函数为：
\[ Z = \sum_{\{\sigma_1, \dots, \sigma_N\}} e^{-\beta E} = \sum_{\{\sigma_1, \dots, \sigma_N\}} e^{\beta J \sum_{i=1}^{N-1} \sigma_i \sigma_{i+1}} \]
其中求和遍历所有 \(2^N\) 种可能的自旋构型。

为了理解此类系统的整体行为，我们常研究关联函数。例如，可以问：如果我们知道第 \(k\) 个自旋的状态（例如 \(\sigma_k = +1\)），那么第 \(m\) 个自旋（\(m \neq k\)）也向上的概率是多少？这与计算两个自旋乘积的平均值 \(\langle \sigma_k \sigma_m \rangle\) 有关，它量化了自旋状态沿链的相关强度。

为了计算有限开链的配分函数 \(Z\)，可以进行变量变换。令 \(\mu_i = \sigma_i \sigma_{i+1}\)（对于 \(i = 1, \dots, N-1\)）。每个 \(\mu_i\) 可以是 +1 或 -1，表示相邻自旋是同向（对齐）还是反向（反平行）。
能量即可用这些“键变量”来表示：
\[ E = -J \sum_{i=1}^{N-1} \mu_i \]
我们需要把对自旋构型的求和 \(\{\sigma_k\}\) 与对这些新变量的求和联系起来。
注意，如果知道第一个自旋 \(\sigma_1\) 的状态，以及所有 \(\mu_i\) 的取值，我们就能确定之后每一个自旋的状态：
\(\sigma_2 = \mu_1 \sigma_1\)
\(\sigma_3 = \mu_2 \sigma_2 = \mu_2 \mu_1 \sigma_1\)
一般地，对于 \(k > 1\) 有 \(\sigma_k = \sigma_1 \prod_{j=1}^{k-1} \mu_j\)。

因此，一个系统构型可以由第一个自旋 \(\sigma_1\) 的状态（2 种选择：+1 或 -1）以及 \(N-1\) 个“键变量” \(\{\mu_1, \mu_2, \dots, \mu_{N-1}\}\) 的状态（每个 \(\mu_i\) 有 2 种选择）唯一确定。总计 \(2 \times 2^{N-1} = 2^N\) 个构型，正确匹配原自旋表述。

配分函数可以改写为对 \(\sigma_1\) 及所有 \(\mu_i\) 求和：
\[ Z = \sum_{\sigma_1 \in \{\pm 1\}} \left( \sum_{\mu_1 \in \{\pm 1\}} \dots \sum_{\mu_{N-1} \in \{\pm 1\}} e^{\beta J \sum_{i=1}^{N-1} \mu_i} \right) \]
由于指数项（表示键能量之和）与 \(\sigma_1\) 无关，对 \(\sigma_1\) 的求和仅给出一个 2 的因子：
\[ Z = 2 \left( \sum_{\mu_1 \in \{\pm 1\}} \dots \sum_{\mu_{N-1} \in \{\pm 1\}} \prod_{j=1}^{N-1} e^{\beta J \mu_j} \right) \]
对 \(\mu_j\) 变量的求和彼此独立，因为每个 \(\mu_j\) 在乘积中只出现一次。因此我们可以把它写成各个单独求和的乘积：
\[ Z = 2 \prod_{j=1}^{N-1} \left( \sum_{\mu_j \in \{\pm 1\}} e^{\beta J \mu_j} \right) \]
对单个 \(\mu_j\) 的每个求和为：
\[ \sum_{\mu \in \{\pm 1\}} e^{\beta J \mu} = e^{\beta J(+1)} + e^{\beta J(-1)} = 2 \cosh(\beta J) \]
代回之后，得到由 \(N\) 个自旋构成的一维开链的配分函数：
\[ Z = 2 [2 \cosh(\beta J)]^{N-1} \]

我们也可以计算“键变量”的平均值 \(\langle \mu_i \rangle\)，它等价于最近邻自旋关联 \(\langle \sigma_i \sigma_{i+1} \rangle\)。
由于配分函数在 \(\mu_j\) 变量上的因式分解：
\[ Z = 2 \prod_{j=1}^{N-1} \left( \sum_{\mu_j \in \{\pm 1\}} e^{\beta J \mu_j} \right) \]
期望值 \(\langle \mu_i \rangle\)（对于任意特定的键 \(i \in \{1, \dots, N-1\}\)）将简化。在形成期望值时，对 \(j \neq i\) 的 \(\mu_j\) 求和将同时出现在分子与分母中并相互抵消。这是因为每个 \(\mu_j\) 在 \(Z\) 的乘积形式中都是独立变量。对 \(\langle \mu_i \rangle\) 的计算实质上孤立出第 \(i\) 项：
\[ \langle \mu_i \rangle = \frac{\sum_{\mu_i \in \{\pm 1\}} \mu_i e^{\beta J \mu_i}}{\sum_{\mu_i \in \{\pm 1\}} e^{\beta J \mu_i}} \]
这个表达式与单个、孤立自旋的平均自旋 \(\langle \sigma \rangle\)（其能量为 \(E = -J\sigma\)）的形式完全相同。如之前推导（参见前文对单自旋 \(\langle \sigma \rangle = \tanh(\beta J)\) 的计算），这类平均的取值为 \(\tanh(\beta J)\)。
因此：
\[ \langle \mu_i \rangle = \langle \sigma_i \sigma_{i+1} \rangle = \tanh(\beta J) \]

---

在平均场近似中，我们通过聚焦一个单独的中心自旋，并把它与邻居的相互作用用某种平均或“均值”的方式处理，从而简化伊辛模型。这一方法在每个自旋与大量其他自旋相互作用（即高维）时特别有效。

考虑 \(d\) 维晶格上的一个自旋 \(\sigma\)。该自旋被 \(2d\) 个最近邻包围。来自该中心自旋与邻居相互作用的精确能量贡献为：
\[ E = -J \sigma \sum_{j=1}^{2d} \sigma_j \]
其中求和遍历 \(2d\) 个最近邻，记作 \(\sigma_j\)。

平均场近似的核心思想是用每个邻近自旋 \(\sigma_j\) 的统计平均（平均磁化）来替代它的瞬时取值，我们将其记为 \(\langle \sigma \rangle\) 或 \(\bar{\sigma}\)。这一近似假设各个自旋围绕该平均值的涨落效应可以忽略。

在该近似下，相互作用项简化为：
\[ \sum_{j=1}^{2d} \sigma_j \approx \sum_{j=1}^{2d} \langle \sigma \rangle = 2d \langle \sigma \rangle \]

把它代回中心自旋的能量表达式，得到“平均场能量”：
\[ E_{MF} = -J \sigma (2d \langle \sigma \rangle) = -(2dJ) \sigma \langle \sigma \rangle \]

该平均场能量等价于单个自旋 \(\sigma\) 在一个有效磁场 \(H_{eff}\) 下的能量，该有效场由 \(H_{eff} = 2dJ\langle \sigma \rangle\) 给出。

处于该有效场中的单自旋的统计力学很容易分析。中心自旋的平均值 \(\langle \sigma \rangle\) 可以像我们已推导的外场下的单自旋那样计算：
\[ \langle \sigma \rangle = \tanh(\beta H_{eff}) \]

代入我们的有效场 \(H_{eff}\) 的表达式，并将平均磁化 \(\langle \sigma \rangle\) 记为 \(\bar{\sigma}\)，我们得到平均场理论的中心方程：
\[ \bar{\sigma} = \tanh(2d\beta J \bar{\sigma}) \]

为理解其含义，我们可以用图像法分析。

定义新变量 \(y = 2d\beta J \bar{\sigma}\)。由此得到 \(\bar{\sigma} = \frac{y}{2d\beta J}\)。代回该方程得到：
\[ \frac{y}{2d\beta J} = \tanh(y) \]
回忆 \(\beta = 1/(k_B T)\)，其中 \(T\) 是温度、\(k_B\) 是玻尔兹曼常数，我们可以把方程改写为：
\[ \frac{k_B T}{2dJ} y = \tanh(y) \]
\(y\)（从而 \(\bar{\sigma}\)）的解，是两条函数的交点：
1. 一条过原点的直线 \(f(y) = \left(\frac{k_B T}{2dJ}\right) y\)，其斜率依赖于温度。
2. 双曲正切函数 \(g(y) = \tanh(y)\)。

我们立刻看到 \(y=0\) 始终是一个解，对应 \(\bar{\sigma}=0\)。这表示无净磁化的状态（顺磁态）。

要判断是否可能出现非零磁化，我们需要分析这两条函数在原点的斜率。`tanh(y)` 在 \(y=0\) 的斜率为：
\[ \left. \frac{d}{dy} \tanh(y) \right|_{y=0} = \left. (1 - \tanh^2(y)) \right|_{y=0} = 1 \]

系统的行为由直线 \(\frac{k_B T}{2dJ}\) 的斜率决定：

*   情形 1：高温。如果该直线的斜率大于 \(\tanh(y)\) 的初始斜率，即 \(\frac{k_B T}{2dJ} > 1\)，唯一的交点在 \(y=0\)。在该范围内，唯一解是 \(\bar{\sigma}=0\)。
*   情形 2：低温。如果该直线的斜率小于 \(\tanh(y)\) 的初始斜率，即 \(\frac{k_B T}{2dJ} < 1\)，直线将与 \(\tanh(y)\) 曲线在三个点相交：\(y=0\) 以及两个对称的非零解 \(\pm y_0\)。它们分别对应 \(\bar{\sigma}=0\) 和 \(\bar{\sigma}=\pm\bar{\sigma}_0\)。

这一分析揭示了一个“临界温度”\(T_c\) 的存在，它标志着上述两种行为的分界。当直线斜率恰为 1 时发生转变：
\[ \frac{k_B T_c}{2dJ} = 1 \implies T_c = \frac{2dJ}{k_B} \]

这个临界温度也称为居里温度，它分隔了材料的两种不同相：
- 当 \(T > T_c\) 时，系统只有一个稳定状态且 \(\bar{\sigma}=0\)。热能占主导，阻止自旋排列。这是“顺磁相”。
- 当 \(T < T_c\) 时，解 \(\bar{\sigma}=0\) 变得不稳定，同时出现两个新的稳定解 \(\pm\bar{\sigma}_0\)。当相互作用能战胜热涨落时，系统自发形成非零磁化。这是“铁磁相”。

在临界温度以下出现的自发磁化是一种“相变”。平均场近似尽管做了简化，但成功捕捉了伊辛模型中的这一基本的集体现象。

---

现在引入一个外加磁场 \(B\)。单个自旋 \(\sigma\) 的能量现在多了一个来自与该外场相互作用的项：
\[ E_{spin} = -J \sigma \sum_{j=1}^{2d} \sigma_j - B\sigma \]

沿用同样的平均场近似（\(\sum \sigma_j \approx 2d\bar{\sigma}\)），中心自旋的平均场能量为：
\[ E_{MF} = -J \sigma (2d \bar{\sigma}) - B\sigma = -(2dJ\bar{\sigma} + B)\sigma \]
该自旋所经历的总有效磁场是来自邻居的内部平均场与外场 \(B\) 的和，因此 \(H_{eff} = 2dJ\bar{\sigma} + B\)。

平均磁化 \(\bar{\sigma}\) 的自洽方程随之变为：
\[ \bar{\sigma} = \tanh(\beta H_{eff}) = \tanh(\beta(2dJ\bar{\sigma} + B)) \]

我们用之前的代换 \(y = 2d\beta J \bar{\sigma}\) 和 \(\bar{\sigma} = \frac{k_B T}{2dJ} y\) 来分析。方程变为：
\[ \frac{k_B T}{2dJ} y = \tanh(y + \beta B) \]

外场 \(B\) 从根本上改变了系统行为。在图像分析中，我们仍有直线 \(f(y) = \frac{k_B T}{2dJ} y\)，但第二个函数现在是 \(g(y) = \tanh(y + \beta B)\)。\(\beta B\) 项使 \(\tanh\) 曲线发生水平位移。

这导致重要的物理后果：

1.  无“尖锐”的相变：在外场（\(B \neq 0\)）存在时，\(\tanh(y + \beta B)\) 曲线不再经过原点。对于 \(B>0\)，它向左平移并在纵轴截距为 \(\tanh(\beta B) > 0\)。因此总会有一个非零交点，意味着 \(\bar{\sigma}\) 始终大于零。发生在 \(T_c\) 的尖锐相变消失。磁化不再在临界温度“自发”出现，而是随温度平滑变化。

2.  显式对称性破缺：外场显式打破了在 \(B=0\) 时存在的“上下”对称性。各温度下自旋都倾向于与外场对齐。因此，系统不再“选择”沿两个方向之一自发磁化，其方向由外场决定。

总之，外加磁场通过在各温度强制产生净磁化而消除了尖锐的铁磁相变。集体的自发有序被外场的引导作用所取代，表现为对外场的平滑响应。
