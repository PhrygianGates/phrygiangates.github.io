+++
date = '2025-10-22T18:00:00+08:00'
title = 'Spin'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

For the one-dimensional harmonic oscillator, its Hamiltonian can be written as \(H = \frac{p^2}{2} + \frac{1}{2}\omega^2 x^2\). Our goal is to solve its energy eigenvalue equation \(H\varphi = E\varphi\). To solve it using a more concise algebraic method, we introduce a pair of ladder operators defined as:
\[
a^{\pm} = \frac{p \pm i\omega x}{\sqrt{2\omega}}
\]
Here, \(a^+\) is commonly called the creation operator \(a^\dagger\), while \(a^-\) is called the annihilation operator \(a\). Through these operators, we can express the Hamiltonian in a more compact form. We define the number operator as \(N = a^\dagger a\). After derivation, we find that the relation between the Hamiltonian and the number operator is:
\[
H = \omega \left(N + \frac{1}{2}\right)
\]
This form greatly simplifies the solution process.

---

Directly solving the Schrödinger equation for the harmonic oscillator is a second-order ordinary differential equation and is rather cumbersome. Dirac invented a deeper algebraic method whose core idea is to attempt to “factorize” the Hamiltonian operator \(H\). The Hamiltonian \(H = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2\) in natural units (setting \(m=1, \hbar=1\)) is \(H = \frac{p^2}{2} + \frac{1}{2}\omega^2 x^2\), which resembles a sum of squares \(A^2+B^2\). Although in quantum mechanics the position operator \(x\) and the momentum operator \(p\) do not commute (\([x, p] = i\)) and cannot be directly factorized like ordinary numbers, this idea inspires us to construct a pair of operators \(a\) and \(a^\dagger\) that are Hermitian conjugates of each other, such that \(H\) can be compactly expressed using their product \(a^\dagger a\). This pair of operators is precisely the raising and lowering operators introduced earlier.

Let us compute the explicit form of \(a^\dagger a\), where \(a^\dagger = a^+\) while \(a = a^-\):
\[
\begin{aligned}
a^\dagger a &= \left( \frac{p + i\omega x}{\sqrt{2\omega}} \right) \left( \frac{p - i\omega x}{\sqrt{2\omega}} \right) \\
&= \frac{1}{2\omega} (p + i\omega x)(p - i\omega x) \\
&= \frac{1}{2\omega} (p^2 - i\omega px + i\omega xp + \omega^2 x^2) \\
&= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - i\omega(px - xp))
\end{aligned}
\]
Using the commutation relation \([p, x] = -i\), i.e., \(px - xp = -i\), substitute into the above to obtain:
\[
\begin{aligned}
a^\dagger a &= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - i\omega(-i)) \\
&= \frac{1}{2\omega} (p^2 + \omega^2 x^2 - \omega) \\
&= \frac{p^2 + \omega^2 x^2}{2\omega} - \frac{1}{2}
\end{aligned}
\]
Thus we obtain \(a^\dagger a = \frac{H}{\omega} - \frac{1}{2}\), and after rearrangement we arrive at the compact form of the Hamiltonian \(H = \omega (a^\dagger a + \frac{1}{2})\). If we define the number operator \(N = a^\dagger a\), then \(H = \omega(N + \frac{1}{2})\). This algebraic form is very powerful and can directly lead to all the core physical conclusions of the quantum harmonic oscillator.

First, the energy of the system is quantized. Because \(H\) and \(N\) differ only by a constant, they share common eigenstates. If \(|n\rangle\) is an eigenstate of \(N\) with eigenvalue \(n\), namely \(N|n\rangle = n|n\rangle\), then acting with the Hamiltonian yields \(H|n\rangle = \omega(N+\frac{1}{2})|n\rangle = \omega(n+\frac{1}{2})|n\rangle\). This means the system’s energy can only take a series of discrete values:
\[ E_n = \omega\left(n + \frac{1}{2}\right) \]
Second, the operators \(a^\dagger\) and \(a\) play the role of the energy “ladder.” To prove this, we first compute their commutators with the Hamiltonian. Using \([x, p] = i\), we can obtain \([a, a^\dagger] = 1\). It follows that:
\[ [H, a] = [\omega(a^\dagger a + 1/2), a] = \omega[a^\dagger a, a] = -\omega a \]
\[ [H, a^\dagger] = [\omega(a^\dagger a + 1/2), a^\dagger] = \omega[a^\dagger a, a^\dagger] = \omega a^\dagger \]
Now, we apply \(H\) to \(a|n\rangle\), where \(|n\rangle\) is an energy eigenstate with energy \(E_n\):
\[ H(a|n\rangle) = (aH + [H, a])|n\rangle = aE_n|n\rangle - \omega a|n\rangle = (E_n - \omega)(a|n\rangle) \]
This shows that \(a|n\rangle\) is a new energy eigenstate whose energy is exactly one quantum \(\omega\) less than \(E_n\). Therefore, \(a\) acting on the state \(|n\rangle\) yields a new state corresponding to \(n-1\), and is thus called the annihilation operator. Similarly, we can prove the action of \(a^\dagger\):
\[ H(a^\dagger|n\rangle) = (a^\dagger H + [H, a^\dagger])|n\rangle = a^\dagger E_n|n\rangle + \omega a^\dagger|n\rangle = (E_n + \omega)(a^\dagger|n\rangle) \]
This shows that \(a^\dagger|n\rangle\) has energy \(E_n + \omega\), so \(a^\dagger\) is called the creation operator. They respectively decrease or increase the energy eigenvalue by one unit \(\omega\).

Moreover, since the system energy cannot be lowered without bound (\(H\) is positive definite), there must exist a lowest-energy ground state, denoted \(|0\rangle\). The annihilation operator acting on the ground state can no longer lower its energy, so necessarily \(a|0\rangle = 0\). At this point, the eigenvalue of the number operator is \(n=0\), and the corresponding ground-state energy is \(E_0 = \omega(0 + \frac{1}{2}) = \frac{\omega}{2}\). This famous “zero-point energy” is a direct manifestation of quantum effects.

Finally, all excited states can be generated from the ground state via the creation operator. Starting from the ground state \(|0\rangle\) and repeatedly applying the creation operator \(a^\dagger\), one can obtain all excited states like climbing a ladder:
\[ |n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}} |0\rangle \]

The denominator \(\sqrt{n!}\) in the expression is a normalization constant. Its role is to ensure that the state vector \(|n\rangle\) has unit length, i.e., \(\langle n|n\rangle = 1\), which is a basic requirement of the probabilistic interpretation in quantum mechanics. If we start from the ground state \(|0\rangle\) (assumed normalized), each application of the creation operator \(a^\dagger\) changes the length of the state vector. For example, the inner product (norm squared) of the unnormalized \(a^\dagger|0\rangle\) state is \(\langle 0| a a^\dagger |0\rangle = \langle 0| (a^\dagger a + 1) |0\rangle = 1\). And the inner product of the unnormalized \((a^\dagger)^2|0\rangle\) state is \(\langle 0| a^2 (a^\dagger)^2 |0\rangle = 2\). One can infer that the norm squared of \((a^\dagger)^n|0\rangle\) is \(n!\). Therefore, to make the final \(|n\rangle\) state satisfy the normalization condition \(\langle n|n\rangle=1\), we need to divide it by \(\sqrt{n!}\).

This shows that all energy states form an equally spaced spectrum with spacing \(\omega\). This picture is also the origin of the “particle” concept in quantum field theory: each action of \(a^\dagger\) amounts to “creating” a quantum of energy \(\omega\) in the field.
