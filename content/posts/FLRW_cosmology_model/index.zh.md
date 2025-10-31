+++
date = '2025-04-13T17:51:09+08:00'
title = '弗里德曼-勒梅特-罗伯逊-沃尔克宇宙学模型'
tags = ['The Early Universe']
categories = ["Physics"]
+++

在这篇文章中，我想介绍现代宇宙学的基本假设，即FLRW模型，同时也作为爱因斯坦场方程的一个应用。

思路很简单：给定一个FLRW度规，代入场方程，然后我们就能推导出尺度因子\(a\)（它是度规的一个参数）如何随\(t\)坐标变化。这里我用一个Python程序来表达这些计算。

---

```python
import sympy as sp
from sympy.diffgeom import Manifold, Patch, CoordSystem, TensorProduct
from sympy.diffgeom.diffgeom import metric_to_Ricci_components, metric_to_Christoffel_2nd
from sympy import Symbol, Function, sin, simplify, Matrix

# Define spacetime dimensions
dim = 4

# Define manifold and coordinate system (using spherical coordinates)
M = Manifold('M', dim)
patch = Patch('P', M)
coords = CoordSystem('coords', patch, [
    Symbol('t', real=True),
    Symbol('r', real=True, positive=True),
    Symbol('theta', real=True, positive=True),
    Symbol('phi', real=True)
])

# Get coordinate functions and basic one-forms
t, r, theta, phi = coords.coord_functions()
dt, dr, dtheta, dphi = coords.base_oneforms()

# Define scale factor and curvature parameter (using natural units c=1)
a = Function('a')(t)  # Scale factor as a function of time
k = Symbol('k')       # Spatial curvature parameter

# Construct FLRW metric
# ds² = -dt² + a(t)²[dr²/(1-kr²) + r²(dθ² + sin²θ dφ²)]
g = -TensorProduct(dt, dt) + \
    a**2 * (TensorProduct(dr, dr)/(1-k*r**2) + \
            r**2 * TensorProduct(dtheta, dtheta) + \
            r**2 * sin(theta)**2 * TensorProduct(dphi, dphi))

# Matrix form of the metric (for Einstein tensor calculation)
g_matrix = Matrix([
    [-1, 0, 0, 0],
    [0, a**2/(1-k*r**2), 0, 0],
    [0, 0, a**2*r**2, 0],
    [0, 0, 0, a**2*r**2*sin(theta)**2]
])

# Calculate Christoffel symbols
Christoffel = metric_to_Christoffel_2nd(g)

# Calculate Ricci tensor
Ricci_tensor = metric_to_Ricci_components(g)

# Define coordinate index names
coord_names = ['t', 'r', 'θ', 'φ']

# Calculate inverse metric tensor
g_inverse = Matrix([
    [-1, 0, 0, 0],
    [0, (1-k*r**2)/a**2, 0, 0],
    [0, 0, 1/(a**2*r**2), 0],
    [0, 0, 0, 1/(a**2*r**2*sin(theta)**2)]
])

# Calculate Ricci scalar R = g^{μν} * R_{μν}
Ricci_scalar = 0
for i in range(dim):
    for j in range(dim):
        Ricci_scalar += g_inverse[i, j] * Ricci_tensor[i, j]
Ricci_scalar = simplify(Ricci_scalar)

# Calculate Einstein tensor G_μν = R_μν - (1/2) * g_μν * R
Einstein_tensor = Matrix([[0 for _ in range(dim)] for _ in range(dim)])
for i in range(dim):
    for j in range(dim):
        Einstein_tensor[i, j] = Ricci_tensor[i, j] - (1/2) * g_matrix[i, j] * Ricci_scalar
        Einstein_tensor[i, j] = simplify(Einstein_tensor[i, j])

# Print Christoffel symbols
print("Christoffel symbols of FLRW metric (Γ^μ_νρ):")
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            if Christoffel[i, j, k] != 0:
                print(f"Γ^{coord_names[i]}_{coord_names[j]}{coord_names[k]} = {simplify(Christoffel[i, j, k])}")

# Print Ricci tensor
print("\nRicci tensor of FLRW metric (R_μν):")
for i in range(dim):
    for j in range(dim):
        if Ricci_tensor[i, j] != 0:
            print(f"R_{coord_names[i]}{coord_names[j]} = {simplify(Ricci_tensor[i, j])}")

# Print Ricci scalar
print("\nRicci scalar of FLRW metric (R):")
print(f"R = {Ricci_scalar}")

# Print Einstein tensor
print("\nEinstein tensor of FLRW metric (G_μν):")
for i in range(dim):
    for j in range(dim):
        if Einstein_tensor[i, j] != 0:
            print(f"G_{coord_names[i]}{coord_names[j]} = {Einstein_tensor[i, j]}")
```
```
Christoffel symbols of FLRW metric (Γ^μ_νρ):
Γ^t_rr = -a(t)*Subs(Derivative(a(_xi), _xi), _xi, t)/(k*r**2 - 1)
Γ^t_θθ = a(t)*r**2*Subs(Derivative(a(_xi), _xi), _xi, t)
Γ^t_φφ = a(t)*sin(theta)**2*r**2*Subs(Derivative(a(_xi), _xi), _xi, t)
Γ^r_tr = Subs(Derivative(a(_xi), _xi), _xi, t)/a(t)
Γ^r_rt = Subs(Derivative(a(_xi), _xi), _xi, t)/a(t)
Γ^r_rr = -k*r/(k*r**2 - 1)
Γ^r_θθ = k*r**3 - r
Γ^r_φφ = (k*r**2 - 1)*sin(theta)**2*r
Γ^θ_tθ = Subs(Derivative(a(_xi), _xi), _xi, t)/a(t)
Γ^θ_rθ = 1/r
Γ^θ_θt = Subs(Derivative(a(_xi), _xi), _xi, t)/a(t)
Γ^θ_θr = 1/r
Γ^θ_φφ = -sin(2*theta)/2
Γ^φ_tφ = Subs(Derivative(a(_xi), _xi), _xi, t)/a(t)
Γ^φ_rφ = 1/r
Γ^φ_θφ = 1/tan(theta)
Γ^φ_φt = Subs(Derivative(a(_xi), _xi), _xi, t)/a(t)
Γ^φ_φr = 1/r
Γ^φ_φθ = 1/tan(theta)

Ricci tensor of FLRW metric (R_μν):
R_tt = -3*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t)/a(t)
R_rr = (-2*k - a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) - 2*Subs(Derivative(a(_xi), _xi), _xi, t)**2)/(k*r**2 - 1)
R_θθ = (2*k + a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) + 2*Subs(Derivative(a(_xi), _xi), _xi, t)**2)*r**2
R_φφ = (2*k + a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) + 2*Subs(Derivative(a(_xi), _xi), _xi, t)**2)*sin(theta)**2*r**2

Ricci scalar of FLRW metric (R):
R = 6*(k + a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) + Subs(Derivative(a(_xi), _xi), _xi, t)**2)/a(t)**2

Einstein tensor of FLRW metric (G_μν):
G_tt = 3.0*(k + Subs(Derivative(a(_xi), _xi), _xi, t)**2)/a(t)**2
G_rr = (1.0*k + 2.0*a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) + 1.0*Subs(Derivative(a(_xi), _xi), _xi, t)**2)/(k*r**2 - 1)
G_θθ = (-1.0*k - 2.0*a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) - 1.0*Subs(Derivative(a(_xi), _xi), _xi, t)**2)*r**2
G_φφ = (-1.0*k - 2.0*a(t)*Subs(Derivative(a(_xi), (_xi, 2)), _xi, t) - 1.0*Subs(Derivative(a(_xi), _xi), _xi, t)**2)*sin(theta)**2*r**2
```

