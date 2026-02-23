+++
date = '2026-01-03T22:00:00+08:00'
title = 'Quantum Field Theory'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

Let’s talk about the basic setup of quantum field theory.

Start with a single quantum harmonic oscillator. Its energy eigenvalue equation is
\[
H|\psi\rangle = E|\psi\rangle .
\]
It has a set of discrete energy eigenstates. For the harmonic oscillator, a more convenient set of eigenstates is the number states \(|n\rangle\) (\(n=0,1,2,\dots\)), satisfying \(H|n\rangle=E_n|n\rangle\). We introduce the annihilation operator \(a\) and the creation operator \(a^\dagger\), require them to satisfy \([a,a^\dagger]=1\), and define the number operator \(N=a^\dagger a\). The number states are also eigenstates of \(N\):
\[
N|n\rangle = n|n\rangle .
\]
They form an orthonormal basis, satisfying \(\langle n|m\rangle=\delta_{nm}\), and obey the completeness relation \(\sum_{n=0}^{\infty}|n\rangle\langle n|=I\).

The action of the raising and lowering operators on the number states is
\[
a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,\qquad
a|n\rangle=\sqrt{n}\,|n-1\rangle .
\]

Now consider the case of multiple harmonic oscillators (i.e., many independent harmonic-oscillator degrees of freedom). Use \(|n_1,n_2,n_3,\dots\rangle\) to denote: the occupation number of the 1st oscillator is \(n_1\), that of the 2nd oscillator is \(n_2\), and so on. The creation operator \(a_j^\dagger\) of the \(j\)‑th oscillator increases \(n_j\) by 1:
\[
a_j^\dagger|n_1,\dots,n_j,\dots\rangle
=\sqrt{n_j+1}\,|n_1,\dots,n_j+1,\dots\rangle ,
\]
Correspondingly, \(a_j\) decreases \(n_j\) by 1:
\[
a_j|n_1,\dots,n_j,\dots\rangle
=\sqrt{n_j}\,|n_1,\dots,n_j-1,\dots\rangle .
\]

---

In ordinary quantum mechanics, we often fix the particle number when discussing systems. A single-particle wavefunction is \(\psi(x)=\langle x|\psi\rangle\). If the particle number is fixed to \(N\), the many-particle wavefunction can be written as \(\psi(x_1,x_2,\dots,x_N)=\langle x_1,x_2,\dots,x_N|\Psi\rangle\).

If the particle number is not fixed, and we allow 0 particles, 1 particle, 2 particles, … to be discussed simultaneously, then we need a “total” Hilbert space to accommodate them. A very intuitive construction is: choose a complete, orthonormal single-particle basis \(\{|u_j\rangle\}\), regard each label \(j\) as an independent harmonic-oscillator degree of freedom, and use a pair of raising/lowering operators \(a_j,a_j^\dagger\) to decrease/increase the occupation number of this degree of freedom. Next we will also introduce an operator with a position label, \(\hat{\Psi}(x)\). Its Hermitian conjugate \(\hat{\Psi}^\dagger(x_0)\), acting on the state with all occupation numbers zero (to be denoted below as \(|0\rangle\)), gives the single-particle position eigenstate \(|x_0\rangle\):
\[
\hat{\Psi}^\dagger(x_0)\,|0\rangle = |x_0\rangle .
\]

To write this idea in a computable form, we first choose a complete, orthonormal set of single-particle states \(\{|u_j\rangle\}\) (\(j=1,2,\dots\)). Here \(j\) is merely the label of the single-particle basis vectors (for example, the label of momentum eigenstates), not the “particle number”; the particle number is represented by \(n,n_j\) in \(|n\rangle\) or \(|n_1,n_2,\dots\rangle\).

Here we must emphasize a point that is easy to confuse: \(|u_j\rangle\) is a state vector in the “single-particle Hilbert space”, whereas \(|1_j\rangle\) that will appear later is a vector in the “total space” constructed from many harmonic oscillators. Strictly speaking, they do not live in the same space, so we cannot directly write \(|u_j\rangle=|1_j\rangle\). By “correspondence” we mean: if we look only at the part of the total space with total occupation number 1, it can be put into one-to-one correspondence with the single-particle space (more rigorously, with the “single-oscillator space”; even when the particle number is not one, it can still be put into one-to-one correspondence, but those states with total occupation number equal to 2 cannot be in one-to-one correspondence, because it may be that not only one oscillator has occupation number 2, but also that two oscillators each have occupation number 1). For computational convenience, we stipulate the correspondence between bases as
\[
|u_j\rangle \longleftrightarrow |1_j\rangle \equiv a_j^\dagger|0\rangle.
\]
In this way, if an arbitrary single-particle state is written as \(|\psi\rangle=\sum_j c_j|u_j\rangle\), then in the “total occupation number equal to 1” sector it is written as \(\sum_j c_j|1_j\rangle\). Both sides use the same set of coefficients \(c_j\), describing the same physical single-particle state, merely expressed in two different notations.

