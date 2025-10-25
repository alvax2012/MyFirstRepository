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

print(6 % 2)


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql',
              'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: command in x, ignore))


print(ignore_command('alias2'))


countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321,
              67_886_011, 65_273_511, 1_380_004_385]

print(*[f'{y} is the capital of {x}, population equal {z} people.' for x,
      y, z in zip(countries, capitals, population)], sep='\n')

x = '2a'
print(int(x) if x.isdigit() else 0)

s = '10.1.1.a'
print(all(map(lambda n: n.isdigit() and 0 <= int(n) <= 255, s.split('.'))))

# print(all(map(lambda x: 255 >= x >= 0 and x.isdigit(), map(lambda x: int(x) if x.isdigit() else x, s.split('.')))))


def f1(a):
    return all(map(lambda x: a % int(x) == 0, str(a)))


a, b = 1, 25
l = filter(lambda x: not '0' in str(x) and f1(x), range(a, b+1))

print(*filter(lambda x: not '0' in str(x) and f1(x), range(a, b+1)))
# l1 = [list(filter(lambda x: int(x) != 0, list(str(_)))) for _ in range(a, b+1)]
# l = list(zip(range(a, b+1), l1))
# s = [[int(_) % i[0] for _ in i[1]] for i in l]
# print(*l)
# print(s)
# print([list(map(lambda x: [x[1] % _ for _ in x[0]], i))for i in zip(map(lambda x: x, l), range(a, b+1))])


print(f1(14))
