
board = [" " for i in range(9)]

def display():
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")

def winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def minimax(is_computer):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if is_computer:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def computer_move():
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"
    print("Computer chooses position:", move + 1)

print("TIC-TAC-TOE")
print("You = X | Computer = O")
print("Positions:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

while True:
    display()

    try:
        move = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number.")
        continue

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid position! Try again.")
        continue

    board[move] = "X"

    if winner("X"):
        display()
        print("Congratulations! You win!")
        break

    if " " not in board:
        display()
        print("It's a draw!")
        break

    computer_move()

    if winner("O"):
        display()
        print("Computer wins!")
        break

    if " " not in board:
        display()
        print("It's a draw!")
        break
