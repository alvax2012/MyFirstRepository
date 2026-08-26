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


films = {1: {'imdb': 8.8, 'kinopoisk': 8.3},
         2: {'imdb': 7.3, 'kinopoisk': 7.6},
         }
# m = min(sum(v.values()) for v in films.values())
m = min(films, key=lambda i: sum(films[i].values()))
print(m)
# *filter(lambda v: sum(films[v].values()) == m, films),
# t = [k for v in films.values() for k in v.items()]
# print(t)


def dfilm(d):
    p = 20

    def dm(d):
        s = 0
        nonlocal p
        for i in d:
            # s += dfilm(v, s)

            if isinstance(d[i], dict):
                dm(d[i])
                # return s
                # dfilm(v, s)
            else:
                s += d[i]
        if s and s < p:
            p = s
        return s

    dm(d)
    return p


print(dfilm(films))


print(type(repr([1, 2, 3, 4])))


def hash_as_key(data):
    d = {}
    for i in data:
        h = hash(i)

        if h in d:
            if not isinstance(d[h], list):
                d[h] = [d[h]]
            d[h].append(i)
        else:
            d[h] = i
    return d


data = [-1, -2, 3]
# data = [1, 2, 3, 4, 5, 5]
data = [5, 5, 5]

print(hash_as_key(data))


s1 = '[[1, 2], [3, 4], [5, 6]]'
# s1 = "{'Arthur', 'Timur', 'Anri', 'Ruslan', 'Dima'}"
# s1 = "('black', 'blue', 'red', 'orange', 'green', 'gray')"

# res = ''
s = eval(s1)
if isinstance(s, list):
    res = s[-1]
elif isinstance(s, set):
    res = len(s)
else:
    res = s[0]
print(res)


f1 = '2*x**2 + 5*x + 7'
n1 = list(map(int, '-1 5'.split()))
l = []
for x in range(n1[0], n1[1]+1):
    l.append(eval(f1))
    # print(x, eval(f1))

s_out = f'''
Минимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно {min(l)}
Максимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно {max(l)}
'''

print(s_out)

a, b = map(int, '12')

print(a, b)
