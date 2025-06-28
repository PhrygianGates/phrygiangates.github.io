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

We can use this to find the wavefunction of a state with a definite momentum \(p\). Such a state is an eigenvector of the momentum operator, satisfying \(\hat{p}|p\rangle = p|p\rangle\). Writing this in the position basis gives a differential equation for its wavefunction, \(\psi_p(x) = \langle x|p\rangle\):
$$
-i\hbar \frac{\partial}{\partial x} \psi_p(x) = p \, \psi_p(x)
$$
The solution is a plane wave:
$$
\psi_p(x) = A e^{ipx/\hbar}
$$
This shows that a state of definite momentum is a wave with a single, constant wavelength, spread throughout all of space.


