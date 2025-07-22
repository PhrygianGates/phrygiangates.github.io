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

---

#### A Note on Why Observables are Hermitian

It is a fundamental postulate of quantum mechanics that all observables (like position, momentum, and energy) are represented by Hermitian operators. This isn't an arbitrary choice; it's required for the mathematical framework to be consistent with physical reality. There are two primary reasons for this:

1.  **Measurement Outcomes Must Be Real Numbers:** When we measure a physical quantity, the result is always a real number (e.g., 3 meters, -1.5 Joules). A key mathematical property of Hermitian operators is that their **eigenvalues are always real**. Since the possible results of a quantum measurement are the eigenvalues of the corresponding operator, this property ensures that our theoretical predictions for measurements are always real numbers, as they must be.

2.  **Orthogonality of States:** The eigenstates of a Hermitian operator that correspond to different eigenvalues are **orthogonal**. This is crucial for measurement. If we measure an observable and get a specific value, the system's state "collapses" into the corresponding eigenstate. Orthogonality ensures that these possible outcome-states are distinct and independent. After a measurement yielding eigenvalue \(\alpha_1\), the system is in state \(|\alpha_1\rangle\), and the probability of immediately measuring a different value \(\alpha_2\) is zero, because \(\langle\alpha_2|\alpha_1\rangle = 0\). This guarantees that our measurements are unambiguous.

---

We previously found that for an infinitesimal time step \(\epsilon\), the time evolution operator is:
\[
U(\epsilon) = I - \frac{i\epsilon}{\hbar} H
\]
To find the operator for a finite time interval \(t\), we can divide the interval into \(N\) small steps, where \(t = N\epsilon\). The total evolution is the product of these small evolutions:
\[
U(t) = \lim_{N\to\infty} \left(I - \frac{i\epsilon}{\hbar} H\right)^N = \lim_{N\to\infty} \left(I - \frac{it}{N\hbar} H\right)^N
\]
This limit is the definition of the exponential function, which gives us the finite time evolution operator:
\[
U(t) = e^{-iHt/\hbar}
\]
#### Time-Dependent Schrödinger Equation
Let's return to the infinitesimal form to derive the equation of motion for a state vector. We have:
\[
|\psi(t+\epsilon)\rangle = U(\epsilon)|\psi(t)\rangle = \left(I - \frac{i\epsilon}{\hbar} H\right)|\psi(t)\rangle
\]
Rearranging this gives:
\[
\frac{|\psi(t+\epsilon)\rangle - |\psi(t)\rangle}{\epsilon} = -\frac{i}{\hbar} H |\psi(t)\rangle
\]
Taking the limit as \(\epsilon \to 0\), the left side becomes the definition of the derivative, yielding the **Time-Dependent Schrödinger Equation**:
\[
i\hbar \frac{\partial}{\partial t}|\psi(t)\rangle = H|\psi(t)\rangle
\]
This is the central equation of quantum dynamics, describing how a system's state vector changes over time.

#### Time-Independent Schrödinger Equation
A special, but very important, case is to consider states with a definite energy. These are the eigenstates of the Hamiltonian, which we will denote by \(|E\rangle\). They satisfy the eigenvalue equation:
\[
H|E\rangle = E|E\rangle
\]
This is known as the **Time-Independent Schrödinger Equation**.

It is called "time-independent" because its solutions are states whose physical properties do not change in time. These are called **stationary states**. Let's see why. If we take a state with definite energy, \(|\psi(0)\rangle = |E\rangle\), its time evolution is:
\[
|\psi(t)\rangle = U(t)|E\rangle = e^{-iHt/\hbar}|E\rangle
\]
Since \(|E\rangle\) is an eigenstate of \(H\), we can replace \(H\) with its eigenvalue \(E\):
\[
|\psi(t)\rangle = e^{-iEt/\hbar}|E\rangle
\]
The state vector \(|E\rangle\) only acquires a time-dependent phase factor. When we calculate the probability density (or any other observable), this phase factor cancels out. For example:
\[
|\langle x|\psi(t)\rangle|^2 = |e^{-iEt/\hbar}\langle x|E\rangle|^2 = |e^{-iEt/\hbar}|^2 |\langle x|E\rangle|^2 = |\psi_E(x)|^2
\]
The probability distribution is constant in time. The Time-Independent Schrödinger Equation is therefore used to find the set of stable, stationary states and their corresponding energies for a given system.


