#Скратено: имате на располагање 3 садови. Нивниот капацитет е (x, y, z) соодветно. Почетната состојба е (x_0, y_0, z_0).
# Задачата е да стигнете до посакуваната состојба.

from collections import deque
from itertools import combinations

def transfer_to_other_glass(source, sink, sink_capacity):
    return max(source - (sink_capacity - sink), 0), min(sink + source, sink_capacity)


def expand_state(state):
    capacities = (5, 8, 10)
    glass_0, glass_1, glass_2 = state

    new_states = []

    if glass_0 < capacities[0]:
        new_states.append((capacities[0], glass_1, glass_2))
    if glass_1 < capacities[1]:
        new_states.append((glass_0, capacities[1], glass_2))
    if glass_2 < capacities[2]:
        new_states.append((glass_0, glass_1, capacities[2]))

    if glass_0 > 0:
        new_states.append((0, glass_1, glass_2))
    if glass_1 > 0:
        new_states.append((glass_0, 0, glass_2))
    if glass_2 > 0:
        new_states.append((glass_0, glass_1, 0))

    new_source, new_sink = transfer_to_other_glass(glass_0, glass_1, capacities[1])
    new_states.append((new_source, new_sink, glass_2))

    new_source, new_sink = transfer_to_other_glass(glass_1, glass_0, capacities[0])
    new_states.append((new_sink, new_source, glass_2))

    new_source, new_sink = transfer_to_other_glass(glass_0, glass_2, capacities[2])
    new_states.append((new_source, glass_1, new_sink))

    new_source, new_sink = transfer_to_other_glass(glass_2, glass_0, capacities[0])
    new_states.append((new_sink, glass_1, new_source))

    new_source, new_sink = transfer_to_other_glass(glass_1, glass_2, capacities[2])
    new_states.append((glass_0, new_source, new_sink))

    new_source, new_sink = transfer_to_other_glass(glass_2, glass_1, capacities[1])
    new_states.append((glass_0, new_sink, new_source))

    return new_states

def search_path(initial_state, goal_state):
    visited = {initial_state}
    states_queue = deque([[initial_state]])
    while states_queue:
        states_list = states_queue.popleft()
        state_to_expand = states_list[-1]
        for next_state in expand_state(state_to_expand):
            if next_state not in visited:
                if next_state == goal_state:
                    return states_list + [next_state]
                visited.add(next_state)
                states_queue.append(states_list + [next_state])
    return []

def visualise_path(path):
    for states in zip(path, path[1:]):
        old_state, new_state = states
        print(old_state)
        print(tuple(map(lambda x, y: x - y, new_state, old_state)), 'change')
        print(new_state)
        print()


initial_state = (5, 8,3)
goal_state = (1, 0, 0)
path = search_path(initial_state, goal_state)
visualise_path(path)