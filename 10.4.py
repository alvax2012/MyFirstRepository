numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

del numbers[4]

print(list(iterator))


numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

del numbers[0]
del numbers[0]

print(next(iterator), numbers)
