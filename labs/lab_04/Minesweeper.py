import random
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def get_inputs():
    # Get board height (2-10)
    try:
        height = int(input("\nBoard height (2 - 10) : "))
    except ValueError:
        height = 0
    while height < 2 or height > 10:
        try:
            height = int(input("Please enter board height (2 -10) : "))
        except ValueError:
            print("You must enter an integer (2 - 10) : ")
    
    # Get board width (2-10)
    try:
        width = int(input("Board width (2 - 10) : "))
    except ValueError:
        width = 0
    while width < 2 or width > 10:
        try:
            width = int(input("Please enter board width (2 -10) : "))
        except ValueError:
            print("You must enter an integer (2 - 10)")
    
    # Get number of mines
    total = width * height
    try:
        mines = int(input("How many mines (less then " + str(total) + ") : "))
    except ValueError:
        mines = -1
    while mines < 0 or mines >= total:
        try:
            mines = int(input("Invalid number of mines, please re-enter : )"))
        except ValueError:
            print("You must enter a whole number")
    
    return height, width, mines

def create_board(height, width):
    board = []
    for row in range(height):
        board.append([])
        for col in range(width):
            board[row].append("♦")
    return board

def place_mines(board, height, width, num_mines):
    placed = 0
    while placed < num_mines:
        row = random.randrange(height)
        col = random.randrange(width)
        if board[row][col] != "💣":
            board[row][col] = "💣"
            placed += 1


def print_board(board, height, width, reveal=False):
    # Print column numbers
    header = "    "
    for col in range(width):
        header += " " + str(col) + "   "
    print(header)
    
    # Print separator line
    print("    " + "- - - " * width + "-")
    
    for row in range(height):
        line = "  " + str(row) + " "
        for col in range(width):
            cell = board[row][col]
            if reveal:
                if cell == "💣":
                    line += "| 💣 "
                elif cell == "♦":
                    line += "|    "
                else:
                    line += "| " + str(cell) + "  "
            else:
                line += "| ♦  "
            line += "|"
        print(line)
        print("    " + "- - - " * width + "-")

def count_adjacent(board, row, col, height, width):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r >= 0 and r < height and c >= 0 and c < width:
                if board[r][c] == "💣":
                    count += 1
    return count

def calculate_numbers(board, height, width):
    for row in range(height):
        for col in range(width):
            if board[row][col] != "💣":
                num = count_adjacent(board, row, col, height, width)
                if num > 0:
                    board[row][col] = num

# Run the game
height, width, mines = get_inputs()
board = create_board(height, width)
place_mines(board, height, width, mines)
calculate_numbers(board, height, width)

# Game loop
while True:
    try:
        col = int(input("\nHow many over would you like to dig? : "))
    except (ValueError, Exception):
        print("pleasse enter a valid integer : ")
        continue
    while col < 0 or col >= width:
        try:
            col = int(input("please enter an integer between 0 and " + str(width - 1) + " : "))
        except (ValueError, Exception):
            print("pleasse enter a valid integer : ")

    try:
        row = int(input("How many down would you like to dig? : "))
    except (ValueError, Exception):
        print("pleasse enter a valid integer : ")
        continue
    while row < 0 or row >= height:
        try:
            row = int(input("please enter an integer between 0 and " + str(height - 1) + " : "))
        except (ValueError, Exception):
            print("pleasse enter a valid integer : ")

    # Check what's at that cell
    if board[row][col] == "💣":
        print("Uh Oh, you hit a mine, You Lost...")
        print_board(board, height, width, reveal=True)
        break
    else:
        board[row][col] = "v"
        print_board(board, height, width, reveal=True)
        print("Congratulations! You won.")
        break