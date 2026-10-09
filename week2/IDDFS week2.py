
def dls(state, goal, depth, path, visited):
    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new_state = list(state)
            new_state[zero], new_state[j] = new_state[j], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                result = dls(new_state, goal, depth - 1,
                             path + [(new_state, move)], visited)
                if result is not None:
                    return result
                visited.remove(new_state)

    return None

def iddfs(initial, goal, max_depth=50):
    for depth in range(max_depth + 1):
        visited = {initial}
        result = dls(initial, goal, depth, [(initial, "Start")], visited)

        if result is not None:
            return result

    return None

def solvable(initial, goal):
    a = [x for x in initial if x != 0]
    b = [x for x in goal if x != 0]

    inv_a = sum(a[i] > a[j] for i in range(8) for j in range(i + 1, 8))
    inv_b = sum(b[i] > b[j] for i in range(8) for j in range(i + 1, 8))

    return inv_a % 2 == inv_b % 2

def display(state):
    for i in range(0, 9, 3):
        print(*[" " if x == 0 else x for x in state[i:i + 3]])
    print()

def main():
    initial = tuple(map(int, input("Enter initial state (0 for blank): ").split()))
    goal = tuple(map(int, input("Enter goal state (0 for blank): ").split()))

    if len(initial) != 9 or len(goal) != 9:
        print("Enter exactly 9 numbers for each state.")
        return

    if set(initial) != set(range(9)) or set(goal) != set(range(9)):
        print("Each state must contain numbers 0 to 8 exactly once.")
        return

    if not solvable(initial, goal):
        print("Puzzle is unsolvable.")
        return

    result = iddfs(initial, goal)

    if result is None:
        print("No solution found within the depth limit.")
    else:
        print("Solution found in", len(result) - 1, "moves:\n")

        for step, (state, move) in enumerate(result):
            print("Step", step, "-", move)
            display(state)

if __name__ == "__main__":
    main()
