+++
date = '2024-01-04T12:36:09+08:00'
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

---
To be continued...






