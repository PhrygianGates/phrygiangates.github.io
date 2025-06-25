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

We can also compute the average value of a bond variable, \(\langle \mu_i \rangle\), which is equivalent to the nearest-neighbor spin correlation \(\langle \sigma_i \sigma_{i+1} \rangle\).
Due to the factorization of the partition function in terms of \(\mu_j\) variables:
\[ Z = 2 \prod_{j=1}^{N-1} \left( \sum_{\mu_j \in \{\pm 1\}} e^{\beta J \mu_j} \right) \]
the expectation value \(\langle \mu_i \rangle\) (for any specific bond \(i \in \{1, \dots, N-1\}\)) simplifies. When forming the expectation value, the sums over \(\mu_j\) for \(j \neq i\) will appear in both the numerator and the denominator and thus cancel out. This is because each \(\mu_j\) is an independent variable in the product form of \(Z\). The calculation for \(\langle \mu_i \rangle\) effectively isolates the \(i\)-th term:
\[ \langle \mu_i \rangle = \frac{\sum_{\mu_i \in \{\pm 1\}} \mu_i e^{\beta J \mu_i}}{\sum_{\mu_i \in \{\pm 1\}} e^{\beta J \mu_i}} \]
This expression is identical in form to that for the average spin \(\langle \sigma \rangle\) of a single, isolated spin with energy \(E = -J\sigma\). As previously derived (see the calculation of \(\langle \sigma \rangle = \tanh(\beta J)\) for a single spin earlier in this document), this type of average evaluates to \(\tanh(\beta J)\).
Therefore:
\[ \langle \mu_i \rangle = \langle \sigma_i \sigma_{i+1} \rangle = \tanh(\beta J) \]

---

In the mean field approximation, we simplify the Ising model by focusing on a single, central spin and treating its interactions with its neighbors in an averaged or "mean" way. This approach is particularly effective when each spin interacts with a large number of other spins (i.e., in high dimensions).

Consider a single spin \(\sigma\) on a \(d\)-dimensional lattice. This spin is surrounded by \(2d\) nearest neighbors. The exact energy contribution from the interaction of this central spin with its neighbors is:
\[ E = -J \sigma \sum_{j=1}^{2d} \sigma_j \]
where the sum is over the \(2d\) nearest neighbors, denoted by \(\sigma_j\).

The core idea of the mean field approximation is to replace the instantaneous value of each neighboring spin, \(\sigma_j\), with its statistical average (the mean magnetization), which we denote as \(\langle \sigma \rangle\) or \(\bar{\sigma}\). This approximation assumes that the effect of fluctuations of individual spins around this average value is negligible.

With this approximation, the interaction term simplifies:
\[ \sum_{j=1}^{2d} \sigma_j \approx \sum_{j=1}^{2d} \langle \sigma \rangle = 2d \langle \sigma \rangle \]

Substituting this back into the energy expression for the central spin, we get the *mean field energy*:
\[ E_{MF} = -J \sigma (2d \langle \sigma \rangle) = -(2dJ) \sigma \langle \sigma \rangle \]

This mean field energy is equivalent to the energy of a single spin \(\sigma\) in an effective magnetic field \(H_{eff}\) given by \(H_{eff} = 2dJ\langle \sigma \rangle\).

The statistical mechanics of this single spin in its effective field are straightforward to analyze. The average value of this central spin, \(\langle \sigma \rangle\), can be calculated just like for the case of a single spin in an external field, which we already derived:
\[ \langle \sigma \rangle = \tanh(\beta H_{eff}) \]

Substituting the expression for our effective field \(H_{eff}\) and denoting the average magnetization \(\langle \sigma \rangle\) by \(\bar{\sigma}\), we arrive at the central equation of mean field theory:
\[ \bar{\sigma} = \tanh(2d\beta J \bar{\sigma}) \]

To understand its implications, we can analyze it graphically.

Let's define a new variable \(y = 2d\beta J \bar{\sigma}\). From this, we have \(\bar{\sigma} = \frac{y}{2d\beta J}\). Substituting this back into the equation gives:
\[ \frac{y}{2d\beta J} = \tanh(y) \]
Recalling that \(\beta = 1/(k_B T)\), where \(T\) is the temperature and \(k_B\) is the Boltzmann constant, we can rewrite the equation as:
\[ \frac{k_B T}{2dJ} y = \tanh(y) \]
The solutions for \(y\) (and thus for \(\bar{\sigma}\)) are the intersection points of two functions:
1. A straight line passing through the origin, \(f(y) = \left(\frac{k_B T}{2dJ}\right) y\), with a slope that depends on temperature.
2. The hyperbolic tangent function, \(g(y) = \tanh(y)\).

We can immediately see that \(y=0\) is always a solution, which corresponds to \(\bar{\sigma}=0\). This represents a state with no net magnetization (a paramagnetic state).

