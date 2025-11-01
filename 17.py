import random
from functools import reduce
from operator import *


class Pers   o n:

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

d[p.qar()][p.name] = d.get(
    p.qar(), {}).setdefault(p.name, 0) + p.cnt
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

print()
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10,
           4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]

result = {}
for num in numbers:
    # result[num] = result.get(num, 0) + 1
    result.setdefault(num, []).append(True)
    result1 = map(lambda x: (x[0], len(x[1])), result.items())
# print('res1', *result1)


s1 = 'ZIPZIZ'
p = {1: 'AEIOULNSTR',
     2: 'DGZ',
     3: 'BCMP',
     4: 'FHVWY',
     5: 'K',
     8: 'JX',
     10: 'Q'}
t1 = [k for i in s1 for k, v in p.items() if i in v]
t2 = [k for k, v in p.items() for _ in s1 if _ in v]
# print(sum(t1), sum(t2), sep='\n')


def merge(l):
    res = {}
    for d in l:
        for k, v in d.items():

            # res.setdefault(k, set()).add(v)
            res.setdefault(k, set()).add(v)
            # print(type(res.setdefault(k, set())))
    return res


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {
    'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])
# print(result)


dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
         'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
         'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
         'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0)
               for key in set(dict1) | set(dict2)}
# print("Объединенный словарь:", merged_dict)

binary1 = '11'  # Двоичное представление 13
binary2 = '11'  # Двоичное представление 11
# Сложить и преобразовать обратно в двоичное
sum_binary = bin(int(binary1, 2) + int(binary2, 2))[2:]
print(sum_binary)

dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
         'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
         'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
         'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0)
               for key in set(dict1) | set(dict2)}
print("Объединенный словарь:", merged_dict)


print(set({'a': 1, 'b': 2}))

t2 = [(1, 2), (2, 3)]
t2 = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), t2)

print('t2=', dict([t2]), dict([(2, 3)]))


print(set({}) | set({'стол222'}))
