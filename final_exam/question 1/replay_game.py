import json
import os
from Tic_Tac_Toe_Master import create_board, display_board, place_move, clear_screen


def replay_game() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "last_game.json")
    with open(json_path, "r") as f:
        game_data = json.load(f)
    

    moves = game_data["moves"]
    winner = game_data["winner"]
#this satisifes the invariant that X must always go first 
    board = create_board()
    x_moves = True

    clear_screen()
    display_board(board)
    print("Starting position. Press Enter to begin replay.")
    input()
#Because python is 0 based the moves 1-9 need to be converted to 0-8 
    for move in moves:
        index = move - 1
        place_move(board, index, x_moves)

        clear_screen()
        display_board(board)

        if x_moves:
            print("X played square " + str(move))
        else:
            print("O played square " + str(move))

        print("Press Enter for next move...")
        input()

        x_moves = not x_moves

    clear_screen()
    display_board(board)

    if winner == "TIE":
        print("The game ended in a tie.")
    else:
        print(winner + " won the game.")


replay_game()