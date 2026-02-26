### Tic-Tac-Toe
### Creating the rows & numbering them
board = []
num = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(num)
        num += 1
    board.append(row)
    

### Giving space 5 the X value
board[1] = [4, "X", 6]

### Naming rows
row_1 = board[0]
row_2 = board[1]
row_3 = board[2]


## Creating dictionary for position mapping
position_map = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


### Creating the board
def display_board(board):
    horizontal_line = "+-------+-------+-------+"
    for row in board:
        print(horizontal_line)
        print("|       |       |       |")
        print(f"|  {row[0]:^3}  |  {row[1]:^3}  |  {row[2]:^3}  |")
        print("|       |       |       |")
    print(horizontal_line)


###Creating User input
def enter_move(board):
    while True:
        try:
            user_turn = int(input("Enter you space number here 1-9: "))
        except ValueError:
            print("Please enter a number between 1-9.")
            continue
    
        if user_turn in position_map:
            row, col = position_map[user_turn]

            if isinstance(board[row][col], int):
                board[row][col] = "O"
                break
            else:
                print("That space is already taken.")
        else:
            print("Invalid number! Please enter 1-9.")


### Creating CPU input
from random import randrange

def draw_move(board):
    while True:
        cpu_move = randrange(1, 10)
        row, col = position_map[cpu_move]

        if isinstance(board[row][col], int):
                board[row][col] = "X"
                print(f"CPU chose space {cpu_move}")
                break
            

### Creating End Game Options
def victory_for(board):
    ###checking rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    ###checking columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    ###checking diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    ###checking for tie
    empty_spaces = any(isinstance(cell, int) for row in board for cell in row)
    if not empty_spaces:
        return "Tie"
    ###no winner yet
    return None

display_board(board)
while True:
    enter_move(board)
    display_board(board)
    winner = victory_for(board)
    if winner:
        break
    draw_move(board)
    display_board(board)
    winner = victory_for(board)
    if winner:
        break

if winner == "X":
    print("CPU wins!")
elif winner == "O":
    print("You win!")
elif winner == "Tie":
    print("It's a tie!")  