import string

# for i in range(97, 123):
#    print(chr(i))


def convert(n):
    d = {1: bin, 2: oct, 3: hex}
    l = []
    # return bin(n)[2:], oct(n)[2:], hex(n)[2:]
    for i in range(1, 4):
        l.append(d[i](n)[2:])

    return tuple(l)


print(convert(-24))


films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

# m = min(sum(v.values()) for v in films.values())
m = min(films, key=lambda i: sum(films[i].values()))
print(m)
# *filter(lambda v: sum(films[v].values()) == m, films),
# t = [k for v in films.values() for k in v.items()]
# print(t)


def dm(dct, sm=0):
    s = 0
    for i in dct:
        s += dm(dct[i], 0)

    if isinstance(dct, float):
        # res['.'.join(pp)] = dct
        # p = ''
        return dct

    print('s=', s)


# dm(films)

def non_negative_even(num):
    return all(i >= 0 and i % 2 == 0 for i in num)


def non_negative_even(numbers):
    return numbers[0] >= 0 and numbers[0] % 2 == 0 if len(numbers) == 1 else numbers[0] >= 0 and numbers[0] % 2 == 0 and non_negative_even(numbers[1:])


print(non_negative_even([0, 2, 4, 8, 16]))


def is_greater(data, n):
    return any(sum(l) > n for l in data)


data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]

print(is_greater(data, 10))


def custom_isinstance(objects, typeinfo):
    n = 0
    for i in objects:
        if isinstance(i, typeinfo):
            n += 1
    return n


numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))


numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -
           2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]


print(max(enumerate(numbers), key=lambda x: x[1])[0])
print(numbers.index(5023))


def my_pow(n):
    return sum([pow(int(i[1]), i[0]) for i in enumerate(str(n), 1)])


print(my_pow(139))

names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille',
         'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000,
           180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195,
               620702951, 807082196, 857611174, 940335536, 1280802282]

print(*sorted(f'{i[0]}: {i[2]-i[1]}$' for i in zip(names,
      budgets, box_offices)), sep='\n')


def zip_longest(*args, fill=None):
    # if not fill:
    m = max(len(i) for i in args)
    for i in args:
        for j in range(m-len(i)):
            i.append(fill)

    return list(zip(*args))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))


s = 'AnHTqir9brdQrgu5g71uhm1FaJ4fAZjbisIDnJVYekRPdGDc29'
s_lowercase = []
s_uppercase = []
s_digits = []
for i in s:
    if i in string.ascii_lowercase:
        s_lowercase.append(i)
    elif i in string.ascii_uppercase:
        s_uppercase.append(i)
    else:
        s_digits.append(i)

s_lowercase.sort()
s_uppercase.sort()
s_digits.sort()

res = ''.join(s_lowercase) + ''.join(s_uppercase) + \
    ''.join(filter(lambda x: int(x) % 2 != 0, s_digits)) +\
    ''.join(filter(lambda x: int(x) % 2 == 0, s_digits))
print(res)
