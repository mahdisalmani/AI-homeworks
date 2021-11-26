from random import randint, random, uniform
import gym
import time
env = gym.make('MountainCar-v0')


def get_position_state(position):
    return round(position * 10) - round(env.observation_space.low[0] * 10)
def get_velocity_state(velocity):
    return round(velocity * 100) - round(env.observation_space.low[1] * 100)



num_velocity_state = get_velocity_state(env.observation_space.high[1]) + 1 
num_position_state = get_position_state(env.observation_space.high[0]) + 1 
Q_values = [[[uniform(-1, 1) for k in range(3)]for j in range(num_velocity_state)] for i in range(num_position_state)]


def episode_learning(Q_values, discount, epsilon, lr, learning=True):
    initial_state = env.reset()
    initial_state = [get_position_state(initial_state[0]), get_velocity_state(initial_state[1])]
    current_state = initial_state
    
    isTerminal = False
    total_reward = 0
        
    while isTerminal != True: 
        if not learning:
            env.render()
        p = random()
        if p < epsilon and learning:
            action = randint(0, 2)
        else:
            values = Q_values[current_state[0]][current_state[1]]
            action = values.index(max(values))
        
        [position, velocity], reward, isTerminal, _ = env.step(action)
        next_state = [get_position_state(position), get_velocity_state(velocity)]
        total_reward += reward
        if learning:
            if isTerminal and position >= 0.5:
                Q_values[current_state[0]][current_state[1]][action] = reward

            else:
                val = Q_values[next_state[0]][next_state[1]]
                sample = reward + discount * max(val)
                Q_values[current_state[0]][current_state[1]][action] = (1 - lr) * Q_values[current_state[0]][current_state[1]][action] + lr * sample

        current_state = next_state
    if learning:
        return Q_values
    else:
        return total_reward

def Q_learning(Q_values, discount, epsilon, lr, epsilon_lr, start_time):
    while time.time() - start_time < 15 * 60 - 1:
        Q_values = episode_learning(Q_values, discount, epsilon, lr)
        epsilon = epsilon * epsilon_lr
    return Q_values

starting_time = time.time()
Q_values = Q_learning(Q_values, 0.9, 0.8, 0.2, 0.9993, starting_time)

reward = 0
for i in range(100):
    reward += episode_learning(Q_values, 0.9, 0.8, 0.2, learning=False)
print(reward / 100)
