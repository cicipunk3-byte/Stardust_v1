import unittest
import torch
import torch.nn as nn
import numpy as np
from typing import Dict, Tuple, Any, List

# =====================================================================
# RECURRENT LSTM STATE SPACE ARCHITECTURE
# =====================================================================
class LSTMSystemicPolicy(nn.Module):
    """
    Recurrent Neural Network utilizing LSTM units to track long-term historical 
    trauma trajectories before selecting behavioral policy adaptations.
    Inputs: [env_chaos, systemic_denial, systemic_jitter, neighborhood_avg]
    """
    def __init__(self, input_dim: int = 4, hidden_dim: int = 32, action_dim: int = 4):
        super(LSTMSystemicPolicy, self).__init__()
        self.hidden_dim = hidden_dim
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Sequential(
            nn.Linear(hidden_dim, 16),
            nn.ReLU(),
            nn.Linear(16, action_dim)
        )

    def forward(self, sequence: torch.Tensor, hidden: Tuple[torch.Tensor, torch.Tensor] = None) -> Tuple[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]]:
        # sequence shape: (batch, seq_len, input_dim)
        lstm_out, hidden_state = self.lstm(sequence, hidden)
        # Select the last temporal output token for policy evaluation
        last_step = lstm_out[:, -1, :]
        q_values = self.fc(last_step)
        return q_values, hidden_state

# =====================================================================
# GENERATIVE ADVERSARIAL TRAUMA ENVIRONMENT
# =====================================================================
class AdversarialTraumaGenerator(nn.Module):
    """
    Adversarial Network acting as an environmental stress vector.
    Discovers optimal strategic shock sequences to collapse family homeostasis.
    """
    def __init__(self, state_dim: int = 3, output_dim: int = 1):
        super(AdversarialTraumaGenerator, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 16),
            nn.Tanh(),
            nn.Linear(16, output_dim),
            nn.Sigmoid() # Bounds structural shock between 0.0 and 1.0
        )
        
    def forward(self, global_metrics: torch.Tensor) -> torch.Tensor:
        return self.network(global_metrics)

