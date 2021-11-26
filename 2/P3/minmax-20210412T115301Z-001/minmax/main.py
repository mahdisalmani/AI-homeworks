from random_client import choose as random_choose
from minmax_original import get_chooser as original_minmax
from minmax_pruning import get_chooser as pruning_minmax
import time
from matplotlib import pyplot as plt
from utils import *


# %%
def contest(client1, client2, this_game_map: np.ndarray):
    scores = []
    client1_delay, client2_delay = 0, 0
    for i in range(STEPS):
        available_points = get_available_points(this_game_map)
        t0 = time.time()
        client1_choice = client1(this_game_map.copy())
        client1_delay = max(client1_delay, time.time() - t0)
        if not available_points[client1_choice]:
            return -1, scores, client1_delay, client2_delay
        this_game_map[client1_choice] = 1

        available_points = get_available_points(-this_game_map)
        t0 = time.time()
        client2_choice = client2(-this_game_map.copy())
        client2_delay = max(client2_delay, time.time() - t0)
        if not available_points[client2_choice]:
            return 1, scores, client1_delay, client2_delay
        this_game_map[client2_choice] = -1

        scores.append(get_two_side_score(this_game_map))

    score = get_two_side_score(this_game_map)
    if score > 0:
        return 1, scores, client1_delay, client2_delay
    elif score < 0:
        return -1, scores, client1_delay, client2_delay
    else:
        return 0, scores, client1_delay, client2_delay


# %%
def print_contest_result(result):
    final_result, scores, client1_delay, client2_delay = result
    print('Result:', final_result, '  Client1_Delay:', int(1000 * client1_delay) / 1000, '  Client2_Delay:',
          int(1000 * client2_delay) / 1000)
    plt.plot(scores)
    plt.show()


# %%
print_contest_result(contest(random_choose, random_choose, original_game_map.copy()))

print_contest_result(contest(random_choose, original_minmax(1), original_game_map.copy()))
print_contest_result(contest(random_choose, pruning_minmax(1), original_game_map.copy()))
print_contest_result(contest(original_minmax(1), pruning_minmax(1), original_game_map.copy()))

print_contest_result(contest(random_choose, original_minmax(2), original_game_map.copy()))
print_contest_result(contest(random_choose, pruning_minmax(2), original_game_map.copy()))
print_contest_result(contest(original_minmax(2), pruning_minmax(2), original_game_map.copy()))

print_contest_result(contest(random_choose, original_minmax(3), original_game_map.copy()))
print_contest_result(contest(random_choose, pruning_minmax(3), original_game_map.copy()))
print_contest_result(contest(original_minmax(3), pruning_minmax(3), original_game_map.copy()))

print_contest_result(contest(pruning_minmax(4), pruning_minmax(3), original_game_map.copy()))