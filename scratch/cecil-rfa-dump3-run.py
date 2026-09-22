import numpy as np
import json
import random
import urllib.request
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# ============ PIPELINE 1: mesosystem diffusion (doc's claims checked) ============

class MesosystemSimulation:
    def __init__(self, num_clusters: int = 5, timesteps: int = 50, boundary_resistance: float = 0.58):
        self.num_clusters = num_clusters
        self.timesteps = timesteps
        self.boundary_resistance = boundary_resistance
        self.reset()

    def reset(self):
        self.node_variance = np.zeros((self.num_clusters, 4))
        self.node_variance[0, 1] = 1.0
        self.cluster_means_history = []

    def run_simulation(self):
        for t in range(self.timesteps):
            next_variance = self.node_variance.copy()
            for c in range(self.num_clusters):
                local_mean = np.mean(self.node_variance[c])
                next_variance[c, 0] = 0.7 * self.node_variance[c, 0] + 0.3 * (1.0 - local_mean)
                next_variance[c, 1] = 0.85 * self.node_variance[c, 1] + 0.15 * local_mean
                next_variance[c, 2] = 0.95 * self.node_variance[c, 2]
                next_variance[c, 3] = 0.6 * self.node_variance[c, 3] + 0.4 * np.random.normal(0, 0.1)
            for c in range(self.num_clusters):
                if c > 0:
                    spillover = self.node_variance[c-1, 1] * (1.0 - self.boundary_resistance)
                    next_variance[c, 1] += 0.12 * spillover
                if c < self.num_clusters - 1:
                    spillover = self.node_variance[c+1, 1] * (1.0 - self.boundary_resistance)
                    next_variance[c, 1] += 0.12 * spillover
            self.node_variance = np.clip(next_variance, 0.0, 1.0)
            self.cluster_means_history.append(np.mean(self.node_variance, axis=1))
        return np.array(self.cluster_means_history)

print("=== DOC DEMO: 4 clusters, 6 steps ===")
np.random.seed(42)
sim = MesosystemSimulation(num_clusters=4, timesteps=6, boundary_resistance=0.58)
h = sim.run_simulation()
print(f"T=0 infected cluster 0 mean: {h[0,0]:.4f}")
print(f"T=5 cluster 0 mean: {h[-1,0]:.4f} | cluster 1 mean: {h[-1,1]:.4f} | distal cluster 3 mean: {h[-1,3]:.4f}")

print("\n=== CHECK A: does the scapegoat variance actually SPREAD or just decay? ===")
np.random.seed(42)
simA = MesosystemSimulation(num_clusters=4, timesteps=50, boundary_resistance=0.58)
hA = simA.run_simulation()
print(f"cluster scapegoat variance at T=0:  {[1.0, 0, 0, 0]}")
print(f"cluster scapegoat variance at T=50: {simA.node_variance[:,1].round(4)}")

print("\n=== CHECK B: the claimed 0.72 contagion threshold (sweep initial shock) ===")
thresholds = []
for v0 in np.arange(0.4, 1.01, 0.1):
    np.random.seed(0)
    m = MesosystemSimulation(num_clusters=3, timesteps=50, boundary_resistance=0.58)
    m.reset()
    m.node_variance[0,1] = v0
    m.run_simulation()
    peak_neighbor = m.node_variance[1,1]
    thresholds.append((round(v0,2), round(float(peak_neighbor),4)))
    print(f"initial shock {v0:.2f} -> neighbor cluster 1 scapegoat variance: {peak_neighbor:.4f}")
print("(a real 0.72 threshold would show a sharp jump between rows; LINEAR dynamics predict none)")

print("\n=== CHECK C: the claimed 42% per-hop dampening ===")
print(f"boundary_resistance parameter: 0.58. 1 - 0.58 = {1-0.58:.2f}. The 'finding' is the parameter restated.")

# ============ PIPELINE 2: GA evolutionary sandbox (brief smoke + citation check) ============

print("\n=== GA PIPELINE (doc's demo, 3 generations, 6 chromosomes) ===")
random.seed(42); np.random.seed(42)

