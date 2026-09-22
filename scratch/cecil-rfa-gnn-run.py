import torch
import torch.nn as nn
import numpy as np

class FamilyGraphEnvironment:
    """
    State: Evaluates graph feature matrix X and connectivity edge_index.
    Nodes: 4 per family index -> [Hero, Scapegoat, Lost Child, Mascot]
    """
    def __init__(self, num_families: int = 5, max_steps: int = 30):
        self.num_families = num_families
        self.max_steps = max_steps
        self.num_agents = num_families * 4
        self.reset()

    def reset(self):
        self.current_step = 0
        self.chaos_states = np.random.uniform(0.3, 0.7, size=(self.num_families,))
        self.denial_states = np.random.uniform(0.1, 0.3, size=(self.num_families,))
        self.jitter_states = np.random.uniform(0.1, 0.3, size=(self.num_families,))
        return self._build_graph()

    def _build_graph(self):
        node_features = []
        for i in range(self.num_families):
            c, d, j = self.chaos_states[i], self.denial_states[i], self.jitter_states[i]
            node_features.append([c, d, j, 1.0, 0.0, 0.0, 0.0])
            node_features.append([c, d, j, 0.0, 1.0, 0.0, 0.0])
            node_features.append([c, d, j, 0.0, 0.0, 1.0, 0.0])
            node_features.append([c, d, j, 0.0, 0.0, 0.0, 1.0])
        X = torch.tensor(node_features, dtype=torch.float32)
        edges = []
        for i in range(self.num_families):
            base = i * 4
            for u in range(4):
                for v in range(4):
                    if u != v:
                        edges.append([base + u, base + v])
        for i in range(self.num_families - 1):
            edges.append([i * 4 + 0, (i + 1) * 4 + 0])
            edges.append([i * 4 + 1, (i + 1) * 4 + 1])
        edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()
        return X, edge_index

    def step(self, actions):
        self.current_step += 1
        h_acts, s_acts, l_acts, m_acts = actions["hero"], actions["scapegoat"], actions["lost_child"], actions["mascot"]
        rewards = {"hero": 0.0, "scapegoat": 0.0, "lost_child": 0.0, "mascot": 0.0}
        for i in range(self.num_families):
            intrinsic_trauma = np.random.normal(0.08, 0.02)
            h_a, s_a, l_a, m_a = h_acts[i], s_acts[i], l_acts[i], m_acts[i]
            hero_mask = 0.3 if h_a == 1 else 0.0
            scapegoat_absorb = 0.5 if s_a == 2 else 0.0
            lost_child_isolate = 0.2 if l_a == 0 else -0.05
            mascot_noise = 0.25 if m_a == 3 else 0.0
            self.denial_states[i] = 0.85 * self.denial_states[i] + 0.15 * hero_mask
            self.jitter_states[i] = 0.75 * self.jitter_states[i] + 0.25 * mascot_noise
            self.chaos_states[i] = np.clip(
                self.chaos_states[i] + intrinsic_trauma + (0.15 * self.denial_states[i])
                + (0.1 * self.jitter_states[i]) - scapegoat_absorb + (0.12 * lost_child_isolate),
                0.0, 1.0
            )
            rewards["hero"] += float((1.0 - self.chaos_states[i]) + (0.2 if h_a == 1 else -0.1))
            rewards["scapegoat"] += float(-1.0 * (self.chaos_states[i] + (1.0 if s_a == 2 else 0.0)))
            rewards["lost_child"] += float(-0.25 * self.chaos_states[i] - (0.3 if l_a != 0 else 0.0))
            rewards["mascot"] += float((0.2 * (1.0 - self.chaos_states[i])) - (0.4 * self.jitter_states[i] if m_a == 3 else 0.0))
        done = self.current_step >= self.max_steps
        return self._build_graph(), rewards, done

class SimplifiedGCNLayer(nn.Module):
    def __init__(self, in_dim: int, out_dim: int):
        super().__init__()
        self.linear = nn.Linear(in_dim, out_dim)

    def forward(self, x, edge_index):
        num_nodes = x.size(0)
        adj = torch.eye(num_nodes)
        adj[edge_index[0], edge_index[1]] = 1.0
        deg = torch.sum(adj, dim=1)
        deg_inv_sqrt = torch.pow(deg, -0.5)
        deg_inv_sqrt[torch.isinf(deg_inv_sqrt)] = 0.0
        D_inv = torch.diag(deg_inv_sqrt)
        norm_adj = torch.mm(torch.mm(D_inv, adj), D_inv)
        return torch.relu(self.linear(torch.mm(norm_adj, x)))

class GraphQNetwork(nn.Module):
    def __init__(self, node_in_dim: int = 7, action_dim: int = 4):
        super().__init__()
        self.gcn1 = SimplifiedGCNLayer(node_in_dim, 16)
        self.gcn2 = SimplifiedGCNLayer(16, 16)
        self.out_head = nn.Linear(16, action_dim)

    def forward(self, x, edge_index):
        h = self.gcn1(x, edge_index)
        h = self.gcn2(x if h is None else h, edge_index)
        return self.out_head(h)

if __name__ == "__main__":
    np.random.seed(7)
    env = FamilyGraphEnvironment(num_families=3, max_steps=5)
    model = GraphQNetwork(node_in_dim=7, action_dim=4)
    X, edge_index = env.reset()
    q_values = model(X, edge_index)
    print("=== GRAPH EXECUTION VERIFICATION PROCESSED ===")
    print("Node count:", X.shape[0], "| edge count:", edge_index.shape[1], "| Q dims:", tuple(q_values.shape))

    # CHECK: does the graph actually do message passing? perturb one family's chaos, see if Q of a CONNECTED node in another family changes
    X2, ei = X.clone(), edge_index.clone()
    X2[0, 0] = 1.0  # family 0 hero chaos feature maxed
    with torch.no_grad():
        q2 = model(X2, ei)
    delta = (q2 - q_values).abs().max().item()
    print(f"max Q delta after perturbing ONE node's chaos feature: {delta:.5f} (0.0 would mean no information flows)")

    # CHECK: run a full env step loop with random policies
    actions = {"hero": [1, 0, 1], "scapegoat": [2, 0, 2], "lost_child": [0, 1, 0], "mascot": [3, 0, 3]}
    (X3, ei3), rew, done = env.step(actions)
    print(f"one step ok: chaos now {env.chaos_states.round(3)}, done={done}")
