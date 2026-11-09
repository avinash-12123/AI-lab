import random

def conflicts(board):
    count = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count


def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[j] == i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def hill_climbing():

    while True:

        board = [random.randint(0, 7) for _ in range(8)]

        while True:

            current = conflicts(board)

            if current == 0:
                print("Solution Found!")
                print_board(board)
                return

            best = current
            best_board = None

            for col in range(8):
                original = board[col]

                for row in range(8):
                    if row == original:
                        continue

                    board[col] = row
                    h = conflicts(board)

                    if h < best:
                        best = h
                        best_board = board.copy()

                board[col] = original

            if best_board is None:
                break

            board = best_board


hill_climbing()
