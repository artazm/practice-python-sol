# Tic Tac Toe Draw

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
    valid = valid_move(game)
    turn = 1
    while valid:
        play(game, turn)
        turn += 1
        valid = valid_move(game)
        for matrix in game:
            print(*matrix)
    print('No more valid move.')
