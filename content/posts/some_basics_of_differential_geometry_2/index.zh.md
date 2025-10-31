+++
date = '2025-01-28T11:05:09-05:00'
title = '微分几何基础 2'
tags = ['The Early Universe']
categories = ["Physics"]
+++

在本文中，我们将更深入探讨微分几何的概念，主要聚焦于黎曼张量、里奇张量以及标量曲率的概念。

## 一、黎曼张量

### A. 定义

我们从一个\(d\)维流形\(M\)出发，其上赋予了（伪）黎曼度规\(g_{\mu\nu}\)。与该度规相容的联络为Levi-Civita联络\(\nabla\)。黎曼曲率张量（常简称为黎曼张量）\(R^\rho_{\ \sigma\mu\nu}\)定义为作用在向量场\(V^\rho\)上的协变导数的对易子：
\[
\bigl[\nabla_\mu, \nabla_\nu\bigr] V^\rho 
\;=\; R^\rho_{\ \sigma\mu\nu} \, V^\sigma.
\]
用指标记号，另一种常见的写法是：
\[
R^\rho_{\ \sigma\mu\nu}
\;=\;
\partial_\mu \Gamma^\rho_{\nu\sigma}
\;-\;
\partial_\nu \Gamma^\rho_{\mu\sigma}
\;+\;
\Gamma^\rho_{\mu\lambda}\,\Gamma^\lambda_{\nu\sigma}
\;-\;
\Gamma^\rho_{\nu\lambda}\,\Gamma^\lambda_{\mu\sigma},
\]
其中\(\Gamma^\rho_{\mu\nu}\)是与Levi-Civita联络相关的Christoffel符号。

#### 记号约定

- 希腊指标\(\mu, \nu, \rho, \sigma, \ldots\)从0到\(d-1\)（若流形是\(d\)维）。
- 通过度规\(g_{\mu\nu}\)升降指标，例如\(V_\mu = g_{\mu\nu}V^\nu\)。
- \(\Gamma^\rho_{\mu\nu}\)为Christoffel符号，定义为
  \[
    \Gamma^\rho_{\mu\nu} 
    \;=\; 
    \frac{1}{2}\,g^{\rho\lambda}
    \Bigl(
      \partial_\mu g_{\lambda\nu}
      +\partial_\nu g_{\lambda\mu}
      -\partial_\lambda g_{\mu\nu}
    \Bigr).
  \]

### B. 通过沿闭合回路的平行移动推导

#### 1. 平行移动
考虑流形上的一个向量场\(V^\rho\)。沿曲线\(\gamma(\tau)\)对\(V^\rho\)进行的“平行移动”由条件给出：\(V^\rho\)沿该曲线的切向方向的协变导数为零。数学上表示为：
\[
\frac{dV^\rho}{d\tau} = \frac{d x^\mu}{d\tau} \nabla_\mu V^\rho = 0.
\]
展开协变导数，得到：
\[
\frac{dV^\rho}{d\tau} + \Gamma^\rho_{\mu\sigma} V^\sigma \frac{dx^\mu}{d\tau} = 0.
\]
该方程确保向量\(V^\rho\)沿着\(\gamma\)被携带，使其相对于流形的几何保持“尽可能恒定”。

#### 2. 回路平行移动与曲率
为了探究曲率的概念，考虑两条无限接近的曲线\(\gamma_1\)与\(\gamma_2\)，它们共同围成一个微小的闭合回路\(\partial\Sigma\)。将\(V^\rho\)沿此回路做平行移动。在平直流形中，向量完成回路后会返回到其初始值。然而在弯曲流形中，末端向量通常与初始值相差一个与回路面积成正比的小量。

数学上，这个差值（或“未能闭合”的量）由下式给出：
\[
\Delta V^\rho = R^\rho_{\ \sigma\mu\nu}\,V^\sigma\,\oint\!dx^\mu \wedge dx^\nu + \mathcal{O}(\text{higher order in area}),
\]
其中\(\oint dx^\mu \wedge dx^\nu\)表示回路的定向面积元。黎曼张量\(R^\rho_{\ \sigma\mu\nu}\)的出现精确编码了“如何以及相差多少”，即向量绕回路移动后如何“扭转”或“未能返回”，从而刻画流形的内在曲率。

