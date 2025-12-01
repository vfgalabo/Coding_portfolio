# Mars Rover Reinforcement Learning Agent
# This script implements a Q-Learning agent to navigate a Mars Rover in a grid environment.
# The rover must avoid obstacles and reach a designated research target.
import numpy as np
import random
import time

# --- 1. Mars Rover Grid Environment Definition ---
GRID_SIZE = 10
NUM_STATES = GRID_SIZE * GRID_SIZE
NUM_ACTIONS = 4 # North, South, East, West (discreet actions)

# Define the grid layout (0=safe, 1=obstacle, 2=goal)
# This is a simplified 10x10 map
# R=Row, C=Column
MAP = np.zeros((GRID_SIZE, GRID_SIZE))

# Define obstacles - set some cells to 1
MAP[2:4, 4] = 1
MAP[6, 2:5] = 1
MAP[8, 8] = 1

# Goal (Research Target) - set one cell to 2 to represent the goal
GOAL_POS = (9, 9)
MAP[GOAL_POS] = 2

# Initial Start Position
START_POS = (0, 0)

# Initialize the Q-table (States x Actions)
q_table = np.zeros((NUM_STATES, NUM_ACTIONS))

print("Environment: Mars Rover Grid")
print(f"Grid Size: {GRID_SIZE}x{GRID_SIZE}")
print(f"State Space Size: {NUM_STATES}")
print(f"Action Space Size: {NUM_ACTIONS}")
print(f"Goal Position: {GOAL_POS}")

# --- Helper function to convert (row, col) to a single state index ---
def state_to_index(r, c):
    return r * GRID_SIZE + c

# --- Helper function to get the state and reward after an action ---
def take_action(current_r, current_c, action):
    # Action mapping: 0:North(-R), 1:South(+R), 2:East(+C), 3:West(-C)
    
    new_r, new_c = current_r, current_c
    # Wrap around logic for grid boundaries: Prevent the agent from going off the grid
    if action == 0: new_r = max(0, current_r - 1)               # to move North, we substract 1 from the row index (current_r - 1), preventing it from going below 0 with MAX
    elif action == 1: new_r = min(GRID_SIZE - 1, current_r + 1) # to move South, we add 1 to the row index (current_r + 1), preventing it from exceeding GRID_SIZE - 1 with MIN
    elif action == 2: new_c = min(GRID_SIZE - 1, current_c + 1)
    elif action == 3: new_c = max(0, current_c - 1)

    # If the new position is an obstacle, keep the rover in the old position
    if MAP[new_r, new_c] == 1:
        new_r, new_c = current_r, current_c 

    # Determine Reward
    reward = -1 # Cost for movement
    terminated = False

    if (new_r, new_c) == GOAL_POS:
        reward = 100
        terminated = True
    elif MAP[new_r, new_c] == 1: # Hitting an obstacle (if not blocked above)
        reward = -10
        
    next_state = state_to_index(new_r, new_c)
    
    return next_state, reward, terminated, new_r, new_c

# --- Global tracking variables (needed for the training loop) ---
# Define the same hyperparameters
NUM_EPISODES = 20000    # Total episodes for training
MAX_STEPS = 100         # Max steps per episode
LEARNING_RATE = 0.7     # alpha to control how much new info overrides old
DISCOUNT_FACTOR = 0.618 # discount factor gamma to which reduces the present value of future rewards, making immediate rewards more desirable
EPSILON_START = 1.0     # Initial exploration rate (Agent will be fully exploratory at the start)
EPSILON_END = 0.01      # Agent is mostly exploitative at the end
EPSILON_DECAY = 0.999   # Decay rate per episode

## --- 2. Training the Q-Learning Agent (Mars Rover) ---

epsilon = EPSILON_START
print("\n--- Starting Mars Rover Training ---")

for episode in range(NUM_EPISODES):
    # Reset the environment (State = Start Position)
    current_r, current_c = START_POS
    state = state_to_index(current_r, current_c)
    done = False
    
    for step in range(MAX_STEPS):
        # 1. Choose Action: Epsilon-Greedy Strategy (same as before)
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, NUM_ACTIONS - 1) 
        else:
            action = np.argmax(q_table[state]) 
            
        # 2. Take Action and Observe Result (Custom function)
        next_state, reward, terminated, current_r, current_c = take_action(current_r, current_c, action)
        done = terminated 
        
        # 3. Update Q-Table (Bellman Equation - same as before)
        old_q = q_table[state, action]
        max_future_q = np.max(q_table[next_state])
        
        new_q = old_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_future_q - old_q)
        q_table[state, action] = new_q
        
        state = next_state
        
        if done:
            break
            
    # 4. Decay Epsilon (Reduce Exploration)
    epsilon = max(epsilon * EPSILON_DECAY, EPSILON_END)
    
    if (episode + 1) % 5000 == 0:
        print(f"Episode {episode + 1}/{NUM_EPISODES} completed. Epsilon: {epsilon:.4f}")

print("--- Training Complete ---")

## --- 3. Testing and Visualizing the Trained Agent ---

# Load the Q-table (The agent's policy)
try:
    q_table = np.load("mars_rover_q_table.npy")
    print("\n--- Loaded Trained Q-Table for Testing ---")
except FileNotFoundError:
    # If the training loop hasn't run yet, use the Q-table trained in Section 2
    print("\nQ-Table file not found. Testing immediately after training.")

# Create a clean map visualization function
def visualize_path(r, c, path_map):
    display_map = np.copy(path_map)
    display_map[r, c] = 5 # Mark current rover position with '5'
    
    symbols = {
        0: '.',  # Safe spot
        1: 'X',  # Obstacle
        2: 'G',  # Goal
        5: 'R'   # Rover
    }
    
    # Convert the numerical map to a readable string representation
    map_str = "\n".join([" ".join([symbols[int(cell)] for cell in row]) for row in display_map])
    print("\n" * 50) # Clear console for visualization effect
    print(map_str)

# --- Test Run Execution ---
current_r, current_c = START_POS
state = state_to_index(current_r, current_c)
done = False
total_reward = 0
steps = 0

print("\n--- Starting Visualization Run ---")
time.sleep(1) 

while not done and steps < MAX_STEPS:
    # Visualize the current state
    visualize_path(current_r, current_c, MAP)

    # Select the GREEDY action (the best action based on the trained Q-table)
    action = np.argmax(q_table[state])
    
    # Execute the action
    next_state, reward, terminated, current_r, current_c = take_action(current_r, current_c, action)
    
    total_reward += reward
    state = next_state
    done = terminated
    steps += 1
    time.sleep(0.1) # Pause to make visualization readable

# Final visualization on the goal or failure state
visualize_path(current_r, current_c, MAP)

if done and (current_r, current_c) == GOAL_POS:
    print(f"\nSUCCESS! Mars Rover reached the goal in {steps} steps.")
else:
    print(f"\nFAILURE. Max steps reached ({MAX_STEPS}) or stuck in obstacle.")

print(f"Total reward achieved: {total_reward}")
# Save the final Q-table (overwriting the previous save)
np.save("mars_rover_q_table.npy", q_table)
print("Q-Table saved.")