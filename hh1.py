
# ---- # 1
def process(input_string: str) -> str:
    l = list(map(int, input_string.split()))
    print(l)
    return f'выше нуля: {len(list(filter(lambda x: x > 0, l)))}, ниже нуля: {len(list(filter(lambda x: x < 0, l)))}, равна нулю: {len(list(filter(lambda x: x == 0, l)))}'


input_string = '5 -2 0 0 7 8 -1'
output_string = process(input_string)
print(output_string)
print()

# ---- # 2


class Person:

    def __init__(self, dt1,  name1, cnt1):
        self.name = name1
        self.dt = dt1
        self.cnt = int(cnt1)

    def qar(self):
        l = int(self.dt.split('-')[1])
        q = 0
        if l == 6:
            q = 7
        elif l == 3:
            q = 4
        else:
            q = 0
        return q


# tom = Person("Tom", 22)
# tom.display_info()


def report1(s):
    d = {}
    l = map(lambda x: x.split(':'), s.split(';'))
    for i in l:
        p = Person(i[0], i[1], i[2])
        d[p.qar()][p.name] = d.setdefault(
            p.qar(), {}).setdefault(p.name, 0) + p.cnt
    return d


s = '2025-06-08:ручка:1;2025-06-01:ручка:3;2025-06-01:стол:3;2025-03-11:ручка:4;2025-03-01:ручка:7;2025-03-02:стол:5;2025-01-01:ручка:7;2025-02-02:ручка:6;2025-02-22:стол:5'
d1 = report1(s)
print('d1=', d1)

print()
for k, v in d1.items():
    print(f'Q: {k}')
    [print(f'Наименование: {k} \nКолич. {v}') for k, v in v.items()]


def f(a):
    def g():
        nonlocal a
        print(a, end=' ')
        a += 1
    return g


g = f(10)
g()
g()
g()
print('==', g)


def aa(i):
    if i > 3:
        return "3"
    return '444'


print(aa(32))

a = 1


# def g1():
#     print(a)
#     a += 1
#     print(a)

print('---')


def f1(b):
    # global a
    # print('1=', a)
    # a += 1
    # print('2=', a)

    def g1(t):
        nonlocal b
        print(b, t, end=' ')
        b += 1
        t += 1
        print(b, t)
    return g1


ll = f1(77)
ll(1)
ll(2)

res = True | False + 1
print(res)


# class C:
#     def f():
#         pass


# class D():
#     def f(self):
#         pass


# class E(C, D):
#     def f(self):
#         super().f()


# E().f()

s = 0

# Уровень Средний задача 1


def rec_dig(n):

    if n < 10:
        return n

    k = n // 10
    l = n % 10
    return rec_dig(k) + l
    # return s


print(rec_dig(213))


# Уровень Средний задача 2

s = '-x+4=+10+2x'


def solve(s):
    # l = s.split('=')
    res = ''
    l = []

    res = s[0]
    for i in s[1:]:
        if i == '=':
            i = ''
        if i in '+-=':
            if res:
                l.append(res)
            res = ''
            # continue
        res += i
    l.append(res)
    s1 = 0
    s2 = 0
    sig = 1
    k = 1
    for i in l:
        if k > 2:
            sig = -1
        if i[-1].isalpha():
            if i[:-1] == '-':
                s1 += -1
            elif i[:-1] == '+':
                s1 += 1
            else:

                s1 += int(i[:-1])*sig
        else:
            s2 += int(i)*sig
        k += 1

    return l, s1, s2, s2 / s1


s = '3x+5=10x-5'


def solve(s):
    l = s.split('=')

    def dm(l, sg=1):
        s1 = 0
        s2 = 0
        sig = l[0]
        sig1 = ''
        l0 = l[1:]
        l1 = l0.split('+')
        if len(l1) == 1:
            l1 = l0.split('-')
            sig1 = '-'
        l1[0] = sig + l1[0]
        l1[1] = sig1 + l1[1]

        for i in l1:
            if i[-1].isalpha():
                if len(i[:-1]) == 1:
                    s1 += sg * int(i[0] + '1')
                else:
                    s1 += sg * int(i[:-1])
            else:
                s2 += sg * int(i)

        return s1, s2

    res1 = dm(l[0], sg=1)
    res2 = dm(l[1], sg=-1)
    return (res1[1] + res2[1]) / -(res1[0] + res2[0]), res1, res2


print(solve(s))


# Уровень Легкий задача 2


def is_right_triangle(s):
    l = [int(i) for i in s if i.strip() != '']
    l.sort()
    return l[0]**2 + l[1]**2 == l[2]**2


print(is_right_triangle('5 3 4'))


# Уровень Легкий задача 1

def filter_unique_words(s):
    l = s.split()
    return ' '.join(filter(lambda x: l.count(x) == 1, l))


s = ' чай кофе чай чай молоко'

print(filter_unique_words(s))

# Уровень Легкий задача 3


def mask(s: str) -> str:
    if len(s) < 4:
        return s

    l = list(s)
    # s = s[:-4]
    return ''.join(list(map(lambda x: '#', s[:-4])) + list(s[-4:]))


s = '123456'
print(mask(s))


l = [1, 2, 3]
l1 = []
for i in range(len(l)):
    p = l.pop()
    l1.append(p)
    print(l1,  l,  p)

num_list = [1, 2, 3]
ll = [y for x in num_list if (y := pow(x, 2)) < 20]
# ll = [pow(x, 2) for x in num_list if pow(x, 2) < 20]
print(ll)

l = [1, 2, 3]
i = 0
while (line := l[i] != 3):
    print(line, l[i], i)
    i += 1

# line = 0
# while (line != 3):
#     line = l[i]
#     print(line, l[i], i)
#     i += 1

# help('process')

if (value := pow(2, 4)) > 10:
    print(value)


# анонимные функции являются выражениями, то есть их можно сразу вызывать в момент определения


numbers = filter(lambda x: x > 0, [-3, -2, -1, 0, 1, 2, 3, 1])

if 1 in numbers:
    print('bee')
if 1 in numbers:
    print('geek')


data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [
    1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
# data = [1, 2, '14']
print(*map(int, filter(lambda x: isinstance(x, (int, float)), data)))

numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 9, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396,
           2842, -3879, -3824, -9, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

print((map(lambda x: x**2, filter(lambda x: x % 9 == 0 and x // 100 == 0, numbers))))

dd = [-90, 1, 90]
print(*filter(lambda x: x % 9 == 0 and -100 < x < 100 == 0, dd))
print('==', *filter(lambda x: x % 9 == 0 and abs(x) // 100 == 0, dd))
