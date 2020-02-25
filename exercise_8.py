# Rock Paper Scissors
play = input('Play Rock Paper Scissors? (Y/N): ')
if (play == 'N' or play == 'n'):
    print('Maybe Next Time.')
else:
    while (True):
        player_1 = input('Player 1 command: ')
        player_2 = input('Player 2 command: ')

        if (player_1 == player_2):
            print('Draw')
        elif (player_1 == 'rock' and player_2 == 'scissors'):
            print('Player 1 win')
        elif (player_1 == 'rock' and player_2 == 'paper'):
            print('Player 2 win')
        elif (player_1 == 'paper' and player_2 == 'rock'):
            print('Player 1 win')
        elif (player_1 == 'paper' and player_2 == 'scissors'):
            print('Player 2 win')
        elif (player_1 == 'scissors' and player_2 == 'rock'):
            print('Player 2 win')
        elif (player_1 == 'scissors' and player_2 == 'paper'):
            print('Player 1 win')
        else:
            print('Invalid')
        play = input('Keep playing? (Y/N): ')
        if (play == 'n' or play == 'N'):
            print('See you again.')
            break