class EvolutionaryMacroSandbox:
    def __init__(self, num_clusters: int = 4, lifecycle_steps: int = 20):
        self.num_clusters = num_clusters
        self.lifecycle_steps = lifecycle_steps

    def evaluate_chromosome(self, boundary_resistances, inject_shock_at: int = 10):
        node_variance = np.zeros((self.num_clusters, 4))
        node_variance[:, 1] = 0.4
        cumulative_trauma = 0.0
        chaos_trajectory = []
        for t in range(self.lifecycle_steps):
            current_variance = node_variance.copy()
            next_variance = node_variance.copy()
            macro_shock = 0.45 if t == inject_shock_at else 0.0
            intrinsic_noise = np.random.normal(0.06, 0.02) + macro_shock
            cancellation_signals = np.zeros(self.num_clusters)
            for c in range(self.num_clusters):
                if current_variance[c, 3] > 0.1:
                    cancellation_signals[c] = 0.25 * current_variance[c, 3] * np.std(current_variance[c])
            for c in range(self.num_clusters):
                local_mean = np.mean(current_variance[c])
                effective_noise = max(0.0, local_mean - cancellation_signals[c]) + intrinsic_noise
                next_variance[c, 0] = 0.70 * current_variance[c, 0] + 0.30 * (1.0 - effective_noise)
                next_variance[c, 1] = 0.80 * current_variance[c, 1] + 0.20 * effective_noise
                next_variance[c, 2] = 0.95 * current_variance[c, 2]
                next_variance[c, 3] = 0.60 * current_variance[c, 3] + 0.40 * np.random.uniform(0.0, 0.15)
                left_neighbor = (c - 1) % self.num_clusters
                insulation_efficiency = 1.0 - boundary_resistances[c]
                next_variance[c, 1] += 0.06 * current_variance[left_neighbor, 1] * insulation_efficiency
            node_variance = np.clip(next_variance, 0.0, 1.0)
            step_chaos = float(np.mean(node_variance[:, 1]))
            cumulative_trauma += step_chaos ** 2
            chaos_trajectory.append(step_chaos)
        fitness = 1.0 / (1.0 + cumulative_trauma)
        return fitness, chaos_trajectory

    def evolve_population(self, generations: int = 3, pop_size: int = 6):
        population = [np.random.uniform(0.2, 0.8, size=(self.num_clusters,)) for _ in range(pop_size)]
        for gen in range(generations):
            fitness_scores, trajectories = [], []
            for chrom in population:
                fit, traj = self.evaluate_chromosome(chrom)
                fitness_scores.append(fit); trajectories.append(traj)
            best_idx = int(np.argmax(fitness_scores))
            print(f"Gen {gen}: best fitness {fitness_scores[best_idx]:.5f}, alleles {np.round(population[best_idx],3)}")
            probs = np.array(fitness_scores) / np.sum(fitness_scores)
            selected_parents = [population[np.random.choice(pop_size, p=probs)] for _ in range(pop_size)]
            next_pop = []
            for i in range(0, pop_size, 2):
                p1, p2 = selected_parents[i], selected_parents[i+1]
                mask = np.random.rand(self.num_clusters) > 0.5
                c1 = np.where(mask, p1, p2) + np.random.normal(0, 0.05, size=(self.num_clusters,))
                c2 = np.where(~mask, p1, p2) + np.random.normal(0, 0.05, size=(self.num_clusters,))
                next_pop.extend([np.clip(c1, 0.1, 0.95), np.clip(c2, 0.1, 0.95)])
            population = next_pop

ga = EvolutionaryMacroSandbox(num_clusters=4, lifecycle_steps=15)
ga.evolve_population(generations=3, pop_size=6)

# ============ PIPELINE 3: REST API + untrained deep policies (does it serve? what drives the policies?) ============

import torch
import torch.nn as nn

class DeepSystemicPolicy(nn.Module):
    def __init__(self, input_dim: int = 4, action_dim: int = 4):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 64), nn.LeakyReLU(0.1),
            nn.Linear(64, 32), nn.LeakyReLU(0.1),
            nn.Linear(32, action_dim)
        )
    def forward(self, state):
        return self.network(state)

