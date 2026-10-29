numbers = [4, 8, 15, 16, 23, 42]

iterator = iter(numbers)              # создаем итератор на основе списка

print(15 in iterator)
# print(23 in iterator)

x, *y = iterator
print(x, y)


numbers = iter([1, 2, 3, 4, 5])

print(max(numbers), list(numbers))


positive = iter((1, 2, 3))
negative = map(lambda x: -x, positive)

for a, b in zip(positive, negative):
    print(a + b)


def filterfalse(predicate, iterable):
    if not predicate:
        return filter(lambda x: not x, iterable)

    return filter(lambda x: not predicate(x), iterable)


objects = [0, 1, True, False, 17, []]

print(*filterfalse(None, objects))


def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)

print(*zip('12', '34'))

matrix = [['1', '2'],
          ['4', '5'],
          ['7', '8'],
          ['3', 4],
          [True, None],
          [9, 80],
          [1, -1]]

print(transpose(matrix))

data = [2, 3, 8, 1, 7]

print()


def get_min_max(data):
    l = list(enumerate(data))
    if data:
        return min(l, key=lambda x: x[1])[0], max(l, key=lambda x: x[1])[0]


data = [2, 3, 8, 1, 7]
data = [9, 9, 9, 9, 9]
print(get_min_max(data))
