+++
date = '2025-01-21T07:21:09-05:00'
title = '微分几何的一些基础'
tags = ['The Early Universe']
categories = ["Physics"]
+++

在这篇文章中，我希望建立一些微分几何的基础，以便理解爱因斯坦场方程。

## 1. 黎曼曲率张量及其性质

### 黎曼曲率张量的定义：
黎曼曲率张量 \( R^i_{jkl} \) 是微分几何中的一个基本对象，表示流形的内禀曲率。其定义为：
\[
R^i_{jkl} = \partial_k \Gamma^i_{jl} - \partial_l \Gamma^i_{jk} + \Gamma^i_{km} \Gamma^m_{jl} - \Gamma^i_{lm} \Gamma^m_{jk}
\]
其中 \( \Gamma^i_{jk} \) 是克里斯托费尔符号。

### 黎曼曲率张量的性质：
1. 比安基恒等式：
   \[
   \nabla_m R^i_{jkl} + \nabla_k R^i_{jlm} + \nabla_l R^i_{jmk} = 0
   \]

2. 对称性：
   - 在最后两个指标上反对称：
     \[
     R^i_{jkl} = -R^i_{jlk}
     \]
   - 在交换第一对与第二对指标时反对称：
     \[
     R^i_{jkl} = -R^j_{ikl}
     \]

3. 应用：
   - 黎曼张量刻画当沿闭合回路进行平行输运时，向量被旋转或改变的程度。


## 2. 测地线及其推导原理

### 测地线方程：
测地线是在弯曲空间中连接两点的最短路径，其方程可通过极小化作用量得到：
\[
\int ds = \int \sqrt{g_{\mu \nu} \frac{dx^\mu}{d\tau} \frac{dx^\nu}{d\tau}} \, d\tau
\]
其中 \( g_{\mu \nu} \) 是度量张量，\( \tau \) 是仿射参数。

对该作用量取变分得到测地线方程：
\[
\frac{d^2 x^k}{d\tau^2} + \Gamma^k_{ij} \frac{dx^i}{d\tau} \frac{dx^j}{d\tau} = 0
\]
其中 \( \Gamma^k_{ij} \) 是克里斯托费尔符号。

### 关键要点：
- 物理意义：测地线将直线的概念推广到弯曲空间。
- 克里斯托费尔符号 \( \Gamma^k_{ij} \) 编码了空间的弯曲方式，并影响测地线的路径。


## 3. 协变导数与克里斯托费尔符号的作用

### 定义：
协变导数将导数的概念推广到弯曲空间，考虑了坐标基的变化。对于向量场 \( v^i \)，其协变导数为：
\[
\nabla_j v^i = \partial_j v^i + \Gamma^i_{jk} v^k
\]
其中 \( \Gamma^i_{jk} \) 是克里斯托费尔符号。

### 克里斯托费尔符号的直观含义：
克里斯托费尔符号 \( \Gamma^k_{ij} \) 描述了基矢量沿某一坐标方向如何变化。例如：
\[
\partial_j \vec{e}_i = \Gamma^k_{ij} \vec{e}_k 
\]
这意味着基矢量 \( \vec{e}_i \) 对第 \( j \) 个坐标的导数是基矢量的线性组合。直观地，它刻画了坐标基在流形中如何“扭转”或“伸缩”。

## 4. 球坐标中克里斯托费尔符号的几何推导

### 1. 克里斯托费尔符号 \( \Gamma^\phi_{\;r\phi} = \frac{1}{r} \)

#### 几何意义：
克里斯托费尔符号 \( \Gamma^\phi_{\;r\phi} \) 编码了向量 \( \frac{\partial}{\partial \phi} \)（切于常数 \( r \) 与 \( \theta \) 的圆）在 \( r \) 变化时如何变化。这反映了由于这些圆的扩张或收缩而导致的 \( \phi \) 基矢量的尺度变化。

#### 推导：
1. 回忆球坐标下 \( \frac{\partial}{\partial \phi} \) 的表达式：
   \[
   \frac{\partial}{\partial \phi} = r \sin\theta \, (-\sin\phi, \cos\phi, 0).
   \]

2. 对 \( r \) 求导：
   \[
   \frac{\partial}{\partial r} \biggl(\frac{\partial}{\partial \phi}\biggr) = \sin\theta \, (-\sin\phi, \cos\phi, 0).
   \]

3. 提取出原始向量 \( \frac{\partial}{\partial \phi} \) 作为因子：
   \[
   \frac{\partial}{\partial r} \biggl(\frac{\partial}{\partial \phi}\biggr) = \frac{1}{r} \, \frac{\partial}{\partial \phi}.
   \]

4. 解释：
   - 这表明 \( \frac{\partial}{\partial \phi} \) 对 \( r \) 的变化与其自身成正比。
   - 比例常数是 \( \frac{1}{r} \)，对应于 \( \Gamma^\phi_{\;r\phi} \)。

#### 物理洞见：
随着 \( r \) 增大，\( \phi \) 圆的半径随 \( r \) 线性增长，导致 \( \frac{\partial}{\partial \phi} \)（切向于该圆）按比例伸长。这种线性缩放解释了为何 \( \Gamma^\phi_{\;r\phi} = \frac{1}{r} \)。

---

### 2. 克里斯托费尔符号 \( \Gamma^\phi_{\;\theta\phi} = \cot\theta \)

#### 几何意义：
克里斯托费尔符号 \( \Gamma^\phi_{\;\theta\phi} \) 反映当 \( \theta \) 变化时向量 \( \frac{\partial}{\partial \phi} \) 如何变化。这描述了在不同余纬（\( \theta \)）处圆的半径变化的影响。

#### 推导：
1. 回忆 \( \frac{\partial}{\partial \phi} \) 的表达式：
   \[
   \frac{\partial}{\partial \phi} = r \sin\theta \, (-\sin\phi, \cos\phi, 0).
   \]

2. 对 \( \theta \) 求导：
   \[
   \frac{\partial}{\partial \theta} \biggl(\frac{\partial}{\partial \phi}\biggr) = r \cos\theta \, (-\sin\phi, \cos\phi, 0).
   \]

3. 提取 \( \frac{\partial}{\partial \phi} \)：
   \[
   \frac{\partial}{\partial \theta} \biggl(\frac{\partial}{\partial \phi}\biggr) = \cot\theta \, \frac{\partial}{\partial \phi}.
   \]

4. 解释：
   - \( \frac{\partial}{\partial \phi} \) 对 \( \theta \) 的变化与其自身成正比，比例常数为 \( \cot\theta \)，对应于 \( \Gamma^\phi_{\;\theta\phi} \)。

#### 物理洞见：
在不同的 \( \theta \) 处，\( \phi \) 圆的半径为 \( r \sin\theta \)。当 \( \theta \) 变化时，该半径按 \( \cos\theta \) 缩放。相对于半径的变化率是 \( \cot\theta \)，这就解释了为何 \( \Gamma^\phi_{\;\theta\phi} = \cot\theta \)。
