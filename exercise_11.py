# Check Primality Function

def get_integer(help_text = 'Give me a number: '):
    return int(input(help_text))

def is_prime(number):
    if int(number) <= 1:
        print(str(number) + ' not a prime number.')
    else:
        x = [elements for elements in range(2, int(number)) if number % elements == 0]
        if (len(x) == 0):
            print(str(number) + ' is a prime number.')
        else:
            print(str(number) + ' is not a prime number and can be divided by ' + str(x))

num = get_integer('Please enter a number: ')

is_prime(num)

