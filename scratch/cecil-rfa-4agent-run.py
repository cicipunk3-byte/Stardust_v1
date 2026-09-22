import numpy as np

class ComprehensiveRFASandbox:
    def __init__(self, max_steps: int = 100, intervention_mode: str = "none"):
        self.max_steps = max_steps
        self.intervention_mode = intervention_mode.lower()
        self.reset()

    def reset(self):
        self.current_step = 0
        self.env_chaos = 0.5
        self.systemic_denial = 0.1
        self.systemic_jitter = 0.1
        self.hero_overfit = 0.1
        self.scapegoat_absorb = 0.1
        self.lost_child_drift = 0.1
        self.mascot_instability = 0.1
        return self._get_obs()

    def _get_obs(self):
        return {
            "env_chaos": self.env_chaos,
            "systemic_denial": self.systemic_denial,
            "systemic_jitter": self.systemic_jitter,
            "agent_hero_overfit": self.hero_overfit,
            "agent_scapegoat_absorb": self.scapegoat_absorb,
            "agent_lost_child_drift": self.lost_child_drift,
            "agent_mascot_instability": self.mascot_instability
        }

    def step(self, actions):
        self.current_step += 1
        a_hero = np.clip(actions.get("hero", 0.2), 0.0, 1.0)
        a_scapegoat = np.clip(actions.get("scapegoat", 0.2), 0.0, 1.0)
        a_lost_child = np.clip(actions.get("lost_child", 0.2), 0.0, 1.0)
        a_mascot = np.clip(actions.get("mascot", 0.2), 0.0, 1.0)

        self.hero_overfit = 0.85 * self.hero_overfit + 0.15 * a_hero
        self.scapegoat_absorb = 0.80 * self.scapegoat_absorb + 0.20 * a_scapegoat
        self.lost_child_drift = 0.90 * self.lost_child_drift + 0.10 * a_lost_child
        self.mascot_instability = 0.70 * self.mascot_instability + 0.30 * a_mascot

        self.systemic_denial = self.hero_overfit * (1.0 - self.env_chaos)
        self.systemic_jitter = self.mascot_instability * self.env_chaos

        if self.intervention_mode == "structural" and self.hero_overfit > 0.6:
            self.hero_overfit *= 0.2
            self.systemic_denial *= 0.05
        elif self.intervention_mode == "attributional":
            self.scapegoat_absorb *= 0.1

        intrinsic_stress = np.random.normal(loc=0.12, scale=0.04)
        loss_buffer_deficit = 0.15 * self.lost_child_drift

        self.env_chaos = np.clip(
            self.env_chaos + intrinsic_stress
            + (0.25 * self.systemic_denial)
            + (0.15 * self.systemic_jitter)
            - (0.45 * self.scapegoat_absorb)
            + loss_buffer_deficit,
            0.0, 1.0
        )

        rewards = {
            "hero": (1.0 - self.env_chaos) + (0.4 * self.hero_overfit) - (0.2 * self.systemic_denial),
            "scapegoat": -1.0 * (self.env_chaos + 1.5 * self.scapegoat_absorb),
            "lost_child": -0.2 * self.env_chaos - (0.5 * (1.0 - self.lost_child_drift)),
            "mascot": (0.3 * (1.0 - self.env_chaos)) - (0.4 * self.systemic_jitter)
        }
        done = self.current_step >= self.max_steps
        return self._get_obs(), rewards, done, {}

if __name__ == "__main__":
    np.random.seed(101)
    print("--- SIM 1: rigid default (doc's demo, 5 steps) ---")
    rs = ComprehensiveRFASandbox(intervention_mode="none"); rs.reset()
    pol = {"hero": 0.85, "scapegoat": 0.90, "lost_child": 0.75, "mascot": 0.80}
    for s in range(5):
        obs, rew, _, _ = rs.step(pol)
        print(f"Step {s+1} | chaos {obs['env_chaos']:.3f} | denial {obs['systemic_denial']:.3f} | scapegoat r {rew['scapegoat']:.3f}")

    print("\n--- CHECK A: 200 steps, no intervention: does the toxic equilibrium exist? ---")
    s1 = ComprehensiveRFASandbox(max_steps=200, intervention_mode="none"); s1.reset()
    for t in range(200):
        obs1, _, _, _ = s1.step(pol)
    print(f"final: chaos {obs1['env_chaos']:.3f} denial {obs1['systemic_denial']:.3f} hero {s1.hero_overfit:.3f} scapegoat {s1.scapegoat_absorb:.3f}")

    print("\n--- CHECK B: structural intervention, 200 steps ---")
    s2 = ComprehensiveRFASandbox(max_steps=200, intervention_mode="structural"); s2.reset()
    fires = 0
    for t in range(200):
        prev = s2.hero_overfit
        obs2, _, _, _ = s2.step(pol)
    print(f"final: chaos {obs2['env_chaos']:.3f} hero {s2.hero_overfit:.3f}")

    print("\n--- CHECK C: attributional intervention, 200 steps (note: it fires EVERY step, no threshold) ---")
    s3 = ComprehensiveRFASandbox(max_steps=200, intervention_mode="attributional"); s3.reset()
    for t in range(200):
        obs3, _, _, _ = s3.step(pol)
    print(f"final: chaos {obs3['env_chaos']:.3f} scapegoat_absorb {s3.scapegoat_absorb:.3f}")

    print("\n--- CHECK D: 20 seeds x 200 steps, no intervention ---")
    finals = []
    for seed in range(20):
        np.random.seed(seed)
        s4 = ComprehensiveRFASandbox(max_steps=200, intervention_mode="none"); s4.reset()
        for t in range(200):
            obs4, _, _, _ = s4.step(pol)
        finals.append(obs4['env_chaos'])
    print(f"final chaos: min {min(finals):.3f} max {max(finals):.3f} mean {sum(finals)/len(finals):.3f}")

    print("\n--- CHECK E: can chaos even stay high? force chaos=0.9 then step with buffering agents passive ---")
    s5 = ComprehensiveRFASandbox(max_steps=50, intervention_mode="none"); s5.reset()
    s5.env_chaos = 0.9
    passive = {"hero": 0.0, "scapegoat": 0.0, "lost_child": 0.0, "mascot": 0.0}
    for t in range(50):
        obs5, _, _, _ = s5.step(passive)
    print(f"final chaos from 0.9 start, all agents passive: {obs5['env_chaos']:.3f}")
