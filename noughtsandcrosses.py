#This is noughtsandcrosses.py module

import random  # built in function and import random 
from os.path import exists  # to check if a file exists or not in our computer
import json  # to load and store leaderboard
random.seed()  # seed


def draw_board(board):
    """
    This is draw_board function which prints
    out board in a 3x3 grid with dashes(-) and pipes(|).
    """
    print('-------------')  # prints top border of board
    for row in board:  # iterates over rows in board
        temp = '| '  # starts with a vertical line for the left border
        for mark in row:  # iterates over every mark in row
            temp += mark + ' | '  # adds the mark enclosed in vertical lines to the temp string
        print(temp)  # prints out the current row of the board
        print('-------------')  # prints out the border between rows



def welcome(board):
    """
    This is the welcome function and prints a blank board.
    """
    # Print welcome message and board layout
    print('''
Welcome to the "Unbeatable Noughts and Crosses" game
The board layout is shown below:''')
    draw_board(board)
    # Print instructions for user
    print('When prompted, enter the number of corresponding to the square you want.')


def initialise_board(board):
    """
    This is initialize_board function.
    Sets all elements to ' '.
    Returns board.
    """
    for i, row in enumerate(board):  # iterates over rows in board
        for j in range(len(row)):  # iterates over every mark in row
            board[i][j] = ' '
    return board


def get_player_move(board):
    """
    This is get_player_move function.
    Prompts user to input row and column number.
    Checks if user's choice is empty or not.
    Returns row and column.
    """
    print('''
                   00 01 02
                   10 11 12
Choose your square:20 21 22 : ''')
    user_choice_row, user_choice_column = '', ''
    while True:
        user_choice_row = input('Enter row: ')
        if not user_choice_row.isdigit():  # handles non numbers
            print('Invalid input. Enter a number.')
            continue
        if not 0 <= int(user_choice_row) < 3:  # handles all numbers except < 0 and >= 2
            print('Invalid input. Please type a number between (0-2)')
            continue
        while True:# loop run until the condition is true.
            user_choice_column = input('Enter column: ')
            if not user_choice_column.isdigit():  # handles non numbers
                print('Invalid input. Enter a number.')
                continue
            if not 0 <= int(user_choice_column) < 3:  # handles all numbers except < 0 and >= 2
                print('Invalid input. Please type a number between (0-2)')
            else:
                break
        break
    row = int(user_choice_row)  # conversion to digit
    col = int(user_choice_column)  # conversion to digit
    user_position = board[row][col]
    if not user_position == ' ':  # checks if user's choice is empty or not
        print('Please choose empty space')
        return None, None
    return row, col




def choose_computer_move(board):
    """
    This is choose_computer_move.
    Randomly generate computer's move in a list of all empty spaces.
    Return row and column.
    """
    empty_position = []  # create an empty list to store all the empty positions on the board
    board_length = len(board)  # get the length of the board
    for i in range(board_length):  # iterate over the rows of the board
        for j in range(board_length):  # iterate over the columns of the board
            if board[i][j] == ' ':  # if the space is empty
                empty_position.append([i, j])  # add the coordinates of the empty space to the empty_position list
    choice = random.choice(empty_position)  # randomly select an empty space from the list of empty spaces
    row = choice[0]  # get the row number of the chosen empty space
    col = choice[1]  # get the column number of the chosen empty space
    return row, col  # return the row and column number of the chosen empty space



def check_for_win(board, mark):
    """Check if the given mark has won the game by checking for winning patterns"""
    board_length = len(board) # Get the length of the board
    for i in range(board_length):  # iterate over rows
        row_win, col_win = True, True  # initialize row and column win variables to True
        for j in range(board_length):  # iterate over marks
            if board[i][j] != mark:  # If the mark is not present in the row i, set row_win to False
                row_win = False
            if board[j][i] != mark:  # If the mark is not present in the column i, set col_win to False
                col_win = False
        if row_win or col_win:  # If either row_win or col_win is True, return True
            return True
    diagonal1_win, diagonal2_win = True, True  # Initialize diagonal win variables to True
    for i in range(board_length):  # iterate over rows
        if board[i][i] != mark:  # If the mark is not present in the main diagonal, set diagonal1_win to False
            diagonal1_win = False
        if board[i][board_length - i - 1] != mark:  # If the mark is not present in the reverse diagonal, set diagonal2_win to False
            diagonal2_win = False
    if diagonal1_win or diagonal2_win:  # If either diagonal1_win or diagonal2_win is True, return True
        return True
    return False  # If no winning pattern is found, return False


def check_for_draw(board):
    """
    This is check_for_draw function.
    Checks for all mark and if any mark is ' '.
    Returns is_drawn.
    """
    for row in board:  # iterates over rows
        if ' ' in row:  # checks if mark is empty or not
            return False
    return True


