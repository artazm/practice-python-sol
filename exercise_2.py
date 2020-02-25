# Odd or Even

num = int(input('Check number: '))
check = int(input('Divide number: '))

if (num % check) == 0:
    print('{} divides evenly into {}.'.format(check, num))
else:
    print('{} is not a multiplier of {}.'.format(num, check))
#if (num % 4) == 0:
#    print('{} is a  Multiplier of 4.'.format(str(num)))
#elif (num % 2) == 0:
#    print('{} is a Even number.'.format(str(num)))
#else:
#    print('{} is a Odd number.'.format(str(num)))
