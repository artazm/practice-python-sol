# Divisors

num = int(input('Please enter a number: '))

x = range(2, num)
y = []

for elements in x:
    if (num % elements) == 0:
        y.append(elements)

print(str(num) + ' can be divided by ' + str(y))
