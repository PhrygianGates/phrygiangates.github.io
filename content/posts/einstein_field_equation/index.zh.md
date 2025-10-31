+++
date = '2025-03-07T00:15:09+08:00'
title = '爱因斯坦场方程'
tags = ['The Early Universe']
categories = ["Physics"]
+++

为了推导爱因斯坦场方程，我们从涉及能量与动量的物理考量出发，并结合来自时空曲率的几何考量。

---
爱因斯坦场方程依赖于三个基本假设：

1. 能量守恒
2. 动量守恒
3. 牛顿引力方程

对于假设1和2，能量-动量张量的守恒律成立：

\[
\nabla_\mu T^{\mu \nu} = 0
\]

能量-动量张量 \(T^{\mu \nu}\) 概括了关键的物理量，其表示为：

\[
T^{\mu \nu} = \begin{pmatrix}
T^{00} & T^{01} & T^{02} & T^{03} \\
T^{10} & T^{11} & T^{12} & T^{13} \\
T^{20} & T^{21} & T^{22} & T^{23} \\
T^{30} & T^{31} & T^{32} & T^{33}
\end{pmatrix}
\]

其中：

- \(T^{00} = \rho\)：能量密度
- \(T^{i0} = P_i\)：在第\(i\)个空间方向上的动量密度
- \(T^{0i} = S_i\)：在第\(i\)个空间方向的能流
- \(\sigma_{ij}\)：空间应力，与压力和应力相关

一个关键特征是该张量的对称性 \(T^{\mu \nu} = T^{\nu \mu}\)，这表明能流 \(S_i\) 等于动量密度 \(P_i\)。尽管这看起来似乎违反直觉，但它自然源于爱因斯坦的质能等价：

\[ E = m c^2 \]

四动量向量为：

\[ p^\mu = m u^\mu \]

其中，\(m\) 为质量，\(u^\mu\) 为四速度。取 \( c = 1 \) 时，第一列（能流）与第一行（动量密度）都由 \( m u^\mu \) 表示，这就解释了为何能流等于动量密度，并建立了能量-动量张量的对称性：

\[ T^{\mu \nu} = T^{\nu \mu} \]

---
在几何方面，爱因斯坦场方程源自时空的曲率，其由黎曼曲率张量 \(R^\rho_{\sigma \mu \nu}\) 描述。曲率的一个关键性质由比安基恒等式给出：

\[
\nabla_\alpha R_{\beta \gamma \mu \nu} + \nabla_\beta R_{\gamma \alpha \mu \nu} + \nabla_\gamma R_{\beta \mu \alpha \nu} = 0
\]

用 \(g^{\beta \mu}\) 收缩该方程，得到：

\[
\nabla_\alpha R_{\gamma \nu} + \nabla^\mu R_{\gamma \alpha \mu \nu} - \nabla_\gamma R_{\alpha \nu} = 0
\]

再与 \(g^{\gamma \nu}\) 收缩，得到：

\[
\nabla_\alpha R - 2 \nabla^\mu R_{\alpha \mu} = 0
\]

该式可重写为：

\[
\nabla^\mu \left(R_{\alpha \mu} - \frac{1}{2} g_{\alpha \mu} R\right) = 0
\]

我们定义爱因斯坦张量 \(G_{\mu \nu}\)（其为对称的，因为 \(g_{\mu\nu}\) 与 \(R_{\mu\nu}\) 都是对称张量）：

\[
G_{\mu \nu} = R_{\mu \nu} - \frac{1}{2} g_{\mu \nu} R
\]

因此，我们得到：

\[
\nabla_\mu G^{\mu \nu} = 0
\]

由于我们已从物理假设得到：

\[ \nabla_\mu T^{\mu \nu} = 0 \]

于是可以自然地提出如下形式的爱因斯坦场方程：

\[
G_{\mu \nu} = \kappa T_{\mu \nu}
\]

其中 \(\kappa\) 是一个有待确定的常数。

---

我们希望确定出现在爱因斯坦场方程中的常数 \(\kappa\)：

\[ G_{\mu \nu} = \kappa T_{\mu \nu} \]

我们从由能量-动量张量描述的一个物理模型出发：

\[
T_{\mu \nu} = (\rho + p)u_\mu u_\nu + p g_{\mu \nu}
\]

其中：

- \(\rho\) 为能量密度。
- \(p\) 为压力。

