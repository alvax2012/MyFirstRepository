
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


def rec_dig(n):

    if n < 10:
        return n

    k = n // 10
    l = n % 10
    return rec_dig(k) + l
    # return s


print(rec_dig(213))

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


print(solve(s))