class AdversarialMARLSystem:
    def __init__(self, num_clusters: int = 3, sequence_length: int = 4):
        self.num_clusters = num_clusters
        self.seq_len = sequence_length
        self.reset()
        
        # Initialize architectural agents and adversarial nodes
        self.agents = {role: LSTMSystemicPolicy() for role in ["hero", "scapegoat", "lost_child", "mascot"]}
        self.adversary = AdversarialTraumaGenerator()
        self.adversary_optimizer = torch.optim.Adam(self.adversary.parameters(), lr=1e-3)

    def reset(self):
        self.current_step = 0
        self.env_chaos = np.random.uniform(0.3, 0.5, size=(self.num_clusters,))
        self.denial = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        self.jitter = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        
        # Pre-populate historical queues to fulfill LSTM sequential dependencies
        self.history_buffers = [[] for _ in range(self.num_clusters)]
        for c in range(self.num_clusters):
            for _ in range(self.seq_len):
                self.history_buffers[c].append([self.env_chaos[c], self.denial[c], self.jitter[c], 0.4])

    def step(self) -> Tuple[Dict[str, Any], float]:
        self.current_step += 1
        neighborhood_avg = float(np.mean(self.env_chaos))
        
        # 1. EVALUATE ADVERSARIAL STRESS VECTOR IMPULSE
        global_state = torch.tensor([neighborhood_avg, np.mean(self.denial), np.mean(self.jitter)], dtype=torch.float32)
        adversarial_shock = self.adversary(global_state).item()
        
        # 2. EVALUATE RECURRENT LSTM CONTROLS FOR EACH AGENT NODE
        for c in range(self.num_clusters):
            # Update rolling sequence memory layout
            self.history_buffers[c].pop(0)
            self.history_buffers[c].append([self.env_chaos[c], self.denial[c], self.jitter[c], neighborhood_avg])
            
            seq_tensor = torch.tensor([self.history_buffers[c]], dtype=torch.float32) # (1, seq_len, 4)
            
            with torch.no_grad():
                h_act = torch.argmax(self.agents["hero"](seq_tensor)[0]).item()
                s_act = torch.argmax(self.agents["scapegoat"](seq_tensor)[0]).item()
                l_act = torch.argmax(self.agents["lost_child"](seq_tensor)[0]).item()
                m_act = torch.argmax(self.agents["mascot"](seq_tensor)[0]).item()

            # 3. COMPUTE CYBERNETIC TRANSITION LAWS
            intrinsic_drift = np.random.normal(0.05, 0.01) + (0.35 * adversarial_shock)
            self.denial[c] = 0.85 * self.denial[c] + 0.15 * (0.30 if h_act == 1 else 0.0)
            self.jitter[c] = 0.75 * self.jitter[c] + 0.25 * (0.25 if m_act == 3 else 0.0)
            
            loss_absorption = 0.45 if s_act == 2 else 0.0
            isolation_penalty = 0.15 if l_act == 0 else -0.02
            
            self.env_chaos[c] = np.clip(
                self.env_chaos[c] + intrinsic_drift + (0.15 * self.denial[c]) 
                + (0.10 * self.jitter[c]) - loss_absorption + (0.10 * isolation_penalty),
                0.0, 1.0
            )

        # 4. TRAIN ADVERSARY (Maximizes system variance to uncover failure boundaries)
        final_chaos = float(np.mean(self.env_chaos))
        adversary_loss = -1.0 * torch.tensor(final_chaos, requires_grad=True)
        
        self.adversary_optimizer.zero_grad()
        adversary_loss.backward()
        self.adversary_optimizer.step()
        
        # Run Diagnostics Isolation mapping
        diagnostics = {
            "step": self.current_step,
            "mean_chaos": final_chaos,
            "adversarial_shock_delivered": adversarial_shock,
            "status": "STABLE" if final_chaos < 0.65 else "CRITICAL_COLLAPSE"
        }
        return diagnostics, adversarial_shock

# =====================================================================
# AUTOMATED STRUCTURAL DIAGNOSTIC UNIT TEST HARNESS
# =====================================================================
class TestRFASystemicPipeline(unittest.TestCase):
    def setUp(self):
        self.marl_system = AdversarialMARLSystem(num_clusters=2, sequence_length=4)

    def test_state_dimensions(self):
        """Verifies history queues match target LSTM tensor sequence lengths."""
        self.assertEqual(len(self.marl_system.history_buffers), 2)
        self.assertEqual(len(self.marl_system.history_buffers[0]), 4)

    def test_adversarial_shock_bounding(self):
        """Ensures the trauma adversary output constraints remain strictly inside [0, 1]."""
        _, shock = self.marl_system.step()
        self.assertTrue(0.0 <= shock <= 1.0)

    def test_system_trajectories(self):
        """Validates execution cycles cleanly step without generating NaN boundaries."""
        for _ in range(3):
            diag, _ = self.marl_system.step()
            self.assertIn("mean_chaos", diag)
            self.assertFalse(np.isnan(diag["mean_chaos"]))

# =====================================================================
# PIPELINE EXECUTION VERIFICATION RUNNER
# =====================================================================
if __name__ == "__main__":
    np.random.seed(42)
    torch.manual_seed(42)
    
    print("=== STEP 1: RUNNING ADVERSARIAL LSTM PIPELINE ANALYSIS ===")
    system = AdversarialMARLSystem(num_clusters=3, sequence_length=4)
    
    for i in range(5):
        report, shock_val = system.step()
        print(f"Iteration {report['step']:02d} | Chaos: {report['mean_chaos']:.4f} | "
              f"Adversarial Load Injection: {shock_val:.4f} | Diagnostic: {report['status']}")
              
    print("\n=== STEP 2: LAUNCHING PROACTIVE TESTING HARNESS ===")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRFASystemicPipeline)
    unittest.TextTestRunner(verbosity=2).run(suite)
