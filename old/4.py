import random
import string

key = ['Владимир Смолов',
       'Тагир Хан',
       'Давид Лавров'
       ]

# n = 5
# key = [input() for _ in range(int(input()))]
# print(key)
# n = len(key)
# val = key.copy()
# val = random.sample(val, n)
# m = dict(zip(key, val))

# while False:
# flg = True
# while flg:
#     for k, v in m.items():
#         if k == v:
#             val = random.sample(val, n)
#             m[k] = random.choice(m.values())
#             # m = dict(zip(key, val))
#             flg = False
#             break
#         # print('--', k, v, m)

# # print(m)
# [print(' - '.join(_)) for _ in m.items()]

flg = True
while flg:
    for i in range(7):
        flg = False
        if i == 4:
            # flg = not flg
            print(i, '-', flg)
            break
        print(i, flg)

print('stop')

m = {1: 2,  3: 4}
print(list(m.items())[-1][1])

l = [1, 2, 3, 4, 5]
print(l[:-1])

print()

m = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
val = list(m.keys())
k1 = list(m.items())[-1][0]
v1 = list(m.items())[-1][1]
print(m)
if k1 == v1:
    k2 = random.choice(val[:-1])
    print(k2)
    m[k1], m[k2] = m[k2], m[k1]
print(m)

n = len(key)
val = key.copy()
val = random.sample(val, n)
m = dict(zip(key, val))

# while False:
flg = True
while flg:
    # random.seed(1)
    k1 = list(m.items())[-1][0]
    v1 = list(m.items())[-1][1]
    if k1 == v1:
        k2 = random.choice(val[:-1])
        m[k1], m[k2] = m[k2], m[k1]
    for k, v in m.items():
        print(k, v)
        if k == v:
            # val = random.shuffle(val)
            m[k] = random.choice(val)
            flg = False
            # print('--', k, v, m)
            break


# print(m)
[print(' - '.join(_)) for _ in m.items()]
