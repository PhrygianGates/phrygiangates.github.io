+++
date = '2025-12-16T22:00:00+08:00'
title = 'Fermions'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

We want to classify different particles using wavefunctions. Consider a two-particle system: if we exchange the two particles, how does the state of this system change?

In classical mechanics, even if two particles are completely identical in their physical properties, in principle we can still distinguish them by “labels” (such as “particle 1” and “particle 2”). Therefore, exchanging the positions of two classical particles produces a new, distinguishable microscopic configuration.

But in quantum mechanics, identical particles are fundamentally indistinguishable. When two identical particles are exchanged (moving particle 1 to position \(x_2\) and particle 2 to position \(x_1\)), the physical state of the system must remain unchanged.

Suppose the state vector of the system is \(|\psi\rangle\), and its wavefunction in the position representation is:
\[
\psi(x_1, x_2) = \langle x_1, x_2 | \psi \rangle
\]
When we say “the physical state is unchanged after exchanging the particles,” this does not mean that the wavefunction itself must be strictly equal, i.e., we do not necessarily require \(\psi(x_2, x_1) = \psi(x_1, x_2)\). This is because in quantum mechanics all observable physical quantities (such as probability densities and expectation values) depend only on the modulus squared of the wavefunction \(|\psi|^2\). Therefore, the wavefunction after exchange is allowed to differ from the original wavefunction by a global phase factor \(e^{i\phi}\):
\[
\psi(x_2, x_1) = e^{i\phi} \psi(x_1, x_2)
\]
where \(\phi\) is a real number.

However, if we perform the exchange operation twice, the particles will physically return to their original positions. This “restoration” requires that the wavefunction also return to its initial form:
\[
\psi(x_1, x_2) \xrightarrow{\text{交换一次}} e^{i\phi} \psi(x_2, x_1) \xrightarrow{\text{再交换一次}} e^{i\phi} (e^{i\phi} \psi(x_1, x_2)) = e^{2i\phi} \psi(x_1, x_2)
\]
To ensure consistency of the wavefunction, we must have:
\[
e^{2i\phi} = 1
\]
This equation has only two solutions, which directly leads to the two fundamental classes of particles in nature:

1.  Bosons: corresponding to \(e^{i\phi} = 1\). The wavefunction is unchanged (symmetric) under particle exchange:
    \[ \psi(x_2, x_1) = \psi(x_1, x_2) \]
2.  Fermions: corresponding to \(e^{i\phi} = -1\). The wavefunction changes sign (antisymmetric) under particle exchange:
    \[ \psi(x_2, x_1) = -\psi(x_1, x_2) \]

---
