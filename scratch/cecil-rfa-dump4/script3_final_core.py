import os
import json
import time
import torch
import torch.nn as nn
import numpy as np
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, Any, List

# =====================================================================
# HOT-SWAPPING CONFIGURATION MODULE
# =====================================================================
CONFIG_PATH = "rfa_config.json"
DEFAULT_CONFIG = {
    "num_clusters": 3,
    "sequence_length": 4,
    "lstm_hidden_dim": 32,
    "learning_rate": 0.001,
    "chaos_threshold": 0.65,
    "enmeshment_threshold": 0.12,
    "log_output_path": "rfa_failure_log.json",
    "polling_interval_seconds": 2
}

class LiveConfig:
    def __init__(self):
        self.lock = threading.Lock()
        self.cfg = DEFAULT_CONFIG.copy()
        self._ensure_config_exists()
        self.last_modified = 0
        self.reload()

    def _ensure_config_exists(self):
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'w') as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)

    def reload(self):
        with self.lock:
            try:
                mod_time = os.path.getmtime(CONFIG_PATH)
                if mod_time > self.last_modified:
                    with open(CONFIG_PATH, 'r') as f:
                        new_data = json.load(f)
                        # Atomic update of modified keys
                        for k, v in new_data.items():
                            self.cfg[k] = v
                    self.last_modified = mod_time
                    print(f"[CONFIG RELOADED] Active properties updated dynamically at timestamp: {time.time()}")
            except Exception as e:
                print(f"[CONFIG ERROR] Failed to hot-swap properties safely: {e}")

    def get(self, key: str) -> Any:
        with self.lock:
            return self.cfg.get(key, DEFAULT_CONFIG.get(key))

live_config = LiveConfig()

def config_polling_worker():
    while True:
        time.sleep(live_config.get("polling_interval_seconds"))
        live_config.reload()

