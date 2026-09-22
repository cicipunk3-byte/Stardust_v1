# Faithful reconstruction of rfa_distributed_production.py from dump 4.
# The shipped text is fragmented by scrape damage (split keywords, lost indents);
# every token and constant below is transcribed from the dump, indentation restored.
import os
import json
import time
import math
import torch
import torch.nn as nn
import numpy as np
import threading
from typing import Dict, Any, List, Tuple


class CentralizedMemoryCache:
    def __init__(self):
        self._lock = threading.Lock()
        self._storage = {}

    def set_weights(self, agent_role: str, weights: Dict[str, torch.Tensor]):
        with self._lock:
            self._storage[f"weights:{agent_role}"] = {k: v.clone() for k, v in weights.items()}

    def get_weights(self, agent_role: str) -> Dict[str, torch.Tensor]:
        with self._lock:
            key = f"weights:{agent_role}"
            if key in self._storage:
                return {k: v.clone() for k, v in self._storage[key].items()}
            return None


global_parameter_server = CentralizedMemoryCache()


class LSTMSystemicPolicy(nn.Module):
    def __init__(self, input_dim: int = 4, hidden_dim: int = 32, action_dim: int = 4):
        super(LSTMSystemicPolicy, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Sequential(nn.Linear(hidden_dim, 16), nn.ReLU(), nn.Linear(16, action_dim))

    def forward(self, sequence: torch.Tensor) -> torch.Tensor:
        lstm_out, _ = self.lstm(sequence)
        return self.fc(lstm_out[:, -1, :])


class MultiChannelTraumaAdversary(nn.Module):
    def __init__(self, state_dim: int = 3, target_agents: int = 4):
        super(MultiChannelTraumaAdversary, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, 32),
            nn.Tanh(),
            nn.Linear(32, target_agents),
            nn.Sigmoid()
        )

    def forward(self, macro_state: torch.Tensor) -> torch.Tensor:
        return self.network(macro_state)


class OrchestratedRFASandbox:
    def __init__(self, cluster_id: str, num_clusters: int = 3, seq_len: int = 4):
        self.cluster_id = cluster_id
        self.num_clusters = num_clusters
        self.seq_len = seq_len
        self.agents = {role: LSTMSystemicPolicy() for role in ["hero", "scapegoat", "lost_child", "mascot"]}
        self.adversary = MultiChannelTraumaAdversary()
        self.adv_optimizer = torch.optim.Adam(self.adversary.parameters(), lr=1e-3)
        self.reset()

    def reset(self):
        self.current_step = 0
        self.env_chaos = np.random.uniform(0.3, 0.45, size=(self.num_clusters,))
        self.denial = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        self.jitter = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        self.history_buffers = [[] for _ in range(self.num_clusters)]
        for c in range(self.num_clusters):
            for _ in range(self.seq_len):
                self.history_buffers[c].append([self.env_chaos[c], self.denial[c], self.jitter[c], 0.4])

    def push_local_policies_to_cache(self):
        for role, net in self.agents.items():
            global_parameter_server.set_weights(f"{self.cluster_id}:{role}", net.state_dict())

    def step(self) -> Dict[str, Any]:
        self.current_step += 1
        neighborhood_avg = float(np.mean(self.env_chaos))
        global_metrics = torch.tensor([neighborhood_avg, np.mean(self.denial), np.mean(self.jitter)], dtype=torch.float32)
        attack_vector = self.adversary(global_metrics)

        for c in range(self.num_clusters):
            self.history_buffers[c].pop(0)
            self.history_buffers[c].append([self.env_chaos[c], self.denial[c], self.jitter[c], neighborhood_avg])
            seq_tensor = torch.tensor([self.history_buffers[c]], dtype=torch.float32)

            with torch.no_grad():
                h_act = torch.argmax(self.agents["hero"](seq_tensor)).item()
                s_act = torch.argmax(self.agents["scapegoat"](seq_tensor)).item()
                l_act = torch.argmax(self.agents["lost_child"](seq_tensor)).item()
                m_act = torch.argmax(self.agents["mascot"](seq_tensor)).item()

            h_shock = float(attack_vector[0].item())
            s_shock = float(attack_vector[1].item())
            l_shock = float(attack_vector[2].item())
            m_shock = float(attack_vector[3].item())

            self.denial[c] = 0.85 * self.denial[c] + 0.15 * (0.30 if h_act == 1 else 0.0) + (0.1 * h_shock)
            self.jitter[c] = 0.75 * self.jitter[c] + 0.25 * (0.25 if m_act == 3 else 0.0) + (0.1 * m_shock)
            loss_absorption = 0.50 if s_act == 2 else 0.0
            isolation_penalty = 0.15 if l_act == 0 else -0.02

            self.env_chaos[c] = np.clip(
                self.env_chaos[c] + np.random.normal(0.03, 0.01) + (0.3 * s_shock) + (0.2 * l_shock)
                + (0.15 * self.denial[c]) + (0.10 * self.jitter[c]) - loss_absorption + (0.10 * isolation_penalty),
                0.0, 1.0
            )

        final_chaos = float(np.mean(self.env_chaos))
        adv_loss = -1.0 * torch.tensor(final_chaos, requires_grad=True)
        self.adv_optimizer.zero_grad()
        adv_loss.backward()
        self.adv_optimizer.step()

        return {
            "step": self.current_step,
            "chaos": final_chaos,
            "variance": float(np.std(self.env_chaos)),
            "attack_profile": [round(x.item(), 3) for x in attack_vector]
        }


if __name__ == "__main__":
    np.random.seed(42)
    torch.manual_seed(42)
    sandbox = OrchestratedRFASandbox(cluster_id="cluster_prod_01")
    for _ in range(8):
        data = sandbox.step()
        sandbox.push_local_policies_to_cache()
        print(f"[Step {data['step']:02d}] Chaos: {data['chaos']:.4f} | Variance: {data['variance']:.4f} | "
              f"Attack H:{data['attack_profile'][0]} S:{data['attack_profile'][1]} "
              f"L:{data['attack_profile'][2]} M:{data['attack_profile'][3]}")
    # Weight-sync check: did the cache actually store and return weights?
    got = global_parameter_server.get_weights("cluster_prod_01:hero")
    print("Cache round-trip:", "WORKS" if got and "lstm.weight_ih_l0" in got else "BROKEN")
    # Adversary-learning check (same pattern as script 1)
    w0 = {n: p.clone() for n, p in sandbox.adversary.named_parameters()}
    for _ in range(20):
        sandbox.step()
    w1 = {n: p for n, p in sandbox.adversary.named_parameters()}
    changed = {n: float((w1[n] - w0[n]).abs().max()) for n in w0}
    print("Adversary max weight change over 20 steps:", changed)
    print("VERDICT:", "adversary trains" if any(v > 0 for v in changed.values())
          else "adversary NEVER updates (same decorative backprop as script 1)")
