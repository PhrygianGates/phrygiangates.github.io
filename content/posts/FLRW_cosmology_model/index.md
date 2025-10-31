+++
date = '2025-04-13T17:51:09+08:00'
title = 'FLRW Cosmology Model'
tags = ['The Early Universe']
categories = ["Physics"]
+++

In this post, I would like to introduce the basic assumption of modern cosmology, i.e. the FLRW model, also as an application of Einstein field equation.

The idea is simple, given a FLRW metric, plug into the field equation, then we deduce how the space scale \(a\) (which is a parameter of the metric) changes along with the \(t\) coordinates. Here I express the computation in a Python program.

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

Plug in the final Einstein tensor into the Einstein equation. Let's take \( G_{tt} \) as an example:

\[
G_{tt} = 8\pi G T_{tt} \quad (\text{we use natural units, so } c = 1)
\]

\[
T_{tt} = \rho \quad (\rho \text{ can be understood as energy density or mass density, since } E = mc^2 \text{ in natural units})
\]

So, plugging in the result of \( G_{tt} \), we have:

\[
3 \frac{k + \dot{a}^2}{a^2} = 8\pi G \rho
\]

\[
\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3} \rho - \frac{k}{a^2}
\]

Similarly, for the spatial components of the Einstein tensor \( G_{ij} \), we can get the Friedmann equation for the spatial components:

\[
2 \frac{\ddot{a}}{a} + \left(\frac{\dot{a}}{a}\right)^2 + \frac{k}{a^2} = -8\pi G p
\]

---

The deduction is not difficult, but I would like to emphasize a bit more on the purpose of the FLRW metric. It's based on the assumption that:

1. The space is isotropic, represented by the term \( \frac{dr^2}{1-kr^2} + r^2(d\theta^2 + \sin^2\theta \, d\phi^2) \). This is the origin of this term.

2. The spacetime changes along the \( t \)-axis. This is why we have a time-varying scale factor \( a(t) \) in the FLRW model. This comes from the experimental observation of the redshift phenomenon, where distant stars are moving away from us. However, this does not mean that the shape of the manifold changes over time. Instead, it means that if we move along the \( t \)-axis, we will find that the metric of the manifold changes. The manifold itself does not change.


