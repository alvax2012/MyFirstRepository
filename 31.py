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
