+++
date = '2026-02-23T16:00:00+08:00'
title = 'Second Quantization'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

We start with a setup: the potential energy \(V(x)\) in the Hamiltonian has a shape similar to a symmetric double well, with two symmetric minima and a very high barrier in the middle (insert a diagram of the potential energy here). Let's discuss the energy eigenstates of this system and the time evolution of the states.

First, we need to solve the time-independent Schrödinger equation \(H|\psi\rangle = E|\psi\rangle\) to find the energy eigenvalues and eigenstates. Here, the projection of the eigenstate in the \(x\) basis is the wave function \(\psi(x)=\langle x|\psi\rangle\).

Suppose the barrier in the middle of \(V(x)\) is infinitely high, then the particle is completely confined to the left and right wells, and we can approximate that the system has two localized states, a left state \( |\psi_L\rangle\) and a right state \( |\psi_R\rangle\). Their corresponding energy eigenvalues should be the same, let's call it \(E_0\), which means the energy is degenerate.

But this is not the case in reality: When the barrier is finite and \(V(x)\) is symmetric, the wave functions of the energy eigenstates are either symmetric or antisymmetric, while the localized states \( |\psi_L\rangle\) and \( |\psi_R\rangle\) mentioned above do not satisfy this property by themselves. Thus, the energy eigenstates can be taken as their symmetric/antisymmetric combinations:
\[
|\psi_1\rangle=\frac{|\psi_L\rangle+|\psi_R\rangle}{\sqrt{2}},\qquad E_1=E_0-\epsilon,
\]
\[
|\psi_2\rangle=\frac{|\psi_L\rangle-|\psi_R\rangle}{\sqrt{2}},\qquad E_2=E_0+\epsilon.
\]

For the energy eigenstates, they satisfy the following time evolution (here we take \(\hbar=1\)):
\[
|\psi_n(t)\rangle=e^{-iE_n t}|\psi_n(0)\rangle.
\]

We now assume the initial state is \( |\psi(0)\rangle=|\psi_L\rangle\), i.e., the particle is on the left side. Note that this is not an energy eigenstate, but it can be expressed as a linear combination of eigenstates:
\[
|\psi_L\rangle=\frac{|\psi_1\rangle+|\psi_2\rangle}{\sqrt{2}},\qquad
|\psi_R\rangle=\frac{|\psi_1\rangle-|\psi_2\rangle}{\sqrt{2}}.
\]

As time evolves, at time \(t\), we have
\[
|\psi(t)\rangle=\frac{1}{\sqrt{2}}\left(e^{-iE_1 t}|\psi_1\rangle+e^{-iE_2 t}|\psi_2\rangle\right)
= e^{-iE_0 t}\left(\cos(\epsilon t)\,|\psi_L\rangle+i\sin(\epsilon t)\,|\psi_R\rangle\right).
\]

Taking \(t=\pi/(2\epsilon)\), we find that \( |\psi(t)\rangle = i e^{-iE_0 t}|\psi_R\rangle\), which means (ignoring the overall phase) this corresponds exactly to the particle being on the right side. Thus, the system will oscillate back and forth between the two states \( |\psi_L\rangle\) and \( |\psi_R\rangle\).

---
Let's return to basic quantum mechanics: Given a state \( |\psi\rangle\), its wave functions in the \(x\) basis and the momentum \(p\) basis are \(\psi(x)=\langle x|\psi\rangle\) and \(\tilde\psi(p)=\langle p|\psi\rangle\), respectively. They are connected by a Fourier transform (continuing to take \(\hbar=1\)):
\[
\tilde\psi(p)=\int \frac{dx}{\sqrt{2\pi}}\,e^{-ipx}\psi(x),\qquad
\psi(x)=\int \frac{dp}{\sqrt{2\pi}}\,e^{ipx}\tilde\psi(p).
\]

Now consider the scenario of second quantization. The annihilation field operator can be expanded in a complete orthonormal basis of single-particle states \(\{\psi_i(x)\}\):
\[
\Psi^-(x)=\sum_i a_i^-\,\psi_i(x).
\]
Here, \(\psi_i(x)\) can be taken as the energy eigenstates of the single-particle Hamiltonian, and \(a_i^-\) means lowering the number of particles in the \(i\)-th mode (analogous to the \(i\)-th harmonic oscillator) by 1.

For a free particle \(H=\hat p^{\,2}/(2m)\), in a one-dimensional \(x\) space, the solution to the time-independent equation can be written as a linear combination of plane waves \(Ae^{ikx}+Be^{-ikx}\), and \(E=k^2/(2m)\). Under the convention of \(\hbar=1\), \(p=k\), so \(e^{ipx}\) is the wave function of the momentum eigenstate in the position basis. Since \(p\) is continuous, changing the summation to an integral, we get
\[
\Psi^-(x)=\int \frac{dp}{\sqrt{2\pi}}\,a^-(p)\,e^{ipx},
\]
where \(a^-(p)\) means annihilating a particle with momentum \(p\). To correspond with the form above, it can also be written as a pair of inverse Fourier transforms:
\[
a^-(p)=\int \frac{dx}{\sqrt{2\pi}}\,e^{-ipx}\Psi^-(x).
\]

Formally, this is a Fourier transform, and this also matches our intuition: the meaning of \(\Psi^-(x)\) is to annihilate a particle at position \(x\); \(\Psi^+(x)\) and \(a^+(p)\) have a similar relationship (they are the conjugates of the aforementioned operators, respectively).

---
For these creation and annihilation operators, we already know that they satisfy
\[
[a_i^-,a_j^+]=\delta_{ij},\qquad [a_i^-,a_j^-]=0,\qquad [a_i^+,a_j^+]=0.
\]
That is to say, the only non-zero commutation relation comes from the annihilation and creation operators of the same mode; all creation operators commute with each other, and all annihilation operators also commute with each other.

By expanding the field operators \(\Psi^-(x)\) and \(\Psi^+(x)\) in terms of these \(a_i^-\) and \(a_i^+\), and then substituting the commutation relations above, we can deduce that the field operators in position space satisfy
\[
[\Psi^-(x),\Psi^+(y)]=\delta(x-y),
\]
Also
\[
[\Psi^-(x),\Psi^-(y)]=0,\qquad [\Psi^+(x),\Psi^+(y)]=0.
\]

It should be noted here that \(\Psi^+(x)\) and \(\Psi^-(x)\) are themselves complex, they are not Hermitian operators, and thus are not observables on their own. However, this point itself is not the most important, because one can construct Hermitian observables by taking the real part, the imaginary part, or appropriate linear combinations.

We can recall other non-commuting operators. The most standard example is position and momentum, which satisfy \([X,P]=i\hbar\). The physical meaning of non-commutation is: these two quantities cannot be measured simultaneously with precision; in other words, a measurement of one quantity will affect the other.

Returning to the field operator example above, if \(x\neq y\), then \(\delta(x-y)=0\). This shows that the field operators at different spatial points commute with each other. Therefore, measuring the field at point \(A\) will not affect the measurement of the field at point \(B\).
