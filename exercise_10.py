# List Overlap Comprehensions

a = [1, 1, 1, 1, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [element_a for element_a in a if element_a in b]


print(c)