#### 3. 从平行移动导出黎曼张量
考虑\(x^\mu\)-\(x^\nu\)平面内边长为\(\delta a\)与\(\delta b\)的一条小矩形回路。向量\(V^\rho\)沿四段路径被平行移动：
1. \(x \to x + \delta a e_\mu\)（沿\(\mu\)正向），
2. \(x + \delta a e_\mu \to x + \delta a e_\mu + \delta b e_\nu\)（沿\(\nu\)正向），
3. \(x + \delta a e_\mu + \delta b e_\nu \to x + \delta b e_\nu\)（沿\(\mu\)反向），
4. \(x + \delta b e_\nu \to x\)（沿\(\nu\)反向）。

对每一段，将平行移动方程展开到\(\delta a\)与\(\delta b\)的一阶。例如：
- 沿\(\mu\)正向平行移动：
  \[
  V^\rho \to V^\rho - \Gamma^\rho_{\mu\sigma} V^\sigma \delta a.
  \]
- 沿\(\nu\)正向平行移动：
  \[
  V^\rho \to V^\rho - \Gamma^\rho_{\nu\sigma} V^\sigma \delta b.
  \]
当沿\(-\mu\)与\(-\nu\)返回时，Christoffel符号在位移后的坐标处取值，从而产生类似\(\Gamma^\rho_{\mu\sigma}(x + \delta a e_\mu) \approx \Gamma^\rho_{\mu\sigma} + \delta a \partial_\mu \Gamma^\rho_{\mu\sigma}\)的项。

绕回路一周后，\(V^\rho\)的总变化来源于：
- Christoffel符号的对易子：
  \[
  [\Gamma_\nu, \Gamma_\mu]^\rho_\sigma = \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma} - \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma}.
  \]
- Christoffel符号的导数：
  \[
  \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma}.
  \]

将这些项合并得到：
\[
\Delta V^\rho = \left( \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma} \right) V^\sigma \delta a \delta b.
\]

#### 4. 识别黎曼张量
\(V^\sigma \delta a \delta b\)的系数正是黎曼张量：
\[
R^\rho_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda} \Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda} \Gamma^\lambda_{\mu\sigma}.
\]
反对称面积元\(\oint dx^\mu \wedge dx^\nu\)对应于\(\delta a \delta b\)（不计取向）。因此：
\[
\Delta V^\rho = R^\rho_{\sigma\mu\nu} V^\sigma \cdot (\text{Area of the loop}) + \mathcal{O}(\text{higher order}).
\]

### C. 几何诠释

1. 量化内禀曲率  
   黎曼张量通过描述向量在平行移动下如何变化来完整刻画局部曲率。若\(R^\rho_{\ \sigma\mu\nu} \equiv 0\)在某一区域恒为零，则该区域是平直的；存在（局部的）坐标变换，可将该邻域的度规化为标准欧几里得或闵可夫斯基形式（取决于符号）。