class ProductionRFASandbox:
    def __init__(self, num_clusters: int = 3):
        self.num_clusters = num_clusters
        self.reset()
        self.policies = {role: DeepSystemicPolicy() for role in ["hero", "scapegoat", "lost_child", "mascot"]}

    def reset(self):
        self.current_step = 0
        self.env_chaos = np.random.uniform(0.4, 0.6, size=(self.num_clusters,))
        self.denial = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        self.jitter = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        self.history = []

    def compute_diagnostics(self):
        mean_chaos = float(np.mean(self.env_chaos))
        enmeshment_leakage = float(np.std(self.env_chaos))
        failure_vector = "FUNCTIONAL_ADAPTIVE"
        if enmeshment_leakage > 0.15:
            failure_vector = "CRITICAL_ENMESHMENT_GRADIENT_LEAKAGE"
        elif mean_chaos > 0.70:
            failure_vector = "RIGID_HOMEOSTATIC_SYSTEM_COLLAPSE"
        return {"current_step": self.current_step, "mean_chaos": mean_chaos,
                "enmeshment_leakage_index": enmeshment_leakage, "systemic_diagnostic_status": failure_vector}

    def process_step(self, exogenous_shock: float = 0.0):
        self.current_step += 1
        action_log = []
        for c in range(self.num_clusters):
            neighborhood_avg = float(np.mean(self.env_chaos))
            state_vec = torch.tensor([self.env_chaos[c], self.denial[c], self.jitter[c], neighborhood_avg], dtype=torch.float32)
            with torch.no_grad():
                picks = [int(torch.argmax(self.policies[r](state_vec)).item()) for r in ["hero","scapegoat","lost_child","mascot"]]
            action_log.append(picks)
            h_act, s_act, l_act, m_act = picks
            intrinsic_drift = np.random.normal(0.06, 0.02) + exogenous_shock
            self.denial[c] = 0.8 * self.denial[c] + 0.2 * (0.35 if h_act == 1 else 0.0)
            self.jitter[c] = 0.7 * self.jitter[c] + 0.3 * (0.25 if m_act == 3 else 0.0)
            loss_absorption = 0.45 if s_act == 2 else 0.0
            isolation_penalty = 0.15 if l_act == 0 else -0.02
            self.env_chaos[c] = np.clip(
                self.env_chaos[c] + intrinsic_drift + (0.2 * self.denial[c])
                + (0.1 * self.jitter[c]) - loss_absorption + (0.12 * isolation_penalty),
                0.0, 1.0)
        d = self.compute_diagnostics(); d["action_log"] = action_log
        self.history.append(d)
        return d

print("\n=== API PIPELINE: local validation cycles ===")
torch.manual_seed(1); np.random.seed(42)
sandbox_instance = ProductionRFASandbox()
for i in range(3):
    m = sandbox_instance.process_step(exogenous_shock=0.0)
    print(f"Cycle {i+1} | mean chaos {m['mean_chaos']:.4f} | status {m['systemic_diagnostic_status']} | actions {m['action_log']}")
print("shock cycle:")
m = sandbox_instance.process_step(exogenous_shock=0.55)
print(f"mean chaos {m['mean_chaos']:.4f} | status {m['systemic_diagnostic_status']}")

# ARE the "deep policies" doing anything? untrained random nets: check if their argmax is constant regardless of state
print("\n=== CHECK D: do the untrained deep policies respond to state at all? ===")
st_low = torch.tensor([0.0, 0.0, 0.0, 0.0], dtype=torch.float32)
st_high = torch.tensor([1.0, 1.0, 1.0, 1.0], dtype=torch.float32)
for role in sandbox_instance.policies:
    with torch.no_grad():
        a_low = int(torch.argmax(sandbox_instance.policies[role](st_low)).item())
        a_high = int(torch.argmax(sandbox_instance.policies[role](st_high)).item())
    print(f"{role:10s} argmax at all-zero state: {a_low}, at all-one state: {a_high}, responsive: {a_low != a_high}")

print("\n=== CHECK E: live HTTP round-trip ===")
class HTTPSandboxServer(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status); self.send_header('Content-Type', 'application/json'); self.end_headers()
    def do_GET(self):
        if self.path == '/status':
            self._set_headers(200); self.wfile.write(json.dumps(sandbox_instance.compute_diagnostics()).encode())
        else:
            self._set_headers(404); self.wfile.write(json.dumps({"error": "nope"}).encode())
    def do_POST(self):
        if self.path == '/step':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length) if length > 0 else b'{}'
            try: payload = json.loads(body.decode())
            except Exception: payload = {}
            res = sandbox_instance.process_step(exogenous_shock=float(payload.get("shock", 0.0)))
            self._set_headers(200); self.wfile.write(json.dumps({"message": "ok", "metrics": res}).encode())
        else:
            self._set_headers(404)
    def log_message(self, *a): pass

server = HTTPServer(('', 8123), HTTPSandboxServer)
t = threading.Thread(target=server.serve_forever, daemon=True); t.start()
import time; time.sleep(0.3)
with urllib.request.urlopen("http://localhost:8123/status") as r:
    print("GET /status ->", r.read().decode()[:120])
req = urllib.request.Request("http://localhost:8123/step", data=json.dumps({"shock": 0.3}).encode(), method="POST")
with urllib.request.urlopen(req) as r:
    print("POST /step ->", r.read().decode()[:120])
server.shutdown()
print("HTTP round-trip: WORKS")
