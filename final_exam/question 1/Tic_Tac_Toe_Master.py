"""
TIC TAC TOE - FUNCTION SCAFFOLD

Lab 2 (tictactoe) is due Monday March 9th, 2026

Board Representation Rules:
- Board is a list of 9 integers.
- 1-9  ? open squares
- 10   ? X
- -10  ? O

Winning rule:
- Any row, column, or diagonal that sums to:
    30   ? X wins
   -30   ? O wins


Assume:
- X plays first
- X is human
-O is computer
"""
import json
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

import time
def pause(n=None):
    if n is None:
        input("Press Enter to continue...")
    else:
        time.sleep(n)

def create_board() -> list[int]:
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board(board: list[int]) -> None:
    def cell(value: int) -> str:
        if value == 10: return 'X'
        elif value == -10: return 'O'
        else: return str(value)

    print()
    for row in range(3):
        row_values = []
        for col in range(3):
            value = cell(board[row * 3 + col])
            row_values.append(value)

        print('   |   |   ')
        print(f' {row_values[0]} | {row_values[1]} | {row_values[2]} ')
        print('   |   |   ')
        if row < 2:
            print('-----------')
    print()


def check_tie(board: list[int]) -> bool:
    for space in board:
        if space >= 1 and space <= 9:
            return False
    return True


def check_winner(board: list[int]) -> str | None:
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        total = board[a] + board[b] + board[c]
        if total == 30:
            return 'X'
        elif total == -30:
            return 'O'
    return None


def game_over(board: list[int]) -> str | None:
    winner = check_winner(board)
    if winner is not None:
        return winner
    if check_tie(board):
        return 'TIE'
    return None


def get_human_move() -> str:
    move = input("Choose a square (1-9): ")
    return move


import random
def get_computer_move(board: list[int]) -> int:
    open_squares = []
    for space in board:
        if space >= 1 and space <= 9:
            open_squares.append(space)
    return random.choice(open_squares)


def is_valid_move(board: list[int], move: str) -> tuple[bool, int | None]:
    try:
        move_int = int(move)
    except ValueError:
        return (False, None)

    if move_int < 1 or move_int > 9:
        return (False, None)

    index = move_int - 1

    if board[index] == 10 or board[index] == -10:
        return (False, None)

    return (True, index)


def place_move(board: list[int], index: int, x_moves: bool) -> None:
    if x_moves:
        board[index] = 10
    else:
        board[index] = -10

#moves_played[] this keeps a list of every move played in the game so that we can get last_game.json
def play_game() -> None:
    board = create_board()
    x_moves = True
    moves_played = []

    while True:
        clear_screen()
        display_board(board)

        if x_moves:
            move = get_human_move()
        else:
            print("Computer thinking...")
            pause(1)
            move = str(get_computer_move(board))

        is_valid = is_valid_move(board, move)

        if not is_valid[0]:
            print("Invalid move. Try again.")
            continue

        place_move(board, is_valid[1], x_moves)
        moves_played.append(int(move))

        status = game_over(board)

        if status:
            clear_screen()
            display_board(board)

            if status == "TIE":
                print("The game is a tie.")
            else:
                print(status + " wins the game")
#game_data stores all the moves along with who's the winner. I elected not to save the order of the moves since it's a given that X goes first 
            game_data = {"moves": moves_played, "winner": status}
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir, "last_game.json")
            with open(json_path, "w") as f:
                json.dump(game_data, f)

            break

        x_moves = not x_moves

#this ensures the game copies to the json file correctly 
#I actually had an error where because it said play_game() the game would run before the replay so I added this 
if __name__ == "__main__":
    play_game()