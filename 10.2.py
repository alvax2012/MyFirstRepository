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


def starmap(func, iterable):
    return map(func,  *[list(i) for i in zip(*iterable)])


pairs = [(1, 3), (2, 5), (6, 4)]

print(*starmap(lambda a, b: a + b, pairs))

print(*map(lambda a, b: a + b, (1, 3), (2, 5)))

print([list(i) for i in zip(*pairs)])

print()


def get_min_max(iterable):
    mi, ma = 0, 0
    res = iter(iterable)
    try:
        mi = next(res)
        ma = mi
    except StopIteration:
        return

    for i in res:
        if i < mi:
            mi = i
        if i > ma:
            ma = i

    return mi, ma


iterable = iter(range(10))

print(get_min_max(iterable))

iterable = iter([])

print(get_min_max(iterable))

# data = iter(range(100_000_000))
# print(get_min_max(data))

i = iter([1, 2, 3])
print(*map(lambda x: x, i))
