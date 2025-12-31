+++
date = '2025-12-16T22:00:00+08:00'
title = 'Fermion'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

We want to classify different particles using wavefunctions. Consider a two-particle system: if we exchange the two particles, how does the state of the system change?

In classical mechanics, even if two particles are completely identical in their physical properties, in principle we can still distinguish them by “labels” (such as “particle 1” and “particle 2”). Therefore, exchanging the positions of two classical particles produces a new, distinguishable microscopic configuration.

But in quantum mechanics, identical particles are fundamentally indistinguishable. Here, “identical” means they have exactly the same intrinsic properties (such as mass, charge, and spin). It is important to emphasize that the “exchange” operation we discuss is only meaningful for identical particles. If we have a fermion and a boson (for example, an electron and a photon), they are physically completely distinguishable, so there is no need for, nor any constraint from, exchange symmetry. Only when we exchange two identical particles (for example, moving electron 1 to position \(x_2\) and electron 2 to position \(x_1\)) must the physical state of the system remain unchanged.

Suppose the state vector of the system is \(|\psi\rangle\), and its wavefunction in the position representation is:
\[
\psi(x_1, x_2) = \langle x_1, x_2 | \psi \rangle
\]
When we say “the physical state is unchanged after exchanging the particles,” this does not mean that the wavefunction itself must be strictly equal, i.e., we do not necessarily require \(\psi(x_2, x_1) = \psi(x_1, x_2)\). This is because in quantum mechanics, all observable physical quantities (such as probability density and expectation values) depend only on the modulus squared of the wavefunction \(|\psi|^2\). Therefore, the wavefunction after exchange is allowed to differ from the original wavefunction by a global phase factor \(e^{i\phi}\):
\[
\psi(x_2, x_1) = e^{i\phi} \psi(x_1, x_2)
\]
where \(\phi\) is a real number.

However, if we perform the exchange operation twice, the particles physically return to their original positions. This “restoration” requires the wavefunction to return to its initial form as well:
\[
\psi(x_1, x_2) \xrightarrow{\text{exchange once}} e^{i\phi} \psi(x_2, x_1) \xrightarrow{\text{exchange again}} e^{i\phi} (e^{i\phi} \psi(x_1, x_2)) = e^{2i\phi} \psi(x_1, x_2)
\]
To ensure consistency of the wavefunction, we must have:
\[
e^{2i\phi} = 1
\]
This equation has only two solutions, which directly leads to the two fundamental classes of particles in nature:

1.  Bosons: corresponding to \(e^{i\phi} = 1\). After exchanging particles, the wavefunction is unchanged (symmetric):
    \[ \psi(x_2, x_1) = \psi(x_1, x_2) \]
2.  Fermions: corresponding to \(e^{i\phi} = -1\). After exchanging particles, the wavefunction changes sign (antisymmetric):
    \[ \psi(x_2, x_1) = -\psi(x_1, x_2) \]

---
Now let us consider how to construct the wavefunctions \(\psi(x_1, x_2)\) of bosons and fermions. A simple idea is to write the wavefunction directly as a product of single-particle wavefunctions:
\[ \psi(x_1, x_2) = \psi_1(x_1)\psi_2(x_2) \]
This intuition comes from independent events in probability theory, since the modulus squared of the wavefunction represents probability. If the particles do not interact, their joint probability distribution should be the product of their individual probabilities. However, as we discussed earlier, the wavefunction of identical particles must satisfy specific exchange symmetries. Clearly, the simple product form \(\psi_1(x_1)\psi_2(x_2)\) becomes \(\psi_1(x_2)\psi_2(x_1)\) after exchanging \(x_1\) and \(x_2\), which in general is neither equal to the original wavefunction (not symmetric) nor equal to the negative of the original wavefunction (not antisymmetric), so it is physically invalid.

To satisfy the requirements of symmetry or antisymmetry, we can construct a linear superposition based on the simple product form. For bosons, we need to construct an exchange-symmetric wavefunction by adding the two possible permutations:
\[ \psi_{\text{boson}}(x_1, x_2) = \psi_1(x_1)\psi_2(x_2) + \psi_1(x_2)\psi_2(x_1) \]
For fermions, we need to construct an exchange-antisymmetric wavefunction by subtracting the two possible permutations:
\[ \psi_{\text{fermion}}(x_1, x_2) = \psi_1(x_1)\psi_2(x_2) - \psi_1(x_2)\psi_2(x_1) \]
The wavefunctions constructed in this way perfectly satisfy the symmetry requirements for bosons and fermions. From this we can directly derive the Pauli exclusion principle: if we try to put two fermions in the same quantum state, i.e., set \(\psi_1 = \psi_2\), and substitute into the fermionic wavefunction expression, we find:
\[ \psi_{\text{fermion}} = \psi_1(x_1)\psi_1(x_2) - \psi_1(x_2)\psi_1(x_1) = 0 \]
The wavefunction is identically zero, meaning that such a physical state simply does not exist. This is the mathematical essence of why two fermions cannot occupy the same quantum state.

For many-particle states \(\psi(x_1, x_2, x_3, \dots)\), the same rules still apply. For a fermionic system, exchanging any two particles (for example, \(x_i\) and \(x_j\)) must cause the wavefunction to change sign:
\[ \psi(\dots, x_i, \dots, x_j, \dots) = -\psi(\dots, x_j, \dots, x_i, \dots) \]
For a bosonic system, exchanging any two particles leaves the wavefunction unchanged:
\[ \psi(\dots, x_i, \dots, x_j, \dots) = \psi(\dots, x_j, \dots, x_i, \dots) \]

