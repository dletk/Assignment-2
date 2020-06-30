# Assignment 2, Tic Tac Toe
# Name: Mai Anh Nguyen

import random # import the module random

# Global variables
winner = None

game_in_progress = True

user_position = None 

current_player = None

board_positions = ["1,1", "1,2", "1,3", "2,1", "2,2", "2,3", "3,1", "3,2", "3,3"]

# set up the board
row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]

board = [row1, row2, row3]

# Choose X or O - for user and computer
user_move = input("Choose your type of move (X or O): ")

if user_move == "X":
    computer_move = "O"
else:
    computer_move = "X"

print("User, you are " + user_move + ". Computer, you are " + computer_move  + ". LET'S PLAY!")

# Play game Tic Tac Toe
def play_game(player1):
    
    # show the initial board
    show_board()

    # Create a loop that keeps the game to play until it is over
    while game_in_progress:
        response(player1)
        check_game_over()
        player1 = switch_player() # switch the player

    # Print the result when game is over
    if winner == user_move:
        print("Winner is the user!")
    elif winner == computer_move:
        print("Winner is the computer!")
    elif winner == None:
        print("There is a tie!")

# Show the game board
def show_board():
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "    1,1 | 1,2 | 1,3")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "    2,1 | 2,2 | 2,3")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "    3,1 | 3,2 | 3,3")
    print()

# List the cases that the game is over
# Check the rows 
def check_rows():
    global game_in_progress

    # Check if any of the rows are not empty and have the same values
    check_row1 = board[0][0] == board[0][1] == board[0][2] != "_"
    check_row2 = board[1][0] == board[1][1] == board[1][2] != "_"
    check_row3 = board[2][0] == board[2][1] == board[2][2] != "_"

    # Find the row winner
    if check_row1 or check_row2 or check_row3:
        game_in_progress = False
    if check_row1:
        return board[0][0]
    elif check_row2:
        return board[1][0]
    elif check_row3: 
        return board[2][0]
    else:
        return None # no winner

# Check the columns
def check_columns():
    global game_in_progress

    # Check if any of the columns are not empty and have the same values
    column1 = board[0][0] == board[1][0] == board[2][0] != "_"
    column2 = board[0][1] == board[1][1] == board[2][1] != "_"
    column3 = board[0][2] == board[1][2] == board[2][2] != "_"

    # Find the column winner
    if column1 or column2 or column3:
        game_in_progress = False
    if column1:
        return board[0][0]
    elif column2:
        return board[0][1]
    elif column3: 
        return board[0][2]
    else:
        return None # no winner

# Check the diagonals
def check_diagonals():
    global game_in_progress

    # Check if any of the diagonals are not empty and have the same values
    diagonal1 = board[0][0] == board[1][1] == board[2][2] != "_"
    diagonal2 = board[0][2] == board[1][1] == board[2][0] != "_"

    # Find the diagonal winner
    if diagonal1 or diagonal2:
        game_in_progress = False
    if diagonal1:
        return board[0][0]
    elif diagonal2:
        return board[0][2]
    else:
        return None # no winner

# Check for a tie
def check_tie():
    global game_in_progress

    # If the board has no available space
    if "_" not in row1 and "_" not in row2 and "_" not in row3:
        game_in_progress = False
        return True
    else:
        return False

# Find the winner
def find_winner():
    global winner
    global game_in_progress

    # Check if there is a winner in one of the 3 following cases
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

def check_game_over():
    find_winner()
    check_tie()
 
# Get the response from computer or user
def response(player):
    global user_move
    global computer_move

    valid_input = False

    while not valid_input:
        if player is user_move:
            # User enter their move by type in the terminal, with the format: X,Y
            position = input("Enter your move with the format: X,Y (with X,Y is the coordiate of the move on the 3x3 board): ")

            comma_position = position.find(",") # find the position of comma in the move typed in the terminal
            row_number = int(position[ : comma_position]) - 1 # find the row number
            column_number = int(position[comma_position + 1 : ]) - 1 # find the column number

            # The game tells the user if a move is invalid, and ask for the input again.
            while not (column_number <=2 and 0 <= column_number and row_number <=2 and 0 <= row_number):
                position = input("Enter your move with the format: X,Y (with X,Y is the coordiate of the move on the 3x3 board): ")

            # If the move typed in is available
            if board[row_number][column_number] == "_":
                valid_input = True
                board[row_number][column_number] = user_move
            else:
                print("This position is already filled. Please choose another one!")
                position = input("Enter your move with the format: X,Y (with X,Y is the coordiate of the move on the 3x3 board): ")
        else: 
            # if player is computer, it will randomly choose a cell.
            row_random = random.randint(0,2) 
            column_random = random.randint(0,2)

            # Check if the random cell is available
            if board[row_random][column_random] == "_":
                board[row_random][column_random] = computer_move
                valid_input = True
            
        # Print out to the console (the terminal) the current state of the board after each move
        show_board()

# Switch the player
def switch_player():
    global current_player

    # If the current player was user, make it computer
    if current_player == user_move:
        current_player = computer_move
    # Or if the current player was computer, make it user
    else:
        current_player = user_move
    
    return current_player

# Ask whether the user want to play first or second (answer Y/N in the terminal)
user_answer = input("Do you want to play first or second (Answer Y or N)? ").lower()  

if user_answer == "y":
    current_player = user_move
    play_game(user_move)
else:
    current_player = computer_move
    play_game(computer_move)

# DONEEEEEEEEEEEE 






