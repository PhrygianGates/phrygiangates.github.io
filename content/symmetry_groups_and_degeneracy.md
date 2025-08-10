+++
date = '2025-08-08T23:45:00+08:00'
katex = true
title = 'Symmetry Groups and Degeneracy'
tags = ['Advanced Quantum Mechanics']
+++ 


A symmetry can be understood as an operator that, when applied to a system, leaves its fundamental characteristics unchanged. For instance, a crystal lattice exhibits translational symmetry; shifting its position by a lattice vector does not alter its structure. In quantum mechanics, this concept is deeply tied to the degeneracy of energy levels. Degeneracy means that different quantum states can share the same energy. While symmetry sometimes implies degeneracy, but degeneracy in energy levels is always a sign of an underlying symmetry in the system.

---

Let's start by considering rotational symmetry. Imagine a particle moving on a circle, a system that is invariant under rotation. Its state is described by a wave function, \(\psi(\theta)\). If we rotate the system counter-clockwise by an infinitesimal angle \(\epsilon\), the wave function transforms: \(\psi(\theta) \rightarrow \psi(\theta - \epsilon)\). The change in the wave function, \(\Delta\psi\), can be written as:
\[
\Delta\psi \approx -\epsilon \frac{\partial\psi}{\partial\theta} = -\frac{i\epsilon}{\hbar} \left(-i\hbar\frac{\partial\psi}{\partial\theta}\right)
\]
Recognizing that the angular momentum operator is \(L_z = -i\hbar\frac{\partial}{\partial\theta}\), we see that:
\[
\Delta\psi = -\frac{i\epsilon}{\hbar}L_z\psi
\]
In this context, \(L_z\) is the generator of rotations. Applying it to the wave function describes the effect of a small rotation. This same principle applies to linear momentum, where \(p_x = -i\hbar\frac{\partial}{\partial x}\) is the generator of translations along the x-axis. Note that for simplicity, sometimes \(\hbar\) is set to 1 in calculations, but it is explicitly included here.

---

What are the eigenvalues and eigenvectors of the angular momentum operator? The eigenvalue equation is \(L_z|\psi\rangle = m|\psi\rangle\), where \(m\) is the eigenvalue. This gives the differential equation:
\[
-i\hbar\frac{\partial\psi}{\partial\theta} = m\psi(\theta)
\]
The solution is of the form \(\psi(\theta) = C e^{im\theta/\hbar}\). A physical constraint is that the wave function must be single-valued, meaning \(\psi(\theta) = \psi(\theta + 2\pi)\). This implies that after a full circle rotation, the wave function must return to its original state. This leads to the condition:
\[
e^{im2\pi/\hbar} = 1
\]
This holds if \(m/\hbar\) is an integer. Traditionally, we denote this integer as \(m\), so the angular momentum is quantized, with allowed values being \(L_z = m\hbar\).

---

The energy of the system is connected to the angular momentum quantum number \(m\). A key question is whether energy states are degenerate, for example, if \(E(m) = E(-m)\). This isn't always the case; an external magnetic field, for instance, could break this symmetry. Rotational symmetry alone is not sufficient to guarantee this degeneracy. An additional symmetry is needed, such as reflection symmetry. If the system is symmetric with respect to reflection across an axis (for example, the x-axis in the xy-plane), then clockwise and counter-clockwise motions are equivalent. This mirror symmetry ensures that \(E(m) = E(-m)\). Therefore, it is the combination of these two symmetries—rotation and reflection—that explains the degeneracy of the energy levels in this case.

---

The degeneracy between states with opposite angular momentum, \(E(m) = E(-m)\), arises because the operators for rotation and reflection do not commute. We can demonstrate this by examining the action of these operators on the system's wave function. Let's define a reflection operator \(M\) that acts on the wave function as \(M\psi(\theta) = \psi(-\theta)\). To see how this interacts with the rotation generator, \(L_z\), we can compute their commutator acting on an eigenfunction of angular momentum, \(\psi_m(\theta) = e^{im\theta}\).

We evaluate the action of \(M L_z\) and \(L_z M\) on \(\psi_m(\theta)\). Recalling that \(L_z \psi_m(\theta) = m\hbar \psi_m(\theta)\), we have:
\[
ML_z\psi_m(\theta) = M(m\hbar\psi_m(\theta)) = m\hbar\psi_m(-\theta) = m\hbar e^{-im\theta}
\]
For the other term, we find:
\[
L_zM\psi_m(\theta) = L_z\psi_m(-\theta) = L_z e^{-im\theta} = -m\hbar e^{-im\theta}
\]
The commutator, \([M, L_z] = ML_z - L_zM\), acting on the eigenfunction is therefore:
\[
[M, L_z]\psi_m(\theta) = m\hbar e^{-im\theta} - (-m\hbar e^{-im\theta}) = 2m\hbar e^{-im\theta}
\]
Since the result is not zero (for \(m \neq 0\)), the operators do not commute, so \([M, L_z] \neq 0\). 