def play_game(board):
    """
    This function is used to play the game and return the score.
    The score is 1 if the user wins, -1 if the computer wins, and 0 if the game is a draw.
    """
    did_player_input = False
    is_match_running = True
    board = initialise_board(board)  # initializes empty board with ' ' marks
    welcome(board)  # displays welcome message
    while is_match_running:
        while not did_player_input:
            player_row, player_column = get_player_move(board)  # call get_player_move function to get player's input
            if (player_row, player_column) == (None, None):  # if player's input is not taken
                continue
            board[player_row][player_column] = 'X'  # replace ' ' by 'X' at the player's position
            draw_board(board)  # draw current state of board
            break
        if check_for_win(board, 'X'):  # check if the player has won
            
            draw_board(board)  # draw current state of board
            print('Congratulation. You won')
            return 1
        if check_for_draw(board):  # check if the game is a draw
            draw_board(board)  # draw current state of board
            print('Its a draw')
            return 0
        computer_row, computer_column = choose_computer_move(board)  # get the computer's move
        board[computer_row][computer_column] = 'O'  # replace ' ' by 'O' at the computer's position
        print('''
Computer's move is''')
        draw_board(board)  # draw current state of board
        if check_for_win(board, 'O'):  # check if the computer has won
            print('Sorry you lost')
            draw_board(board)  # draw current state of board
            return -1
        if check_for_draw(board):  # check if the game is a draw
            draw_board(board)  # draw current state of board
            print('Its a draw')
            return 0


def menu():
    """
    menu function is used to choose option from user.
    there is option to user to enter 1, 2, 3, q.
    Calls other functions accordingly.
    """
    while True: # while will run until the condition is true
        user_choice = input('''
Enter one of the following options: 
    1 - Play the game
    2 - Save your score in the leaderboard
    3 - Load and display the leaderboard
    q - End the program
1, 2, 3, or q: ''')  # prompt user to input 1, 2, 3, q
        if user_choice.lower() in ('1', '2', '3', 'q'):
            return user_choice.lower()
        print('''
    Please print a valid mode''') # here else is not used because if loop block contain return statement




def load_scores():
    """
    This is load_scores function.
    Open leaderboard.txt file.
    Use loads function to load dictionary.
    """
    leaderboard = {}
    # check if the leaderboard file exists
    if not exists('leaderboard.txt'):
        # if it doesn't, create a new file and initialize the leaderboard as an empty dictionary
        print("\nLeaderboard does not exist. Creating a new leaderboard file.\n")
        with open('leaderboard.txt', 'w', encoding='utf-8') as new_file:
            json.dump({}, new_file)
    # open the leaderboard file and read its contents
    with open('leaderboard.txt', 'r', encoding='utf-8') as read_file:
        line = read_file.read()
    try:
        # convert the contents of the file into a dictionary using the json.loads function
        leaderboard = json.loads(line)
    except json.JSONDecodeError:
        # if the file does not have a JSON object, initialize the leaderboard as an empty dictionary
        with open('leaderboard.txt', 'w', encoding='utf-8') as write_file:
            json.dump({}, write_file)
    # return the leaderboard
    return leaderboard


def save_score(score):
    """
    here the function is save score.
    Prompt user to input name.
    Calls load_scores function to load all scores from the user.
    Updates dictionary in leaderboard.Opens leaderboard.txt on write mode
    Saves using dump function.
    """
    user_name = input('Enter your name: ').strip().lower()  # prompt user to enter name and lowercase it
    leaderboard = load_scores()  # call load_scores function to get dictionary with names and scores
    all_players = leaderboard.keys()  # get only the usernames from the dictionary
    if user_name in all_players:  # if user is already in leaderboard
        old_score = leaderboard[user_name]
        new_score = old_score + score  # calculate new score as the sum of old score and current score
        leaderboard[user_name] = new_score
    else:  # if user is not in leaderboard
        leaderboard[user_name] = score  # set new score for user in leaderboard
    with open('leaderboard.txt', 'w', encoding='utf-8') as write_file:  # open leaderboard file in write mode
        json.dump(leaderboard, write_file)  # write the leaderboard dictionary to the file
        print('\nSaved Successfully.')


def display_leaderboard(leaders):
    """
    This is display_leaderboard function.
    Displays all players  name as well as score in console.
    """
    print('''
======LEADERBOARD======
''')# print the header of leaderboard
    if leaders == {}:  # empty leaderboard
        print('No leaders yet')
    else:
        for names, scores in leaders.items():  # loops through all names and scores
            print(names, 'scored', scores)# it print the name and scored as well as new score.