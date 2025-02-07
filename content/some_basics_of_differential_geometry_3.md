+++
date = '2025-02-07T21:35:09+08:00'
katex = true
title = 'Some Basics of Differential Geometry 3'
tags = ['The Early Universe']
+++

## I. Connection

**Definition:** A connection \( \nabla \) on a smooth manifold \( (M, \mathcal{O}) \) is a map that takes a pair consisting of a vector field \( X \) and a \( (p, q) \)-tensor field \( T \) and sends them to a \( (p, q) \)-tensor field \( \nabla_X T \), satisfying:

1. \( \nabla_X f = X f \), \(\forall f \in C^\infty(M) \)

2. \( \nabla_X (T + S) = \nabla_X T + \nabla_X S \)

3. \( \nabla_X (T(\omega, Y)) = (\nabla_X T)(\omega, Y) + T(\nabla_X \omega, Y) + T(\omega, \nabla_X Y) \)  
   (For \( (1, 1) \)-tensor field \( T \), but analogously for any \( (p, q) \)-tensor field \( T \)).  
   ("Leibniz")

4. \( \nabla_{fX + Z} T = f \nabla_X T + \nabla_Z T \),  
   \( f \in C^\infty(M) \).


To deduce the covariant derivative of a vector field \( Y \) using the given definition of a connection \( \nabla \), we proceed as follows:

**Step 1: Expand \( Y \) in a Local Basis**
Let \( \{ \partial_i \} \) be a coordinate basis for vector fields and \( Y = Y^i \partial_i \), where \( Y^i \) are smooth functions.

**Step 2: Apply the Connection Linearity in \( X \)**
For \( X = X^i \partial_i \), use condition 4 (linearity in \( X \)):
\[
\nabla_X Y = X^i \nabla_{\partial_i} Y.
\]

**Step 3: Expand \( \nabla_{\partial_i} Y \) Using the Leibniz Rule**
For \( Y = Y^j \partial_j \), apply condition 2 (linearity) and the Leibniz rule (condition 3) for the product \( Y^j \partial_j \):
\[
\nabla_{\partial_i} Y = \nabla_{\partial_i} (Y^j \partial_j) = (\nabla_{\partial_i} Y^j) \partial_j + Y^j \nabla_{\partial_i} \partial_j.
\]
By condition 1, \( \nabla_{\partial_i} Y^j = \partial_i Y^j \). Define the connection coefficients \( \Gamma^k_{ij} \) via:
\[
\nabla_{\partial_i} \partial_j = \Gamma^k_{ij} \partial_k.
\]
Thus:
\[
\nabla_{\partial_i} Y = (\partial_i Y^j) \partial_j + Y^j \Gamma^k_{ij} \partial_k = (\partial_i Y^k + Y^j \Gamma^k_{ij}) \partial_k.
\]

**Step 4: Combine Results**
Substitute back into \( \nabla_X Y \):
\[
\nabla_X Y = X^i (\partial_i Y^k + Y^j \Gamma^k_{ij}) \partial_k.
\]
This gives the covariant derivative of \( Y \) in coordinates:
\[
\nabla_X Y = \left( X^i \partial_i Y^k + X^i Y^j \Gamma^k_{ij} \right) \partial_k.
\]

**Final Expression:**
The covariant derivative of a vector field \( Y = Y^i \partial_i \) with respect to \( X = X^j \partial_j \) is:
\[
\boxed{ \nabla_X Y = \left( X^j \partial_j Y^i + X^j Y^k \Gamma^i_{jk} \right) \partial_i }.
\]

## II. Geodesic Deviation Equation

The **Geodesic Deviation Equation**, also known as the **Jacobi equation**, describes how nearby geodesics in a curved spacetime deviate from each other. This equation is crucial in general relativity as it quantifies tidal forces due to spacetime curvature.

### **Mathematical Formulation**
The equation is:

\[
\frac{D^2 \xi^\mu}{D \tau^2} + R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma = 0
\]

where:
- \( \xi^\mu \) is the **separation vector** between two neighboring geodesics.
- \( U^\mu = \frac{dx^\mu}{d\tau} \) is the **tangent vector** to the geodesic (4-velocity in relativity).
- \( \frac{D}{D\tau} \) is the **covariant derivative** along the geodesic.
- \( R^\mu_{\ \nu\rho\sigma} \) is the **Riemann curvature tensor**.
- \( \tau \) is the **proper time** along the geodesic.

### **Interpretation**
- The first term \( \frac{D^2 \xi^\mu}{D \tau^2} \) represents the **acceleration of separation** between geodesics.
- The second term \( R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma \) describes how spacetime curvature (encoded in the Riemann tensor) influences geodesic separation.

This equation is fundamental in understanding **gravitational tidal effects**, as it shows how small objects in free fall (such as in the presence of a massive body) experience relative acceleration due to the curvature of spacetime.

The geodesic deviation equation is derived by analyzing the relative acceleration between two neighboring geodesics in a curved spacetime. Here's a step-by-step deduction:

### **1. Setup: Family of Geodesics**
Consider a one-parameter family of geodesics \( x^\mu(\tau, s) \), where:
- \( \tau \) is the proper time along each geodesic.
- \( s \) labels neighboring geodesics.

The **tangent vector** to the geodesics is:
\[
U^\mu = \frac{\partial x^\mu}{\partial \tau},
\]
and the **separation vector** between infinitesimally close geodesics is:
\[
\xi^\mu = \frac{\partial x^\mu}{\partial s}.
\]

### **2. Commutator Relation**
Since \( U \) and \( \xi \) are coordinate basis vectors, their Lie bracket vanishes:
\[
[U, \xi] = 0 \implies \nabla_U \xi^\mu = \nabla_\xi U^\mu.
\]
This ensures the separation vector \( \xi^\mu \) is Lie-transported along \( U \).

### **3. First Covariant Derivative**
The first derivative of \( \xi^\mu \) along the geodesic is:
\[
\frac{D \xi^\mu}{D \tau} = \nabla_U \xi^\mu = \nabla_\xi U^\mu.
\]

### **4. Second Covariant Derivative**
The relative acceleration is the second covariant derivative:
\[
\frac{D^2 \xi^\mu}{D \tau^2} = \nabla_U \left( \nabla_U \xi^\mu \right) = \nabla_U \left( \nabla_\xi U^\mu \right).
\]

### **5. Commutator of Covariant Derivatives**
Using the commutator identity for covariant derivatives:
\[
[\nabla_U, \nabla_\xi] U^\mu = \nabla_U \nabla_\xi U^\mu - \nabla_\xi \nabla_U U^\mu.
\]
The second term vanishes because \( \nabla_U U^\mu = 0 \) (geodesic equation). Thus:
\[
\nabla_U \nabla_\xi U^\mu = [\nabla_U, \nabla_\xi] U^\mu.
\]

### **6. Riemann Tensor Relation**
The commutator of covariant derivatives introduces the Riemann curvature tensor:
\[
[\nabla_U, \nabla_\xi] U^\mu = R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma.
\]
Here, \( R^\mu_{\ \nu\rho\sigma} \) encodes the spacetime curvature.

### **7. Final Equation**
Combining the results:
\[
\frac{D^2 \xi^\mu}{D \tau^2} = R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma.
\]
Rearranging gives the **geodesic deviation equation**:
\[
\boxed{\frac{D^2 \xi^\mu}{D \tau^2} + R^\mu_{\ \nu\rho\sigma} U^\nu \xi^\rho U^\sigma = 0.}
\]

