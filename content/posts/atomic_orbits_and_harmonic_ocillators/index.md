+++
date = '2025-09-20T19:00:00+08:00'
title = 'Atomic Orbits And Harmonic Ocillators'
tags = ['Advanced Quantum Mechanics']
category = "Physics"
+++ 


To solve for the state of a particle in a system with a central potential, such as an electron in an atom, we describe its state using a wavefunction \\( \psi(r, \theta, \phi) \\) in spherical coordinates. A key mathematical technique here is the separation of variables. This method is applicable because the system's potential energy is spherically symmetric, meaning it only depends on the distance \\(r\\) from the center, not on the angles \\( \theta \\) or \\( \phi \\). This symmetry allows us to decompose the wavefunction into a product of a radial part \\( R(r) \\) and an angular part \\( Y(\theta, \phi) \\). By expressing \\( \psi(r, \theta, \phi) = R(r)Y(\theta, \phi) \\), we can transform the single complex Schrödinger equation into a set of simpler, one-dimensional ordinary differential equations, which can be solved separately.

---

The angular part of the problem is governed by the angular momentum operators, \\(L_x, L_y, L_z\\). These operators do not commute with each other, obeying commutation relations such as \\( [L_x, L_y] = i\hbar L_z \\). Because they do not commute, a quantum state cannot have a definite value for all three components simultaneously. The standard approach is to choose one component, conventionally \\(L_z\\), and find its common eigenstates with the total angular momentum squared operator \\(L^2\\). We can label these eigenstates by their respective quantum numbers, for example as \\(|m\rangle\\), which corresponds to an eigenvalue of \\(m\hbar\\) for the \\(L_z\\) operator. To explore the spectrum of these eigenvalues, we introduce the ladder operators, defined as \\(L_{\pm} = L_x \pm iL_y\\). These operators have a powerful function: when the raising operator \\(L_+\\) acts on an eigenstate \\(|m\rangle\\), it produces a new state that is also an eigenstate of \\(L_z\\), but with its eigenvalue increased to \\((m+1)\hbar\\). Consequently, we can label this new state as \\(|m+1\rangle\\), leading to the fundamental relation \\( L_+|m\rangle \propto |m+1\rangle \\). This algebraic method reveals a "ladder" of eigenstates, spaced by one unit of angular momentum along the z-axis.

The ladder of eigenstates is both finite and symmetrical. Its finiteness implies that there must be a maximum state \\(|l\rangle\\) and a minimum state \\(|-l\rangle\\), corresponding to the maximum and minimum projections of angular momentum. Acting on these extremal states with the raising or lowering operators, respectively, must yield a null vector: \\(L_+|l\rangle = 0\\) and \\(L_-|-l\rangle = 0\\). The symmetry of the ladder means that the quantum numbers \\(m\\) are centered around zero, leading to two possible structures: integer steps (e.g., ..., -1, 0, 1, ...) or half-integer steps (e.g., ..., -1/2, 1/2, ...).

