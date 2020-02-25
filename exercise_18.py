# Cows and Bulls

import random

def cows_bulls(num, ans):
    num_list = [int(x) for x in str(num)]
    ans_list = [int(y) for y in str(ans)]

    count_cow = 0
    count_bull = 0

    for index_ans, value_ans in enumerate(ans_list):
        for index_num, value_num in enumerate(num_list):
            if index_num == index_ans and value_num == value_ans:
                count_cow += 1
            elif index_num != index_ans and value_num == value_ans:
                count_bull += 1
    if count_bull > 1 and count_cow > 1:
        print('{} cows, {} bulls.'.format(count_cow, count_bull))
    elif count_bull <= 1 and count_cow > 1:
        print('{} cows, {} bull.'.format(count_cow, count_bull))
    elif count_bull > 1 and count_cow <= 1:
        print('{} cow, {} bulls.'.format(count_cow, count_bull))
    elif count_bull <= 1 and count_cow <= 1:
        print('{} cow, {} bull.'.format(count_cow, count_bull))

if __name__=='__main__':
    answer = random.randint(1000, 10000)
    print(answer)
    count = 0
    user_guess = int(input('Please enter a number: '))
    count += 1
    cows_bulls(user_guess, answer)
    while user_guess != answer:
        user_guess = int(input('Please enter a number: '))
        count += 1
        cows_bulls(user_guess, answer)

    print('Congratulations, you got the answer in {} attempt(s)!'.format(count))

