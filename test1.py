from decimal import *
import sys
from datetime import datetime, date, time, timedelta
import csv


# mx = 475
# h1 = 1
# m1 = 55
# d = time(hour=1, minute=55)
# td = time(minute=mx)
# print(d, td, sep='\n')

# print(datetime.strptime(tt, '%Y%m%d'))  # .strftime('%d.%m.%Y'))

# a, b, c, d = 1, 2, 3, 4
# for i in range(a, b+1):
#     for j in range(c, d+1):
#         print('\t', (i, j), end='\t')
#     print()


s = 'acggtgttat'

print(100*(s.count('g')+s.count('c'))/len(s))

s = ''
l = sorted(filter(lambda x: s.count(str(x)) > 1, [
           int(i) for i in s.split()]))
l_out = []
for i in l:
    if i not in l_out:
        l_out.append(i)
print('=', *l_out)


# n = 7

# k = 0
# for i in range(1, n+1):

#     for j in range(i):

#         k += 1
#         if k == n+1:
#             break
#         print(i, end=' ')
#     if k == n+1:
#         break
#     # print('k', k)

# # print(n)


l = [8, 8, 2, 7, 8, 8, 2, 4]
x = 8


if x in l:
    m = -1
else:
    print('Отсутствует')
    exit()

for i in l:
    if i == x:

        try:
            m = l.index(i, m+1)
            print(m, end=' ')
        except ValueError:
            break


for i in enumerate(l):
    print(i)

l = [1, 2, 3, 4, 5, 6]
l1 = l.copy()
ld = []
di = 0
for i in range(len(l1)):
    if l1[i] % 2:
        del l[i-di]
        # l[i] = int(x/2)
        di += 1
        # print(i-di, di)
    else:
        l[i-di] = int(l1[i] / 2)
    # i -= di
#     else:
#         ld.append(i)
# for i in ld:
#     del l[i]
print(l)


def update_dictionary(d, key, value):
    if key in d:
        # d[key] += [value]
        d[key].append(value)
    else:
        d.setdefault(key*2, []).append(value)
        # d[key*2] = []


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)

s = '''Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15'''
d = {}
l = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12',
                                       'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]
s1, s2 = 0, 0
for i in l:
    k1, c1, k2, c2 = i

    if int(c1) < int(c2):
        s1 = 0
        s2 = 3
    elif int(c1) > int(c2):
        s1 = 3
        s2 = 0
    else:
        s1 = 1
        s2 = 1

    d.setdefault(k1, []).append(s1)
    d.setdefault(k2, []).append(s2)
    print(i, k1, c1, k2, c2, s1, s2)

for k, v in d.items():
    p0 = len(list(filter(lambda x: x == 0, v)))
    p1 = len(list(filter(lambda x: x == 1, v)))
    p3 = len(list(filter(lambda x: x == 3, v)))

    print(f'{k}:{len(v)} {p3} {p1} {p0} {sum(v)}', v)

print(d)


print(pow(2.0, 3.0))


print(l_out, l)

string = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested..."""

with open("file.txt", "w") as f:
    for line in string.split("\n"):
        f.write(line.split()[0] + '\n')


# s = '4 8 0 3 4 2 0 3'
# s = '1 1 1 1 1 2 2 2 r'
# l = []
# ls = s.split()
# ls.sort()

# if s:
#     i0 = ls[0]
#     for i in ls[1:]:
#         if i.isdigit() and i == i0:
#             if int(i) not in l:
#                 l.append(int(i))
#         i0 = i
#     l.sort()
# print(*l)


r, a = 0, 0  # [Decimal(i) for i in input().split()]
# r = Decimal(r)
# a = Decimal(a)
p = Decimal(round(a*(3**Decimal(1/3)) / 6, 2))


print(r, p)
print('Yes' if round(r, 2) <= round(p, 2) else 'No')

print(*range(1, 5, -1))
for i in range(1, 5, -1):
    print(i)


with open('meetings.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';', quotechar='"')
    for row in rows:
        print(row)
