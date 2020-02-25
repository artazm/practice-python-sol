# Max of Three

def max_of(a, b, c):
    max_num = a
    if max_num < b:
        max_num = b
    if max_num < c:
        max_num = c
    return max_num

if __name__ == '__main__':

    print(max_of(30,200,1))