2. 例：球面上的平行移动

   为了探究球面的几何，我们从其在球坐标\((\theta, \phi)\)下的度规开始，其中\( \theta \)为极角，\( \phi \)为方位角。度规为：

   \[
   ds^2 = R^2 \bigl(d\theta^2 + \sin^2\theta\, d\phi^2\bigr),
   \]

   其中\( R \)表示球的半径。该表达式通过以坐标\(\theta\)和\(\phi\)的无穷小变化来度量距离，从而封装了球面的内在几何。

   由度规可直接读出度规张量\(g_{\mu\nu}\)的分量：
   - \( g_{\theta\theta} = R^2 \)，
   - \( g_{\phi\phi} = R^2 \sin^2\theta \)，
   - \( g_{\theta\phi} = g_{\phi\theta} = 0 \)（无交叉项）。

   逆度规分量\( g^{\mu\nu} \)满足\( g^{\mu\nu}g_{\nu\sigma} = \delta^\mu_\sigma \)，得到：
   - \( g^{\theta\theta} = \frac{1}{R^2} \)，
   - \( g^{\phi\phi} = \frac{1}{R^2 \sin^2\theta} \)，
   - \( g^{\theta\phi} = g^{\phi\theta} = 0 \)。

   Christoffel符号\(\Gamma^\lambda_{\mu\nu}\)刻画坐标基矢如何变化，其定义为：

   \[
   \Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\sigma} \bigl( \partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu} \bigr),
   \]

   其中\( \partial_\mu \)表示对坐标\(x^\mu\)的偏微分。

   利用度规分量及其导数，我们逐个计算Christoffel符号。

   对于\(\lambda = \theta\)：
   1. \(\Gamma^\theta_{\theta\theta}\)：
      \[
      \Gamma^\theta_{\theta\theta} = \frac{1}{2} g^{\theta\theta} \bigl( \partial_\theta g_{\theta\theta} + \partial_\theta g_{\theta\theta} - \partial_\theta g_{\theta\theta} \bigr) = 0.
      \]

   2. \(\Gamma^\theta_{\theta\phi}\)与\(\Gamma^\theta_{\phi\theta}\)：
      这些项涉及交叉导数并为零：
      \[
      \Gamma^\theta_{\theta\phi} = \Gamma^\theta_{\phi\theta} = 0.
      \]

   3. \(\Gamma^\theta_{\phi\phi}\)：
      利用\(g_{\phi\phi} = R^2 \sin^2\theta\)：
      \[
      \Gamma^\theta_{\phi\phi} = \frac{1}{2} g^{\theta\theta} \bigl( \partial_\phi g_{\phi\phi} + \partial_\phi g_{\phi\phi} - \partial_\theta g_{\phi\phi} \bigr) = -\sin\theta\cos\theta.
      \]

   对于\(\lambda = \phi\)：
   1. \(\Gamma^\phi_{\theta\theta}\)：
      由于\(g_{\phi\phi}\)与\(\phi\)无关，该项为零：
      \[
      \Gamma^\phi_{\theta\theta} = 0.
      \]

   2. \(\Gamma^\phi_{\theta\phi}\)与\(\Gamma^\phi_{\phi\theta}\)：
      使用\(g_{\phi\phi} = R^2 \sin^2\theta\)：
      \[
      \Gamma^\phi_{\theta\phi} = \Gamma^\phi_{\phi\theta} = \frac{1}{2} g^{\phi\phi} \bigl( \partial_\theta g_{\phi\phi} \bigr) = \cot\theta.
      \]

   3. \(\Gamma^\phi_{\phi\phi}\)：
      此项仅涉及\(g_{\phi\phi}\)对\(\phi\)的导数，故为零：
      \[
      \Gamma^\phi_{\phi\phi} = 0.
      \]

   球面的非零Christoffel符号为：
   \[
   \Gamma^\theta_{\phi\phi} = -\sin\theta\cos\theta, \quad \Gamma^\phi_{\theta\phi} = \Gamma^\phi_{\phi\theta} = \cot\theta.
   \]

   在赤道处，\(\sin\theta = 1\)且\(\cos\theta = 0\)。在\(\theta = \pi/2\)附近作小角度近似，令\(\Delta\theta = \theta - \frac{\pi}{2}\)，于是\(\sin\theta \approx 1\)且\(\cos\theta \approx -\Delta\theta\)。代入：

   - \(\Gamma^\theta_{\phi\phi} \approx -\Delta\theta = -\theta + \pi/2\)，
   - \(\Gamma^\phi_{\theta\phi} = \Gamma^\phi_{\phi\theta} \approx -\Delta\theta = -\theta + \pi/2\)。


   利用这些结果，计算黎曼张量的相关分量。

   1. 分量\( R^\theta_{\ \phi\theta\phi} \)：

      \[
      R^\theta_{\ \phi\theta\phi} = \partial_\theta \Gamma^\theta_{\phi\phi} - \partial_\phi \Gamma^\theta_{\theta\phi} + \Gamma^\theta_{\theta\lambda} \Gamma^\lambda_{\phi\phi} - \Gamma^\theta_{\phi\lambda} \Gamma^\lambda_{\theta\phi}.
      \]

      - 项\( \partial_\theta \Gamma^\theta_{\phi\phi} \)计算为\( \partial_\theta (-\sin\theta \cos\theta) = -\cos^2\theta + \sin^2\theta \)。在\( \theta = \pi/2 \)附近，这变为\( -1 \)。
      - 项\( \partial_\phi \Gamma^\theta_{\theta\phi} \)为零，因为\( \Gamma^\theta_{\theta\phi} = 0 \)。
      - 项\( \Gamma^\theta_{\theta\lambda} \Gamma^\lambda_{\phi\phi} \)亦为零，因为\( \Gamma^\theta_{\theta\theta} = 0 \)且\( \Gamma^\theta_{\theta\phi} = 0 \)。
      - 项\( \Gamma^\theta_{\phi\lambda} \Gamma^\lambda_{\theta\phi} \)化简为\( \Gamma^\theta_{\phi\phi} \Gamma^\phi_{\theta\phi} = (-\sin\theta \cos\theta)(\cot\theta) = -\cos^2\theta \)。在\( \theta = \pi/2 \)附近，这变为\( 0 \)。

      综上得到：

      \[
      R^\theta_{\ \phi\theta\phi} = -1 - 0 + 0 - 0 = -1.
      \]

   2. 分量\( R^\phi_{\ \theta\phi\theta} \)：

      由黎曼张量的反对称性，\( R^\phi_{\ \theta\phi\theta} = -R^\phi_{\ \theta\theta\phi} \)。用同样方法可得：

      \[
      R^\phi_{\ \theta\phi\theta} = -1.
      \]

   因此，在赤道附近，非零的黎曼张量分量为：

   \[
   R^\theta_{\ \phi\theta\phi} \approx -1, \quad R^\phi_{\ \theta\phi\theta} \approx -1.
   \]

   向量\( V^\mu \)沿小回路平行移动后的分量变化为：

   \[
   \Delta V^\mu = -\frac{1}{2} R^\mu_{\ \nu\alpha\beta} V^\nu \Sigma^{\alpha\beta},
   \]

   其中\( \Sigma^{\alpha\beta} \)是回路的坐标面积元，对\( \alpha \)与\( \beta \)反对称。对于边长为\( \delta\theta \)与\( \delta\phi \)的小矩形回路，坐标面积为：

   \[
   \Sigma^{\theta\phi} = \delta\theta \delta\phi, \quad \Sigma^{\phi\theta} = -\delta\theta \delta\phi.
   \]

   将黎曼张量分量与坐标面积代入公式，计算向量分量的变化。

   1. \( V^\theta \)的变化：

      \[
      \Delta V^\theta = -\frac{1}{2} R^\theta_{\ \nu\alpha\beta} V^\nu \Sigma^{\alpha\beta}.
      \]

      唯一的非零贡献来自\( R^\theta_{\ \phi\theta\phi} \)：

      \[
      \Delta V^\theta = -\frac{1}{2} R^\theta_{\ \phi\theta\phi} V^\phi \Sigma^{\theta\phi} - \frac{1}{2} R^\theta_{\ \phi\phi\theta} V^\phi \Sigma^{\phi\theta}.
      \]

      利用\( R^\theta_{\ \phi\phi\theta} = -R^\theta_{\ \phi\theta\phi} \)与\( \Sigma^{\phi\theta} = -\Sigma^{\theta\phi} \)，化简为：

      \[
      \Delta V^\theta = -R^\theta_{\ \phi\theta\phi} V^\phi \Sigma^{\theta\phi}.
      \]

      代入\( R^\theta_{\ \phi\theta\phi} \approx -1 \)与\( \Sigma^{\theta\phi} = \delta\theta \delta\phi \)，得到：

      \[
      \Delta V^\theta = V^\phi \delta\theta \delta\phi.
      \]

   2. \( V^\phi \)的变化：

      类似地，对\( V^\phi \)：

      \[
      \Delta V^\phi = -\frac{1}{2} R^\phi_{\ \nu\alpha\beta} V^\nu \Sigma^{\alpha\beta}.
      \]

      唯一的非零贡献来自\( R^\phi_{\ \theta\phi\theta} \)：

      \[
      \Delta V^\phi = -\frac{1}{2} R^\phi_{\ \theta\phi\theta} V^\theta \Sigma^{\theta\phi} - \frac{1}{2} R^\phi_{\ \theta\theta\phi} V^\theta \Sigma^{\phi\theta}.
      \]

      利用\( R^\phi_{\ \theta\theta\phi} = -R^\phi_{\ \theta\phi\theta} \)与\( \Sigma^{\phi\theta} = -\Sigma^{\theta\phi} \)，化简为：

      \[
      \Delta V^\phi = -R^\phi_{\ \theta\phi\theta} V^\theta \Sigma^{\theta\phi}.
      \]

      代入\( R^\phi_{\ \theta\phi\theta} \approx -1 \)与\( \Sigma^{\theta\phi} = \delta\theta \delta\phi \)，得到：

      \[
      \Delta V^\phi = -V^\theta \delta\theta \delta\phi.
      \]

   向量分量\( \Delta V^\theta \)与\( \Delta V^\phi \)的变化意味着该向量发生了一个角度为\( \Delta\alpha \)的旋转。具体地：

   \[
   \Delta\alpha = \delta\theta \delta\phi.
   \]

   为了用回路的物理面积\( \Sigma \)来表述，注意半径为\( R \)的球面上的物理面积为：

   \[
   \Sigma = R^2 \delta\theta \delta\phi.
   \]

   因此，旋转角变为：

   \[
   \Delta\alpha = \frac{\Sigma}{R^2}.
   \]

   #### 另一种方法：利用高斯-博内定理

   为了理解球面上平行移动时切向量的转角，我们借助微分几何中的一个强有力工具——高斯-博内定理，它将曲面的内禀曲率与其区域的拓扑联系起来。在此情境中，高斯-博内定理为确定沿小回路平行移动的切向量的总转角提供了几何框架。

   高斯-博内定理表明，对于带边界的光滑、紧致二维黎曼流形，沿闭合回路平行移动的切向量的总转角与所围区域的高斯曲率积分相关。数学上，对于包围区域\( D \)且高斯曲率为\( K \)的小回路，其总转角\( \Delta\alpha \)为：

   \[
   \Delta\alpha = \int\!\!\!\int_D K \, dA,
   \]

   其中\( dA \)是曲面上的面积元。对于半径为\( R \)的球面，高斯曲率\( K \)为常数，且为：

   \[
   K = \frac{1}{R^2}.
   \]

   对于球面赤道附近的小回路，其所围面积\( \Sigma \)近似可视为平坦，高斯曲率\( K \)可视为在该区域内常数。将\( K = \frac{1}{R^2} \)代入高斯-博内定理，得到：

   \[
   \Delta\alpha = \int\!\!\!\int_D K \, dA = K \cdot \Sigma = \frac{1}{R^2} \cdot \Sigma.
   \]

   因此，沿回路平行移动后切向量的总转角为：

   \[
   \Delta\alpha = \frac{\Sigma}{R^2}.
   \]

