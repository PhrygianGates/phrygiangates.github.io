+++
date = '2026-04-30T22:30:00+08:00'
title = 'Quantum Field Hamiltonian'
tags = ['Advanced Quantum Mechanics']
categories = ["Physics"]
+++

We are given a Hamiltonian:
\[
H=\int dx\left[\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}\right)\Psi(x)+V(x)\Psi^\dagger(x)\Psi(x)\right].
\]
Here we take \(\hbar=1\). The first term is the kinetic energy term, because in single-particle quantum mechanics, \(\hat p^2/(2m)\) in the position representation corresponds to \(-\nabla^2/(2m)\). The second term is the potential energy term, where \(\Psi^\dagger(x)\Psi(x)\) is the particle number density at position \(x\), so \(V(x)\Psi^\dagger(x)\Psi(x)\) represents the potential energy density at \(x\). If we take \(V(x)=mc^2\), it just adds a rest energy to each particle; there is still no interaction force between particles here.

According to the previous article, in the one-dimensional case, we have
\[
\Psi(x)=\int \frac{dp}{\sqrt{2\pi}}\,a(p)e^{ipx},\qquad
\Psi^\dagger(x)=\int \frac{dq}{\sqrt{2\pi}}\,a^\dagger(q)e^{-iqx}.
\]
Here, \(a(p)\) is the operator that annihilates a particle with momentum \(p\), and \(a^\dagger(q)\) is the operator that creates a particle with momentum \(q\). Let's first look at the particle number density integral that appears in the potential energy term:
\[
\int dx\,\Psi^\dagger(x)\Psi(x)
=\int dx\int \frac{dq}{\sqrt{2\pi}}\int \frac{dp}{\sqrt{2\pi}}\,
a^\dagger(q)a(p)e^{i(p-q)x}.
\]
Rearranging, we get
\[
\int dx\,\Psi^\dagger(x)\Psi(x)
=\int dp\,dq\,a^\dagger(q)a(p)\left[\frac{1}{2\pi}\int dx\,e^{i(p-q)x}\right].
\]
The integral in the square brackets is the Dirac delta function:
\[
\frac{1}{2\pi}\int dx\,e^{i(p-q)x}=\delta(p-q).
\]
Intuitively, when \(p\neq q\), the exponential factor oscillates with \(x\), and the positive and negative parts cancel each other out; when \(p=q\), the exponential factor is equal to 1, and the integral over all space diverges. The Dirac delta function is precisely the object that combines these two properties: it only contributes at \(p=q\), and in an integral, it requires setting \(p=q\). Therefore,
\[
\int dx\,\Psi^\dagger(x)\Psi(x)
=\int dp\,dq\,a^\dagger(q)a(p)\delta(p-q)
=\int dp\,a^\dagger(p)a(p).
\]
The action of the operator \(a^\dagger(p)a(p)\) is to first annihilate a particle with momentum \(p\) and then create a particle with the same momentum \(p\), so it is actually counting the number of particles with momentum \(p\). From this, we can see that when this term acts on a certain state, it does not change the momentum of the particles; if \(V(x)\) is a constant, then this term only adds the same energy to each particle and does not change the total momentum.

Now let's look at the first term, the kinetic energy term:
\[
\int dx\,\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}\right)\Psi(x).
\]
After expanding \(\Psi(x)\) into momentum modes, \(-\nabla^2/(2m)\) only acts on \(e^{ipx}\) and gives a factor of \(p^2/(2m)\):
\[
-\frac{\nabla^2}{2m}e^{ipx}=\frac{p^2}{2m}e^{ipx}.
\]
Therefore, an integral over \(x\) also appears:
\[
\frac{1}{2\pi}\int dx\,e^{i(p-q)x}=\delta(p-q),
\]
Thus, the kinetic energy term becomes
\[
\int dx\,\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}\right)\Psi(x)
=\int dp\,\frac{p^2}{2m}a^\dagger(p)a(p).
\]
This shows that the kinetic energy term just counts how many particles there are for each momentum \(p\) and multiplies them by their respective energies \(p^2/(2m)\), but it does not change a particle with momentum \(p\) into a particle with another momentum.

So in the case where \(V(x)\) is a constant, for example \(V(x)=mc^2\), the entire Hamiltonian can be written as
\[
H=\int dp\left(\frac{p^2}{2m}+mc^2\right)a^\dagger(p)a(p).
\]
If we apply this \(H\) to a state with a definite total momentum, it will only change the phase or energy weight of this state, not its total momentum. This is the meaning of momentum conservation in this free particle system. If \(V(x)\) is not a constant but truly depends on position, then the spatial translation symmetry is broken by the external potential, and momentum is generally no longer conserved.

---
When we consider local interactions of multiple types of particles, the same mechanism gives total momentum conservation, rather than requiring the momentum of each particle to be conserved separately.

