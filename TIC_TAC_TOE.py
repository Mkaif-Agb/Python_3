import random


def display_board(board):
    print("\n"*100)
    print('  | |')
    print(' ' + board[7]+'|' + board[8]+'|'+board[9] + ' ')
    print('  | |')
    print('--------')
    print(' '+ board[4] + '|' + board[5] + '|' + board[6]+ ' ')
    print('  | |')
    print('--------')
    print('  | |')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3]+ ' ')
    print('  | |')


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, Choose X or O: ").upper()
    player1 = marker
    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# player1.marker , player2.marker =player_input()
# print(player2.marker)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    return (board[1] == mark and board[2] == mark and board[3] == mark) \
            or (board[4] == mark and board[5] == mark and board[6] == mark)\
            or (board[7] == mark and board[8] == mark and board[9] == mark)\
            or (board[7] == mark and board[4] == mark and board[1] == mark) \
            or (board[8] == mark and board[5] == mark and board[2] == mark) \
            or (board[3] == mark and board[6] == mark and board[9] == mark) \
            or (board[7] == mark and board[5] == mark and board[3] == mark) \
            or (board[9] == mark and board[5] == mark and board[1] == mark)

def choose_first():

    flip = random.randint(0,1)
    if flip == 0:
        print("Player 1 Plays First.")
    else:
        print("Player 2 Plays First")


def space_check(board,position):
    return board[position]== ' '


def full_board_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board,position):
        position = int(input("Enter The Position"))
    return position



def replay():
    choice = input("Type Yes if u want to play again or No if u dont want to play")
    return choice == "Yes"

# ------------------------------------------------------------------------------------------------------------ #
# -------------------------------------------CODE IMPLEMENTATION---------------------------------------------- #


print("WELCOME TO TIC TAC TOE")
turn = ''

while True:

    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    choose_first()
    play = input("Are you ready to play the game, Enter Y or N: ")
    if play.upper() == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has Won the Game")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player 2"

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has Won the Game")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():

        break
