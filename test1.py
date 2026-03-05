import sys
from datetime import datetime, date, time, timedelta
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


l = []
l_out = []
l = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]

n = len(l)
m = len(l[0])

for i in range(n):
    l_out.append([])

    for j in range(m):
        m0 = j - 1
        m1 = j + 1
        n0 = i - 1
        n1 = i + 1
        if i == 0 and 0 < j < n:
            n0 = 1
            n1 = n - 1
        elif j == 0 and 0 < i < m:
            m0 = 1
            m1 = m - 1
        elif i == n - 1 and 0 < j < m:
            n0 = n - 2
            n1 = 0
        elif j == m - 1 and 0 < i < n:
            m0 = m - 2
            m1 = 0
        elif i == 0 and j == 0:
            n0 = n - 1
            m0 = m - 1
        elif i == n-1 and j == m-1:
            n1 = 0
            m1 = 0
        print(i, j, n0, n1, m0, m1)
        # l_out[-1].append(l[n0][j] + l[n1][j] + l[i][m0] + l[i][m1])


print(l_out, l)

print(sys.getsizeof(268435459))

print(2**28)
