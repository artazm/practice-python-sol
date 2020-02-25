# Pick Word
import random

def pick_word():
    with open('sowpods.txt', 'r') as f:
        words = list(f)
    pick = random.choice(words).strip()
    return pick

def check_end(g_letter, incorrect):
    if '_' in g_letter and incorrect > 0:
        return True
    return False

def end_message(count_try):
    if count_try <= 8:
        print('You only need {} tries to guess the answer. Incredible!'.format(count_try))
    elif count_try <= 15:
        print('It took {} tries for you to get the answer. Good Job.'.format(count_try))
    else:
        print('{} tries. You can do better than that!'.format(count_try))


if __name__ == '__main__':
    g_letter = [] # List for guessed letter
    g_answer = ' ' # String for guessed letter
    history = []
    check = True
    answer = pick_word()
    count_try = 0
    incorrect = 6

    for i in list(answer):
        g_letter.append('_')

    print('Welcome to Hangman!')
    print(g_answer.join(g_letter))
    while check:
        guess = input('\nGuess a letter: ')
        guess = guess.upper()
        count_try += 1

        # Make user guess another letter if it's already guessed before
        while guess in history:
            guess = input('Try another letter, you have guessed this letter before. ')
            guess = guess.upper()
            count_try += 1
        history.append(guess)

        # Check whether user guessed the correct letter, if correct print the new sentence, display message if incorrect
        if guess in answer:
            for index, value in enumerate(answer):
                if value == guess:
                    g_letter[index] = value
            print(g_answer.join(g_letter))
        else:
            print('Incorrect!')
            incorrect -= 1
        check = check_end(g_letter, incorrect)
    if incorrect == 0:
        print('Better luck next time!')
        print('The answer is ' + answer)
    else:
        end_message(count_try)

