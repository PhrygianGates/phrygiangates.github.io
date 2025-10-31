+++
date = '2025-02-07T21:35:09+08:00'
title = '微分几何基础 3'
tags = ['The Early Universe']
categories = ["Physics"]
+++

在这篇文章中，我希望学习关于\( \nabla \)符号的一些基础知识，以及一个与黎曼曲率张量相关的重要公式。

## I. 联络

定义：光滑流形\( (M, \mathcal{O}) \)上的联络\( \nabla \)是一个映射，它把由向量场\( X \)和\( (p, q) \)-张量场\( T \)组成的有序对映射为\( (p, q) \)-张量场\( \nabla_X T \)，满足：

1. \( \nabla_X f = X f \), \(\forall f \in C^\infty(M) \)

2. \( \nabla_X (T + S) = \nabla_X T + \nabla_X S \)

3. \( \nabla_X (T(\omega, Y)) = (\nabla_X T)(\omega, Y) + T(\nabla_X \omega, Y) + T(\omega, \nabla_X Y) \)  
   （对于\( (1, 1) \)-张量场\( T \)，但对任意\( (p, q) \)-张量场\( T \)同理）。  
   （“莱布尼茨”）

4. \( \nabla_{fX + Z} T = f \nabla_X T + \nabla_Z T \),  
   \( f \in C^\infty(M) \).


为了使用给定的联络\( \nabla \)的定义来推导向量场\( Y \)的协变导数，我们按如下步骤进行：

步骤 1：在局部基中展开\( Y \)
设\( \{ \partial_i \} \)是向量场的坐标基且\( Y = Y^i \partial_i \)，其中\( Y^i \)是光滑函数。

步骤 2：应用联络在\( X \)上的线性性
对于\( X = X^i \partial_i \)，使用条件 4（在\( X \)上的线性性）：
\[
\nabla_X Y = X^i \nabla_{\partial_i} Y.
\]

步骤 3：使用莱布尼茨法则展开\( \nabla_{\partial_i} Y \)
对于\( Y = Y^j \partial_j \)，应用条件 2（线性性）和对乘积\( Y^j \partial_j \)的莱布尼茨法则（条件 3）：
\[
\nabla_{\partial_i} Y = \nabla_{\partial_i} (Y^j \partial_j) = (\nabla_{\partial_i} Y^j) \partial_j + Y^j \nabla_{\partial_i} \partial_j.
\]
由条件 1，\( \nabla_{\partial_i} Y^j = \partial_i Y^j \)。通过如下方式定义联络系数\( \Gamma^k_{ij} \)：
\[
\nabla_{\partial_i} \partial_j = \Gamma^k_{ij} \partial_k.
\]
于是：
\[
\nabla_{\partial_i} Y = (\partial_i Y^j) \partial_j + Y^j \Gamma^k_{ij} \partial_k = (\partial_i Y^k + Y^j \Gamma^k_{ij}) \partial_k.
\]

步骤 4：合并结果
代回到\( \nabla_X Y \)：
\[
\nabla_X Y = X^i (\partial_i Y^k + Y^j \Gamma^k_{ij}) \partial_k.
\]
这给出在坐标中的\( Y \)的协变导数：
\[
\nabla_X Y = \left( X^i \partial_i Y^k + X^i Y^j \Gamma^k_{ij} \right) \partial_k.
\]

最终表达式：
向量场\( Y = Y^i \partial_i \)关于\( X = X^j \partial_j \)的协变导数为：
\[
\boxed{ \nabla_X Y = \left( X^j \partial_j Y^i + X^j Y^k \Gamma^i_{jk} \right) \partial_i }.
\]

## II. 测地线偏差方程

测地线偏差方程（也称为雅可比方程）描述了弯曲时空中相邻测地线彼此如何偏离。该方程在广义相对论中至关重要，因为它量化了由于时空曲率而产生的潮汐力。

数学表述
该方程为：

\[
\frac{D^2 \xi^\mu}{D \tau^2} + R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma = 0
\]

其中：
- \( \xi^\mu \)是相邻测地线之间的分离向量。
- \( U^\mu = \frac{dx^\mu}{d\tau} \)是测地线的切向量（在相对论中为四速度）。
- \( \frac{D}{D\tau} \)是沿测地线的协变导数。
- \( R^\mu_{\ \nu\rho\sigma} \)是黎曼曲率张量。
- \( \tau \)是沿测地线的固有时。

解释
- 第一项\( \frac{D^2 \xi^\mu}{D \tau^2} \)表示测地线之间分离的加速度。
- 第二项\( R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma \)描述了时空曲率（由黎曼张量编码）如何影响测地线分离。

该方程对于理解引力潮汐效应是基础性的，因为它揭示了自由下落中的小物体（例如在大质量天体附近）如何由于时空曲率而经历相对加速度。

测地线偏差方程是通过分析弯曲时空中两条相邻测地线之间的相对加速度推导得到的。以下是逐步推导：

1. 设置：测地线族
考虑一族单参数测地线\( x^\mu(\tau, s) \)，其中：
- \( \tau \)是每条测地线上的固有时。
- \( s \)为相邻测地线的标记。

测地线的切向量为：
\[
U^\mu = \frac{\partial x^\mu}{\partial \tau},
\]
而两条无限接近的测地线之间的分离向量为：
\[
\xi^\mu = \frac{\partial x^\mu}{\partial s}.
\]

2. 交换子关系
由于\( U \)和\( \xi \)是坐标基矢量，它们的李括号为零：
\[
[U, \xi] = 0 \implies \nabla_U \xi^\mu = \nabla_\xi U^\mu.
\]
这保证了分离向量\( \xi^\mu \)沿着\( U \)被李输运。

3. 第一阶协变导数
沿测地线的\( \xi^\mu \)的第一阶导数为：
\[
\frac{D \xi^\mu}{D \tau} = \nabla_U \xi^\mu = \nabla_\xi U^\mu.
\]

4. 第二阶协变导数
相对加速度即为第二阶协变导数：
\[
\frac{D^2 \xi^\mu}{D \tau^2} = \nabla_U \left( \nabla_U \xi^\mu \right) = \nabla_U \left( \nabla_\xi U^\mu \right).
\]

5. 协变导数的交换子
使用协变导数的交换子恒等式：
\[
[\nabla_U, \nabla_\xi] U^\mu = \nabla_U \nabla_\xi U^\mu - \nabla_\xi \nabla_U U^\mu.
\]
第二项为零，因为\( \nabla_U U^\mu = 0 \)（测地线方程）。因此：
\[
\nabla_U \nabla_\xi U^\mu = [\nabla_U, \nabla_\xi] U^\mu.
\]

6. 黎曼张量关系
协变导数的交换子引入黎曼曲率张量：
\[
[\nabla_U, \nabla_\xi] U^\mu = R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma.
\]
这里，\( R^\mu_{\ \nu\rho\sigma} \)编码了时空曲率。

7. 最终方程
综合上述结果：
\[
\frac{D^2 \xi^\mu}{D \tau^2} = R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma.
\]
重排得到测地线偏差方程：
\[
\boxed{\frac{D^2 \xi^\mu}{D \tau^2} + R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma = 0.}
\]