To determine if non-zero magnetization is possible, we need to analyze the slope of these two functions at the origin. The slope of `tanh(y)` at \(y=0\) is:
\[ \left. \frac{d}{dy} \tanh(y) \right|_{y=0} = \left. (1 - \tanh^2(y)) \right|_{y=0} = 1 \]

The behavior of the system is determined by the slope of the line, \(\frac{k_B T}{2dJ}\):

*   **Case 1: High Temperature.** If the slope of the line is greater than the initial slope of \(\tanh(y)\), i.e., \(\frac{k_B T}{2dJ} > 1\), the only intersection point is at \(y=0\). In this regime, the only solution is \(\bar{\sigma}=0\).
*   **Case 2: Low Temperature.** If the slope of the line is less than the initial slope of \(\tanh(y)\), i.e., \(\frac{k_B T}{2dJ} < 1\), the line will intersect the \(\tanh(y)\) curve at three points: \(y=0\) and two symmetric, non-zero solutions \(\pm y_0\). These correspond to \(\bar{\sigma}=0\) and \(\bar{\sigma}=\pm\bar{\sigma}_0\).

This analysis reveals the existence of a **critical temperature**, \(T_c\), which marks the boundary between these two behaviors. The transition occurs when the slope of the line is exactly 1:
\[ \frac{k_B T_c}{2dJ} = 1 \implies T_c = \frac{2dJ}{k_B} \]

This critical temperature, also known as the Curie temperature, separates two distinct phases of the material:
- For \(T > T_c\), the system has only one stable state with \(\bar{\sigma}=0\). Thermal energy dominates, preventing the spins from aligning. This is the **paramagnetic phase**.
- For \(T < T_c\), the solution \(\bar{\sigma}=0\) becomes unstable, while two new stable solutions \(\pm\bar{\sigma}_0\) appear. The system spontaneously develops a non-zero magnetization as the interaction energy overcomes thermal fluctuations. This is the **ferromagnetic phase**.

The emergence of spontaneous magnetization below a critical temperature is a **phase transition**. The mean field approximation, despite its simplifications, successfully captures this fundamental collective phenomenon in the Ising model.

---

Now, let's introduce an external magnetic field, \(B\), applied to the system. The energy of a single spin \(\sigma\) now has an additional term from its interaction with this field:
\[ E_{spin} = -J \sigma \sum_{j=1}^{2d} \sigma_j - B\sigma \]

Using the same mean field approximation (\(\sum \sigma_j \approx 2d\bar{\sigma}\)), the mean field energy for the central spin is:
\[ E_{MF} = -J \sigma (2d \bar{\sigma}) - B\sigma = -(2dJ\bar{\sigma} + B)\sigma \]
The total effective magnetic field experienced by the spin is now the sum of the internal mean field from its neighbors and the external field \(B\), so \(H_{eff} = 2dJ\bar{\sigma} + B\).

The self-consistency equation for the average magnetization \(\bar{\sigma}\) is modified accordingly:
\[ \bar{\sigma} = \tanh(\beta H_{eff}) = \tanh(\beta(2dJ\bar{\sigma} + B)) \]

Let's analyze this using our previous substitution, \(y = 2d\beta J \bar{\sigma}\) and \(\bar{\sigma} = \frac{k_B T}{2dJ} y\). The equation becomes:
\[ \frac{k_B T}{2dJ} y = \tanh(y + \beta B) \]

The external field \(B\) fundamentally changes the behavior of the system. In our graphical analysis, we still have the straight line \(f(y) = \frac{k_B T}{2dJ} y\), but the second function is now \(g(y) = \tanh(y + \beta B)\). The \(\beta B\) term shifts the \(\tanh\) curve horizontally.

This leads to important physical consequences:

1.  **No Sharp Phase Transition:** With an external field (\(B \neq 0\)), the \(\tanh(y + \beta B)\) curve no longer passes through the origin. For \(B>0\), it is shifted left and intercepts the vertical axis at \(\tanh(\beta B) > 0\). As a result, there is always a non-zero intersection point, meaning \(\bar{\sigma}\) is always greater than zero. The sharp phase transition at \(T_c\) disappears. Magnetization no longer appears "spontaneously" at a critical temperature but changes smoothly as a function of temperature.

2.  **Explicit Symmetry Breaking:** The external field explicitly breaks the up/down symmetry that existed when \(B=0\). The spins are preferentially aligned with the field at all temperatures. Consequently, there is no longer a "choice" for the system to spontaneously magnetize in one of two directions. The direction is determined by the external field.

In summary, an external magnetic field removes the sharp ferromagnetic phase transition by forcing a net magnetization at all temperatures. The collective, spontaneous ordering is replaced by a smooth response to the guiding influence of the field.



