# Receipt check: does the "adversarial training loop" actually train the adversary?
# Runs script 1 exactly as shipped, then inspects gradients.
import sys
sys.path.insert(0, '.')
import numpy as np
import torch

np.random.seed(42)
torch.manual_seed(42)

from script1_adversarial_lstm import AdversarialMARLSystem  # noqa: E402

system = AdversarialMARLSystem(num_clusters=3, sequence_length=4)
shocks = []
for i in range(5):
    report, shock_val = system.step()
    shocks.append(shock_val)
    print(f"Iteration {report['step']:02d} | Chaos: {report['mean_chaos']:.4f} | "
          f"Adversarial Load: {shock_val:.4f} | {report['status']}")

# Claim under test: "adversary ... Discovers optimal strategic shock sequences"
# If the training loop were real, adversary weights change and shocks vary with state.
p = system.adversary
grads = {n: (param.grad is not None) for n, param in p.named_parameters()}
print("\nAdversary parameter gradient present after backward():", grads)
w0 = {n: param.clone() for n, param in p.named_parameters()}
for _ in range(20):
    system.step()
w1 = {n: param for n, param in p.named_parameters()}
changed = {n: float((w1[n] - w0[n]).abs().max()) for n in w0}
print("Max weight change over 20 steps:", changed)
print("Shocks across first 5 steps:", [round(s, 4) for s in shocks])
print("VERDICT:", "adversary trains" if any(v > 0 for v in changed.values())
      else "adversary NEVER updates: training loop is decorative")
