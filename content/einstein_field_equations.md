+++
date = '2025-01-04T00:36:09+08:00'
katex = true
title = 'Einstein Field Equations'
tags = ['The Early Universe']
+++

In this post, I would like to build some fundational knowledge about the Einstein Field Equations. First, I will pose several questions based on the last post about cosmology:
1. What are the einstein tensor and the stress-energy tensor?
2. How is Einstein Field Equations derived?
3. In the context of cosmology, what is the perfect fluid approximation?
4. How can we derive the Friedmann Equation and Acceleration Equation from the Einstein Field Equations?

## Stress-Energy Tensor
We refer to [this course](https://ocw.mit.edu/courses/8-962-general-relativity-spring-2020/resources/lecture-4-volumes-and-volume-elements-conservation-laws/).

### 1. **4-Velocity and Proper Time**

The **4-velocity** \\( u^\mu \\) describes the motion of a particle in spacetime and is defined as:  
\\[
u^\mu = \frac{dx^\mu}{d\tau}
\\]  
where:
- \\( x^\mu = (ct, x, y, z) \\): Spacetime coordinates.
- \\( \tau \\): Proper time, the time measured in the rest frame of the particle.

In general relativity, using the \\( (-, +, +, +) \\) metric convention, the normalization condition for the 4-velocity is:  
\\[
u^\mu u_\mu = -c^2
\\]

If we use **natural units** (\\( c = 1 \\)), this simplifies to:  
\\[
u^\mu u_\mu = -1
\\]

---

### 2. **Energy and Momentum**

The **4-momentum** \\( P^\mu \\) combines the energy \\( E \\) and spatial momentum \\( \vec{p} \\):  
\\[
P^\mu = (E/c, \vec{p})
\\]

Key components:
- \\( E = \gamma m c^2 \\): Relativistic energy.
- \\( \vec{p} = \gamma m \vec{v} \\): Relativistic momentum.

Key relations:
- For particles with rest mass \\( m \\):
  \\[
  P^\mu P_\mu = -m^2 c^2
  \\]
- For **massless particles** (e.g., photons):
  \\[
  P^\mu P_\mu = 0
  \\]

---

### 3. **Number Density and Flow**

The **number density** \\( n \\) represents the particle density in a given frame, while the **flow number** \\( N^\mu \\) is a 4-vector describing the particle flux.

#### Relation between densities in different frames:
- Rest frame density: \\( n_0 \\)
- Moving frame density (boosted by Lorentz factor):
  \\[
  n = n_0 \gamma
  \\]

#### Flow number:
\\[
N^\mu = n u^\mu
\\]
where \\( u^\mu \\) is the 4-velocity. Explicitly:
\\[
N^\mu = (n_0 \gamma, n_0 \gamma \vec{v}) = (n, n \vec{v})
\\]

#### Components:
- **Time direction**: \\( N^0 = n \\) (number density in the lab frame).
- **Spatial direction**: \\( N^i = n v^i \\) (flux of particles in the \\( x, y, z \\) directions).

#### Relating \\( n_t \\) and \\( n_x \\):

From the relation:
\\[
n_t V = n_x (S t)
\\]

Since \\( V = S \cdot l \\), where \\( S \\) is the cross-sectional area and \\( l \\) is the length of the system:

\\[
n_t (S \cdot l) = n_x (S \cdot t)
\\]

Canceling \\( S \\):
\\[
n_t \cdot l = n_x \cdot t
\\]

Solving for \\( n_x \\):
\\[
n_x = \frac{n_t \cdot l}{t}
\\]

Since \\( l/t = v \\) (velocity of the flow):
\\[
n_x = n_t \cdot v
\\]

This shows that the spatial number density \\( n_x \\) is proportional to the time direction density \\( n_t \\) and the flow velocity \\( v \\).

#### Conservation of Particle Number

The **continuity equation** expresses the conservation of particle number in 4-dimensional spacetime:
\\[
\partial_\mu N^\mu = 0
\\]

This comes from the following relation:
\\[
\frac{\partial n}{\partial t} + \nabla \cdot (n \vec{v}) = 0
\\]
Here:
- The **time component**: \\(\frac{\partial n}{\partial t}\\) represents the rate of change of particle density.
- The **spatial component**: \\(\nabla \cdot (n \vec{v})\\) represents the divergence of the particle flux.

---

Certainly! Below is an organized and structured version of your content, complete with sections, explanations, and properly formatted equations.

---

### 4. Levi-Civita Notation

#### Levi-Civita Notation

The **Levi-Civita symbol** (ε) is a fundamental tensor used in vector calculus and differential geometry to express operations involving cross products and determinants. In three dimensions, it is defined as:

\\[
\epsilon_{ijk} =
\begin{cases}
+1 & \text{if } (i,j,k) \text{ is an even permutation of } (1,2,3), \\\\
-1 & \text{if } (i,j,k) \text{ is an odd permutation of } (1,2,3), \\\\
0 & \text{otherwise}.
\end{cases}
\\]

#### Volume Form in Three Dimensions

Given three vectors **A**, **B**, and **C** in \\(\mathbb{R}^3\\), the volume \\( V^3 \\) they span can be expressed using the Levi-Civita symbol:

\\[
V^3 = \epsilon(A, B, C) = \epsilon_{ijk} A^i B^j C^k
\\]

#### Differential Forms and 1-Forms

When reducing the number of vectors, we can define a 1-form using the Levi-Civita symbol by fixing one of the indices. For instance, by "only putting in 2 vectors" **B** and **C**, we obtain:

\\[
\epsilon(-, B, C) = \epsilon_{ijk} B^j C^k
\\]

This expression represents a **1-form** in three-dimensional space.

--- 

### 5. Continuity Equation

#### Gauss's Theorem in Three Dimensions

Gauss's theorem, also known as the divergence theorem, relates the flux of a vector field **A** through a closed surface \\( S \\) to the divergence of **A** within the volume \\( V \\) bounded by \\( S \\):

\\[
\oint_{S} \mathbf{A} \cdot d\mathbf{\Sigma} = \int_{V} (\nabla \cdot \mathbf{A}) \, dV
\\]

In differential form language, this can be written as:

\\[
\oint_{S} \delta \mathbf{A} \, dV = \oint_{S} \mathbf{A} \cdot d\mathbf{\Sigma}
\\]

where \\( \delta \\) represents the codifferential operator.

#### Generalization to Four Dimensions

Extending Gauss's theorem to four-dimensional spacetime involves considering a **4-vector field** and its associated 3-dimensional hypersurface. The generalized Gauss's theorem in four dimensions relates the flux of a 4-vector field **N** through the boundary of a 4-volume \\( V^4 \\) to the divergence of **N** within \\( V^4 \\):

\\[
\oint_{\partial V^4} \mathbf{N} \cdot d\mathbf{\Sigma} = \int_{V^4} (\partial_\mu N^\mu) \, dV^4
\\]

Here, \\( d\mathbf{\Sigma} \\) is the oriented 3-dimensional hypersurface element in four-dimensional space.

#### Conservation Laws

Conservation laws are fundamental in physics, expressing the invariance of certain quantities over time. A general conservation law can be written as:

\\[
\partial_\mu N^\mu = 0
\\]

This equation implies that the 4-divergence of the current 4-vector **N** is zero, representing the conservation of the associated quantity.

Applying Gauss's theorem to the conservation law:

\\[
\oint_{\partial V^4} \mathbf{N} \cdot d\mathbf{\Sigma} = 0
\\]

This states that the net flux of **N** through the boundary of any 4-volume \\( V^4 \\) is zero, ensuring conservation within the volume.

#### Derivation of the Continuity Equation

To derive the continuity equation from the conservation law, consider the time evolution of the conserved quantity within a spatial volume \\( V \\).

Starting from the conservation law:

\\[
\partial_\mu N^\mu = 0
\\]

Expanding the divergence in four-dimensional spacetime:

\\[
\frac{\partial N^0}{\partial t} + \nabla \cdot \mathbf{N} = 0
\\]

Integrating over the spatial volume \\( V \\):

\\[
\int_{V} \frac{\partial N^0}{\partial t} \, dV + \int_{V} \nabla \cdot \mathbf{N} \, dV = 0
\\]

Applying Gauss's theorem to the second term:

\\[
\frac{d}{dt} \int_{V} N^0 \, dV = - \oint_{S} \mathbf{N} \cdot d\mathbf{a}
\\]

Where:
- \\( S \\) is the boundary surface of the volume \\( V \\).
- \\( d\mathbf{a} \\) is the outward-pointing area element on \\( S \\).

This is the **continuity equation**, expressing the rate of change of the conserved quantity within \\( V \\) in terms of the flux across its boundary.

--- 

### 6. Examples of Continuity Equations

The continuity equation is a powerful tool in physics for expressing the conservation of various quantities, such as energy and momentum. By appropriately defining the **current 4-vector** **N**, the general continuity equation

\\[
\partial_\mu N^\mu = 0
\\]

can be specialized to represent the conservation laws for energy and momentum. Below, we explore how this framework applies to both energy conservation and momentum conservation.

#### Energy Conservation

##### Defining the Energy Current

To express energy conservation using the continuity equation, we define the components of the current 4-vector **N** as follows:

- **\\( N^0 \\)**: Represents the **energy density** \\( \rho \\), which is the amount of energy per unit volume.
- **\\( \mathbf{N} \\)**: Represents the **energy flux vector** \\( \mathbf{S} \\), which describes the flow of energy through space (e.g., the Poynting vector in electromagnetism).

Thus, the 4-vector **N** for energy conservation is:

\\[
\mathbf{N} = (\rho, \mathbf{S})
\\]

##### Applying the Continuity Equation

Substituting these definitions into the continuity equation:

\\[
\partial_\mu N^\mu = \frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{S} = 0
\\]

This equation states that the rate of change of energy within a volume \\( V \\) plus the net energy flux out of the volume is zero, ensuring that energy is conserved.

##### Integral Form: Energy Conservation

Integrating the continuity equation over a spatial volume \\( V \\) and applying Gauss's theorem:

\\[
\frac{d}{dt} \int_{V} \rho \, dV + \oint_{S} \mathbf{S} \cdot d\mathbf{a} = 0
\\]

This integral form states that the **time rate of change of the total energy** within the volume \\( V \\) is equal to the **negative of the net energy flux** through the boundary surface \\( S \\). In other words, energy can neither be created nor destroyed within \\( V \\); it can only flow in or out.

##### Example: Electromagnetic Energy Conservation

In electromagnetism, the energy density \\( \rho \\) and the Poynting vector \\( \mathbf{S} \\) are given by:

\\[
\rho = \frac{1}{2} (\epsilon_0 \mathbf{E}^2 + \frac{1}{\mu_0} \mathbf{B}^2)
\\]
\\[
\mathbf{S} = \mathbf{E} \times \mathbf{B}
\\]

Substituting these into the continuity equation yields Poynting's theorem, which describes the conservation of electromagnetic energy.

#### Momentum Conservation

##### Defining the Momentum Current

For momentum conservation, the current 4-vector **N** is defined in terms of the **momentum density** and the **momentum flux**. Specifically:

- **\\( N^0 \\)**: Represents the **momentum density** \\( \mathbf{p} \\), which is the momentum per unit volume.
- **\\( \mathbf{N} \\)**: Represents the **momentum flux tensor** \\( \mathbf{T} \\), also known as the **stress tensor**, which describes the flow of momentum through space.

In tensor notation, the stress tensor \\( T^{ij} \\) (where \\( i, j \\) denote spatial components) encapsulates the flux of the \\( i \\)-th component of momentum across a surface perpendicular to the \\( j \\)-th axis.

Thus, the 4-vector **N** for momentum conservation can be expressed as:

\\[
\mathbf{N} = (\mathbf{p}, \mathbf{T})
\\]

##### Applying the Continuity Equation

Substituting these definitions into the continuity equation for each component of momentum \\( p^i \\):

\\[
\partial_\mu N^{\mu i} = \frac{\partial p^i}{\partial t} + \nabla \cdot \mathbf{T}^i = 0
\\]

Here, \\( \mathbf{T}^i \\) is the \\( i \\)-th column of the stress tensor, representing the flux of the \\( i \\)-th component of momentum.

##### Integral Form: Momentum Conservation

Integrating over a spatial volume \\( V \\) and applying Gauss's theorem:

\\[
\frac{d}{dt} \int_{V} \mathbf{p} \, dV + \oint_{S} \mathbf{T} \cdot d\mathbf{a} = 0
\\]

This equation states that the **time rate of change of the total momentum** within the volume \\( V \\) is equal to the **negative of the net momentum flux** through the boundary surface \\( S \\). This ensures that momentum is conserved within the volume, accounting for any momentum entering or leaving through the surface.

##### Example: Fluid Dynamics

In fluid dynamics, the stress tensor \\( \mathbf{T} \\) includes contributions from both pressure and viscous stresses:

\\[
T^{ij} = -p \delta^{ij} + \sigma^{ij}
\\]

where:
- \\( p \\) is the pressure,
- \\( \delta^{ij} \\) is the Kronecker delta,
- \\( \sigma^{ij} \\) represents the viscous stress tensor.

Substituting into the momentum continuity equation yields the Navier-Stokes equations, which describe the motion of fluid substances.