The property of the maximum state, \\(L_+|l\rangle = 0\\), allows us to determine the eigenvalue of the total angular momentum squared operator, \\(L^2\\). By expressing \\(L^2\\) in terms of the ladder operators and \\(L_z\\), we can find its value. Using the identity \\(L^2 = L_-L_+ + L_z^2 + \hbar L_z\\) and applying it to the state \\(|l\rangle\\) gives us the result:
$$
\begin{aligned}
L^2 |l\rangle &= (L_-L_+ + L_z^2 + \hbar L_z) |l\rangle \\
&= L_- (L_+|l\rangle) + (L_z^2 + \hbar L_z)|l\rangle \\
&= 0 + ((l\hbar)^2 + \hbar(l\hbar))|l\rangle \\
&= l(l+1)\hbar^2 |l\rangle
\end{aligned}
$$
A crucial insight is that every state within the same multiplet shares this same eigenvalue for \\(L^2\\). We can demonstrate this by showing that if a state is an eigenstate of \\(L^2\\), then the state created by applying \\(L_-\\) is also an eigenstate with the same eigenvalue. This follows from the fact that \\(L^2\\) commutes with its components \\(L_i\\), and therefore also with the ladder operator \\(L_-\\) (i.e., \\([L^2, L_-] = 0\\)). The derivation is as follows:
$$
\begin{aligned}
L^2 |l-1\rangle &\propto L^2 (L_-|l\rangle) \\
&= L_- (L^2 |l\rangle) \\
&= L_- (l(l+1)\hbar^2 |l\rangle) \\
&= l(l+1)\hbar^2 (L_-|l\rangle) \\
&\propto l(l+1)\hbar^2 |l-1\rangle
\end{aligned}
$$
By repeatedly applying the lowering operator, we can see that this holds for all states down to \\(|-l\rangle\\), confirming that the value \\(l(l+1)\hbar^2\\) is a characteristic of the entire multiplet, independent of the magnetic quantum number \\(m\\).

There is a helpful classical analogy. Classically, an angular momentum vector of a fixed length can point in any direction in space, and its projection onto an axis can vary continuously. In quantum mechanics, the situation is different. While the magnitude of the angular momentum vector is fixed for a given multiplet (determined by \\(L^2\\)), its "direction" is quantized. The vector's projection onto the z-axis can only take on a discrete set of \\(2l+1\\) values, corresponding to the allowed states from \\(m = -l\\) to \\(m = +l\\).

Another powerful way to visualize this is through the lens of linear algebra. We can picture the \\(L^2\\) operator as an infinite block-diagonal matrix. Each block corresponds to a specific integer \\(l\\) and acts on a \\((2l+1)\\)-dimensional subspace. For a given \\(l\\), the block is simply the identity matrix multiplied by the eigenvalue \\(l(l+1)\hbar^2\\). The \\(2l+1\\) basis vectors of this subspace are the degenerate eigenstates \\(|l, m\rangle\\) (for \\(m = -l, ..., +l\\)). This entire matrix represents the universal structure of angular momentum, before considering any specific physical system.

However, the \\(L^2\\) operator alone cannot distinguish between the \\(2l+1\\) basis vectors within each block, as they all share the same eigenvalue. To resolve this degeneracy, we introduce the \\(L_z\\) operator, which commutes with \\(L^2\\). In the same basis, \\(L_z\\) is also a block-diagonal matrix. Crucially, within each block for a given \\(l\\), it is a diagonal matrix whose \\(2l+1\\) diagonal entries are the unique eigenvalues \\(m\hbar\\) (from \\(-l\hbar\\) to \\(+l\hbar\\)). This provides a unique label for each state, allowing us to specify a unique basis vector using the pair of quantum numbers \\((l, m)\\). These states are the simultaneous eigenstates of both \\(L^2\\) and \\(L_z\\).

---

The angular part of the wavefunction, \\( Y(\theta, \phi) \\), is described by the spherical harmonics, denoted \\( Y_{l,m}(\theta, \phi) \\). These functions are the simultaneous eigenfunctions of the total angular momentum squared operator \\(L^2\\) and its z-component \\(L_z\\). In the language of wavefunctions, they are the position-space representation of the abstract eigenstates \\(|l, m\rangle\\), satisfying the eigenvalue equations \\( L^2 Y_{l,m}(\theta, \phi) = l(l+1)\hbar^2 Y_{l,m}(\theta, \phi) \\) and \\( L_z Y_{l,m}(\theta, \phi) = m\hbar Y_{l,m}(\theta, \phi) \\).

---

