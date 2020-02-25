# Check Tic Tac Toe

# 0 = empty square
def check_win(game):
    winner = ''
    matrix_1 = game[0]
    matrix_2 = game[1]
    matrix_3 = game[2]

    # Winner in one row
    # 1st row
    if matrix_1[0] == matrix_1[1] == matrix_1[-1]:
        winner = str(matrix_1[0])

    # 2nd row
    if matrix_2[0] == matrix_2[1] == matrix_2[-1]:
        winner = str(matrix_2[0])

    # 3rd row
    if matrix_3[0] == matrix_3[1] == matrix_3[-1]:
        winner = str(matrix_3[0])

    # Winner in one column
    # 1st column
    if matrix_1[0] == matrix_2[0] == matrix_3[0]:
        winner = str(matrix_1[0])

    # 2nd column
    if matrix_1[1] == matrix_2[1] == matrix_3[1]:
        winner = str(matrix_1[1])

    # 3rd column
    if matrix_1[2] == matrix_2[2] == matrix_3[2]:
        winner = str(matrix_1[2])

    # Winner in diagonal
    if matrix_1[0] == matrix_2[1] == matrix_3[-1]:
        winner = matrix_1[0]
    if matrix_1[-1] == matrix_2[1] == matrix_3[0]:
        winner = matrix_1[-1]
    return winner

if __name__ == '__main__':
    game = [[1, 2, 1],
        [2, 1, 2],
        [1, 1, 0]]

    winner = check_win(game)
    if winner == '0' or winner == '':
        print('No winner')
    else:
        print(winner)
