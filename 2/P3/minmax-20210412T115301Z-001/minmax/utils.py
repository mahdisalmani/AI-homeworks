from scipy.ndimage import convolve
from configs import *


def get_available_points(this_game_map):
    full_points = (this_game_map != 0)
    my_points = (this_game_map == 1)
    return convolve(my_points, available_points_kernel) & ~full_points


def get_one_side_score(client_points):
    client_score_table = convolve(client_points, score_kernel, mode='constant') * client_points
    return np.sum(client_score_table)


def get_two_side_score(this_game_map):
    score_client1 = get_one_side_score(1 * (this_game_map == 1))
    score_client2 = get_one_side_score(1 * (this_game_map == -1))
    return score_client1 - score_client2
