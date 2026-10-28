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
