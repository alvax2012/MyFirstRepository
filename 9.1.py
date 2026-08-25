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