---

A symmetry in physics is a transformation that leaves the laws of physics unchanged. In quantum mechanics, this has a profound consequence: for every continuous symmetry of a system, there is a corresponding conserved quantity. This is the quantum mechanical version of Noether's theorem.

Let's consider a transformation represented by a unitary operator \(V\). This operator acts on a state vector \(|\psi\rangle\) to produce a transformed state \(|\psi'\rangle = V|\psi\rangle\).

For \(V\) to be a symmetry of the dynamics, the time evolution of the system must be the same for the original and transformed states. If a state \(|\psi_1\rangle\) at time \(t_1\) evolves to \(|\psi_2\rangle\) at time \(t_2\), then the transformed state \(V|\psi_1\rangle\) must evolve to \(V|\psi_2\rangle\) over the same time interval.

Let \(U(t_2-t_1)\) be the time evolution operator. The evolution of the original state is:
\[ |\psi_2\rangle = U(t_2-t_1) |\psi_1\rangle \]
The evolution of the transformed state must be:
\[ V|\psi_2\rangle = U(t_2-t_1) (V|\psi_1\rangle) \]
Substituting the first equation into the second gives:
\[ V(U(t_2-t_1)|\psi_1\rangle) = U(t_2-t_1)V|\psi_1\rangle \]
Since this must hold for any state \(|\psi_1\rangle\), it implies that the symmetry operator \(V\) must commute with the time evolution operator \(U(t)\):
\[ [V, U(t)] = VU(t) - U(t)V = 0 \]

This is a general condition for a transformation to be a symmetry. Now, let's see what this means for the Hamiltonian. We know that \(U(t) = e^{-iHt/\hbar}\). For \(V\) to commute with \(U(t)\), it must commute with \(H\). We can see this by considering an infinitesimal time step \(\epsilon\):
\[ U(\epsilon) = I - \frac{i\epsilon}{\hbar} H \]
The commutation relation becomes:
\[ V\left(I - \frac{i\epsilon}{\hbar} H\right) = \left(I - \frac{i\epsilon}{\hbar} H\right)V \]
Expanding both sides:
\[ V - \frac{i\epsilon}{\hbar} VH = V - \frac{i\epsilon}{\hbar} HV \]
This simplifies to \(VH = HV\), or:
\[ [V, H] = 0 \]

#### From Symmetries to Observable Conservation Laws

The condition \([V, H] = 0\) shows that a symmetry operator commutes with the Hamiltonian. But how does this lead to a conservation law for a measurable quantity like energy or momentum? The key is to shift focus from the transformation operator \(V\) to its **generator**.

Conservation laws in physics apply to *observables*—quantities represented by Hermitian operators whose eigenvalues are the real numbers we measure in experiments.
*   The **symmetry operator \(V\)** (e.g., a finite rotation) is unitary, but typically not Hermitian. Its expectation value \(\langle V \rangle\) is conserved if \([V,H]=0\), but this value doesn't correspond to a standard physical observable.
*   The **generator \(G\)** of a continuous symmetry is a Hermitian operator. Therefore, it represents a physical observable.

This is why we make the connection: the symmetry of the system (represented by \(V\)) implies the existence of a conserved *observable* (represented by \(G\)). The statement \(\frac{d}{dt}\langle G \rangle = 0\) is the conservation law we are looking for.

Let's illustrate this with the most important examples.

#### Example: Spatial Translation and Momentum Conservation
Consider a system that is symmetric under spatial translation. This means the laws of physics governing the system are the same everywhere; for example, the potential energy is constant, \(V(x) = V_0\).

