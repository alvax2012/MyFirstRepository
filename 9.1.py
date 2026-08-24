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


films = {'Spider-Man': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},

         }

# m = min(sum(v.values()) for v in films.values())
m = min(films, key=lambda i: sum(films[i].values()))
print(m)
# *filter(lambda v: sum(films[v].values()) == m, films),
# t = [k for v in films.values() for k in v.items()]
# print(t)


def dfilm(d, p=20):
    s = 0
    for i in d:
        # s += dfilm(v, s)

        if isinstance(d[i], dict):
            s += dfilm(d[i])
            # return s
            # dfilm(v, s)
        else:
            return d[i]
    return s


print(dfilm(films))