## 二、里奇张量与标量曲率

### A. 定义

从黎曼张量\(R^\rho_{\ \sigma\mu\nu}\)出发，通过对第1与第3指标做缩并构造里奇张量\(R_{\mu\nu}\)：
\[
R_{\mu\nu} 
\;=\; 
R^\rho_{\ \mu\rho\nu}.
\]
“里奇标量”（常称为标量曲率）\(R\)则是将里奇张量与度规再做一次缩并：
\[
R 
\;=\; 
g^{\mu\nu} R_{\mu\nu}.
\]

### B. 几何诠释与用途

全部的黎曼张量描述了曲率的所有方面（包括沿两个方向同时的“扭转”），而里奇张量是其迹，抓取“体积（或二维中的面积）如何变化”的信息。 

**1. 体积畸变与里奇张量**

在弯曲空间中，可以通过考察一个小区域的体积相对于平直空间的偏离来理解里奇张量与体积畸变之间的关系。以某点\(P\)为中心使用黎曼法向坐标（RNC），度规张量\(g_{\mu\nu}\)在\(P\)附近可展开为：

\[
g_{\mu\nu}(x) = \delta_{\mu\nu} - \frac{1}{3} R_{\mu\alpha\nu\beta} x^\alpha x^\beta + \mathcal{O}(x^3),
\]

