
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


def get_biggest(l: list):
    if l == []:
        return -1
    ls = list(map(str, l))
    n = len(max(ls, key=lambda x: len(x)))  # len(''.join(ls))
    return int(''.join(sorted(ls, key=lambda x: x*n, reverse=True))), sorted(ls, key=lambda x: x.ljust(n, x[0]), reverse=True)
    # ls1 = sorted(ls, key=lambda x: tuple(x),  reverse=True)
    # return ls1


print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34,
      65, 65, 2, 1]), 78554656558534233433222211311, sep='\n')

print(get_biggest([13, 1, 1]))

print(get_biggest([62, 626]))
