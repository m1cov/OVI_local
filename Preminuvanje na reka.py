#Фармерот треба да пренесе волк, коза и зелка преку река. Меѓутоа, фармерот може да земе само едно од овие три нешта со себе во чамецот.
#Постојат одредени правила кои мора да ги следи за да не се случи несакана ситуација на брегот

def is_valid_state(state):
    """Check if the current state is valid."""
    farmer, goat, wolf, cabbage = state
    # Wolf and goat left alone
    if farmer != wolf and wolf == goat:
        return False
    # Goat and cabbage left alone
    if farmer != goat and goat == cabbage:
        return False
    return True

def get_possible_moves(state):
    """Generate all possible valid moves from the current state."""
    farmer, goat, wolf, cabbage = state
    moves = []
    # Farmer moves alone
    new_state = (1 - farmer, goat, wolf, cabbage)
    if is_valid_state(new_state):
        moves.append(new_state)
    # Farmer takes goat
    if farmer == goat:
        new_state = (1 - farmer, 1 - goat, wolf, cabbage)
        if is_valid_state(new_state):
            moves.append(new_state)
    # Farmer takes wolf
    if farmer == wolf:
        new_state = (1 - farmer, goat, 1 - wolf, cabbage)
        if is_valid_state(new_state):
            moves.append(new_state)
    # Farmer takes cabbage
    if farmer == cabbage:
        new_state = (1 - farmer, goat, wolf, 1 - cabbage)
        if is_valid_state(new_state):
            moves.append(new_state)
    return moves

def dfs(state, goal_state, path, visited):
    """Perform DFS to find a solution."""
    if state == goal_state:
        return path
    visited.add(state)
    for next_state in get_possible_moves(state):
        if next_state not in visited:
            result = dfs(next_state, goal_state, path + [next_state], visited)
            if result:
                return result
    visited.remove(state)
    return None

# Initial and goal states
initial_state = (1, 0, 0, 1)
goal_state = (1, 1, 1, 1)

# Perform DFS
solution = dfs(initial_state, goal_state, [initial_state], set())
if solution:
    print("Solution path:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
