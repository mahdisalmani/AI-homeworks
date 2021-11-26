from utils import *
import numpy as np
import math


def get_chooser(depth):
    def temp(this_game_map: np.ndarray):
        return choose(this_game_map, depth)[1]

    return temp


def choose(this_game_map: np.ndarray, depth):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))

    if depth == 0:
        return (get_two_side_score(this_game_map), None)
    
    best = (-np.inf, None)
    for choice in choices:
        new = (calculate_score_next_move(this_game_map, choice, depth), choice)
        if best[0] < new[0]:
            best = new
    return best


def calculate_score_next_move(this_game_map: np.ndarray, next_move, depth):
    this_game_map[next_move] = 1
    (score, opponent_move) = choose(-this_game_map.copy(), depth - 1)
    this_game_map[next_move] = 0
    return -score