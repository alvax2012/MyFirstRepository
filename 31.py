import random
from functools import reduce
from operator import *


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
    m = []
    d = {}
    l = list(map(lambda x: x.split(':'), s.split(';')))
    for i in l:
        p = Person(i[0], i[1], i[2])
        m.append(
            f'Q: {p.qar()}\n Наименование: {p.name} \n Количество: {p.cnt}')
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

print('-'*40)
d = {
    ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'): 1,
    ('Д', 'К', 'Л', 'М', 'П', 'У'): 2,
    ('Б', 'Г', 'Ё', 'Ь', 'Я'): 3,
    ('Й', 'Ы'): 4,
    ('Ж', 'З', 'Х', 'Ц', 'Ч'): 5,
    ('Ш', 'Э', 'Ю'): 8,
    ('Ф', 'Щ', 'Ъ'): 10
}

s = 'ноутбук'
l = sum(x[1] for i in s for x in d.items() if i.upper() in x[0])
print(l)

l = ((i, x) for i in [5, 7] for x in [1, 3] if x > 2)
print(*l)


def foo(*args, **kwar):
    return args[0]+args[1]


print(foo(1, 2))

print('---')


def print_given(*args, **kwargs):
    [print(i, type(i)) for i in args]
    [print(i[0], i[1], type(i[1])) for i in sorted(kwargs.items())]


print_given(1, [1, 2, 3], 'three', two=2)


def convert(s: str):
    l = list(filter(str.isalpha, list(s)))
    l_l = len(list(filter(str.islower, l)))
    l_u = len(list(filter(str.isupper, l)))
    return s.upper() if l_u > l_l else s.lower()


print(convert.__defaults__)


things = {'зажигалка': 20, 'компас': 100}
sorted_things = dict(sorted(things.items(), key=lambda x: x[1], reverse=True))

print(sorted_things)
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

d11 = sorted(f'{i}@{k}' for k, v in emails.items() for i in v)

print(*d11)
l11 = []
dd22 = map(
    lambda x: [f'{i}@{x[0]}' for i in x[1]], emails.items())
# dd33 = sorted(reduce(lambda x, y: x+y, dd22))
dd33 = [l11.extend(i) for i in dd22]
print(sorted(l11))

# [l11.append(i) for i in [1, 2, 7]]
# print(l11)
