
import heapq

def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return distance

def solvable(initial, goal):
    a = [x for x in initial if x != 0]
    b = [x for x in goal if x != 0]
    inv_a = sum(a[i] > a[j] for i in range(8) for j in range(i + 1, 8))
    inv_b = sum(b[i] > b[j] for i in range(8) for j in range(i + 1, 8))
    return inv_a % 2 == inv_b % 2

def solve(initial, goal):
    pq = [(heuristic(initial, goal), 0, initial)]
    parent = {initial: None}
    moves = {}
    cost = {initial: 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        if state == goal:
            path = []
            while state is not None:
                path.append((state, moves.get(state, "Start")))
                state = parent[state]
            return path[::-1]

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for dr, dc, move in [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]:
            r, c = row + dr, col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                j = r * 3 + c
                new_state = list(state)
                new_state[zero], new_state[j] = new_state[j], new_state[zero]
                new_state = tuple(new_state)
                new_cost = g + 1

                if new_cost < cost.get(new_state, float("inf")):
                    cost[new_state] = new_cost
                    parent[new_state] = state
                    moves[new_state] = move
                    heapq.heappush(
                        pq,
                        (new_cost + heuristic(new_state, goal),
                         new_cost, new_state)
                    )

    return None

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
        print("The goal state is not reachable from the initial state.")
        return

    path = solve(initial, goal)

    if path is None:
        print("No solution found.")
        return

    print("\nSolution found in", len(path) - 1, "moves\n")

    for step, (state, move) in enumerate(path):
        print("Step", step, "-", move)
        display(state)

if __name__ == "__main__":
    main()
