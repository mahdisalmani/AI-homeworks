import numpy as np

MAP_SIZE = 20
STEPS = 20
CENTER = MAP_SIZE // 2 - 0.5
original_game_map = np.zeros([MAP_SIZE] * 2, np.int)
original_game_map[0, int(CENTER - 2)] = 1
original_game_map[0, int(CENTER + 2)] = -1

available_points_kernel = np.array([[False, False, False],
                                    [True, False, True],
                                    [False, True, False]])

score_kernel = np.array([[1000, 0, 0, 0, 1000],
                         [0, 0, 10, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 10, 0, 0],
                         [1000, 0, 0, 0, 1000]])
