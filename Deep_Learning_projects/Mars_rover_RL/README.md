## Project Goal
This project demonstrates the implementation of a **Tabular Q-Learning** agent to solve a pathfinding and sequential decision-making problem. The agent is trained to navigate a custom $10 \times 10$ Martian grid to reach a research target, avoiding various obstacles (e.g. craters and uneven terrain) with maximum efficiency.

---

## Theoretical Background: Reinforcement Learning (RL)

This solution utilizes **Model-Free Reinforcement Learning**, meaning the agent learns the optimal behavior directly through trial and error, without needing a pre-programmed map of the environment.

It is specifically an **Off-Policy** method, meaning the agent learns the optimal value function, $\mathbf{Q(s, a)}$, regardless of the specific policy it is currently using to explore the environment (the $\epsilon$-greedy policy). This separation makes the learning process highly efficient.

### 1. The Learning Framework: Markov Decision Process (MDP)

The environment is mathematically modeled as an MDP. The agent follows a continuous learning loop:

1.  **State ($S$):** The agent observes its current position on the grid.
2.  **Action ($A$):** The agent performs a move (North, South, East, West).
3.  **Reward ($R$):** The environment returns a feedback signal (e.g., $+100$ for reaching the goal, $-1$ for movement).
4.  The environment transitions to a new state ($S'$).

The goal is to find a **Policy**, $\mathbf{\pi_(s)}, (the set of rules for actions) that maximizes the cumulative long-term reward.



### 2. The Algorithm: Q-Learning

The agent's policy is stored in a **Q-Table**, which is a look-up table storing the estimated maximum future reward ($\mathbf{Q(s, a)}$) for taking a specific action ($\mathbf{a}$) in a specific state ($\mathbf{s}$). The table is updated using the Q-Learning update rule (derived from the Bellman Equation).

The Q-table is updated using the Q-Learning update rule, which is derived from the **Bellman Equation**:

$$
Q(s, a) \leftarrow Q(s, a) + \alpha \left( R + \gamma \max_{a'} Q(s', a') - Q(s, a) \right)
$$

Here:
* $Q(s, a)$: The current estimate of the Q-value.
* $\alpha$: The **Learning Rate**.
* $R$: The immediate reward.
* $\gamma$: The **Discount Factor** which reduces the present value of future rewards, making immediate rewards more desirable.
* $\max_{a'} Q(s', a')$: The maximum predicted Q-value for the next state ($s'$).

### 3. The $\epsilon$-Greedy Policy (Exploration vs. Exploitation)

To ensure the agent finds the optimal path, it must balance two behaviors:

* **Exploitation:** Following the path it already knows is best (the maximum Q-value).
* **Exploration:** Trying new, potentially better paths it hasn't discovered yet.

This balance is managed by the **$\epsilon$ (epsilon)-greedy policy**:

| Behavior | Condition | Action Selection | Epsilon ($\epsilon$) Value |
| :--- | :--- | :--- | :--- |
| **Exploratory** | Probability $\mathbf{P} = \mathbf{\epsilon}$ | The agent chooses a **random** action. | $\epsilon = 1.0$ (Start of training) |
| **Greedy** | Probability $\mathbf{P} = 1 - \mathbf{\epsilon}$ | The agent chooses the action with the **highest Q-value**. | $\epsilon \to 0.01$ (End of training) |

As training progresses, the $\mathbf{\epsilon}$ value decays (`EPSILON_DECAY`), shifting the agent from being fully exploratory to mostly greedy, allowing the policy to converge.

---

## Implementation Details
* **Environment:** Custom 10x10 GridWorld defined in NumPy.
* **Algorithm:** Tabular Q-Learning.
* **Libraries:** Python, NumPy.

## Author

[Vanya Fernandez Galabo]