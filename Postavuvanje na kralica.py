from collections import deque
import os

def is_valid(new_state, new_queen_i, new_queen_j):
    vertical_check = new_queen_j not in new_state
    if not vertical_check:
        return False
    main_diagonal = new_queen_i - new_queen_j
    anti_diagonal = new_queen_i + new_queen_j
    other_queens = new_state[:N - new_state.count(None)]
    for other_queen_i, other_queen_j in enumerate(other_queens):
        if other_queen_i - other_queen_j == main_diagonal:
            return False
        if other_queen_i + other_queen_j == anti_diagonal:
            return False
    return True

def expand_state(state):
    new_states = []
    available_places = state.count(None)
    if not available_places:
        return []
    new_queen_i = N - available_places
    for new_queen_j in range(N):
        if is_valid(state, new_queen_i, new_queen_j):
            new_state = list(state)
            new_state[new_queen_i] = new_queen_j
            new_states.append(tuple(new_state))
    return new_states

def search(initial_state, alg):
    visited = {initial_state}
    states_queue = deque([initial_state])
    while states_queue:
        state_to_expand = states_queue.popleft()
        for next_state in expand_state(state_to_expand):
            if next_state not in visited:
                if next_state.count(None) == 0:
                    return next_state
                visited.add(next_state)
                if alg == 'dfs':
                    states_queue.appendleft(next_state)
                elif alg == 'bfs':
                    states_queue.append(next_state)

def visualise_queens(queens):
    import numpy as np
    import skimage
    from skimage import io

    if not queens:
        print('Не постои реше.astype(np.uint8)ние за N =', N)
        return
    border_color = (0, 0, 0, 1)
    queen = skimage.img_as_float(io.imread('../code/images/queen.png'))
    table = np.zeros((queen.shape[0] * N, queen.shape[1] * N, queen.shape[2]))
    margin = queen.shape[0] // 20
    for i, j in enumerate(queens):
        table[i*queen.shape[0]:(i+1)*queen.shape[0], j*queen.shape[1]:(j+1)*queen.shape[1]] = queen
    for index in range(1, N):
        table[index * queen.shape[0] - margin: index * queen.shape[0] + margin] = border_color
        table[:, index * queen.shape[1] - margin: index * queen.shape[1] + margin] = border_color
    image_directory = 'queens'
    os.makedirs(f'images/{image_directory}', exist_ok=True)
    io.imsave(f'images/{image_directory}/{N}.png', 255*table.astype(np.uint8))
    return f'Погледни ја сликата images/{image_directory}/{N}.png'

N = 8
initial_state = (None,) * N
queens = search(initial_state, alg='dfs')