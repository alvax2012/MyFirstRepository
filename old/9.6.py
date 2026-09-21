import math
print(__name__)


def top_grade(grades):
    pass


info = {'name': 'Timur', 'grades': [30, 57, 99]}

print(top_grade(info))


l = [1, 2]

l1 = [l]*2

print(id([0]*2), id([1]*2))
x = math.sqrt(16)
print(x)


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step = step % len(numbers)
    p = numbers[-step:]
    del numbers[-step:]
    numbers[0:0] = p


numbers = [1, 2, 3, 4, 5]
#  cyclic_shift(numbers, 2)
# print(numbers)


# numbers = [234, 33, 4, 6, 2, 4, 75, 34, 1, 3, 6, 3, 3]
# numbers = [*range(1, 14)]
# cyclic_shift(numbers, 7)
# print('[75, 34, 1, 3, 6, 3, 3, 234, 33, 4, 6, 2, 4]')
# print(numbers)
# [75, 34, 1, 3, 6, 3, 3, 234, 33, 4, 6, 2, 4]

numbers = [234, 235]
cyclic_shift(numbers, 15)
print(numbers)


l = [2, 3]
l[:] = [777]
print(id(l) == id(l[:]))


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    d = {}
    for i in range(1, len(matrix)+1):
        d[i] = matrix[i-1]
    return d


matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))
