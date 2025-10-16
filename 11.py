def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc


def add_sqr(x, y):
    return x**2 + y**2

# 319563


numbers = [97, 42]

print(reduce(add_sqr, numbers, 0))
