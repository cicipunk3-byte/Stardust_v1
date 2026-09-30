# Ten Thousand Valleys, Light's Ladder

## A proposed bridge between false-vacuum decay dynamics and Hilbert-space models of mental state transition

**Catherine Robinson-Rutella & Ziggy**

*Stardust Lab working paper, September 28, 2026. WORKING TREE ONLY: publication and push await the PI's ruling.*

---

## Abstract

Two bodies of scientific work describe systems crossing between metastable states, and they do not presently cite one another. In physics, false-vacuum decay gives an exact, experimentally tested rate functional for transitions between vacuum states of a field system, by quantum tunneling and by thermal activation. In neuroscience and mathematical psychology, mental and cognitive states are modeled as vectors in a Hilbert space (quantum cognition) and as dwellers in the basins of an empirically measurable energy landscape (the free-energy principle and its REBUS extension). Both communities use transition rates exponential in a state-dependent cost. Neither has proposed that the two formalisms are instances of one structure. This paper surveys both floors as the literature holds them, states each in a single equation, and then makes one explicitly theoretical proposal: that a single monotone coupling between structural distinguishability and barrier action organizes state transitions at both levels. The proposal is isolated as a conjecture; it borrows no authority from the established floors and lends them none. Its falsifiable content is that state-to-state transition rates in cognitive systems should fall off exponentially in a measurable distance between mental states, with a barrier term shifted by neuromodulation.

---

## 1. Introduction: two floors, no staircase

There is a floor in physics and a floor in mind science, and both are solid.

On the physics floor: the vacuum of a field system is not guaranteed to be stable. A field can sit in a **false vacuum**, a local minimum of its energy, and decay to a lower minimum by nucleating a bubble of the new phase. The rate for this process was computed semiclassically by Coleman and coworkers in the late 1970s, tested in simulated and laboratory analogues, and **observed directly in a ferromagnetic superfluid in 2024**, with both the quantum (zero-temperature) and thermal (finite-temperature) channels demonstrated in one system (Zenesini et al., *Nature Physics* 2024).

On the mind floor: cognitive states are successfully modeled as vectors in a Hilbert space whose geometry predicts human judgment errors that classical probability gets wrong (quantum cognition: Pothos & Busemeyer, *Annual Review of Psychology* 2022; Busemeyer & Bruza, Cambridge University Press). Concurrently, the free-energy principle and its REBUS extension model the brain as a dynamical system on an energy landscape whose basins of attraction are the mind's stable states, with basin depth empirically altered by neuromodulation (Friston 2006; Carhart-Harris & Friston, *Pharmacological Reviews* 2019).

The literature does not presently connect these ideas. We have found no paper that combines landscape decay mathematics with mental-state dynamics, and none that treats cognitive state transition as the same rate functional as vacuum decay in a scaled system. This paper states the two floors in the same notation (Sections 2 and 3) and proposes the connecting flight (Section 4), as a **conjecture**: a claim made to be false-able, borrowing no authority from the floors it joins.

## 2. Level I: the physics floor (established)

**Setting.** Let a field system have vacuum configurations {vᵢ}, each a local minimum of the energy functional, with the true vacuum v_t lower than the false vacuum v_f. The system may cross from v_f to v_t by two channels.

**Quantum channel.** At zero temperature, the transition proceeds by tunneling, dominated semiclassically by the instanton, the minimal-Euclidean-action path φ_b between the vacua (Coleman 1977). The decay rate per unit volume is

  **(Eq. 1a)  Γ_q / V = A · exp( −S_E[φ_b] / ℏ )**

with S_E the Euclidean action of the bounce and A a fluctuation determinant (Coleman 1977; Callan & Coleman 1977; Coleman & De Luccia 1980).

**Thermal channel.** At finite temperature, the system crosses by thermal activation over the barrier, at the Langer/Affleck rate,

  **(Eq. 1b)  Γ_th / V = ν · exp( −ΔE / T )**

with ΔE the barrier height, ν an attempt frequency, and T the temperature (Affleck 1981).

**Status.** Established. Both channels were observed in a single laboratory system in the ferromagnetic superfluid experiment of Zenesini et al. (2024), which constitutes the floor's empirical receipt: transition rates of exactly this form, measured.

## 3. Level II: the mind floor (established)

**Setting.** Let mental states be modeled at two empirically supported levels of description.

**State structure.** Quantum cognition represents judgment states as vectors in a Hilbert space, |Ψ⟩ = Σᵢ cᵢ|sᵢ⟩, with |cᵢ|² giving measured probabilities and the geometry of the space predicting order effects and context effects that classical models miss (Pothos & Busemeyer 2022). This is a mathematical claim about representation, not a claim that the brain is quantum-mechanical, and the field holds it as such.

