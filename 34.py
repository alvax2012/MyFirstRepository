
def choose_plural(amount: int, declensions: tuple):
    # i = 0
    p = ((amount // 10) % 10)*10 + (amount % 10)
    print('--', p, amount % 10, p % 10)

    if p % 10 == 0:
        i = 2
    elif amount % 10 in range(5, 10) or p in range(11, 20):
        i = 2
    elif amount % 10 == 1:
        i = 0
    elif amount % 10 in range(2, 5):
        i = 1

    # if p in range(11, 20):
    #     i = 2
    # elif amount == 0 or amount % 10 in [0, range(5, 10)] or amount in range(5, 20):
    #     i = 2
    # elif amount % 10 in range(2, 5):
    #     i = 1
    # else:
    #     i = 0

    return declensions[i]


print(choose_plural(240, ('курица', 'курицы', 'куриц')))

num = 1234
d4 = num % 10
d3 = (num // 10) % 10
d2 = (num // 100) % 10
d1 = num // 1000

print('Цифра в позиции тысяч равна', d1, num // 1000)
print('Цифра в позиции сотен равна', d2, (num // 100) % 10, num // 100)
print('Цифра в позиции десятков равна', d3, (num // 10) % 10, num // 10)
print('Цифра в позиции единиц равна', d4, num % 10)
