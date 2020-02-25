# Guessing Game One

import random

a = random.randint(1, 9)
print(a)

count = 0
guess = int(input('Guess the number: '))
count += 1

while (True):
    if guess < a:
        print('Too low!')
    elif guess > a:
        print('Too high!')
    else:
        print('You got it!')
        break
    count += 1
    guess = int(input('Guess the number: '))
if (count == 1):
    print('You got it in the first try!')
else:
    print('It takes you ' + str(count) + ' times to get it right.')
