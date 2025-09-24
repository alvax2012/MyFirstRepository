import random
import string
m1 = random.sample(range(1, 76), 25)
# print(len(m) == len(set(m)))
# m = [*range(1, 76)]
# random.shuffle(m)
# m = m[:26]
# print(m1)
s12 = [m1[_*5:_*5+5] for _ in range(5)]
# s[2][2] = 0
# print('-', s12)

# s12 = [['0'.ljust(2) if row == 2 and col == 2 else str(s12[row][col]).ljust(1)
#        for row in range(5)] for col in range(5)]
print('--', s12)
[print(*row, sep=' ') for row in s12]


s = ['Владимир Смолов',
     'Тагир Хан',
     'Давид Лавров',
     'Арина Приходько',
     'Глеб Анисимов']
# val = key.copy()
# val = random.sample(val, 5)
# random.shuffle(val)
# print(key, val, sep='\n')
# n = 5

# m = dict(zip(key, val))
# print(m)
# [print(' - '.join(_)) for _ in m.items()]

print(s)
sd = []
td = []
l = dict()
# for i in range(len(s)):
#     for j in range(len(s)):
#         if s[i] not in sd:
#             key = s[i]
#             sd.append(key)
#             val = s[j]
#             if val not in td:
#                 td.append(val)
#                 l.setdefault(key, val)

# print('---', l)
print()
i = 1
d = s.copy()
d1 = []
sd = dict.fromkeys(d)
print('sd', d, sd)

for k in sd.keys():
    tt = ''
    for j in d:
        if (k != j) and (j not in sd.values()):
            sd[k] = j
            tt = j
            break
    # d1.append(tt)
    print('k', k, 'j', j, 'sd[k]', sd[k], 'd1', d1, sd.values())
print()
print(sd, d1)

# for _ in s:
#     key = sd.pop()
#     l.setdefault(key)
#     for val in s:
#         val =
#         if val not in sd and val != key:

#     # sd.append(key)

#     print(i, _, s, sd, l, sep='\n')
#     i += 1


def shs(s: list, h):
    t = len(s)
    s1 = []
    for i in range(t):
        s1.append(s[(i+h) % t])
        # print(i, h, t, (i+h) % t)
    # print(s1)
    return s1


s1 = [1, 2, 3, 4, 5]
print()
print('-', s1)
print('--', s1, shs(s1, 1), shs(s1, 2), sep='\n')


print()


def aa(a):
    a[1] = 777
    a = [22, 44]
    a[0] = 33
    a1 = a.copy()
    return a1


a = [2, 1]
print(aa(a), a)
