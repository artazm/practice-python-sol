# Fibonacci

def fibonacci():
    n = int(input('How many Fibonacci numbers to generate: '))
    i = 1
    if n == 0:
        a = []
    elif n == 1:
        a = [1]
    elif n == 2:
        a = [1, 1]
    elif n > 2:
        a = [1, 1]
        while i < (n - 1):
            a.append(a[i] + a[i-1])
            i += 1
    return a

print(fibonacci())
