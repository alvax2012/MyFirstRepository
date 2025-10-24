from functools import reduce
s = '2 4 3'
x = 10

s = s.split()[::-1]
l = map(int, s)
d = tuple(zip(range(len(s)), l))

print(l)
print(*d)


def evaluate(x, d):
    return reduce(lambda x, y: x + y, map(lambda y: y[1]*pow(x, y[0]), d), 0)


print('--+', evaluate(x, d),  l)
print(d)


s = '2 4 3'
x = 10

s = s.split()[::-1]
l = map(int, s)
n = range(len(s))

# k = list(l)


def mn(l, n):
    def mmn(x):
        return reduce(lambda x, y: x + y, map(lambda l1, n1: l1*pow(x, n1), l, n))
    return mmn


f = mn(l, n)
print(f(x))

print(type(0j))


numbers = [17, 90, 78, 56, 231, 45, 5, 89, 91, 11, 19]

res = map(lambda x: x if x > 10 else False, numbers)
print(*res)
res = filter(lambda x:  x > 10, numbers)
print(*res)
res = map(lambda x:  x > 10, numbers)
print(*res)