A translation by a vector \(\vec{a}\) is performed by the operator \(T(\vec{a})\). When this operator acts on a wavefunction, it shifts its argument:
\[ T(\vec{a}) \psi(\vec{x}) = \psi(\vec{x}-\vec{a}) \]
Let's find the generator of this transformation by considering an infinitesimal translation along the x-axis, \(T(\delta x)\). We can Taylor expand the shifted wavefunction:
\[ \psi(x-\delta x, y, z) \approx \psi(x, y, z) - \delta x \frac{\partial}{\partial x} \psi(x, y, z) \]
Recall that the momentum operator's x-component is \(\hat{p}_x = -i\hbar \frac{\partial}{\partial x}\), which means \(\frac{\partial}{\partial x} = \frac{i}{\hbar}\hat{p}_x\). Substituting this in:
\[ T(\delta x)\psi(\vec{x}) \approx \psi(\vec{x}) - \delta x \left(\frac{i}{\hbar}\hat{p}_x\right) \psi(\vec{x}) = \left(I - \frac{i}{\hbar} \delta x \hat{p}_x\right) \psi(\vec{x}) \]
This shows that for an infinitesimal translation, the operator is \(T(\delta x) \approx I - \frac{i}{\hbar} \delta x \hat{p}_x\). By extending this to a finite translation \(a\), we get the exponential form:
\[ T(a) = e^{-ia\hat{p}_x/\hbar} \]
This reveals that the **momentum operator \(\hat{p}\) is the generator of spatial translations.**

If the Hamiltonian is invariant under translation, then \([T(a), H] = 0\), which implies that the generator also commutes with the Hamiltonian:
\[ [\hat{p}, H] = 0 \]
Following our derivation for a general generator \(G\), this immediately means that the expectation value of momentum is conserved: \(\frac{d}{dt}\langle \hat{p} \rangle = 0\).

#### Example: Rotational Invariance and Angular Momentum Conservation
Now consider a system symmetric under rotations, such as an atom in a central potential \(V(r) = V(|\vec{r}|)\).

