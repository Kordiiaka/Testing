from functools import reduce
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]

sum = reduce(lambda x, y: x + y, list_1)
print(sum)