For example, suppose there are two types of particles, \(A\) and \(B\). In addition to their respective kinetic energy terms, we can add a local interaction term to the Hamiltonian:
\[
H=H_{\text{kinetic}}+g\int dx\,\Psi_A^\dagger(x)\Psi_B^\dagger(x)\Psi_B(x)\Psi_A(x).
\]
Here, \(g\) is the coupling constant, which represents the strength of this interaction. This term actually describes the scattering of \(A\) and \(B\): on the right, \(\Psi_A(x)\) and \(\Psi_B(x)\) first annihilate a \(A\) particle and a \(B\) particle at the same position \(x\), and then on the left, \(\Psi_A^\dagger(x)\) and \(\Psi_B^\dagger(x)\) create a \(A\) particle and a \(B\) particle at the same position. The particle types do not change, but their individual momenta can change.

If we expand all these fields into momentum space, we will get something like
\[
\int dp_A\,dp_B\,dq_A\,dq_B\,
a_A^\dagger(q_A)a_B^\dagger(q_B)a_B(p_B)a_A(p_A)\,
\delta(p_A+p_B-q_A-q_B).
\]
Here, \(p_A,p_B\) are the momenta of the annihilated incoming particles, and \(q_A,q_B\) are the momenta of the created outgoing particles. The integral over \(x\) only gives total momentum conservation:
\[
p_A+p_B=q_A+q_B,
\]
but it does not require \(p_A=q_A\) or \(p_B=q_B\). So the momentum of a single particle can change, as long as the total momentum before and after is the same. This is why it is called scattering.

As another example, if we want the Hamiltonian to describe a \(A\) particle turning into a \(B\) particle and a \(C\) particle, we can write down
\[
\Psi_B^\dagger(x)\Psi_C^\dagger(x)\Psi_A(x).
\]
Its action is to annihilate a \(A\) and create a \(B\) and a \(C\). But the Hamiltonian must be Hermitian, because it corresponds to the observable energy and also ensures that the time evolution is unitary. Therefore, we must also add its Hermitian conjugate term:
\[
\Psi_A^\dagger(x)\Psi_C(x)\Psi_B(x).
\]
So the interaction Hamiltonian can be written as
\[
H_I=g\int dx\left[\Psi_B^\dagger(x)\Psi_C^\dagger(x)\Psi_A(x)+\Psi_A^\dagger(x)\Psi_C(x)\Psi_B(x)\right].
\]
The first term describes \(A\to B+C\), and the second term describes the reverse process \(B+C\to A\).

Time evolution comes from the Schrödinger equation. Here we still take \(\hbar=1\), and if \(H\) does not explicitly depend on time, then
\[
|\phi(t+\epsilon)\rangle=e^{-iH\epsilon}|\phi(t)\rangle.
\]
Expanding the exponential function, we get
\[
|\phi(t+\epsilon)\rangle
=\left(1-i\epsilon H-\frac{\epsilon^2}{2}H^2+\cdots\right)|\phi(t)\rangle.
\]
So the first-order term \(-i\epsilon H|\phi(t)\rangle\) represents the Hamiltonian acting once, and the second-order term \(-\epsilon^2H^2|\phi(t)\rangle/2\) represents the Hamiltonian acting twice. For the \(H_I\) above, acting once can give \(A\to B+C\) or \(B+C\to A\). Acting twice can give \(A\to B+C\to A\), and also processes like \(B+C\to A\to B+C\).

Here, "first-order" and "second-order" do not mean that in the real world a first-order process happens first, and then a second-order process happens simultaneously; they are different order contributions to the same time evolution amplitude. The total amplitude is the superposition of these terms:
\[
\mathcal A=\mathcal A^{(1)}+\mathcal A^{(2)}+\mathcal A^{(3)}+\cdots.
\]
If the coupling constant \(g\) is small, the first-order term is usually of order \(g\), and the second-order term is of order \(g^2\), so we can approximate it order by order. Pictorially, saying that \(A\) "temporarily" appears or disappears is just a convenient language to describe higher-order terms; strictly speaking, it is the contribution of intermediate states in the expansion of the time evolution operator.

---

We now want to look at the relativistic case. Let's first consider only a one-dimensional free particle, without adding potential energy.

In the ordinary non-relativistic case, the single-particle Hamiltonian is
\[
H=\frac{p^2}{2m}.
\]
In the relativistic case, energy and momentum satisfy
\[
H^2=p^2+m^2,
\]
Here we take \(c=1\). If we write \(c\) back in, it is
\[
H^2=p^2c^2+m^2c^4.
\]
The relationship between the two can be seen from the low-speed limit. When \(p\ll m\),
\[
H=\sqrt{p^2+m^2}
=m\sqrt{1+\frac{p^2}{m^2}}
\approx m+\frac{p^2}{2m}.
\]
Here, \(m\) is the rest energy, which in non-relativistic problems usually just gives an overall constant and can be ignored. What remains is
\[
\frac{p^2}{2m}.
\]
So the non-relativistic Hamiltonian can be seen as the result of the relativistic energy in the low-speed limit after removing the rest energy.

