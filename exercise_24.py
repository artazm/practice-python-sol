# Draw A Game Board

def print_horizontal(n):
    i = 0
    while i < n:
        print(' ---', end = '')
        i += 1
    print('\n')

def print_vertical(game, row, n):
    j = 0
    while j < n:
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

#size = int(input('Size of the game board? '))
game = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
draw(game, 3)