其中\(R_{\mu\alpha\nu\beta}\)为黎曼曲率张量，\(\delta_{\mu\nu}\)表示平直度规。弯曲空间中的体积元与度规行列式\(g = \det(g_{\mu\nu})\)相关，其表达式为：

\[
\Delta V = \sqrt{g}\, \Delta V_\text{flat}.
\]

对于小区域，弯曲体积与平直体积之比为\(\sqrt{g}\)。对\(g_{\mu\nu} = \delta_{\mu\nu} + h_{\mu\nu}\)处的行列式\(g\)做展开，其中\(h_{\mu\nu} = -\frac{1}{3} R_{\mu\alpha\nu\beta} x^\alpha x^\beta\)，可得：

\[
g \approx 1 + \text{Tr}(h) + \mathcal{O}(h^2).
\]

\(h_{\mu\nu}\)的迹为：

\[
\text{Tr}(h) = h_{\mu\mu} = -\frac{1}{3} R_{\mu\alpha\mu\beta} x^\alpha x^\beta.
\]

利用\(R_{\mu\alpha\mu\beta} = R_{\alpha\beta}\)的对称与缩并性质（定义了里奇张量），这可化简为：

\[
\text{Tr}(h) = -\frac{1}{3} R_{\alpha\beta} x^\alpha x^\beta.
\]