---

将最终的爱因斯坦张量代入爱因斯坦方程。以\( G_{tt} \)为例：

\[
G_{tt} = 8\pi G T_{tt} \quad (\text{we use natural units, so } c = 1)
\]

\[
T_{tt} = \rho \quad (\rho \text{ can be understood as energy density or mass density, since } E = mc^2 \text{ in natural units})
\]

因此，代入\( G_{tt} \)的结果，我们有：

\[
3 \frac{k + \dot{a}^2}{a^2} = 8\pi G \rho
\]

\[
\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3} \rho - \frac{k}{a^2}
\]

类似地，对于爱因斯坦张量的空间分量\( G_{ij} \)，我们可以得到空间分量的弗里德曼方程：

\[
2 \frac{\ddot{a}}{a} + \left(\frac{\dot{a}}{a}\right)^2 + \frac{k}{a^2} = -8\pi G p
\]

---

推导并不困难，但我想多强调一下FLRW度规的目的。它基于如下假设：

1. 空间是各向同性的，用\( \frac{dr^2}{1-kr^2} + r^2(d\theta^2 + \sin^2\theta \, d\phi^2) \)这一项来表示。这就是该项的由来。

2. 时空沿着\( t \)轴发生变化。这就是为什么在FLRW模型中会出现随时间变化的尺度因子\( a(t) \)。这源于对红移现象的实验观测，即遥远的恒星正在远离我们。然而，这并不意味着流形的形状会随时间改变。相反，这意味着如果我们沿着\( t \)轴移动，我们会发现流形的度规发生变化。流形本身并未改变。