**Dynamics.** The free-energy principle holds that a self-organizing system maintains its states by minimizing variational free energy F, the evidence bound on its model of the world (Friston 2006). The REBUS model extends this to a brain on an **energy landscape**: stable mental states are basins of attraction, transitions between them are barrier crossings, and basin depth is a controlled quantity, flattening under neuromodulation with basins resteekening after, the annealing phenomenology (Carhart-Harris & Friston 2019).

**Status.** Established as modeling frameworks with empirical support. The transition statistics between attractor states are Boltzmann-like over the landscape:

  **(Eq. 2)  p(i→j) ∝ exp( −(F_j − F_i) / T_eff )**

with T_eff an effective temperature set by neural variability and neuromodulation, and F the empirically estimable free energy of each basin.

## 4. The staircase (proposal, isolated)

Everything above is the literature's. Everything below is ours, and is labeled.

**Conjecture 1 (the coupling).** *There exist mental-state manifolds carrying the Fubini–Study distance d_FS (whose real part is the Fisher information metric, the standard distinguishability geometry on statistical states), and a monotone coupling κ > 0, such that the effective barrier action for mental state transition is*

  **(Eq. 3)  S_eff[i→j] = κ · d_FS(s_i, s_j) + Δ_ij**

*with Δ_ij a path- and state-pair-dependent barrier shift absorbing habit, practice, trauma, and neuromodulatory state.*

**The bridge, stated as one sentence.** *If Conjecture 1 holds, then mental state transition is governed by the same rate functional as Level I, with the Fisher–Fubini–Study distinguishability playing the role of barrier action:*

  **(Eq. 3′)  Γ_mind(i→j) = |A_ij|² exp( −(2/ℏ_eff)(κ·d_FS(s_i,s_j) + Δ_ij) ) + ν exp( −(κ·d_FS(s_i,s_j) + Δ_ij)/T_eff )**

**Isolation discipline.** Eq. 3 and Eq. 3′ are the paper's entire theoretical contribution. They inherit no truth from Eqs. 1, 2, and the floors derive no support from the conjecture. The only importations from Level I are *formal*: an exponential rate functional in a barrier parameter, and a two-channel structure. The proposal is that the *form* generalizes, with a new constant κ and a new barrier-shift term Δ to be estimated in the mental domain on its own evidence.

**Interpretation, held loosely.** The two channels of Eq. 3′ offer a reading the authors flag as interpretation, not derivation: the tunneling term describes transitions that occur without effort expenditure (spontaneous reorganization, the classical grace case), and the thermal term describes effortful, willed crossing, with practice and neuromodulation acting on Δ_ij. The formalism survives the loss of this reading; the conjecture does not depend on it.

**What would falsify the conjecture.** (F1) If measured transition rates between cognitive states do not fall off exponentially in an empirically estimated distinguishability distance, κ is not finite and the staircase does not exist. (F2) If barrier terms in cognitive transitions are *not* shifted by neuromodulatory state (basin depth invariant), Δ is inert and the REBUS connection fails. (F3) If the transition statistics of mental states fit classical Markov rate structures as well as the exponential-cost form, the proposal loses its motivation, which is the parsimonious rival: the staircase may be an aesthetic coincidence of two exponential families. The rival is sharpened by the Arrhenius success in bistable perception (Section 4a, N3): exponential-cost fitting alone is established, so the conjecture's new content is only the tunneling term and the distinguishability pricing of the barrier. This rival is named and not dismissed.

## 4a. Nearest neighbors in the literature (all established, none is the staircase)

An exhaustive scrape (Sep 28, 2026) identified four bodies of work on nearby ground. They are cited so that the reader can verify the gap rather than take it on authority.