In the position representation, the wavefunctions corresponding to this set of single-particle states are denoted by
\[
u_j(x)\equiv \langle x|u_j\rangle,\qquad \langle u_j|x\rangle=u_j^*(x).
\]
and satisfy completeness
\[
\sum_j |u_j\rangle\langle u_j| = I
\]
(here \(I\) is the identity operator on the single-particle Hilbert space).

Next, for each label \(j\) (that is, the label of the chosen single-particle basis \(|u_j\rangle\)), we introduce a pair of annihilation/creation operators \(a_j, a_j^\dagger\). You can think of them as the raising/lowering operators of the “\(j\)‑th oscillator”: the occupation number (excitation number) of the \(j\)‑th oscillator is denoted by \(n_j\). These operators satisfy
\[
[a_j,a_k^\dagger]=\delta_{jk},\qquad [a_j,a_k]=0,\qquad [a_j^\dagger,a_k^\dagger]=0.
\]
This set of commutation relations ensures that, for each fixed \(j\), the algebraic structure of \(\{a_j,a_j^\dagger\}\) is the same as that of the raising/lowering operators of a single oscillator, so number states and coefficients like \(\sqrt{n_j}\) naturally appear. Using the occupation-number basis (the basis labeled by the occupation number \(n_j\) of each oscillator)
\[
|n_1,n_2,\dots\rangle
\]
we define their action as
\[
a_j|n_1,\dots,n_j,\dots\rangle=\sqrt{n_j}\,|n_1,\dots,n_j-1,\dots\rangle,
\]
\[
a_j^\dagger|n_1,\dots,n_j,\dots\rangle=\sqrt{n_j+1}\,|n_1,\dots,n_j+1,\dots\rangle.
\]
The state with all occupation numbers zero (i.e., all oscillators have occupation number 0) is defined as
\[
|0\rangle \equiv |0,0,0,\dots\rangle.
\]
Thus, the state “only the \(j\)‑th oscillator has occupation number 1, all others 0” is
\[
a_j^\dagger|0\rangle = |0,\dots,1_j,\dots\rangle \equiv |1_j\rangle.
\]
Here \(|1_j\rangle\) denotes the state “only the \(j\)‑th oscillator is excited once”. If we look only at the sector with total occupation number 1, it naturally corresponds to the single-particle Hilbert space: under this correspondence, \(|1_j\rangle\) and the single-particle state \(|u_j\rangle\) are in one-to-one correspondence.

Now define the set of operators with position labels as
\[
\hat{\Psi}(x)=\sum_j a_j\,u_j(x)=\sum_j a_j\langle x|u_j\rangle,
\qquad
\hat{\Psi}^\dagger(x)=\sum_j a_j^\dagger\,u_j^*(x)=\sum_j a_j^\dagger\langle u_j|x\rangle.
\]

Using this expansion, we can verify the above property. Acting on \(|0\rangle\):
\[
\hat{\Psi}^\dagger(x_0)|0\rangle
\;=\sum_j a_j^\dagger\,\langle u_j|x_0\rangle\,|0\rangle
\;=\sum_j \langle u_j|x_0\rangle\,(a_j^\dagger|0\rangle)
\;=\sum_j \langle u_j|x_0\rangle\,|1_j\rangle .
\]
On the other hand, from the completeness relation \(\sum_j|u_j\rangle\langle u_j|=I\) (this is an equation in the single-particle space) we immediately obtain
\[
|x_0\rangle = \sum_j |u_j\rangle\langle u_j|x_0\rangle
= \sum_j \langle u_j|x_0\rangle\,|u_j\rangle .
\]
After identifying the single-particle state \(|u_j\rangle\) with the “total occupation number 1” state \(|1_j\rangle\) via the above one-to-one correspondence, the two equations match term by term, hence \(\hat{\Psi}^\dagger(x_0)|0\rangle=|x_0\rangle\) holds.

