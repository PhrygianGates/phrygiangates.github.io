+++
date = '2025-06-26T22:40:00+08:00'
katex = true
title = 'Review of quantum mechanics'
tags = ['Advanced Quantum Mechanics']
+++

In quantum mechanics, the state of a physical system is described by a state vector, denoted using Dirac's bra-ket notation as \(|\psi\rangle\). These state vectors are elements of a complex vector space called a Hilbert space.

Given two state vectors \(|\psi\rangle\) and \(|\phi\rangle\), their inner product is a complex number denoted by \(\langle\phi|\psi\rangle\). If the inner product of two different states is zero, i.e., \(\langle\phi|\psi\rangle = 0\), the states are said to be orthogonal, representing completely independent physical situations.

Physical quantities that can be measured, such as position, momentum, and energy, are called observables. In quantum mechanics, observables are represented by Hermitian operators. An operator \(A\) is Hermitian if it is equal to its own conjugate transpose, \(A = A^\dagger\). A key property of Hermitian operators is that their eigenvalues are always real, which is necessary as they correspond to the results of physical measurements.

When an observable \(A\) is measured, the only possible results are the eigenvalues of that operator. The eigenvalue equation is given by:
$$
A |\alpha\rangle = \alpha |\alpha\rangle
$$
Here, \(\alpha\) is an eigenvalue and \(|\alpha\rangle\) is the corresponding eigenvector. If we perform a measurement of \(A\) and obtain the result \(\alpha\), the state of the system collapses to the corresponding eigenstate \(|\alpha\rangle\).

To describe a particle in space, we often work in the position basis. The basis vectors are denoted by \(|x\rangle\), representing a state of definite position \(x\). The representation of a state vector \(|\psi\rangle\) in this basis is the wavefunction, \(\psi(x)\), which is defined by the inner product:
$$
\psi(x) = \langle x|\psi\rangle
$$

---

The notation \(\langle x|\psi\rangle\) can be confusing. It's helpful to draw an analogy to a familiar discrete vector space, like 3D Euclidean space.

**In a Discrete Basis:**

Imagine a standard 3D vector, \(\vec{V}\). We can express it in a basis, which is a set of three orthogonal unit vectors, \(B = \{\hat{e}_1, \hat{e}_2, \hat{e}_3\}\) (like \(\hat{i}, \hat{j}, \hat{k}\)).
*   The **basis** is the complete set \(B\).
*   A **basis vector** is a single member of that set, like \(\hat{e}_1\). The `1` is a discrete **index**.
*   To find the component of \(\vec{V}\) along the \(\hat{e}_1\) direction, we take the dot product (the inner product): \(V_1 = \hat{e}_1 \cdot \vec{V}\).
*   The vector can be reconstructed by summing over its components: \(\vec{V} = V_1 \hat{e}_1 + V_2 \hat{e}_2 + V_3 \hat{e}_3 = \sum_{i=1}^3 (\hat{e}_i \cdot \vec{V}) \hat{e}_i\).

**In the Continuous Position Basis:**