在低速近似（牛顿近似）下，假设 \(\rho \gg p\)。

将四速度 \(u^\mu\) 定义为：

\[
u^\mu = (u^0, 0, 0, 0)\]

该假设意味着流体在空间中静止，只有时间在推进。

由于 \(u^\mu\) 是四维向量，它满足：

\[g_{\mu\nu} u^\mu u^\nu = -1\]

我们假设在闵可夫斯基度规 \(\eta_{\mu\nu}\) 附近的微扰度规 \(g_{\mu \nu}\)：

\[g_{\mu \nu} = \eta_{\mu \nu} + h_{\mu \nu}, \quad \text{where} \quad |h_{\mu \nu}| \ll 1\]

因此，有：

\[ g_{00}(u^0)^2 = -1 \quad \Rightarrow \quad u^0 = \left(-\frac{1}{g_{00}}\right)^{\frac{1}{2}} \approx 1 + \frac{1}{2}h_{00} \]

现在，将这些假设逐步代入张量方程，显式计算 \(T_{00}\) 分量：

\[
T_{00} = (\rho + p)(u^0)^2 + p g_{00}
\]

由 \(\rho \gg p\)，可化简为：

\[
T_{00} \approx \rho (1 - h_{00})
\]

接着，将能量-动量张量与度规张量 \(g^{\mu\nu}\) 收缩，计算标量 \(T\)：

\[
T = g^{\mu\nu} T_{\mu\nu}
\]

逐步显式计算可得：

\[
T = -\rho + 3p
\]

利用这些结果，我们将几何张量 \(G_{\mu\nu}\) 与物理张量 \(T_{\mu\nu}\) 联系起来，从而得到里奇张量分量 \(R_{00}\) 的表达式：

\[
R_{00} = G_{00} - \frac{1}{2} g_{00} G = \kappa\left(T_{00} - \frac{1}{2} g_{00} T\right)
\]

将对 \(T_{00}\) 与 \(T\) 的近似代入，并进一步逐步化简，最终得到：

\[
R_{00} = \frac{1}{2}\kappa \rho
\]

由此，我们成功建立了将时空几何曲率（黎曼张量分量 \(R_{00}\)）与物质的物理性质（能量密度 \(\rho\)）联系起来的关系。

然而，黎曼张量本身不够直观，因此我们引入其他几何量以便说明。具体而言，我们利用克里斯托费尔符号 \(\Gamma^\mu_{\alpha\beta}\) 的定义来展开里奇张量分量 \(R_{00}\)：

\[
R_{00} = R^\mu_{0\mu 0} = \partial_\mu \Gamma^\mu_{00} - \partial_0 \Gamma^\mu_{\mu 0} + \Gamma^\mu_{\mu \lambda} \Gamma^\lambda_{00} - \Gamma^\mu_{0\lambda}\Gamma^\lambda_{\mu 0}
\]

根据我们的慢速运动假设（\(\partial_0 \approx 0\)），可将该式化简为：

\[
R_{00} \approx \partial_\mu \Gamma^\mu_{00}
\]

现在，将克里斯托费尔符号用度规张量分量显式展开：

\[
\Gamma^\mu_{\alpha \beta} = \frac{1}{2}g^{\mu \lambda}(\partial_\beta g_{\lambda \alpha} + \partial_\alpha g_{\beta\lambda} - \partial_\lambda g_{\alpha\beta})
\]

代入该式，得到：

\[
R_{00} = \partial_\mu \left(\frac{1}{2}g^{\mu\lambda}(\partial_0 g_{\lambda 0} + \partial_0 g_{0\lambda} - \partial_\lambda g_{00})\right)
\]

由于在低速近似下 \(\partial_0 \approx 0\)，这可进一步化简为：

\[
R_{00} \approx -\frac{1}{2}\partial_\mu (g^{\mu\lambda}\partial_\lambda g_{00})
\]

考虑度规张量的微扰 \(g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}\) 并只保留一阶项（\(|h_{\mu\nu}|\ll 1\)），得到：

\[
R_{00} \approx -\frac{1}{2}\partial_\mu \partial^\mu h_{00}
\]

显式使用空间指标后，这成为一个类泊松方程：

\[
\nabla^2 h_{00} = -\kappa \rho
\]

---

既然我们已经在几何中的度规分量 \(h_{00}\) 与物理上的能量密度 \(\rho\) 之间建立了联系，我们的目标就是显式确定常数 \(\kappa\)。