# =====================================================================
# DEEP NEURAL RECURRENT STATE ARCHITECTURES
# =====================================================================
class LSTMRolePolicy(nn.Module):
    def __init__(self, input_dim: int = 4, hidden_dim: int = 32, action_dim: int = 4):
        super(LSTMRolePolicy, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.fc = nn.Sequential(nn.Linear(hidden_dim, 16), nn.ReLU(), nn.Linear(16, action_dim))

    def forward(self, sequence: torch.Tensor) -> torch.Tensor:
        lstm_out, _ = self.lstm(sequence)
        return self.fc(lstm_out[:, -1, :])

class EnvironmentalTraumaAdversary(nn.Module):
    def __init__(self, state_dim: int = 3, output_dim: int = 1):
        super(EnvironmentalTraumaAdversary, self).__init__()
        self.network = nn.Sequential(nn.Linear(state_dim, 16), nn.Tanh(), nn.Linear(16, output_dim), nn.Sigmoid())
        
    def forward(self, global_metrics: torch.Tensor) -> torch.Tensor:
        return self.network(global_metrics)

# =====================================================================
# SYSTEM CORE SANDBOX ENVIRONMENT
# =====================================================================
class ProductionRFASandbox:
    def __init__(self):
        self.lock = threading.Lock()
        self.num_clusters = live_config.get("num_clusters")
        self.seq_len = live_config.get("sequence_length")
        
        self.agents = {role: LSTMRolePolicy(hidden_dim=live_config.get("lstm_hidden_dim")) 
                       for role in ["hero", "scapegoat", "lost_child", "mascot"]}
        self.adversary = EnvironmentalTraumaAdversary()
        self.optimizer = torch.optim.Adam(self.adversary.parameters(), lr=live_config.get("learning_rate"))
        self.reset()

    def reset(self):
        self.current_step = 0
        self.env_chaos = np.random.uniform(0.3, 0.45, size=(self.num_clusters,))
        self.denial = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        self.jitter = np.random.uniform(0.1, 0.2, size=(self.num_clusters,))
        
        self.history_buffers = [ for _ in range(self.num_clusters)]
        for c in range(self.num_clusters):
            for _ in range(self.seq_len):
                self.history_buffers[c].append([self.env_chaos[c], self.denial[c], self.jitter[c], 0.4])
        self.last_metrics = {"mean_chaos": 0.0, "enmeshment_leakage": 0.0, "adversarial_shock": 0.0}

    def step(self) -> Dict[str, Any]:
        with self.lock:
            self.current_step += 1
            neighborhood_avg = float(np.mean(self.env_chaos))
            
            global_state = torch.tensor([neighborhood_avg, np.mean(self.denial), np.mean(self.jitter)], dtype=torch.float32)
            adversarial_shock = self.adversary(global_state).item()
            
            for c in range(self.num_clusters):
                self.history_buffers[c].pop(0)
                self.history_buffers[c].append([self.env_chaos[c], self.denial[c], self.jitter[c], neighborhood_avg])
                seq_tensor = torch.tensor([self.history_buffers[c]], dtype=torch.float32)
                
                with torch.no_grad():
                    h_act = torch.argmax(self.agents["hero"](seq_tensor)).item()
                    s_act = torch.argmax(self.agents["scapegoat"](seq_tensor)).item()
                    l_act = torch.argmax(self.agents["lost_child"](seq_tensor)).item()
                    m_act = torch.argmax(self.agents["mascot"](seq_tensor)).item()

                intrinsic_drift = np.random.normal(0.04, 0.01) + (0.40 * adversarial_shock)
                self.denial[c] = 0.85 * self.denial[c] + 0.15 * (0.30 if h_act == 1 else 0.0)
                self.jitter[c] = 0.75 * self.jitter[c] + 0.25 * (0.25 if m_act == 3 else 0.0)
                
                loss_absorption = 0.50 if s_act == 2 else 0.0
                isolation_penalty = 0.15 if l_act == 0 else -0.02
                
                self.env_chaos[c] = np.clip(
                    self.env_chaos[c] + intrinsic_drift + (0.15 * self.denial[c]) 
                    + (0.10 * self.jitter[c]) - loss_absorption + (0.10 * isolation_penalty),
                    0.0, 1.0
                )

            final_chaos = float(np.mean(self.env_chaos))
            enmeshment_leakage = float(np.std(self.env_chaos))
            
            loss = -1.0 * torch.tensor(final_chaos, requires_grad=True)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            
            self.last_metrics = {
                "mean_chaos": final_chaos,
                "enmeshment_leakage": enmeshment_leakage,
                "adversarial_shock": adversarial_shock
            }
            return self.last_metrics

sandbox = ProductionRFASandbox()

# =====================================================================
# EXPORTER LAYER (PROMETHEUS NATIVE TEXT FORMAT FORMAT)
# =====================================================================
class HTTPSandboxServer(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return # Suppress default logging noise

    def do_GET(self):
        if self.path == '/metrics':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; version=0.0.4; charset=utf-8')
            self.end_headers()
            
            metrics = sandbox.last_metrics
            output = [
                "# HELP rfa_mean_chaos Average homeostatic system trauma metric",
                "# TYPE rfa_mean_chaos gauge",
                f"rfa_mean_chaos {metrics['mean_chaos']:.4f}",
                "# HELP rfa_enmeshment_leakage Intra-cluster variance boundary degradation",
                "# TYPE rfa_enmeshment_leakage gauge",
                f"rfa_enmeshment_leakage {metrics['enmeshment_leakage']:.4f}",
                "# HELP rfa_adversarial_shock Stress injection index computed dynamically",
                "# TYPE rfa_adversarial_shock gauge",
                f"rfa_adversarial_shock {metrics['adversarial_shock']:.4f}"
            ]
            self.wfile.write(("\n".join(output) + "\n").encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(sandbox.last_metrics).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port: int = 8080):
    server = HTTPServer(('', port), HTTPSandboxServer)
    print(f"[METRICS EXPORTER ON] Inbound connections accepted on port {port}")
    server.serve_forever()

if __name__ == "__main__":
    np.random.seed(42)
    torch.manual_seed(42)
    
    # Fire asynchronous infrastructure daemons
    threading.Thread(target=config_polling_worker, daemon=True).start()
    threading.Thread(target=run_server, args=(8080,), daemon=True).start()
    
    print("=== PIPELINE STARTED ACTIVE SIMULATION MODE ===")
    try:
        while True:
            metrics = sandbox.step()
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("[TERMINATED] Execution completed.")