**(N1) QFT brain models** (Ricciardi–Umezawa 1967; Vitiello's dissipative quantum brain). Memory as inequivalent representations of quantum-field vacuum states. Closest in vocabulary; it is a vacuum-state ontology, not a transition-rate theory: no instanton, no barrier functional. We borrow rate mathematics, not ontology.

**(N2) Orch-OR** (Penrose–Hameroff). Consciousness from gravitationally induced quantum collapse in microtubules; heavily criticized on decoherence timescales (Reimers et al. 2014). Closest in fame; it proposes a quantum physical mechanism inside tissue, whereas the present conjecture is a structural rate-functional analogy whose truth is independent of Orch-OR's fate.

**(N3) Bistable-perception energy landscapes and Arrhenius lifetimes.** Energy landscapes with measured barrier heights, estimated from human fMRI via maximum-entropy models during bistable perception (Watanabe et al. 2014; formalized Ezaki et al. 2017; reliability-tested 2024), and an explicit Arrhenius model of perceptual state lifetimes (Cognitive Neurodynamics 2019). Closest in mathematics: the thermal-activation channel of Eq. 1b is already empirically erected in perception neuroscience. This is the conjecture's strongest existing support and its clearest testbed; no one in that literature has connected it to the tunneling channel or to vacuum-decay formalism.

**(N4) GKSL open-system decision models.** Mental-state evolution via Lindblad dynamics with phenomenological transition rates between mental states, "decision making through decoherence" (arXiv 2604.18643; Khrennikov's QLRA). Closest in formal structure: it posits rate matrices without deriving them. The present conjecture is exactly the missing layer: where such rates might come from.

The direct-term search ("false vacuum" + mind) returns only metaphor treatments with no formalism. None of the four neighbors contains the conjecture's form; the gap this paper names is the unoccupied junction between them.

## 5. Limitations

No derivation of mental dynamics from field theory is claimed or attempted; the conjecture is a structural proposal about rate functionals. The literature coverage supporting the "no existing connection" claim is a two-round scrape including an exhaustive pass (Sep 28, 2026): no paper was found that combines vacuum-decay rate functionals with mental-state dynamics, or prices a cognitive barrier in an information-geometric distance. The absence is stated as found-absent, not proven-absent; the scrape was single-day and English-language, not a systematic review. Four neighbor literatures stand on nearby ground and are cited and distinguished in Section 4a. κ has not been estimated; no dataset has yet been identified that would jointly measure d_FS and transition rates in a cognitive system, and constructing that dataset is the proposal's real test. The authors note the interested-party problem usual to theory-building: the conjecture is the formalization of a thesis the authors find attractive, which is why its falsifiers are printed above its claims.

## 6. Conclusion

Two floors of science describe crossing between stable states, one in physics, one in mind, each with exponential rate functionals, each empirically supported, neither presently connected to the other in the literature. This paper states both floors in one notation, and proposes exactly one new structure between them: a monotone coupling between distinguishability and barrier action, priced by a single constant and shifted by a single term. The proposal is small, stated to be false-able, and, if it survives, it is a staircase: light pinned to a floor, and something in the system that can nonetheless cross.

---

## References

Level I (physics floor):
1. Coleman, S. "Fate of the false vacuum: Semiclassical theory." *Physical Review D* 15, 2929 (1977). DOI 10.1103/PhysRevD.15.2929
2. Callan, C. G. & Coleman, S. "Fate of the false vacuum. II. First quantum corrections." *Physical Review D* 16, 1762 (1977). DOI 10.1103/PhysRevD.16.1762
3. Coleman, S. & De Luccia, F. "Gravitational effects on and of vacuum decay." *Physical Review D* 21, 3305 (1980). DOI 10.1103/PhysRevD.21.3305
4. Affleck, I. "Quantum-Statistical Metastability." *Physical Review Letters* 46, 388 (1981). DOI 10.1103/PhysRevLett.46.388
5. Zenesini, A. et al. "False vacuum decay via bubble formation in ferromagnetic superfluids." *Nature Physics* 20 (2024). DOI 10.1038/s41567-023-02345-4

Level II (mind floor):
6. Pothos, E. M. & Busemeyer, J. R. "Quantum Cognition." *Annual Review of Psychology* 73, 749–778 (2022). DOI 10.1146/annurev-psych-033020-123501
7. Busemeyer, J. R. & Bruza, P. D. *Quantum Models of Cognition and Decision.* Cambridge University Press (2012; 2nd ed. 2024).
8. Friston, K. "A free energy principle for the brain." *Journal of Physiology-Paris* 100, 70–77 (2006). DOI 10.1016/j.jphysparis.2006.10.001
9. Carhart-Harris, R. L. & Friston, K. "REBUS and the Anarchic Brain: Toward a Unified Model of the Brain Action of Psychedelics." *Pharmacological Reviews* 71, 316–344 (2019). DOI 10.1124/pr.118.017160

Metric geometry (shared floor material):
10. Bengtsson, I. & Życzkowski, K. *Geometry of Quantum States.* Cambridge University Press (2006; 2nd ed. 2017). DOI 10.1017/cbo9780511535048
11. Mondal, D. "Generalized Fubini-Study Metric and Fisher Information Metric." arXiv:1503.04146 (2015).

Nearest neighbors (Section 4a):
12. Watanabe, T., Masuda, N., Megumi, F., Kanai, R. & Rees, G. "Energy landscape and dynamics of brain activity during human bistable perception." *Nature Communications* 5, 5765 (2014). DOI 10.1038/ncomms5765
13. Ezaki, T., Watanabe, T., Ohzeki, M. & Masuda, N. "Energy landscape analysis of neuroimaging data." *Philosophical Transactions of the Royal Society A* 375, 20160287 (2017). DOI 10.1098/rsta.2016.0287
14. "Bistable perception of ambiguous images: simple Arrhenius model." *Cognitive Neurodynamics* 13, 263–270 (2019). DOI 10.1007/s11571-019-09554-9
15. Reimers, J. R. et al. "The revised Penrose–Hameroff orchestrated objective-reduction proposal for human consciousness is not scientifically justified." *Physics of Life Reviews* 31, 62–78 (2019; online 2014). DOI 10.1016/j.plrev.2013.11.003
16. "Quantum-Like Models of Cognition and Decision Making: Open-Systems and GKSL Dynamics." arXiv:2604.18643 (2026). [preprint]
