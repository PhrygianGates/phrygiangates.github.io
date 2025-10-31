+++
date = '2025-08-23T23:45:00+08:00'
title = 'Symmetry Groups and Degeneracy'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
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

---

When a system possesses multiple symmetries, their interplay can generate additional conservation laws. Suppose we have two symmetry operators, \(A\) and \(B\), both of which commute with the Hamiltonian \(H\), so that \([A,H]=0\) and \([B,H]=0\). The commutator of these two operators may not be zero. If \(A\) and \(B\) are Hermitian, their commutator is anti-Hermitian, and we can define a new Hermitian operator \(C\) such that \([A,B] = iC\). This new operator is also a conserved quantity. We can show that it commutes with the Hamiltonian, because \([A,H]\) and \([B,H]\) are both zero:
\[
[AB-BA, H] = A[B,H] + [A,H]B - B[A,H] - [B,H]A = 0
\]
This process of generating new symmetries can be continued by taking further commutators, such as with \(A\) and \(C\), or \(B\) and \(C\), which may yield new operators \(D, E\), and so on. This procedure might continue indefinitely, leading to an infinite number of symmetries, or it might terminate after a finite number of steps. The resulting set of symmetry operators forms a closed system under commutation, known as a commutator algebra, which characterizes the full symmetry of the system.


---
This principle can be illustrated with a classical analogy: the Kepler problem of a planetary orbit. Consider an orbit with a specific energy E and an angular momentum vector \(\vec{L}\) perpendicular to its orbital plane. Due to the rotational symmetry of the central gravitational force, we can reorient the entire orbit—for example, by rotating it around the y-axis—to a new configuration. This new orbit has the exact same energy E, but the direction of its angular momentum vector has changed. This is a direct physical manifestation of the principle that rotating an angular momentum component about one axis affects its component on another, a concept formalized by the commutation relations of angular momentum operators. More profoundly, the Kepler problem possesses an additional "hidden" symmetry associated with the conservation of the Laplace-Runge-Lenz vector. It is the complete set of symmetries, combining both rotational invariance and this additional conservation law, that explains the extensive degeneracy of the system, where orbits of different eccentricities can share the same energy. 

--- 
We can generalize this concept by considering a particle moving freely in a two-dimensional xy-plane, rather than being confined to a circle. To find the generator of rotations in this more general case, we start by examining how the coordinates \((x, y)\) transform under an infinitesimal counter-clockwise rotation by an angle \(\epsilon\). The change in the coordinates is given by \(\Delta x = -\epsilon y\) and \(\Delta y = \epsilon x\). This rotation induces a change in the wave function \(\psi(x, y)\). Using the total differential, we can express the change in the wave function as:
\[
\Delta\psi \approx \frac{\partial\psi}{\partial x}\Delta x + \frac{\partial\psi}{\partial y}\Delta y = \frac{\partial\psi}{\partial x}(-\epsilon y) + \frac{\partial\psi}{\partial y}(\epsilon x) = \epsilon\left(x\frac{\partial\psi}{\partial y} - y\frac{\partial\psi}{\partial x}\right)
\]
To connect this to quantum mechanical operators, we recall the definition of the momentum operators in the position representation: \(p_x = -i\hbar\frac{\partial}{\partial x}\) and \(p_y = -i\hbar\frac{\partial}{\partial y}\). Substituting these into our expression for \(\Delta\psi\) yields:
\[
\Delta\psi = -\frac{i\epsilon}{\hbar}(xp_y - yp_x)\psi
\]
By comparing this to the general form for an infinitesimal transformation, \(\Delta\psi = -\frac{i\epsilon}{\hbar}G\psi\), where \(G\) is the generator, we can identify the generator of rotations about the z-axis. The position operator \(y\) and the momentum operator \(p_x\) commute, as they act on independent coordinates. The resulting generator is the z-component of the angular momentum operator, \(L_z = xp_y - yp_x\), which is the quantum mechanical analogue of the classical definition \(\vec{L} = \vec{r} \times \vec{p}\).

---
A particle moving in a central force field exhibits rotational invariance. This symmetry implies that the components of the angular momentum operator, \(L_i\), commute with the Hamiltonian, \([L_i, H] = 0\), leading to the conservation of angular momentum. While the components of angular momentum are conserved with respect to the system's energy evolution, they do not necessarily commute with each other. To investigate this, we can compute the commutator of \(L_x\) and \(L_y\). This relies on the fundamental commutation relations of position and momentum, such as \([x,y]=0\), \([p_x, p_y]=0\), and the canonical commutation relation \([x, p_x] = i\hbar\), which is a cornerstone of quantum mechanics. Using the definitions \(L_x = yp_z - zp_y\) and \(L_y = zp_x - xp_z\), we can evaluate their commutator:
\[
[L_x, L_y] = [yp_z - zp_y, zp_x - xp_z] = i\hbar(xp_y - yp_x) = i\hbar L_z
\]
By cyclic permutation, we also find \([L_y, L_z] = i\hbar L_x\) and \([L_z, L_x] = i\hbar L_y\). The set of operators \(\{L_x, L_y, L_z\}\) is closed under the operation of commutation. Such a structure, where the "product" is defined by the commutator, forms a Lie algebra. This algebra encapsulates the geometry of rotations.

