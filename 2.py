import random
import string

n = 7    # количество попыток
s = {0: 'Орел', 1: 'Решка'}
s = {0: 1, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
for _ in range(n):
    print(s[random.randrange(1, 7)])


# s = [i in range(n) if   random.randrange(0, 2)	== 0:
length = 5
i = random.randrange(0, 2)
s = [chr(random.randrange(65, 92)) if i == 1 else chr(
    random.randrange(97, 123)) for i in range(length)]
print(*s, sep='')

n = 7
s = set()

while len(s) < 7:
    s.add(random.randrange(1, 50))
s = list(s)
print(*sorted(s))


def generate_index():
    s = string.ascii_uppercase
    return f'{random.choice(s)}{random.choice(s)}{random.randrange(100)}_{random.randrange(100)}{random.choice(s)}{random.choice(s)}'


print(generate_index())

print('--'.join('asd'))

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
print(matrix)

n = string.digits
s = [[random.choice(n) if _ != 0 else random.randrange(1, 10)
      for _ in range(7)] for _ in range(3)]

for _ in s:
    print(*_, sep='')


s = [int(_) for _ in random.sample(string.digits, 6)]

s.insert(0, random.randrange(1, 10))
# print(s)
s = [random.sample(range(10), 7) for _ in range(3)]
print(s)

s = 'липа'
# s = list(s)
s = random.sample(s, len(s))
# random.shuffle(s)
print(''.join(s))


for _ in range(5):
    s = random.sample(range(1, 76), 5)
    if _ == 2:
        s[2] = 0
    s = [str(_).ljust(2) for _ in s]
    # print(*s)


# m = set()
# while len(m) < 5:
#     m.add(random.randrange(1, 50))
#     print(m)


n = [*range(1, 76)]
# print(s)

s = [[str(n.pop()).ljust(3) for _ in range(5)] for _ in range(5)]
s[2][2] = '0'.ljust(3)
[print(*row) for row in s]

m1 = random.sample(range(1, 76), 25)
# print(len(m) == len(set(m)))
# m = [*range(1, 76)]
# random.shuffle(m)
# m = m[:26]
print(m1)
s12 = [m1[_*5:_*5+4] for _ in range(5)]
# s[2][2] = 0
print('-', s12)

s12 = [['0'.ljust(2) if row == 2 and col == 2 else str(s12[row][col]).ljust(1)
        for row in range(5)] for col in range(5)]
print('--', s12)
[print(*row, sep=' ') for row in s12]
# print(s)

# t = [[i for i in range(j)] for j in range(3)]
# print(t)

# s = [_ for _ in range(int(input()))]
# print(s)
s = ['Владимир Смолов',
     'Тагир Хан',
     'Давид Лавров',
     'Арина Приходько',
     'Глеб Анисимов'][::-1]
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
    for j in d:
        if (k != j) and (j not in d1):
            sd[k] = j
    d1.append(j)
    print('k', k, 'j', j, 'sd[k]', sd[k], 'd1', d1)
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
