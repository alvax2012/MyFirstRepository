import random
# key = [input() for _ in range(int(input()))]

key = ['Владимир Смолов',
       'Тагир Хан',
       'Давид Лавров',
       'Арина Приходько',
       'Глеб Анисимов']


n = len(key)
# random.seed(1)

val = key.copy()
# val = random.sample(val, n)
m = dict(zip(key, val))

flg = True
while flg:
    for k, v in m.items():
        if k == v:
            k1 = random.choice(val)
            m[k], m[k1] = m[k1], m[k]
            flg = False
            # print('--', k, v, m)
            break


# print(m)
[print(' - '.join(_)) for _ in m.items()]