---

The commutation relations derived above allow us to explore the spectrum of angular momentum eigenvalues algebraically, a method reminiscent of the one used for the harmonic oscillator. We begin with the eigenstates of one component, say \(L_z\), denoted by \(|m\rangle\), which satisfy the eigenvalue equation \(L_z|m\rangle = m\hbar|m\rangle\). To navigate between these eigenstates, we can invent new operators. Let us define the ladder operators \(L_+\) and \(L_-\) as:
\[
L_+ = L_x + iL_y \quad \text{and} \quad L_- = L_x - iL_y
\]
Using the commutation relations for \(L_x, L_y, L_z\), we can find the commutators of these new operators with \(L_z\):
\[
[L_+, L_z] = - \hbar L_+ \quad \text{and} \quad [L_-, L_z] = \hbar L_-
\]
Let's see how \(L_+\) acts on an eigenstate \(|m\rangle\). We examine the state \(L_+|m\rangle\) and check if it is also an eigenstate of \(L_z\).
\[
L_z(L_+|m\rangle) = (L_+L_z - [L_+, L_z])|m\rangle = (L_+ (m\hbar) - (-\hbar L_+))|m\rangle = (m+1)\hbar(L_+|m\rangle)
\]
This shows that \(L_+|m\rangle\) is a new eigenstate of \(L_z\) with a new eigenvalue of \((m+1)\hbar\). Thus, \(L_+\) acts as a raising operator, increasing the angular momentum quantum number by one unit. Similarly, \(L_-\) is a lowering operator. For any physical system, we expect the angular momentum to be bounded; there must be a highest and a lowest possible value for \(m\). This termination is necessary because quantities like total angular momentum squared, \(L^2\), are related to energy and must be finite. If there is a maximum state \(|m_{max}\rangle\), applying the raising operator must yield zero: \(L_+|m_{max}\rangle = 0\). Similarly, for a minimum state, \(L_-|m_{min}\rangle=0\). From this requirement, one can show that \(m_{max} = -m_{min}\), and that the allowed values for the angular momentum quantum number fall into two categories: integers (\(\dots, -1, 0, 1, \dots\)) and half-integers (\(\dots, -1/2, 1/2, \dots\)). For orbital angular momentum, which originates from the spatial motion of particles (\(\vec{L} = \vec{r} \times \vec{p}\)), only the integer values are physically realized.


---

For a rotationally symmetric system, the angular momentum operators commute with the Hamiltonian, which implies that they share a common set of eigenstates. This is a fundamental result from quantum mechanics: if two operators commute, we can always find a basis of states that are simultaneous eigenstates of both. This is because for any energy eigenstate \(|\psi\rangle\) of \(H\) with energy \(E\), the state \(L_z|\psi\rangle\) also has the same energy, since \(H(L_z|\psi\rangle) = L_z H |\psi\rangle = E(L_z|\psi\rangle)\). For a non-degenerate energy level, this forces \(|\psi\rangle\) to also be an eigenstate of \(L_z\). By definition, a non-degenerate energy level has only one unique state (up to a constant factor) associated with it. Since both \(|\psi\rangle\) and \(L_z|\psi\rangle\) have the same energy \(E\), \(L_z|\psi\rangle\) must be proportional to \(|\psi\rangle\), meaning \(L_z|\psi\rangle = c|\psi\rangle\) for some constant \(c\). This is precisely the definition of \(|\psi\rangle\) being an eigenstate of \(L_z\). For degenerate levels, where multiple states can share the same energy, this argument doesn't hold for a single state, but it guarantees that \(L_z\) maps the degenerate subspace onto itself, allowing us to construct a basis of simultaneous eigenstates within that subspace. We can therefore label an energy eigenstate by its angular momentum quantum number, \(m\), and consider a state \(|m\rangle\) such that \(H|m\rangle = E|m\rangle\). We can then examine the energy of the state that results from applying the raising operator, \(L_+|m\rangle\), which is proportional to \(|m+1\rangle\). Applying the Hamiltonian to this new state, and using the fact that all angular momentum operators commute with \(H\), we find:
\[
HL_+|m\rangle = L_+H|m\rangle = L_+(E|m\rangle) = E(L_+|m\rangle)
\]
This demonstrates that the new state, and by extension the eigenstate \(|m+1\rangle\), has the same energy \(E\). It follows that all states connected by the ladder operators, from a minimum to a maximum \(m\) value, are degenerate. This energy degeneracy is a direct consequence of the system's rotational symmetry.

