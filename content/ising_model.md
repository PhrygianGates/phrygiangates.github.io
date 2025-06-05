+++
date = '2025-06-05T21:24:00+08:00'
katex = true
title = 'Ising Model'
tags = ['Statistical Mechanics']
+++

Following Susskind's Statistical Mechanics course, lecture 9.

The energy of a single spin in the Ising model is given by:

\[E = -J\sigma\]

where:
- \(E\) is the energy of the spin
- \(J\) is the coupling constant (strength of interaction)
- \(\sigma\) is the spin value, which can be either +1 (spin up) or -1 (spin down)

Focus on a single spin.
Its partition function \(Z\), summing over the two configurations (\(\sigma = +1, \sigma = -1\)), is:
\[
Z = \sum_{\sigma \in \{+1, -1\}} e^{-\beta(-J\sigma)} = \sum_{\sigma \in \{+1, -1\}} e^{\beta J\sigma} = e^{\beta J(+1)} + e^{\beta J(-1)} = e^{\beta J} + e^{-\beta J} = 2 \cosh(\beta J)
\]

(For a system of \(N\) independent, non-interacting spins, the logarithm of the total partition function is additive: \(\ln Z_{total} = N \ln Z\).)

Let's compute the average energy \(\langle E \rangle\) of the spin:
The average energy is given by \(\langle E \rangle = -\frac{1}{Z} \frac{\partial Z}{\partial \beta}\).
Since \(Z = 2 \cosh(\beta J)\), its derivative with respect to \(\beta\) is \(\frac{\partial Z}{\partial \beta} = 2J \sinh(\beta J)\).
Substituting these into the expression for \(\langle E \rangle\):
\[
\langle E \rangle = -\frac{2J \sinh(\beta J)}{2 \cosh(\beta J)} = -J \frac{\sinh(\beta J)}{\cosh(\beta J)} = -J \tanh(\beta J)
\]

The average spin \(\langle \sigma \rangle\) is given by:
\[ \langle \sigma \rangle = \frac{1}{Z} \sum_{\sigma \in \{+1, -1\}} \sigma e^{\beta J\sigma} = \tanh(\beta J) \]

---

Now, let's consider a one-dimensional (1D) chain of \(N\) spins. This is the 1D Ising model.
The energy of the system, assuming interactions only between nearest neighbors, is given by:
\[ E = -J \sum_{i=1}^{N-1} \sigma_i \sigma_{i+1} \]
Here, we assume an open chain with \(N\) spins and \(N-1\) bonds (interactions). For a closed chain (periodic boundary conditions), the sum would typically go up to \(N\), with \(\sigma_{N+1} = \sigma_1\). We will focus on the open chain for this calculation.

The partition function is:
\[ Z = \sum_{\{\sigma_1, \dots, \sigma_N\}} e^{-\beta E} = \sum_{\{\sigma_1, \dots, \sigma_N\}} e^{\beta J \sum_{i=1}^{N-1} \sigma_i \sigma_{i+1}} \]
where the sum is over all \(2^N\) possible spin configurations.

To understand the collective behavior of such systems, we often study correlation functions. For example, one might ask: if we know the state of the \(k\)-th spin (e.g., \(\sigma_k = +1\)), what is the probability that the \(m\)-th spin (\(m \neq k\)) is also up? This is related to calculating the average of the product of the two spins, \(\langle \sigma_k \sigma_m \rangle\), which quantifies how strongly spin states are correlated across the chain.

To compute the partition function \(Z\) for the finite open chain, we can use a change of variables. Let \(\mu_i = \sigma_i \sigma_{i+1}\) for \(i = 1, \dots, N-1\). Each \(\mu_i\) can be either +1 or -1, representing whether the neighboring spins are aligned or anti-aligned.
The energy can then be written in terms of these bond variables:
\[ E = -J \sum_{i=1}^{N-1} \mu_i \]
We need to relate the sum over spin configurations \(\{\sigma_k\}\) to a sum over these new variables.
Note that if we know the state of the first spin, \(\sigma_1\), and all the \(\mu_i\) values, we can determine the state of every subsequent spin:
\(\sigma_2 = \mu_1 \sigma_1\)
\(\sigma_3 = \mu_2 \sigma_2 = \mu_2 \mu_1 \sigma_1\)
And in general, \(\sigma_k = \sigma_1 \prod_{j=1}^{k-1} \mu_j\) for \(k > 1\).

Thus, a configuration of the system can be uniquely specified by the state of the first spin \(\sigma_1\) (2 choices: +1 or -1) and the states of the \(N-1\) bond variables \(\{\mu_1, \mu_2, \dots, \mu_{N-1}\}\) (each \(\mu_i\) has 2 choices). This gives a total of \(2 \times 2^{N-1} = 2^N\) configurations, correctly matching the original spin representation.

The partition function can be rewritten by summing over \(\sigma_1\) and all \(\mu_i\):
\[ Z = \sum_{\sigma_1 \in \{\pm 1\}} \left( \sum_{\mu_1 \in \{\pm 1\}} \dots \sum_{\mu_{N-1} \in \{\pm 1\}} e^{\beta J \sum_{i=1}^{N-1} \mu_i} \right) \]
Since the exponential term (representing the sum of bond energies) does not depend on \(\sigma_1\), the sum over \(\sigma_1\) simply yields a factor of 2:
\[ Z = 2 \left( \sum_{\mu_1 \in \{\pm 1\}} \dots \sum_{\mu_{N-1} \in \{\pm 1\}} \prod_{j=1}^{N-1} e^{\beta J \mu_j} \right) \]
The sums over the \(\mu_j\) variables are independent of each other because each \(\mu_j\) appears only once in the product. So, we can write this as a product of individual sums:
\[ Z = 2 \prod_{j=1}^{N-1} \left( \sum_{\mu_j \in \{\pm 1\}} e^{\beta J \mu_j} \right) \]
Each individual sum over a single \(\mu_j\) is:
\[ \sum_{\mu \in \{\pm 1\}} e^{\beta J \mu} = e^{\beta J(+1)} + e^{\beta J(-1)} = 2 \cosh(\beta J) \]
Substituting this back, we get the partition function for the 1D open chain of \(N\) spins:
\[ Z = 2 [2 \cosh(\beta J)]^{N-1} \]
This result is for an open chain with \(N\) spins and \(N-1\) bonds.

To be continued...
