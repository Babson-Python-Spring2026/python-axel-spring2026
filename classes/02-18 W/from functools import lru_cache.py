from functools import lru_cache

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diags
]

def winner(board: str):
    """Return 'X' or 'O' if there is a winner, else None."""
    for a, b, c in WIN_LINES:
        if board[a] != "." and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board: str) -> bool:
    return "." not in board

@lru_cache(None)
def terminal_boards(board: str, player: str):
    """
    Return a frozenset of all DISTINCT terminal boards reachable
    from (board, player) under legal play, stopping immediately on a win.
    """
    w = winner(board)
    if w is not None or is_full(board):
        return frozenset([board])

    next_sets = []
    for i, cell in enumerate(board):
        if cell == ".":
            new_board = board[:i] + player + board[i+1:]
            next_player = "O" if player == "X" else "X"
            next_sets.append(terminal_boards(new_board, next_player))

    # Union all reachable terminal boards
    out = set()
    for s in next_sets:
        out.update(s)
    return frozenset(out)

def count_terminal_positions():
    finals = terminal_boards("." * 9, "X")

    x_wins = 0
    o_wins = 0
    draws  = 0

    for b in finals:
        w = winner(b)
        if w == "X":
            x_wins += 1
        elif w == "O":
            o_wins += 1
        else:
            draws += 1

    return len(finals), x_wins, o_wins, draws

if __name__ == "__main__":
    total, xw, ow, dr = count_terminal_positions()
    print("Distinct terminal boards (no symmetry reduction):", total)
    print("X wins:", xw)
    print("O wins:", ow)
    print("Draws :", dr)