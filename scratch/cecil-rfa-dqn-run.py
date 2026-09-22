import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from collections import deque

class DynamicMARLFamilyEnv:
    """
    State: [env_chaos, systemic_denial, systemic_jitter]
    Actions: 0 = Passive/Drift, 1 = Hyper-Function, 2 = Absorb Loss, 3 = Inject Jitter
    """
    def __init__(self, max_steps: int = 50):
        self.max_steps = max_steps
        self.reset()

    def reset(self):
        self.current_step = 0
        self.env_chaos = 0.5
        self.systemic_denial = 0.1
        self.systemic_jitter = 0.1
        return self._get_state()

    def _get_state(self):
        return np.array([self.env_chaos, self.systemic_denial, self.systemic_jitter], dtype=np.float32)

    def step(self, agent_actions):
        self.current_step += 1
        h_act, s_act, l_act, m_act = agent_actions["hero"], agent_actions["scapegoat"], agent_actions["lost_child"], agent_actions["mascot"]
        intrinsic_trauma_generation = np.random.normal(0.10, 0.03)
        hero_stabilization = 0.35 if h_act == 1 else 0.0
        scapegoat_grounding = 0.50 if s_act == 2 else 0.0
        lost_child_withdrawal = 0.20 if l_act == 0 else -0.05
        mascot_noise = 0.30 if m_act == 3 else 0.0
        self.systemic_denial = 0.8 * self.systemic_denial + 0.2 * hero_stabilization
        self.systemic_jitter = 0.7 * self.systemic_jitter + 0.3 * mascot_noise
        self.env_chaos = np.clip(
            self.env_chaos + intrinsic_trauma_generation + (0.2 * self.systemic_denial)
            + (0.1 * self.systemic_jitter) - scapegoat_grounding + (0.15 * lost_child_withdrawal),
            0.0, 1.0
        )
        rewards = {
            "hero": float((1.0 - self.env_chaos) + (0.3 if h_act == 1 else -0.2)),
            "scapegoat": float(-1.0 * (self.env_chaos + (1.2 if s_act == 2 else 0.0))),
            "lost_child": float(-0.3 * self.env_chaos - (0.4 if l_act != 0 else 0.0)),
            "mascot": float((0.2 * (1.0 - self.env_chaos)) - (0.5 * self.systemic_jitter if m_act == 3 else 0.0))
        }
        done = self.current_step >= self.max_steps
        return self._get_state(), rewards, done

class QNetwork(nn.Module):
    def __init__(self, state_dim: int, action_dim: int):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 32), nn.ReLU(),
            nn.Linear(32, 32), nn.ReLU(),
            nn.Linear(32, action_dim)
        )
    def forward(self, x):
        return self.fc(x)

class DQNAgent:
    def __init__(self, state_dim: int, action_dim: int):
        self.action_dim = action_dim
        self.policy_net = QNetwork(state_dim, action_dim)
        self.target_net = QNetwork(state_dim, action_dim)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=1e-3)
        self.memory = deque(maxlen=2000)
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.05
        self.batch_size = 32

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.action_dim - 1)
        state_t = torch.FloatTensor(state).unsqueeze(0)
        with torch.no_grad():
            return int(torch.argmax(self.policy_net(state_t)).item())

    def store(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_step(self):
        if len(self.memory) < self.batch_size:
            return
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        states_t = torch.FloatTensor(np.array(states))
        actions_t = torch.LongTensor(actions).unsqueeze(1)
        rewards_t = torch.FloatTensor(rewards).unsqueeze(1)
        next_states_t = torch.FloatTensor(np.array(next_states))
        dones_t = torch.FloatTensor(dones).unsqueeze(1)
        current_q = self.policy_net(states_t).gather(1, actions_t)
        max_next_q = self.target_net(next_states_t).max(1)[0].unsqueeze(1)
        target_q = rewards_t + (0.95 * max_next_q * (1.0 - dones_t))
        loss = nn.MSELoss()(current_q, target_q)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def update_target(self):
        self.target_net.load_state_dict(self.policy_net.state_dict())

if __name__ == "__main__":
    torch.manual_seed(0); np.random.seed(0); random.seed(0)
    env = DynamicMARLFamilyEnv()
    agents = {name: DQNAgent(state_dim=3, action_dim=4) for name in ["hero", "scapegoat", "lost_child", "mascot"]}

    print("Training 20 episodes (doc's spec)...")
    for episode in range(20):
        state = env.reset()
        done = False
        while not done:
            actions = {name: agents[name].select_action(state) for name in agents}
            next_state, rewards, done = env.step(actions)
            for name in agents:
                agents[name].store(state, actions[name], rewards[name], next_state, done)
                agents[name].train_step()
            state = next_state
        if episode % 5 == 0:
            for name in agents:
                agents[name].update_target()
    print(f"final epsilon: {agents['hero'].epsilon:.3f}")

    # THE CHECK THE DUMP SKIPPED: it claims "Agents have converged to optimal internal roles."
    # Evaluate: greedy policies after training, 10 fresh episodes, averaged chaos + per-agent action distribution.
    print("\nEVAL: greedy policies, 10 episodes")
    chaos_finals = []
    action_counts = {n: [0,0,0,0] for n in agents}
    for ep in range(10):
        state = env.reset(); done = False
        while not done:
            actions = {}
            for name in agents:
                st = torch.FloatTensor(state).unsqueeze(0)
                with torch.no_grad():
                    a = int(torch.argmax(agents[name].policy_net(st)).item())
                actions[name] = a
                action_counts[name][a] += 1
            state, _, done = env.step(actions)
        chaos_finals.append(float(state[0]))
    print(f"mean final chaos: {sum(chaos_finals)/len(chaos_finals):.3f}")
    for name in agents:
        c = action_counts[name]
        print(f"{name:10s} greedy action distribution [drift, hyper, absorb, jitter]: {c}")

    # Compare against hand-picked role strategies (the doc's claim: agents DISCOVER these)
    print("\nHand-designed pathological policies, 10 episodes:")
    pol = {"hero": 1, "scapegoat": 2, "lost_child": 0, "mascot": 3}
    chaos_finals2 = []
    for ep in range(10):
        state = env.reset(); done = False
        while not done:
            state, _, done = env.step(pol)
        chaos_finals2.append(float(state[0]))
    print(f"mean final chaos: {sum(chaos_finals2)/len(chaos_finals2):.3f}")
    print("\nOptimal-ish per-agent greedy check (each agent alone vs env):")
    # what does each agent's Q say at a mid-range state?
    st = torch.FloatTensor([0.5, 0.1, 0.1]).unsqueeze(0)
    for name in agents:
        with torch.no_grad():
            q = agents[name].policy_net(st).numpy().round(3)
        print(f"{name:10s} Q at [0.5,0.1,0.1]: {q}")
