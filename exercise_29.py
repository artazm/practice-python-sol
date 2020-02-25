# Tic Tac Toe Game

def print_horizontal(n):
    i = 0
    while i < n:
        print(' ---', end = '')
        i += 1
    print('\n')

def print_vertical(game, row, n):
    j = 0
    while j < n:
        if game[row][j] == 0:
            print('|   ', end = '')
        else:
            print('| {} '.format(str(game[row][j])), end = '')
        j += 1
    print('|\n')

def draw(game, n):
    i = 0
    while i < n:
        print_horizontal(n)
        print_vertical(game, i, n)
        i += 1
    print_horizontal(n)

def check_win(game):
    winner = ''
    matrix_1 = game[0]
    matrix_2 = game[1]
    matrix_3 = game[2]

    # Winner in one row
    # 1st row
    if matrix_1[0] == matrix_1[1] == matrix_1[-1]:
        winner = matrix_1[0]

    # 2nd row
    if matrix_2[0] == matrix_2[1] == matrix_2[-1]:
        winner = matrix_2[0]

    # 3rd row
    if matrix_3[0] == matrix_3[1] == matrix_3[-1]:
        winner = matrix_3[0]

    # Winner in one column
    # 1st column
    if matrix_1[0] == matrix_2[0] == matrix_3[0]:
        winner = matrix_1[0]

    # 2nd column
    if matrix_1[1] == matrix_2[1] == matrix_3[1]:
        winner = matrix_1[1]

    # 3rd column
    if matrix_1[2] == matrix_2[2] == matrix_3[2]:
        winner = matrix_1[2]

    # Winner in diagonal
    if matrix_1[0] == matrix_2[1] == matrix_3[-1]:
        winner = matrix_1[0]
    if matrix_1[-1] == matrix_2[1] == matrix_3[0]:
        winner = matrix_1[-1]
    return winner

def valid_move(game):
    matrix_1 = game[0]
    matrix_2 = game[1]
    matrix_3 = game[2]
    valid = True
    for i in matrix_1:
        if i == 0:
            valid = True
            break
        elif i != 0:
            valid = False
    for i in matrix_2:
        if i == 0:
            valid = True
            break
        elif i != 0:
            valid = False
    for i in matrix_3:
        if i == 0:
            valid = True
            break
        elif i != 0:
            valid = False
    return valid

def play(game, turn):
    if (turn % 2) != 0:
        # Player 1
        move_1 = input('Where do you want to put the piece Player 1 (in the format "row,column")? ')
        move_1 = move_1.split(',')
        row = int(move_1[0])
        col = int(move_1[1]) - 1
        if row == 1:
            game[0][col] = 'X'
        elif row == 2:
            game[1][col] = 'X'
        elif row == 3:
            game[2][col] = 'X'
        else:
            print('Invalid Input')
    elif (turn % 2) == 0:
        # Player 2
        move_2 = input('Where do you want to put the piece Player 2 (in the format "row,column")? ')
        move_2 = move_2.split(',')
        row = int(move_2[0])
        col = int(move_2[1]) - 1
        if row == 1:
            game[0][col] = 'O'
        elif row == 2:
            game[1][col] = 'O'
        elif row == 3:
            game[2][col] = 'O'
        else:
            print('Invalid Input')

if __name__ == '__main__':
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    turn = 1
    valid = valid_move(game)
    draw(game, 3)
    while valid:
        play(game, turn)
        turn += 1
        draw(game, 3)
        valid = valid_move(game)
        winner = check_win(game)
        if winner == 'O' or winner == 'X':
            valid = False
            break
    if winner == '0' or winner == '':
        print("It's a draw!")
    elif winner == 'X':
        print('Player 1 wins. Congratulations!')
    elif winner == 'O':
        print('Player 2 wins. Congratulations!')
