import random
import numpy as np
from utils import get_available_points


def choose(this_game_map: np.ndarray):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    return random.choice(choices)
