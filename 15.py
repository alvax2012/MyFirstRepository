from functools import reduce
from operator import *
import random

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


def f11():
    print('11')
    return print('11', '22', sep='\n')


f11()


def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'


print(generate_letter('lara@yandex.ru', 'Лариса',
      '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
                      'Часова 23, корпус 2', 'Василь Ярошевич', 23))


t = (
    'qq\n'
    'rr'
)
t = '''
a
c
v
'''
print(t)


def pretty_print(data, side='-', delimiter='|'):
    d = list(zip([delimiter]*len(data), data)) + [(delimiter, '')]
    l = sum(map(lambda x: len(x) if x is str else len(
        str(x)), data)) + len(data)*3 - 1
    # print(l)
    s = ''
    for i in d:
        s += f'{i[0]} {i[1]} '
    print('', side*l)
    print(s.strip())
    print('', side*l)
    # print(side*len(d), end=' ')
    # print()
    # [print(_[0], _[1], end=' ') for _ in d]
    # print()


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


print([1] + [1, 2] + [])


def concat(*l, sep=' '):
    return f'{sep}'.join(map(str, l))


print(concat(1, 2, sep='$$'))


def product_of_odds(data):
    return reduce(lambda x, y: x*y, filter(lambda x: x % 2 == 1, data), 1)


print(product_of_odds([10]))

words = 'the world is mine take a look what you have started'.split()

print(*map(lambda x: f'"{x}"', words))


numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908,
           8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x) != str(x)[::-1], numbers))


numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1),
           (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)

print(sorted_numbers)


def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


def call(f, *arg):
    return f(*arg)


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


def compose(f, g):
    def ff(x):
        return f(g(x))
    return ff


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))


def arithmetic_operation(operation):
    d = {'+': add, '-': sub, '*': mul, '/': truediv}
    return d[operation]


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(arithmetic_operation('/')(20, 5))

s = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'
print(*sorted(s.split(), key=lambda x: x.upper()))

r = ['basis', 'after', 'chief', 'agenda']

# print([reduce(lambda x, y: ord(x)+ord(y), i.upper()) for i in s2])
print(*sorted(r, key=lambda c: reduce(lambda x, y: x +
                                      (ord(y) - ord('A')), c.upper(), 0)), sep='\n')

print('+', reduce(lambda x, y: x + (ord(y) - ord('A')), r[0], 0), sep='\n')

# s = ['128.199.44.24', '128.199.201.245', '143.198.168.95', '172.67.181.62',
#   '172.67.222.111', '172.67.10.90', '45.8.106.59', '203.13.32.156', '172.67.181.194']


#    def gem(ip):
#    s = 0
#    # print(*enumerate(ip.split('.')))
#    for i in enumerate(ip.split('.')):
#    s += (256**(3-i[0]))*(int(i[1]))
#    return s


#    # print(*map(lambda x: (x, gem(x)), s))
#      print(*sorted(s, key=gem), sep='\n')

#      print()
#      print(gem('192.168.1.2'))

print('bbhh b'.strip('b'))
print('123aaa6\rbb')
print('123aaaaaa8\nbb')

f = open('c:/1/nums.txt', encoding='utf-8')
print(sum(map(lambda x: int(x.strip()), list(f))))
f.close()