因而到二阶为止，行列式变为：

\[
g \approx 1 - \frac{1}{3} R_{\alpha\beta} x^\alpha x^\beta.
\]

对\(g\)开方并展开至二阶得到：

\[
\sqrt{g} \approx 1 + \frac{1}{2} \text{Tr}(h) = 1 - \frac{1}{6} R_{\alpha\beta} x^\alpha x^\beta.
\]

于是，体积比表示为：

\[
\frac{\Delta V}{\Delta V_\text{flat}} \approx 1 - \frac{1}{6} R_{\mu\nu} X^\mu X^\nu,
\]

其中\(X^\mu\)表示该区域的特征尺度，例如按体积大小缩放的径向坐标。该公式揭示：弯曲空间中体积的主导阶畸变由里奇张量\(R_{\mu\nu}\)控制，它量化了相对于平直空间，小区域体积受到曲率影响的程度。

**2. 对畸变积分与标量曲率**

半径为\(\epsilon\)（其中\(\|\mathbf{X}\| = \epsilon\)）的测地球的体积\(V\)为：

\[
V = \int_{B(\epsilon)} \sqrt{\det g}\, d^dx \approx \int_{B(\epsilon)} \left(1 - \frac{1}{6}R_{kl}x^k x^l\right) d^dx
\]

其平直体积为\(V_{\text{flat}} = \omega_d \epsilon^d\)，其中\(\omega_d\)是单位\(d\)球的体积。

借助球对称性，积分\(\int_{B(\epsilon)} x^k x^l d^dx\)计算为：

\[
\int_{B(\epsilon)} x^k x^l d^dx = \frac{\omega_d \epsilon^{d+2}}{d+2} \delta^{kl}
\]

与里奇张量缩并得：

\[
\int_{B(\epsilon)} R_{kl}x^k x^l d^dx = R \frac{\omega_d \epsilon^{d+2}}{d+2}
\]

其中\(R = R_{kl}\delta^{kl}\)为里奇标量（标量曲率）。

代回体积积分：

\[
V \approx V_{\text{flat}} - \frac{1}{6} R \frac{\omega_d \epsilon^{d+2}}{d+2} = V_{\text{flat}} \left(1 - \frac{R}{6(d+2)} \epsilon^2 + \cdots \right)
\]

识别\(\epsilon^2 = \|\mathbf{X}\|^2\)，得到：

\[
\Delta V = \Delta V_{\text{flat}} \left(1 - \frac{R}{6(d+2)} \|\mathbf{X}\|^2 + \cdots \right)
\]

这表明，在\(d\)维中，小测地球体积的主导阶修正与里奇标量\(R\)成正比，说明\(R\)量化了由曲率导致的体积畸变。

\[
\Delta V = \Delta V_\mathrm{flat} \Bigl(1 - \frac{R}{6(d+2)} \|\mathbf{X}\|^2 + \ldots \Bigr)
\]

当把这些局部体积变化对一个区域积分时，标量曲率\(R\)会自然出现。这让人联想到二维中的高斯-博内定理如何把曲率的积分与Euler示性数联系起来，而在更高维度中，我们在体积与超曲面面积的展开式中看到里奇项与标量曲率的出现。

### C. 例：球面上小圆的面积