---
Having considered exchange transformations, we now turn to rotational transformations. In classical physics, rotating an object by a full turn (\(2\pi\)) is an identity transformation: the object returns to exactly the same state.

In quantum mechanics, however, rotations are generated by the total angular momentum operator \(J\). By analogy, just as the momentum operator \(P\) is the generator of spatial translations (corresponding to differentiation with respect to position), the angular momentum operator \(J\) corresponds to differentiation with respect to the angle \(\theta\). For an eigenstate \(|\psi\rangle\) of the angular momentum operator, with eigenvalue \(m\):
\[ J |\psi\rangle = -i \frac{\partial}{\partial \theta} |\psi\rßangle = m |\psi\rangle \]
The solution to this differential equation tells us that after a rotation by angle \(\theta\), the wavefunction becomes:
\[ |\psi(\theta)\rangle = e^{im\theta} |\psi(0)\rangle \]
Now we examine the case of a full rotation (\(\theta = 2\pi\)):
\[ |\psi(2\pi)\rangle = e^{i m 2\pi} |\psi(0)\rangle \]
From the commutation relations of angular momentum, one can derive that the angular momentum quantum number \(m\) can only take integer or half-integer values. This again divides particles into two classes:
*   Bosons (integer spin): \(m\) is an integer, \(e^{i 2\pi m} = 1\). After a rotation by \(2\pi\), the wavefunction remains unchanged (\(|\psi\rangle \to |\psi\rangle\)), in line with classical intuition.
*   Fermions (half-integer spin): \(m\) is a half-integer (such as \(1/2\)), \(e^{i 2\pi m} = -1\). After a rotation by \(2\pi\), the wavefunction changes sign (\(|\psi\rangle \to -|\psi\rangle\)). This means that for fermions, a rotation by \(360^\circ\) does not truly restore the wavefunction; one must rotate by \(720^\circ\) (\(4\pi\)) to return to the original state.

---
How do we understand the deep connection between “rotation” and “exchange,” two operations that seem unrelated at first glance? This can be visualized through a topological demonstration (often called the “belt trick” or “Dirac belt”).

![](images/Screenshot%202025-12-31%20at%2011.32.13 PM.png)

Imagine that particles are some kind of topological structure attached to the spacetime background (for example, one end of a belt).
1.  Rotation operation: If we rotate one of the particles (one end of the belt) by \(2\pi\) (360 degrees), the belt acquires a twist (a single twist). This corresponds to the fermionic wavefunction acquiring a phase of \(-1\).
2.  Exchange operation: If we exchange the positions of two particles, this is topologically equivalent to winding the belt segments connecting them around each other once.

The remarkable thing is that if you perform both operations—first rotate one particle by \(2\pi\) (introducing a twist), then exchange the two particles (winding once)—you will find that these two topological deformations can cancel each other out! Through continuous deformation (without cutting the belt), you can restore the entire system to its original flat configuration.

This implies:
\[ \text{rotation phase} \times \text{exchange phase} = 1 \]
*   For bosons: rotation by \(2\pi\) leaves the state unchanged (phase \(1\)), exchange also leaves it unchanged (phase \(1\)), \(1 \times 1 = 1\). Self-consistent.
*   For fermions: rotation by \(2\pi\) changes the sign (phase \(-1\)), exchange also changes the sign (phase \(-1\)), \((-1) \times (-1) = 1\). Also self-consistent.

This provides a profound physical picture: particles should not be regarded as simple points, but rather as knots or solitons in the spatial field.
*   A particle is a twist in a particular orientation.
*   An antiparticle is a twist in the mirror orientation.
*   When a particle meets its antiparticle, just like a left-handed knot meeting a right-handed knot, they can completely cancel each other topologically, smoothly untie, and return to the trivial vacuum state. This is the geometric essence of particle–antiparticle annihilation.

---

How can we prove that a fermion indeed acquires a phase of \(-1\) after a rotation by \(2\pi\), rather than this being merely a mathematical trick? We can verify this through an interference experiment.

If we directly rotate an isolated electron by \(2\pi\), its wavefunction changes from \(\psi\) to \(-\psi\). However, in quantum mechanics, observables depend only on the modulus squared of the wavefunction \(|\psi|^2\), and since \(|-\psi|^2 = |\psi|^2\), such a change in global phase cannot be directly observed experimentally.

To observe this minus sign, we need to use quantum interference. We can split an electron’s wavefunction into two parts using a beam splitter, forming a superposition of paths A and B:
\[ \Psi = \psi_A + \psi_B \]
Then we leave path A unchanged, and apply a magnetic field only along path B, causing the spin of the electron on path B to rotate by \(2\pi\). According to theory, the wavefunction on path B will acquire a phase of \(-1\):
\[ \psi_B \xrightarrow{\text{rotate } 2\pi} -\psi_B \]
At this point, when the two paths recombine, the total state becomes:
\[ \Psi_{\text{new}} = \psi_A - \psi_B \]
The original constructive interference (\(\psi_A + \psi_B\)) turns into destructive interference (\(\psi_A - \psi_B\)), leading to a clear shift in the interference fringes. This effect has been precisely confirmed in neutron interference experiments, thereby demonstrating that a fermion does not truly return to its original state after a rotation by \(360^\circ\); it must be rotated by \(720^\circ\) to be fully restored.
