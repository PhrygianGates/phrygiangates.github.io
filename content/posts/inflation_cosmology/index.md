+++
date = '2024-12-23T17:01:09+08:00'
title = 'Inflation Cosmology: Is our universe part of a multiuniverse?'
tags = ['The Early Universe']
categories = ["Physics"]
+++

I want to learn about cosmology, maybe start with the book "An Introduction to Modern Cosmology" by Andrew Liddle and the lecture "The Early Universe" by MIT OpenCourseWare.

## The standard Big Bang
It does not tell the cause of the Bang, but the aftermath of the Bang. It assumes all the matter already existed before the Bang.

## Cosmic Inflation
A prequal to the Big Bang.
- gravity can be repulsive when pressure is negative. (Find out more about the relationship between gravity and pressure in the next part.)  
There is a patch of repulsive gravity material in the early universe, which is the cause of the Big Bang.  
The (mass/energy) density of the repulsive material is not lowered as it expands.The resolution is to introduce negative energy.

## Complementarity: The relationship between gravity and pressure

Below is a high-level introduction to these ideas, followed by some of the key formulas in cosmology and general relativity that show why negative pressure can produce a repulsive gravitational effect.

---

### 1. Stress-Energy Tensor and Einstein’s Field Equations

In general relativity (GR), gravity is described by Einstein’s field equations, which relate the geometry of spacetime (through the Einstein tensor \(G_{\mu\nu}\)) to the energy and momentum content of spacetime (through the stress-energy tensor \(T_{\mu\nu}\)):

\[
G_{\mu\nu} \;=\; \frac{8\pi G}{c^4}\,T_{\mu\nu},
\]

where \(G\) is the gravitational constant, and \(c\) is the speed of light. The left-hand side encapsulates the curvature of spacetime, while the right-hand side tells us how mass, energy, momentum, and pressure determine that curvature.

#### Perfect Fluid Approximation

In cosmology, we often model the contents of the universe (whether it be matter, radiation, or an inflaton field) as a “perfect fluid,” whose stress-energy tensor is written as:

\[
T_{\mu\nu} \;=\; (\rho + p)\,u_{\mu}\,u_{\nu} \;+\; p\,g_{\mu\nu}.
\]

- \(\rho\) is the energy density.
- \(p\) is the pressure.
- \(u_\mu\) is the 4-velocity of the fluid.
- \(g_{\mu\nu}\) is the metric tensor of spacetime.

This formula captures the idea that both \(\rho\) and \(p\) play significant roles in determining spacetime curvature, not just the mass or energy density alone.

---

### 2. Friedmann–Lemaître–Robertson–Walker (FLRW) Cosmology

For cosmological applications, we often assume a homogeneous, isotropic universe described by the FLRW metric. Two key equations (the Friedmann equations) emerge from Einstein’s field equations under this assumption:

1. **Friedmann Equation** (for the expansion rate \(H = \dot{a}/a\)):

   \[
   H^2 \;=\; \left(\frac{\dot{a}}{a}\right)^2 \;=\; \frac{8\pi G}{3}\,\rho \;-\; \frac{k}{a^2} \;+\; \frac{\Lambda}{3},
   \]

   where
   - \(a(t)\) is the scale factor describing how distances in the universe scale with time,
   - \(k\) is a parameter related to spatial curvature,
   - \(\Lambda\) is the cosmological constant (sometimes included on the right side instead).

2. **Acceleration Equation** (for the second derivative \(\ddot{a}\)):

   \[
   \frac{\ddot{a}}{a} \;=\; -\frac{4\pi G}{3}\,(\rho + 3p) \;+\; \frac{\Lambda}{3}.
   \]

   This equation is especially telling: the combination \(\rho + 3p\) directly governs whether the universe’s expansion accelerates or decelerates. 

---

### 3. Repulsive Gravity and Negative Pressure

Notice in the **acceleration equation**:

\[
\frac{\ddot{a}}{a} \;=\; -\frac{4\pi G}{3}(\rho + 3p) + \frac{\Lambda}{3}.
\]

- If \(\rho + 3p > 0\), the term \(-\frac{4\pi G}{3}(\rho + 3p)\) is negative, slowing the expansion.
- If \(\rho + 3p < 0\), this term becomes positive, contributing to \(\ddot{a} > 0\), i.e. **accelerated expansion**—often described as a repulsive gravitational effect.

In simpler terms, because pressure enters the equations with a factor of 3 compared to density, a sufficiently large negative pressure (\(p < 0\)) can overpower \(\rho\) in \(\rho + 3p\) and make the combination negative. This is precisely what happens during cosmic inflation (driven by the “inflaton field” with an effective negative pressure) and in scenarios with a cosmological constant \(\Lambda\) (dark energy) where the vacuum energy acts like negative pressure.

---

### 4. The Inflaton Field and Negative Pressure

During inflation, the universe is dominated by an inflaton field whose energy density \(\rho_{\phi}\) remains nearly constant, while its effective pressure \(p_{\phi}\) is negative. (In fact, for a slowly rolling scalar field, \(p_{\phi} \approx -\rho_{\phi}\) at times.) This makes:

\[
\rho_{\phi} + 3p_{\phi} \; \approx \; \rho_{\phi} + 3(-\rho_{\phi}) \;=\; \rho_{\phi} - 3\rho_{\phi} \;=\; -2\rho_{\phi} < 0,
\]

leading to \(\ddot{a} > 0\), and thus an exponentially accelerating expansion (repulsive effect).

---

### Putting It All Together

1. **Einstein’s field equations** show that pressure as well as energy density affect spacetime curvature.
2. **Negative pressure** can cause a runaway expansion (i.e., the scale factor \(a(t)\) grows at an accelerating rate).
3. **Inflation** is an example of this effect, where the inflaton’s negative pressure dominates and drives exponential growth of the universe.

In summary:

- **Gravity is not just about mass.** Energy density \(\rho\) and pressure \(p\) both appear in the stress-energy tensor.
- **Repulsive gravity arises** when \(\rho + 3p < 0\). This condition makes the cosmic scale factor’s acceleration positive (\(\ddot{a} > 0\)), indicating accelerated expansion.

## Additional Thoughts
Where does the negative pressure come from? There's not a determined theory yet. Some suggests there should be some particles called inflatons. From a classical point of view, it's a senario that when a particle flies into a wall, it doesn't bounce back, but it goes through the wall and comes out from the other side. This is a quantum effect. The inflaton field is a quantum field that has a negative pressure.

In next post, I will review the key concepts of Einstein's field equations and the meaning of those tensors. 

