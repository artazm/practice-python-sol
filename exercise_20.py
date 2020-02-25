# Search Element Using Binary Search

def BinSearch(num, sort_list):
    left = 0
    right = len(sort_list) - 1
    while True:
        if num == sort_list[left] or num == sort_list[right]:
            return True
            break
        mid = int((right + left) / 2)
        if mid >= right or mid <= left or mid <= 0:
            return False
            break
        if num > sort_list[mid]:
            left = mid
        elif num < sort_list[mid]:
            right = mid
        elif num == sort_list[mid]:
            return True



if __name__ == '__main__':
    a = [1, 3, 5, 30, 42, 43, 500]
    while True:
        num = int(input('Search element: '))
        exist = BinSearch(num, a)
        if exist:
            print('{} is in the list.'.format(num))
        else:
            print('{} is not exist in the list.'.format(num))