Following this line of thought, we can also use \(\hat{\Psi}^\dagger(x)\) to “add one excitation at position \(x\)”, thereby constructing a twice-excited state. Note that the creation operators of bosons commute:
\[
[a_j^\dagger,a_k^\dagger]=0,
\]
Thus, from
\(\hat{\Psi}^\dagger(x)=\sum_j a_j^\dagger\,\langle u_j|x\rangle\)
we can expand the commutator directly:
\[
[\hat{\Psi}^\dagger(x),\hat{\Psi}^\dagger(y)]
=\hat{\Psi}^\dagger(x)\hat{\Psi}^\dagger(y)-\hat{\Psi}^\dagger(y)\hat{\Psi}^\dagger(x).
\]
Substituting the expansion of \(\hat{\Psi}^\dagger\):
\[
\hat{\Psi}^\dagger(x)\hat{\Psi}^\dagger(y)
=\sum_{j,k} a_j^\dagger a_k^\dagger\,\langle u_j|x\rangle\,\langle u_k|y\rangle,
\]
\[
\hat{\Psi}^\dagger(y)\hat{\Psi}^\dagger(x)
=\sum_{j,k} a_j^\dagger a_k^\dagger\,\langle u_j|y\rangle\,\langle u_k|x\rangle.
\]
Therefore
\[
[\hat{\Psi}^\dagger(x),\hat{\Psi}^\dagger(y)]
=\sum_{j,k}\Bigl(a_j^\dagger a_k^\dagger-a_k^\dagger a_j^\dagger\Bigr)\,\langle u_j|x\rangle\,\langle u_k|y\rangle
=\sum_{j,k}[a_j^\dagger,a_k^\dagger]\,\langle u_j|x\rangle\,\langle u_k|y\rangle
=0.
\]
Hence we define
\[
|x,y\rangle\equiv \hat{\Psi}^\dagger(x)\hat{\Psi}^\dagger(y)|0\rangle,
\]
Exchanging the two position labels does not change this state:
\[
|y,x\rangle=\hat{\Psi}^\dagger(y)\hat{\Psi}^\dagger(x)|0\rangle
=\hat{\Psi}^\dagger(x)\hat{\Psi}^\dagger(y)|0\rangle
=|x,y\rangle.
\]
This shows that the twice-excited state is symmetric under exchange, which is precisely the exchange symmetry of bosons.

---

As a concrete example, consider the energy eigenstates \(|n\rangle\) (\(n=0,1,2,\dots\)) of the single-particle harmonic oscillator. They satisfy orthonormality
\[
\langle m|n\rangle=\delta_{mn},
\]
and form a complete basis, so we have the decomposition of the identity operator
\[
\sum_{n=0}^{\infty}|n\rangle\langle n|=I.
\]

In the position representation, define their wavefunctions
\[
\psi_n(x)\equiv \langle x|n\rangle,\qquad \langle n|x\rangle=\psi_n^*(x).
\]
Then the orthogonality relation of the continuous position basis \(\langle y|x\rangle=\delta(y-x)\) can be written as
\[
\delta(y-x)=\langle y|I|x\rangle
=\sum_{n=0}^{\infty}\langle y|n\rangle\langle n|x\rangle
=\sum_{n=0}^{\infty}\psi_n(y)\psi_n^*(x).
\]

---
Here is a commonly used calculation: \(\int dx\,\hat{\Psi}^\dagger(x)\hat{\Psi}(x)\) equals the total occupation-number operator.

Note that \(\langle m|n\rangle=\delta_{mn}\) is equivalent in the position representation to
\[
\int dx\,\psi_m^*(x)\psi_n(x)=\delta_{mn}.
\]
If we use this set of basis states to label each oscillator degree of freedom, then
\[
\hat{\Psi}(x)=\sum_n a_n\psi_n(x),\qquad \hat{\Psi}^\dagger(x)=\sum_n a_n^\dagger\psi_n^*(x).
\]
Thus
\[
\int dx\,\hat{\Psi}^\dagger(x)\hat{\Psi}(x)
=\sum_{m,n}a_m^\dagger a_n\int dx\,\psi_m^*(x)\psi_n(x)
=\sum_n a_n^\dagger a_n
\equiv \sum_n N_n
\equiv N.
\]
where \(N_n\equiv a_n^\dagger a_n\) is the occupation-number operator of the \(n\)‑th degree of freedom, and \(N\) is the total occupation number (total excitation number) operator (also often called the total particle-number operator).