为此，我们利用一种物理解释将度规分量 \(h_{00}\) 直接联系到牛顿引力。其直观依据是：广义相对论给出的几何描述在低速近似下必须与牛顿引力方程一致。

回顾牛顿引力满足：

\[
m\mathbf{a} = \mathbf{F} = -m\nabla \phi
\]

其中，\(\phi\) 表示引力势。要得到加速度 \(\mathbf{a}\) 的张量化表示，我们从四速度 \(u^\mu\) 出发。加速度 \(A^\mu\) 的张量形式为：

\[
A^\mu = \nabla_u u^\mu
\]

显式展开为：

\[
\nabla_u u 
= \nabla_{\frac{d x^p}{d \tau} \frac{\partial}{\partial x^p}} \frac{d x^\mu}{d \tau} \frac{\partial}{\partial x^\mu} 
= \frac{d x^p}{d \tau} \nabla_{\frac{\partial}{\partial x^p}} \frac{d x^\mu}{d \tau} \frac{\partial}{\partial x^\mu} 
\]

\[
= \frac{d x^p}{d \tau} \left[ \frac{\partial}{\partial x^p} \frac{d x^\mu}{d \tau} \frac{\partial}{\partial x^\mu} + \frac{\partial}{\partial x^p} \frac{\partial}{\partial x^\mu} \frac{d x^\mu}{d \tau} \right] 
\]

\[
= \frac{d x^p}{d \tau} \left[ \frac{\partial}{\partial x^p} \left( \frac{d x^\mu}{d \tau} \right) \frac{\partial}{\partial x^\mu} + \Gamma_{\rho \mu}^k \frac{\partial}{\partial x^p} \frac{d x^\mu}{d \tau} \right] 
\]

\[
= \frac{d x^p}{d \tau} \left[ \frac{\partial}{\partial x^p} \left( \frac{d x^\mu}{d \tau} \right) \frac{\partial}{\partial x^\mu} + \Gamma_{\rho \sigma}^\mu \frac{d x^\rho}{d \tau} \frac{\partial}{\partial x^\mu} \right] 
\]

\[
= \frac{d x^p}{d \tau} \left[ \frac{\partial}{\partial x^p} \left( \frac{d x^\mu}{d \tau} \right) + \Gamma_{p\sigma}^\mu \frac{d x^\sigma}{d \tau} \right] \frac{\partial}{\partial x^\mu}.
\]

从而得到：

\[
A^\mu = u^\nu\left(\frac{\partial u^\mu}{\partial x^\nu} + \Gamma^\mu_{\rho\nu} u^\rho\right)
\]

--- 

考虑 \( \mathbf{F} = 0 \) 的情形（不计引力以外的作用）。测地线方程变为：

\[
\frac{d^2 x^\mu}{d \tau^2} + \Gamma^\mu_{\rho\nu} \frac{d x^\rho}{d \tau} \frac{d x^\nu}{d \tau} = 0
\]

在慢速近似下，\( u^0 \gg u^i \)，因此可化简为：

\[
\frac{d^2 x^\mu}{d \tau^2} + \Gamma^\mu_{00} \left( \frac{d x^0}{d \tau} \right)^2 = 0
\]

由先前的计算可知：

\[
\Gamma^\mu_{00} = - \frac{1}{2} \eta^{\mu\lambda} \partial_\lambda h_{00}
\]

代入得：

\[
\frac{d^2 x^\mu}{d \tau^2} = \frac{1}{2} \eta^{\mu\lambda} \partial_\lambda h_{00} \left( \frac{d x^0}{d \tau} \right)^2
\]

只关注空间分量：

\[
\frac{d^2 x^i}{d t^2} = \frac{1}{2} \delta^{ij} \partial_j h_{00}
\]

由传统的牛顿方程，有：

\[
\frac{d^2 x^i}{d t^2} = - \delta^{ij} \partial_j \phi
\]

因此，得到：

\[
h_{00} = -2 \phi, g_{00} = -1 - 2\phi
\]

---

由牛顿引力中的泊松方程：

\[
\nabla^2 \phi = 4\pi G \rho
\]

鉴于 \( h_{00} = -2\phi \)，得到：

\[
\nabla^2 h_{00} = -8\pi G \rho
\]

于是得到

\[
\kappa = 8\pi G 
\]
