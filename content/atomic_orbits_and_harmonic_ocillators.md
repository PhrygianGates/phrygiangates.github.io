+++
date = '2025-09-20T19:00:00+08:00'
katex = true
title = 'Atomic Orbits And Harmonic Ocillators'
tags = ['Advanced Quantum Mechanics']
+++ 


To solve for the state of a particle in a system with a central potential, such as an electron in an atom, we describe its state using a wavefunction \\( \psi(r, \theta, \phi) \\) in spherical coordinates. A key mathematical technique here is the separation of variables. This method is applicable because the system's potential energy is spherically symmetric, meaning it only depends on the distance \\(r\\) from the center, not on the angles \\( \theta \\) or \\( \phi \\). This symmetry allows us to decompose the wavefunction into a product of a radial part \\( R(r) \\) and an angular part \\( Y(\theta, \phi) \\). By expressing \\( \psi(r, \theta, \phi) = R(r)Y(\theta, \phi) \\), we can transform the single complex Schrödinger equation into a set of simpler, one-dimensional ordinary differential equations, which can be solved separately.

---

The angular part of the problem is governed by the angular momentum operators, \\(L_x, L_y, L_z\\). These operators do not commute with each other, obeying commutation relations such as \\( [L_x, L_y] = i\hbar L_z \\). Because they do not commute, a quantum state cannot have a definite value for all three components simultaneously. The standard approach is to choose one component, conventionally \\(L_z\\), and find its common eigenstates with the total angular momentum squared operator \\(L^2\\). We can label these eigenstates by their respective quantum numbers, for example as \\(|m\rangle\\), which corresponds to an eigenvalue of \\(m\hbar\\) for the \\(L_z\\) operator. To explore the spectrum of these eigenvalues, we introduce the ladder operators, defined as \\(L_{\pm} = L_x \pm iL_y\\). These operators have a powerful function: when the raising operator \\(L_+\\) acts on an eigenstate \\(|m\rangle\\), it produces a new state that is also an eigenstate of \\(L_z\\), but with its eigenvalue increased to \\((m+1)\hbar\\). Consequently, we can label this new state as \\(|m+1\rangle\\), leading to the fundamental relation \\( L_+|m\rangle \propto |m+1\rangle \\). This algebraic method reveals a "ladder" of eigenstates, spaced by one unit of angular momentum along the z-axis.