from random import choice


def random_numbers(left, right):
    return iter(lambda: choice(list(range(left, right)) if left != right else [left, right]), None)


iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))


iterator = random_numbers(5, 5)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
