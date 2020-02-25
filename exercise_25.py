# Guessing Number Two
import random

answer = random.randint(0, 100)
answer_list = list(range(0, 101))

count_try = 0
left = 0
right = len(answer_list) - 1
mid = int((right + left) / 2)
my_guess = answer_list[mid]

print("Let's Start! Think of a number between 0 to 100. %s" %str(answer))
mark = input('Is this your number? {} (1 : Correct, 2 : Too High, 3 : Too Low)'.format(my_guess))
count_try += 1

while mark != '1':
    if mark == '2':
        right =  mid
    elif mark == '3':
        left = mid
    mid = int((right + left) / 2)
    my_guess = answer_list[mid]
    mark = input('Is this your number? {} (1 : Correct, 2 : Too High, 3 : Too Low)'.format(my_guess))
    count_try += 1

if count_try <= 2:
    print("Yes! It only took me %s try!" % str(count_try))
elif count_try <= 10:
    print("Pretty well for a robot, %s tries." % str(count_try))
else:
    print("That's so bad, %s tries." % str(count_try))
