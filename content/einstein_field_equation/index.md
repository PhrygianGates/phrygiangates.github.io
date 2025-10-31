+++
date = '2025-03-07T00:15:09+08:00'
title = 'Einstein Field Equation'
tags = ['The Early Universe']
+++

To derive the Einstein field equation, we start from physical considerations involving energy and momentum, and geometry considerations from the curvature of spacetime.

---
The Einstein field equation relies on three fundamental assumptions:

1. Energy conservation
2. Momentum conservation
3. Newtonian gravity equation

For assumptions 1 and 2, the conservation law for the stress-energy tensor holds:

\[
\nabla_\mu T^{\mu \nu} = 0
\]

The stress-energy tensor \(T^{\mu \nu}\) encapsulates crucial physical quantities and is expressed as:

\[
T^{\mu \nu} = \begin{pmatrix}
T^{00} & T^{01} & T^{02} & T^{03} \\
T^{10} & T^{11} & T^{12} & T^{13} \\
T^{20} & T^{21} & T^{22} & T^{23} \\
T^{30} & T^{31} & T^{32} & T^{33}
\end{pmatrix}
\]

where:

- \(T^{00} = \rho\): energy density
- \(T^{i0} = P_i\): momentum density in the \(i\)-th spatial direction
- \(T^{0i} = S_i\): energy flux in the \(i\)-th spatial direction
- \(\sigma_{ij}\): spatial stresses, related to pressure and stresses

An essential feature is the symmetry of the tensor, \(T^{\mu \nu} = T^{\nu \mu}\), indicating energy flux \(S_i\) equals momentum density \(P_i\). Though this may seem counterintuitive, it arises naturally from Einstein’s mass-energy equivalence:

\[ E = m c^2 \]

The four-momentum vector is given by:

\[ p^\mu = m u^\mu \]

with \(m\) being mass and \(u^\mu\) the four-velocity. When setting \( c = 1 \), the first column (energy flux) and the first row (momentum density) are both represented by \( m u^\mu \), explaining why energy flux equals momentum density and establishing the symmetry of the stress-energy tensor:

\[ T^{\mu \nu} = T^{\nu \mu} \]

---
On the geometric side, the Einstein field equations derive from the curvature of spacetime, described by the Riemann curvature tensor \(R^\rho_{\sigma \mu \nu}\). A key property of curvature is expressed through the Bianchi identity:

\[
\nabla_\alpha R_{\beta \gamma \mu \nu} + \nabla_\beta R_{\gamma \alpha \mu \nu} + \nabla_\gamma R_{\beta \mu \alpha \nu} = 0
\]

Contracting this equation with \(g^{\beta \mu}\), we have:

\[
\nabla_\alpha R_{\gamma \nu} + \nabla^\mu R_{\gamma \alpha \mu \nu} - \nabla_\gamma R_{\alpha \nu} = 0
\]

Then contracting again with \(g^{\gamma \nu}\), we get:

\[
\nabla_\alpha R - 2 \nabla^\mu R_{\alpha \mu} = 0
\]

This expression can be rearranged as:

\[
\nabla^\mu \left(R_{\alpha \mu} - \frac{1}{2} g_{\alpha \mu} R\right) = 0
\]

We define the Einstein tensor \(G_{\mu \nu}\) (which is symmetric since \(g_{\mu\nu}\) and \(R_{\mu\nu}\) are symmetric tensors):

\[
G_{\mu \nu} = R_{\mu \nu} - \frac{1}{2} g_{\mu \nu} R
\]

Hence, we conclude:

\[
\nabla_\mu G^{\mu \nu} = 0
\]

Since we already established from physical assumptions that:

\[ \nabla_\mu T^{\mu \nu} = 0 \]

We can naturally propose the Einstein field equations in the form:

\[
G_{\mu \nu} = \kappa T_{\mu \nu}
\]

where \(\kappa\) is a constant to be determined later.

---

We want to determine the constant \(\kappa\) appearing in Einstein's field equations:

\[ G_{\mu \nu} = \kappa T_{\mu \nu} \]

We start with a physical model described by the stress-energy tensor:

\[
T_{\mu \nu} = (\rho + p)u_\mu u_\nu + p g_{\mu \nu}
\]

where:

- \(\rho\) is the energy density.
- \(p\) is the pressure.

For a low-speed approximation (Newtonian approximation), we assume \(\rho \gg p\).

Let's define the four-velocity \(u^\mu\) as:

\[
u^\mu = (u^0, 0, 0, 0)\]

This assumption means the flow is stationary in space, with only time progressing.

Since \(u^\mu\) is a 4-vector, it satisfies:

\[g_{\mu\nu} u^\mu u^\nu = -1\]

We assume a perturbed metric \(g_{\mu \nu}\) around the Minkowski metric \(\eta_{\mu\nu}\):

\[g_{\mu \nu} = \eta_{\mu \nu} + h_{\mu \nu}, \quad \text{where} \quad |h_{\mu \nu}| \ll 1\]

Thus, we have:

\[ g_{00}(u^0)^2 = -1 \quad \Rightarrow \quad u^0 = \left(-\frac{1}{g_{00}}\right)^{\frac{1}{2}} \approx 1 + \frac{1}{2}h_{00} \]

Now, we compute the \(T_{00}\) component explicitly by plugging these assumptions into the tensor equation step by step:

\[
T_{00} = (\rho + p)(u^0)^2 + p g_{00}
\]

Given \(\rho \gg p\), we simplify to:

\[
T_{00} \approx \rho (1 - h_{00})
\]

Next, we compute the scalar \(T\) by contracting the stress-energy tensor with the metric tensor \(g^{\mu\nu}\):

