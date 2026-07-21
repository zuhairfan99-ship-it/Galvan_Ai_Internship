# Tic-Tac-Toe with AI
import math
def print_board(board):
    print()
    for i in range(3):
        row = [board[i * 3 + j] for j in range(3)]
        print(" " + " | ".join(row))
        if i < 2:
            print("-----------")
    print()
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_full(board):
    return " " not in board
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
def get_best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
def main():
    board = [" "] * 9
    print("Welcome to Tic-Tac-Toe! You are 'X', AI is 'O'.")
    print_board([str(i + 1) for i in range(9)])
    human = "X"
    ai = "O"
    while True:
        while True:
            try:
                move = int(input("Choose your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == " ":
                    board[move] = human
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number from 1 to 9.")
        print_board(board)
        if check_winner(board, human):
            print("Congratulations! You won!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        print("AI is making a move...")
        ai_move = get_best_move(board)
        board[ai_move] = ai
        print_board(board)
        if check_winner(board, ai):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    main()