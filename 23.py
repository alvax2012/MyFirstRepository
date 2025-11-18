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
    # d = d.setdefault
    print(l)
    for i in l:
        # print(i)
        p = Person(i[0], i[1], i[2])
        m.append(
            f'Q: {p.qar()}\n Наименование: {p.name} \n Количество: {p.cnt}')

        # d[p.qar()][p.name] = d.setdefault(
        #    p.qar(), {}).setdefault(p.name, 0) + p.cnt

        d[p.qar()][p.name] = d.get(p.qar(), {}).setdefault(p.name, 0) + p.cnt
        # d[p.qar()][p.name] = d.setdefault(
        #     p.qar(), {}).setdefault(p.name, 0) + p.cnt

        d[p.qar()] = d.get(
            p.qar(), ())
        # d[p.qar()][p.name] = d[p.qar()].get(p.name, 0) + p.cnt

        d[p.qar()] += ({p.name: p.cnt},)

        # print('d', l, m, d, sep='\n')
        return d


s = '2025-06-08:ручка:1;2025-06-01:ручка:3;2025-06-01:стол:3;2025-03-11:ручка:4;2025-03-01:ручка:7;2025-03-02:стол:5;2025-01-01:ручка:7;2025-02-02:ручка:6;2025-02-22:стол:5'
tt = report1(s)
print('tt=', tt)
d1 = dict()
for k, v in tt.items():
    merged_dict = {}
    print('k=', k, 'v=', v)
    for _ in v:
        merged_dict = {k: merged_dict.get(k, 0) + _.get(k, 0)
                       for k in set(merged_dict) | set(_)}
        # merged_dict = merged_dict[k].setdefault()
    d1.update({k: merged_dict})

    print('merged_dict', merged_dict)
print('d1=', d1)


print()
for k, v in d1.items():
    print(f'Q: {k}')
    [print(f'Наименование: {k} \nКолич. {v}') for k, v in v.items()]
    # print(f'Наименование: {v} \n')  # Количество: {v.values()}')
[print(_, end='')
 for _ in ls[::-1]] if len(ls) > 0 else print('Best Programming Team')


buf, pos = [None] * 10, 0
with open(s) as f:
    while True:
        s = f.readline().strip()
        if s == '':
            break
        buf[pos], pos = s, (pos + 1) % 10
[print(text) for text in buf[pos:] + buf[:pos] if not text is None]
