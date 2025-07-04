import random


def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "


def take_turn(board, player):
    row, col = map(int, input(
        f"Player {player}, enter row and column (0-2): ").split())
    while not is_valid_move(board, row, col):
        print("Invalid move. Try again.")
        row, col = map(int, input(
            f"Player {player}, enter row and column (0-2): ").split())

    board[row][col] = player
    print_board(board)


def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def is_board_full(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))


def play_game():
    board = initialize_board()
    current_player = "X"

    while True:
        take_turn(board, current_player)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


play_game()
