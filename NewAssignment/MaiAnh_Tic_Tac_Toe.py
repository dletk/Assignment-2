import random

winner = None

game_in_progress = True

user_position = None 

# Choose X or O - for user and computer
user_move = input("Choose your type of move (X or O): ")
computer_move = None

if user_move == "X":
    computer_move = "O"
else:
    computer_move = "X"

print("User, you are " + user_move + ". Computer, you are " + computer_move  + ". LETS PLAY!")

def play_game():
    
    user_answer = input("Do you want to play first or second (Answer Y or N)? ")  

    show_board()
    print()

    while game_in_progress:
        if user_answer == "Y":
            user_response()
            computer_response()
        else:
            computer_response()
            user_response()
            
    if winner == user_move:
        print("Winner is the user!")
    elif winner == computer_move:
        print("Winner is the computer!")
    elif winner == None:
        print("There is a tie!")

# set up the board
row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

board = [row1, row2, row3]

def show_board():
    print(row1[0] + " | " + row1[1] + " | " + row1[2] + "    1,1 | 1,2 | 1,3")
    print(row2[0] + " | " + row2[1] + " | " + row2[2] + "    2,1 | 2,2 | 2,3")
    print(row3[0] + " | " + row3[1] + " | " + row3[2] + "    3,1 | 3,2 | 3,3")

def find_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# list cases that the game is over
# Check the rows 
def check_rows():
    global game_in_progress

    #Check if any of the rows are not empty and have the same values
    check_row1 = row1[0] == row1[1] == row1[2] != "-"
    check_row2 = row2[0] == row2[1] == row2[2] != "-"
    check_row3 = row3[0] == row3[1] == row3[2] != "-"

    if check_row1 or check_row2 or check_row3:
        game_in_progress = False
    if check_row1:
        return row1[0]
    elif check_row2:
        return row2[0]
    elif check_row3: 
        return row3[0]
    else:
        return None # no winner

# Check the columns
def check_columns():
    global game_in_progress

    column1 = row1[0] == row2[0] == row3[0] != "-"
    column2 = row1[1] == row2[1] == row3[1] != "-"
    column3 = row1[2] == row2[2] == row3[2] != "-"

    if column1 or column2 or column3:
        game_in_progress = False
    if column1:
        return row1[0]
    elif column2:
        return row1[1]
    elif column3: 
        return row1[2]
    else:
        return None # no winner

# Check the diagonals
def check_diagonals():
    global game_in_progress

    diagonal1 = row1[0] == row2[1] == row3[2] != "-"
    diagonal2 = row1[2] == row2[1] == row3[0] != "-"

    if diagonal1 or diagonal2:
        game_in_progress = False
    if diagonal1:
        return row1[0]
    elif diagonal2:
        return row1[2]
    else:
        return None # no winner

# Check for a tie
def check_tie():
    global game_in_progress

    if "-" not in row1 and "-" not in row2 and "-" not in row3:
        game_in_progress = False
        return True
    else:
        return False

 
# Who plays first?
def user_response():

    position2 = input("Enter your move with the format: X,Y (with X,Y is the coordiate of the move on the 3x3 board): ")
    response(position2, user_move)

def computer_response():

    position3 = random.choice(["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"])
    response(position3, computer_move)

def response(position, move):
    valid_input = False

    number = None

    while not valid_input:
        while position not in ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]:
            position = input("Enter your move with the format: X,Y (with X,Y is the coordiate of the move on the 3x3 board): ")
        
        number = int(position[-1]) - 1

        if position == "1,1" or position == "1,2" or position == "1,3":
            row1[number] = move
        elif position == "2,1" or position == "2,2" or position == "2,3":
            row2[number] = move
        elif position == "3,1" or position == "3,2" or position == "3,3":
            row3[number] = move

        if row1[number] == "_" or row2[number] == "_" or row3[number] == "_":
            valid_input = True
        else:
            print("This position is already filled. Please choose another one!")

    show_board()
    print()

play_game()