A profound consequence of the spherical symmetry of the central potential is the degeneracy of energy levels. The Hamiltonian \\(H\\) commutes with all components of the angular momentum operator, which implies \\([H, L^2] = 0\\) and \\([H, L_z] = 0\\). This allows for a set of common eigenstates for \\(H\\), \\(L^2\\), and \\(L_z\\). The commutation of \\(H\\) with the ladder operators \\(L_{\pm}\\) means that applying these operators to an energy eigenstate does not change its energy. We can show this mathematically:
$$
\begin{aligned}
H(L_{\pm}|\psi\rangle) &= L_{\pm}(H|\psi\rangle) \quad (\text{since } [H, L_{\pm}] = 0) \\
&= L_{\pm}(E|\psi\rangle) \\
&= E(L_{\pm}|\psi\rangle)
\end{aligned}
$$
Since the ladder operators connect all the \\(2l+1\\) states within a multiplet (from \\(m=-l\\) to \\(m=+l\\)), all these states must share the same energy eigenvalue \\(E\\). This energy degeneracy is a direct result of the rotational symmetry of the system.

---

Having addressed the angular behavior of the wavefunction, we now turn our attention to its radial dependence. A classical analogy provides a useful starting point. For a particle in a central potential, the total energy, or Hamiltonian, can be expressed in terms of its radial and angular momentum. The kinetic energy separates into a radial component and a rotational component, leading to the expression:
$$
H = \frac{p_r^2}{2m} + \frac{L^2}{2mr^2} + V(r)
$$
Here, \\( p_r \\) is the radial momentum and \\( L \\) is the magnitude of the angular momentum. This formulation effectively reduces the problem to a one-dimensional system in the radial coordinate \\(r\\), where the particle moves in an effective potential \\( V_{\text{eff}}(r) = V(r) + \frac{L^2}{2mr^2} \\). The additional term, \\( \frac{L^2}{2mr^2} \\), is known as the centrifugal barrier; it represents a repulsive potential that pushes the particle away from the origin due to its angular motion.

---

The rigorous path to the quantum mechanical radial equation begins with the time-independent Schrödinger equation in three dimensions, \\( \hat{H}\psi = E\psi \\), where the Hamiltonian operator is \\( \hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(r) \\). The crucial step is to express the Laplacian operator, \\(\nabla^2\\), in spherical coordinates, which separates it into radial and angular parts. The angular part is directly related to the total angular momentum squared operator, \\(\hat{L}^2\\), allowing us to write the Laplacian in the compact form:
$$
\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) - \frac{\hat{L}^2}{\hbar^2 r^2}
$$
Substituting this back into the Schrödinger equation and applying the separation of variables \\( \psi(r, \theta, \phi) = R(r)Y_{l,m}(\theta, \phi) \\), we can make use of the fact that \\( Y_{l,m} \\) is an eigenfunction of \\( \hat{L}^2 \\) with eigenvalue \\( l(l+1)\hbar^2 \\). This allows us to replace the operator \\( \hat{L}^2 \\) with this constant value and cancel the angular part \\( Y_{l,m} \\) from both sides, yielding the radial Schrödinger equation for \\( R(r) \\):
$$
\left[ -\frac{\hbar^2}{2m} \frac{1}{r^2} \frac{d}{dr} \left(r^2 \frac{d}{dr}\right) + \frac{l(l+1)\hbar^2}{2mr^2} + V(r) \right] R(r) = E R(r)
$$

To simplify this equation for practical problem-solving, a substitution is commonly introduced. By defining a new radial function, \\( u(r) = rR(r) \\), the radial Schrödinger equation can be rewritten into a form that is mathematically identical to the one-dimensional Schrödinger equation:
$$
\left[ -\frac{\hbar^2}{2m} \frac{d^2}{dr^2} + V_{\text{eff}}(r) \right] u(r) = E u(r)
$$
Here, the effective potential \\( V_{\text{eff}}(r) = V(r) + \frac{l(l+1)\hbar^2}{2mr^2} \\) includes both the central potential and the centrifugal barrier. This simplified form is particularly useful for analyzing the behavior of the wavefunction and for finding the energy eigenvalues of the system.


