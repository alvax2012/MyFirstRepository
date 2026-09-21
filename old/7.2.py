food = ['chocolate', 'chicken', 'corn', 'sandwich',
        'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        fifth.append('_')

print(fifth)

numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainders = []

for number in numbers:
    try:
        remainders.append(36 % number)
    except ZeroDivisionError:
        # pass
        ...

print(remainders)