为了利用所给公式计算球面上小圆的面积，我们聚焦于二维，因为球面的表面本质上是二维的。我们将探讨里奇标量\(R\)如何与球面的曲率相关，并推导小测地圆的面积。

考虑一个二维球面（如地球表面），其半径为\(a\)。二维球面的里奇标量\(R\)与其高斯曲率\(K = 1/a^2\)的关系为：
\[
R = 2K = \frac{2}{a^2}.
\]
现在设想球面上一个坐标半径为\(\epsilon\)的小测地圆，其中\(\|\mathbf{X}\| = \epsilon\)且\(\epsilon \ll a\)。在平直（欧几里得）空间中，此圆的面积为：
\[
\Delta V_{\text{flat}} = \pi \epsilon^2.
\]

为了计入球面的曲率，我们使用体积展开公式：
\[
\Delta V = \Delta V_{\text{flat}} \left(1 - \frac{R}{6(d+2)} \|\mathbf{X}\|^2 + \ldots \right),
\]
其中\(d = 2\)表示球面表面的维数。代入\(R = 2/a^2\)与\(\|\mathbf{X}\|^2 = \epsilon^2\)，得到：
\[
\Delta V = \pi \epsilon^2 \left(1 - \frac{2/a^2}{6(2+2)} \epsilon^2 + \ldots \right).
\]
化简该系数：
\[
\frac{2/a^2}{24} = \frac{1}{12a^2},
\]
得到：
\[
\Delta V = \pi \epsilon^2 \left(1 - \frac{\epsilon^2}{12a^2} + \ldots \right).
\]

为了比较，我们来看半径为\(\epsilon\)（按弧长度量）的测地圆在球面上的精确面积：
\[
A_{\text{exact}} = 2\pi a^2 \left(1 - \cos\left(\frac{\epsilon}{a}\right)\right).
\]
对小的\(\epsilon \ll a\)，可将\(\cos(\epsilon/a)\)展开到四阶：
\[
\cos\left(\frac{\epsilon}{a}\right) \approx 1 - \frac{\epsilon^2}{2a^2} + \frac{\epsilon^4}{24a^4}.
\]
将其代入精确面积公式，得到：
\[
A_{\text{exact}} \approx 2\pi a^2 \left(\frac{\epsilon^2}{2a^2} - \frac{\epsilon^4}{24a^4}\right) = \pi \epsilon^2 - \frac{\pi \epsilon^4}{12a^2} + \ldots
\]

该结果与先前由体积展开公式得到的表达式一致：
\[
\Delta V = \pi \epsilon^2 \left(1 - \frac{\epsilon^2}{12a^2} + \ldots \right).
\]
校正项\(-\frac{\pi \epsilon^4}{12a^2}\)来自里奇标量\(R = 2/a^2\)，它量化了球面曲率相较于平直空间如何减小面积。

\[
\Delta A = \pi \epsilon^2 \left(1 - \frac{\epsilon^2}{12a^2} + \ldots \right)
\]

---

## 结论

1. 黎曼张量  
   - 定义：描述向量沿小回路平行移动后未能返回原方向的行为。  
   - 几何作用：编码关于曲率的最细致局部信息，包括在不同方向上的扭转与弯曲。

2. 里奇张量  
   - 定义：黎曼张量经\(R_{\mu\nu} = R^\rho_{\ \mu\rho\nu}\)缩并得到。  
   - 几何作用：聚焦曲率如何导致体积（二维中为面积）发生畸变。可视为黎曼张量的部分“迹”。

3. 标量曲率  
   - 定义：进一步的缩并\(R = g^{\mu\nu}R_{\mu\nu}\)。  
   - 几何作用：提供单一标量来度量曲率对体积畸变的影响，常出现在全局几何量的积分表达式中。

层级关系如下：
\[
\text{Riemann} \;\longrightarrow\; \text{Ricci} \;\longrightarrow\; \text{Scalar curvature}.
\]
越往下包含的细节越少，但提供更简洁与更聚合的曲率度量，最终归结为单一的标量\(R\)。在实际的几何与物理情境（例如广义相对论）中，里奇张量与标量曲率对于描述物质-能量如何扭曲时空几何至关重要，而黎曼张量则包含了关于几何方向如何“扭转与回旋”的全部信息。