Now let's quantize it. In the position representation,
\[
H\to i\frac{\partial}{\partial t},
\qquad
p\to -i\frac{\partial}{\partial x}.
\]
For
\[
H=\frac{p^2}{2m},
\]
we get
\[
i\frac{\partial \phi}{\partial t}
=-\frac{1}{2m}\frac{\partial^2\phi}{\partial x^2},
\]
which is the ordinary Schrödinger equation.

For the relativistic relation
\[
H^2=p^2+m^2,
\]
we can formally write
\[
H=\pm\sqrt{p^2+m^2}.
\]
This is of course one way to do it. But below we want to discuss a more special and elegant form: can we write \(H\) as a linear expression in \(p\) and \(m\). More specifically, let's first consider a free particle moving in one dimension.

The simplest case is
\[
m=0.
\]
In this case,
\[
H=\pm p.
\]
where \(H=p\) corresponds to a right-moving particle, and \(H=-p\) corresponds to a left-moving particle. We denote these two components as \(\phi_1\) and \(\phi_2\).

For \(\phi_1\), we have
\[
H=p,
\]
So
\[
i\frac{\partial\phi_1}{\partial t}
=p\phi_1
=-i\frac{\partial\phi_1}{\partial x}.
\]
which is
\[
\frac{\partial\phi_1}{\partial t}
+\frac{\partial\phi_1}{\partial x}=0.
\]
Its solution is
\[
\phi_1=f(x-t),
\]
representing a right-moving wave.

Similarly, for \(\phi_2\), we have
\[
H=-p,
\]
So
\[
i\frac{\partial\phi_2}{\partial t}
=-p\phi_2
=i\frac{\partial\phi_2}{\partial x}.
\]
which is
\[
\frac{\partial\phi_2}{\partial t}
-\frac{\partial\phi_2}{\partial x}=0.
\]
Its solution is
\[
\phi_2=g(x+t),
\]
representing a left-moving wave.

Now we want to write these two equations in a unified form. Combine the two components:
\[
\Phi=
\begin{pmatrix}
\phi_1\\
\phi_2
\end{pmatrix}.
\]
According to the relations above, the Hamiltonian should give \(+p\) for the first component and \(-p\) for the second component. Therefore,
\[
H\Phi
=p
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\Phi.
\]
We denote
\[
\alpha=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\]
Thus, the massless case can be written uniformly as
\[
H=\alpha p.
\]

Now consider
\[
m\neq 0.
\]
We guess that the Hamiltonian can be written as
\[
H=\alpha p+\beta m,
\]
where \(\beta\) is also a matrix acting on the two-component space. To satisfy the relativistic relation
\[
H^2=p^2+m^2,
\]
let's square this expression. Since \(\alpha,\beta\) only act on the two-component space \((\phi_1,\phi_2)\), while \(p=-i\partial_x\) acts on \(x\); here \(m\) is the rest mass parameter of the particle, not a new operator or matrix, and can be seen as a constant times the identity operator, so they can commute with \(p,m\):
\[
[\alpha,p]=0,\qquad [\beta,p]=0,\qquad [p,m]=0.
\]
Thus,
\[
H^2
=\alpha^2p^2+\beta^2m^2+(\alpha\beta+\beta\alpha)pm.
\]
To make it equal to
\[
p^2+m^2,
\]
we need
\[
\alpha^2=1,\qquad
\beta^2=1,\qquad
\alpha\beta+\beta\alpha=0.
\]

We have already chosen
\[
\alpha=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\]
which satisfies
\[
\alpha^2=1.
\]
In fact, this is a Pauli matrix. The square of any Pauli matrix is \(1\), and different Pauli matrices anti-commute with each other. Therefore, we can take another Pauli matrix as \(\beta\), for example,
\[
\beta=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]
Thus,
\[
H=\alpha p+\beta m =
\begin{pmatrix}
p&m\\
m&-p
\end{pmatrix}.
\]

Applying it to
\[
\Phi=
\begin{pmatrix}
\phi_1\\
\phi_2
\end{pmatrix}
\]
, we get
\[
i\frac{\partial\phi_1}{\partial t}
=p\phi_1+m\phi_2,
\]
\[
i\frac{\partial\phi_2}{\partial t}
=m\phi_1-p\phi_2.
\]
Therefore, once \(m\neq0\), the time evolutions of \(\phi_1\) and \(\phi_2\) become correlated. The evolution of the first component involves the second component, and the evolution of the second component also involves the first component. In other words, the mass term couples the right-moving and left-moving components.

Looking back, being able to write
\[
H^2=p^2+m^2
\]
as
\[
H=\alpha p+\beta m
\]
such a linear form relies on a very important assumption: the wave function is not a single \(\phi\), but can be divided into
\[
\Phi=
\begin{pmatrix}
\phi_1\\
\phi_2
\end{pmatrix}
\]
these two components. It is precisely because of this two-component structure that \(\alpha\) and \(\beta\) can be matrices and can possibly satisfy the anti-commutation relation
\[
\alpha\beta+\beta\alpha=0.
\]
This step is much like a kind of factorization: instead of directly dealing with the quadratic form \(H^2=p^2+m^2\), we write it as a linear Hamiltonian by introducing matrices and a two-component wave function.