\[
T = g^{\mu\nu} T_{\mu\nu}
\]

Doing this explicitly, step by step, we obtain:

\[
T = -\rho + 3p
\]

With these results, we now connect the geometric tensor \(G_{\mu\nu}\) to the physical tensor \(T_{\mu\nu}\), allowing us to derive an expression for the Ricci tensor component \(R_{00}\):

\[
R_{00} = G_{00} - \frac{1}{2} g_{00} G = \kappa\left(T_{00} - \frac{1}{2} g_{00} T\right)
\]

By substituting our approximations for \(T_{00}\) and \(T\) and simplifying further step by step, we finally arrive at:

\[
R_{00} = \frac{1}{2}\kappa \rho
\]

Thus, we have successfully established a relationship linking the geometric curvature of spacetime (the Riemann tensor component \(R_{00}\)) with physical properties of matter (energy density \(\rho\)).

However, the Riemann tensor itself is not sufficiently intuitive, so we introduce other geometric quantities for clarity. Specifically, we expand the Ricci tensor component \(R_{00}\) using its definition with Christoffel symbols \(\Gamma^\mu_{\alpha\beta}\):

\[
R_{00} = R^\mu_{0\mu 0} = \partial_\mu \Gamma^\mu_{00} - \partial_0 \Gamma^\mu_{\mu 0} + \Gamma^\mu_{\mu \lambda} \Gamma^\lambda_{00} - \Gamma^\mu_{0\lambda}\Gamma^\lambda_{\mu 0}
\]

Given our slow-motion assumption (\(\partial_0 \approx 0\)), we simplify the expression to:

\[
R_{00} \approx \partial_\mu \Gamma^\mu_{00}
\]

Now, we expand the Christoffel symbol explicitly in terms of the metric tensor components:

\[
\Gamma^\mu_{\alpha \beta} = \frac{1}{2}g^{\mu \lambda}(\partial_\beta g_{\lambda \alpha} + \partial_\alpha g_{\beta\lambda} - \partial_\lambda g_{\alpha\beta})
\]

Substituting this expression, we have:

\[
R_{00} = \partial_\mu \left(\frac{1}{2}g^{\mu\lambda}(\partial_0 g_{\lambda 0} + \partial_0 g_{0\lambda} - \partial_\lambda g_{00})\right)
\]

Since \(\partial_0 \approx 0\) in our low-speed approximation, this simplifies further to:

\[
R_{00} \approx -\frac{1}{2}\partial_\mu (g^{\mu\lambda}\partial_\lambda g_{00})
\]

Considering the metric tensor perturbation \(g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}\) and keeping only first-order terms (\(|h_{\mu\nu}|\ll 1\)), we obtain:

\[
R_{00} \approx -\frac{1}{2}\partial_\mu \partial^\mu h_{00}
\]

Using spatial indices explicitly, this becomes a Poisson-like equation:

\[
\nabla^2 h_{00} = -\kappa \rho
\]

---

Now that we have established a connection between the geometric metric component \(h_{00}\) and the physical energy density \(\rho\), our goal is to explicitly determine the constant \(\kappa\).

To achieve this, we use a physical interpretation to link the metric component \(h_{00}\) directly to Newtonian gravity. The intuition behind this is that the geometric description provided by General Relativity must coincide with Newtonian gravity equations under the low-speed approximation.

We recall that Newtonian gravity follows:

\[
m\mathbf{a} = \mathbf{F} = -m\nabla \phi
\]

Here, \(\phi\) represents the gravitational potential. To achieve a tensorial representation of the acceleration \(\mathbf{a}\), we start with the four-velocity \(u^\mu\). The tensorial form of the acceleration \(A^\mu\) is given by:

\[
A^\mu = \nabla_u u^\mu
\]

Expanding explicitly, this becomes:

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

Then it gives:

\[
A^\mu = u^\nu\left(\frac{\partial u^\mu}{\partial x^\nu} + \Gamma^\mu_{\rho\nu} u^\rho\right)
\]

--- 

Consider the case where \( \mathbf{F} = 0 \) (excluding gravity). The geodesic equation becomes:

\[
\frac{d^2 x^\mu}{d \tau^2} + \Gamma^\mu_{\rho\nu} \frac{d x^\rho}{d \tau} \frac{d x^\nu}{d \tau} = 0
\]

In the slow-motion approximation, \( u^0 \gg u^i \), so the equation simplifies to:

\[
\frac{d^2 x^\mu}{d \tau^2} + \Gamma^\mu_{00} \left( \frac{d x^0}{d \tau} \right)^2 = 0
\]

From previous calculations, we know:

\[
\Gamma^\mu_{00} = - \frac{1}{2} \eta^{\mu\lambda} \partial_\lambda h_{00}
\]

Plugging this in, we get:

\[
\frac{d^2 x^\mu}{d \tau^2} = \frac{1}{2} \eta^{\mu\lambda} \partial_\lambda h_{00} \left( \frac{d x^0}{d \tau} \right)^2
\]

Focusing on the spatial components:

\[
\frac{d^2 x^i}{d t^2} = \frac{1}{2} \delta^{ij} \partial_j h_{00}
\]

From the traditional Newtonian equation, we have:

\[
\frac{d^2 x^i}{d t^2} = - \delta^{ij} \partial_j \phi
\]

Therefore, we find:

\[
h_{00} = -2 \phi, g_{00} = -1 - 2\phi
\]

---


From Poisson's equation in Newtonian gravity:

\[
\nabla^2 \phi = 4\pi G \rho
\]

Given \( h_{00} = -2\phi \), we have:

\[
\nabla^2 h_{00} = -8\pi G \rho
\]

We get

\[
\kappa = 8\pi G 
\]