A rotation of the physical system by an angle \(\theta\) about an axis \(\hat{n}\) is performed by the operator \(R(\hat{n}, \theta)\). When this operator acts on a wavefunction, it rotates the coordinate system in the opposite direction:
\[ R(\hat{n}, \theta) \psi(\vec{r}) = \psi(R^{-1}(\hat{n}, \theta)\vec{r}) \]
Let's find the generator by considering an infinitesimal rotation by an angle \(\delta\phi\) around the z-axis. The inverse rotation transforms the coordinates as:
*   \(x' = x \cos(-\delta\phi) - y \sin(-\delta\phi) \approx x + y\delta\phi\)
*   \(y' = x \sin(-\delta\phi) + y \cos(-\delta\phi) \approx y - x\delta\phi\)
*   \(z' = z\)

Applying this to the wavefunction and performing a Taylor expansion:
\[ R(\hat{z}, \delta\phi)\psi(x,y,z) = \psi(x+y\delta\phi, y-x\delta\phi, z) \approx \psi(x,y,z) + y\delta\phi \frac{\partial\psi}{\partial x} - x\delta\phi \frac{\partial\psi}{\partial y} \]
\[ R(\hat{z}, \delta\phi)\psi \approx \left( I + \delta\phi \left(y\frac{\partial}{\partial x} - x\frac{\partial}{\partial y}\right) \right) \psi \]
We recognize the z-component of the angular momentum operator: \(\hat{L}_z = \hat{x}\hat{p}_y - \hat{y}\hat{p}_x = -i\hbar\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right) = i\hbar\left(y\frac{\partial}{\partial x} - x\frac{\partial}{\partial y}\right)\).
This means \(\left(y\frac{\partial}{\partial x} - x\frac{\partial}{\partial y}\right) = \frac{-i}{\hbar}\hat{L}_z\). Substituting this in:
\[ R(\hat{z}, \delta\phi)\psi \approx \left( I + \delta\phi \left(\frac{-i}{\hbar}\hat{L}_z\right) \right)\psi = \left( I - \frac{i}{\hbar} \delta\phi \hat{L}_z \right)\psi \]
The finite rotation operator is therefore:
\[ R(\hat{z}, \theta) = e^{-i\theta\hat{L}_z/\hbar} \]
This shows that the **angular momentum operator \(\hat{L}\) is the generator of rotations.**

If the Hamiltonian is rotationally invariant, then \([R, H] = 0\), which implies \([\hat{L}, H] = 0\). This leads to the conservation of angular momentum: \(\frac{d}{dt}\langle \hat{L} \rangle = 0\).

Many symmetries in physics are continuous, meaning they can be built up from infinitesimal transformations. Examples include translations in space, rotations, and time translation itself. A continuous unitary symmetry operator \(V(\lambda)\) depending on a parameter \(\lambda\) can be written in terms of a Hermitian operator \(G\), called the **generator** of the symmetry:
\[ V(\lambda) = e^{i\lambda G} \]
For an infinitesimal transformation with a small parameter \(\delta\lambda\), the operator is approximately:
\[ V(\delta\lambda) \approx I + i\delta\lambda G \]
If \(V\) is a symmetry, then \([V(\lambda), H] = 0\) for any \(\lambda\). This implies that the generator \(G\) must also commute with the Hamiltonian:
\[ [G, H] = 0 \]
This is a crucial result. It tells us that the observable corresponding to the generator of a symmetry is a conserved quantity. To see this, let's look at the time evolution of the expectation value of \(G\), \(\langle G \rangle\). Using the Schrödinger equation:
\[ \frac{d}{dt}\langle G \rangle = \frac{d}{dt}\langle\psi(t)|G|\psi(t)\rangle \]
The time derivative of a state is given by \(\frac{\partial}{\partial t}|\psi(t)\rangle = -\frac{i}{\hbar}H|\psi(t)\rangle\), and for the bra, \(\frac{\partial}{\partial t}\langle\psi(t)| = \frac{i}{\hbar}\langle\psi(t)|H\). Applying the product rule:
\[ \frac{d}{dt}\langle G \rangle = \left(\frac{d}{dt}\langle\psi(t)|\right)G|\psi(t)\rangle + \langle\psi(t)|G\left(\frac{d}{dt}|\psi(t)\rangle\right) \]
\[ \frac{d}{dt}\langle G \rangle = \left(\frac{i}{\hbar}\langle\psi(t)|H\right)G|\psi(t)\rangle + \langle\psi(t)|G\left(-\frac{i}{\hbar}H|\psi(t)\rangle\right) \]
\[ \frac{d}{dt}\langle G \rangle = \frac{i}{\hbar}\left(\langle\psi(t)|HG|\psi(t)\rangle - \langle\psi(t)|GH|\psi(t)\rangle\right) \]
\[ \frac{d}{dt}\langle G \rangle = \frac{i}{\hbar}\langle\psi(t)|[H, G]|\psi(t)\rangle \]
Since \([G, H] = 0\), it follows that \([H, G] = 0\). Therefore:
\[ \frac{d}{dt}\langle G \rangle = 0 \]
The expectation value of \(G\) is constant in time. This is the essence of Noether's theorem: if a system has a continuous symmetry, then there is a corresponding observable (the generator of the symmetry) whose expectation value is conserved.

Here are some key examples:
*   **Time Translation Invariance:** The generator is the Hamiltonian \(H\) itself. If \(H\) is not explicitly time-dependent, the system is symmetric under time translation, and energy (the expectation value of \(H\)) is conserved.
*   **Spatial Translation Invariance:** The generator is the momentum operator \(\hat{p}\). If a system is symmetric under spatial translations (i.e., the potential is uniform), then momentum is conserved.
*   **Rotational Invariance:** The generator is the angular momentum operator \(\hat{L}\). If a system is symmetric under rotations (e.g., a central potential), then angular momentum is conserved.

---