Quantum mechanics uses the same logic, but for an infinite, continuous basis.
*   The **basis** is the infinite set of all position eigenvectors, \( \{ |x\rangle \} \) for every possible value of \(x\).
*   A **basis vector** is a single member of that set, \(|x\rangle\). The position \(x\) itself acts as a continuous **index**. So, \(|2\rangle\) and \(|3.14\rangle\) are two different basis vectors in this infinite set.
*   The expression \(\langle x|\psi\rangle\) means "take the inner product of the state vector \(|\psi\rangle\) with the *specific basis vector indexed by x*".
*   The result is a complex number, \(\psi(x)\), which is the component of \(|\psi\rangle\) along that basis vector \(|x\rangle\). The collection of these components for all \(x\) forms the wavefunction.
*   The state vector can be reconstructed by "summing" (integrating) over the continuous basis: \(|\psi\rangle = \int dx' |x'⟩⟨x'|ψ⟩\).

So, when we write \(\psi(x) = \langle x|\psi\rangle\), we are simply asking, "What is the projection of the quantum state \(|\psi\rangle\) onto the specific direction in Hilbert space that corresponds to the definite position \(x\)?"

The wavefunction \(\psi(x)\) gives us a continuous function that describes the quantum state in terms of position.

The physical meaning of the wavefunction is related to the probability of finding the particle at a certain position. According to Born's rule, the probability density of finding the particle at a position \(x\) is given by the square of the absolute value of the wavefunction:
$$
p(x) = |\psi(x)|^2 = \psi^*(x)\psi(x)
$$
where \(\psi^*(x)\) is the complex conjugate of \(\psi(x)\).

---

Just as state vectors can be represented in a basis, so can operators. The form an operator takes depends on the basis you choose to work in.

#### Position Operator
The simplest operator in the position basis is the **position operator**, \(\hat{x}\). Its action on a state vector \(|\psi\rangle\), when viewed from the position basis, is simply multiplication by the position \(x\):
$$
\langle x | \hat{x} | \psi \rangle = x \langle x | \psi \rangle = x \psi(x)
$$
So, in the position representation, the \(\hat{x}\) operator is just "multiply by \(x\)".

#### Momentum Operator
The **momentum operator**, \(\hat{p}\), has a less trivial representation. In the position basis, the action of \(\hat{p}\) is that of a differential operator:
$$
\langle x | \hat{p} | \psi \rangle = -i\hbar \frac{\partial}{\partial x} \psi(x)
$$
This is a fundamental postulate of quantum mechanics. It establishes a deep connection between momentum and the spatial variation of the wavefunction. A state with high momentum has a wavefunction that oscillates very rapidly as a function of position.

We can use this to find the wavefunction of a state with a definite momentum \langle p \rangle. Such a state is an eigenvector of the momentum operator, satisfying \(\hat{p}|p\rangle = p|p\rangle\). Writing this in the position basis gives a differential equation for its wavefunction, \(\psi_p(x) = \langle x|p\rangle\) (think of \(|p\rangle\) as \(|\psi\rangle\) in the previous equation):
$$
-i\hbar \frac{\partial}{\partial x} \psi_p(x) = \langle x | \hat{p} | p \rangle = p \langle x | p \rangle = p \, \psi_p(x)
$$
The solution is a plane wave:
$$
\psi_p(x) = A e^{ipx/\hbar}
$$
This shows that a state of definite momentum is a wave with a single, constant wavelength, spread throughout all of space.

---
The time evolution of a quantum state is governed by a unitary operator. Let's denote the state of a system at time \(t_0\) by \(|\psi(t_0)\rangle\). At a later time \(t_0+t\), the state will be \(|\psi(t_0+t)\rangle\), and the transformation is given by the time evolution operator \(U(t)\):
\[
|\psi(t_0+t)\rangle = U(t) |\psi(t_0)\rangle
\]
A fundamental postulate of quantum mechanics is that the inner product between two states is preserved during time evolution. This is because the total probability of finding the particle in some state must always be 1, meaning the norm of the state vector is conserved. If we have two states \(|\psi\rangle\) and \(|\phi\rangle\), then their inner product \(\langle\phi|\psi\rangle\) must be constant in time.
\[
\langle\phi(t_0+t)|\psi(t_0+t)\rangle = \langle\phi(t_0)|\psi(t_0)\rangle
\]
Substituting the time evolution operator:
\[
\langle\phi(t_0)|U^\dagger(t)U(t)|\psi(t_0)\rangle = \langle\phi(t_0)|\psi(t_0)\rangle
\]
Since this must hold for any pair of states, the operator \(U(t)\) must be unitary:
\[
U^\dagger(t)U(t) = I
\]

Now, let's consider an infinitesimal time evolution by a small amount \(\epsilon\). At \(t=0\), there is no evolution, so \(U(0)=I\). For a small \(\epsilon\), we can write the time evolution operator as:
\[
U(\epsilon) \approx I + \epsilon G
\]
where \(G\) is called the generator of the time translation. The adjoint of this operator is:
\[
U^\dagger(\epsilon) \approx I + \epsilon G^\dagger
\]
Applying the unitary condition \(U^\dagger(\epsilon)U(\epsilon) = I\):
\[
(I + \epsilon G^\dagger)(I + \epsilon G) = I
\]
Expanding this and keeping terms up to the first order in \(\epsilon\):
\[
I + \epsilon G + \epsilon G^\dagger + O(\epsilon^2) = I
\]
This implies that the generator \(G\) must be anti-Hermitian:
\[
G + G^\dagger = 0
\]

Any anti-Hermitian operator can be written as an imaginary number times a Hermitian operator. We define a Hermitian operator \(H\) such that:
\[
G = -\frac{i}{\hbar} H
\]
Here, \(\hbar\) is the reduced Planck constant, introduced to make \(H\) have units of energy. The operator \(H\) being Hermitian (\(H=H^\dagger\)) is consistent with \(G\) being anti-Hermitian. The Hermitian operator \(H\) is the Hamiltonian, which corresponds to the observable of the total energy of the system. All observables in quantum mechanics are represented by Hermitian operators.

So, the infinitesimal time evolution operator is:
\[
U(\epsilon) = I - \frac{i\epsilon}{\hbar} H
\]
From this expression, one can derive the Schrödinger equation, which governs the time evolution of quantum states.

---

### A Note on Why Observables are Hermitian

It is a fundamental postulate of quantum mechanics that all observables (like position, momentum, and energy) are represented by Hermitian operators. This isn't an arbitrary choice; it's required for the mathematical framework to be consistent with physical reality. There are two primary reasons for this:

1.  **Measurement Outcomes Must Be Real Numbers:** When we measure a physical quantity, the result is always a real number (e.g., 3 meters, -1.5 Joules). A key mathematical property of Hermitian operators is that their **eigenvalues are always real**. Since the possible results of a quantum measurement are the eigenvalues of the corresponding operator, this property ensures that our theoretical predictions for measurements are always real numbers, as they must be.

2.  **Orthogonality of States:** The eigenstates of a Hermitian operator that correspond to different eigenvalues are **orthogonal**. This is crucial for measurement. If we measure an observable and get a specific value, the system's state "collapses" into the corresponding eigenstate. Orthogonality ensures that these possible outcome-states are distinct and independent. After a measurement yielding eigenvalue \(\alpha_1\), the system is in state \(|\alpha_1\rangle\), and the probability of immediately measuring a different value \(\alpha_2\) is zero, because \(\langle\alpha_2|\alpha_1\rangle = 0\). This guarantees that our measurements are unambiguous.



