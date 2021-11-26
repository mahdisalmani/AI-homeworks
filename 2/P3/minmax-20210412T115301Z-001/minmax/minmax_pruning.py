from utils import *
import numpy as np
import math


def get_chooser(depth):
    def temp(this_game_map: np.ndarray):
        return choose(this_game_map, depth, -np.inf, -np.inf)[1]

    return temp


def choose(this_game_map: np.ndarray, depth, alpha, beta):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))

    if depth == 0:
        return (get_two_side_score(this_game_map), None)
    
    best = (-np.inf, None)
    for choice in choices:
        new = (calculate_score_next_move(this_game_map, choice, depth, alpha, beta), choice)
        if -new[0] < beta:
            return new
        alpha = max(alpha, new[0])
        if best[0] < new[0]:
            best = new
    return best


def calculate_score_next_move(this_game_map: np.ndarray, next_move, depth, alpha, beta):
    this_game_map[next_move] = 1
    (score, opponent_move) = choose(-this_game_map.copy(), depth - 1, beta, alpha)
    this_game_map[next_move] = 0
    return -score