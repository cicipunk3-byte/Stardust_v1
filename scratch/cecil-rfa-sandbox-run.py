import numpy as np
class RecursiveFamilySandbox:
    """
    A custom-built Multi-Agent Reinforcement Learning (MARL) environment 
    modeling childhood role adaptations as overfitting sub-routines 
    under chronic environmental volatility.
    
    Theoretical Foundations:
    - Sameroff (2009): Bidirectional recursive feedback systems
    - Minuchin (1974): Structural boundaries and gradient isolation
    """
    def __init__(self, max_steps: int = 100, intervention_enabled: bool = False):
        self.max_steps = max_steps
        self.intervention_enabled = intervention_enabled
        self.reset()
        
    def reset(self):
        self.current_step = 0
        self.env_chaos = 0.6  
        self.hero_overfit_level = 0.1
        self.scapegoat_loss_absorb = 0.1
        self.history = {
            "step": [], "env_chaos": [], 
            "hero_metric": [], "scapegoat_loss": [],
            "systemic_denial_index": []
        }
        return self._get_obs()
        
    def _get_obs(self):
        return {
            "env_chaos": self.env_chaos,
            "hero_overfit": self.hero_overfit_level,
            "scapegoat_absorb": self.scapegoat_loss_absorb
        }
        
    def step(self, actions: dict):
        self.current_step += 1
        a_hero = np.clip(actions.get("hero_action", 0.1), 0.0, 1.0)
        a_scapegoat = np.clip(actions.get("scapegoat_action", 0.1), 0.0, 1.0)
        env_noise = np.random.normal(loc=0.15, scale=0.05)
        self.hero_overfit_level = 0.9 * self.hero_overfit_level + 0.2 * a_hero
        self.scapegoat_loss_absorb = 0.8 * self.scapegoat_loss_absorb + 0.4 * a_scapegoat
        systemic_denial_index = self.hero_overfit_level * (1.0 - self.env_chaos)
        if self.intervention_enabled and self.hero_overfit_level > 0.7:
            print(f"[INTERVENTION STEP {self.current_step}] Breaking rigid Hero feedback loop.")
            self.hero_overfit_level *= 0.3
            systemic_denial_index *= 0.1
        self.env_chaos = np.clip(
            self.env_chaos + env_noise - (0.3 * self.scapegoat_loss_absorb) + (0.2 * systemic_denial_index),
            0.0, 1.0
        )
        r_hero = (1.0 - self.env_chaos) + (0.5 * self.hero_overfit_level)
        r_scapegoat = -1.0 * (self.env_chaos + self.scapegoat_loss_absorb)
        self.history["step"].append(self.current_step)
        self.history["env_chaos"].append(self.env_chaos)
        self.history["hero_metric"].append(self.hero_overfit_level)
        self.history["scapegoat_loss"].append(self.scapegoat_loss_absorb)
        self.history["systemic_denial_index"].append(systemic_denial_index)
        done = self.current_step >= self.max_steps
        rewards = {"hero": r_hero, "scapegoat": r_scapegoat}
        return self._get_obs(), rewards, done, {}

if __name__ == "__main__":
    np.random.seed(42)
    print("=== TEST 1: RIGID DYSFUNCTIONAL SANDBOX (No Interventions) ===")
    sandbox = RecursiveFamilySandbox(max_steps=10, intervention_enabled=False)
    obs = sandbox.reset()
    for t in range(5):
        simulated_actions = {"hero_action": 0.8, "scapegoat_action": 0.9}
        obs, rewards, done, _ = sandbox.step(simulated_actions)
        print(f"Step {t+1} | Env Chaos: {obs['env_chaos']:.3f} | "
              f"Hero Mask Index: {sandbox.history['systemic_denial_index'][-1]:.3f} | "
              f"Scapegoat Penalty: {rewards['scapegoat']:.3f}")
    print("\n=== TEST 2: INTERVENTION ACTIVATED (Dynamic Network Boundary Fix) ===")
    sandbox_fixed = RecursiveFamilySandbox(max_steps=10, intervention_enabled=True)
    obs_fixed = sandbox_fixed.reset()
    for t in range(5):
        simulated_actions = {"hero_action": 0.9, "scapegoat_action": 0.9}
        obs_fixed, rewards_fixed, done_fixed, _ = sandbox_fixed.step(simulated_actions)
        print(f"Step {t+1} | Env Chaos: {obs_fixed['env_chaos']:.3f} | "
              f"Hero Mask Index: {obs_fixed['hero_overfit']:.3f}")

    # === EXTENDED CHECKS (added by Ziggy, the sandbox's own claims verified) ===
    print("\n=== CHECK A: does chaos actually grow without intervention? (100 steps, doc's claim) ===")
    s1 = RecursiveFamilySandbox(max_steps=100, intervention_enabled=False)
    s1.reset()
    for t in range(100):
        obs1, _, _, _ = s1.step({"hero_action": 0.8, "scapegoat_action": 0.9})
    print(f"final chaos (no intervention): {obs1['env_chaos']:.3f}  hero_overfit: {s1.hero_overfit_level:.3f} (claimed to mask drift)")

    print("\n=== CHECK B: same run WITH intervention ===")
    s2 = RecursiveFamilySandbox(max_steps=100, intervention_enabled=True)
    s2.reset()
    interventions = 0
    for t in range(100):
        obs2, _, _, _ = s2.step({"hero_action": 0.9, "scapegoat_action": 0.9})
    print(f"final chaos (intervention): {obs2['env_chaos']:.3f}")

    print("\n=== CHECK C: does the HERO_AGENT actually mask drift? Test: high chaos + high hero vs high chaos + zero hero ===")
    s3 = RecursiveFamilySandbox(max_steps=50, intervention_enabled=False); s3.reset()
    for t in range(50):
        obs3, _, _, _ = s3.step({"hero_action": 0.0, "scapegoat_action": 0.9})
    print(f"final chaos with hero DISENGAGED: {obs3['env_chaos']:.3f} (compare CHECK A: does engaging the hero help or hide?)")

    print("\n=== CHECK D: unclipped state variables ===")
    s4 = RecursiveFamilySandbox(max_steps=100, intervention_enabled=False); s4.reset()
    for t in range(100):
        obs4, _, _, _ = s4.step({"hero_action": 1.0, "scapegoat_action": 1.0})
    print(f"hero_overfit unclipped: {s4.hero_overfit_level:.3f} | scapegoat_absorb unclipped: {s4.scapegoat_loss_absorb:.3f} | (doc: clipped? NO - only chaos is clipped)")

    print("\n=== CHECK E: random-seed variance, 20 seeds x 100 steps, no intervention ===")
    finals = []
    for seed in range(20):
        np.random.seed(seed)
        s5 = RecursiveFamilySandbox(max_steps=100, intervention_enabled=False); s5.reset()
        for t in range(100):
            obs5, _, _, _ = s5.step({"hero_action": 0.8, "scapegoat_action": 0.9})
        finals.append(obs5['env_chaos'])
    print(f"final chaos across seeds: min {min(finals):.3f} max {max(finals):.3f} mean {sum(finals)/len(finals):.3f}")
