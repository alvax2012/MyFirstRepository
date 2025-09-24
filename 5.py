import random

key = ['Светлана Зуева',
       'Аркадий Белых',
       'Борис Боков'
       ]


n = len(key)
val = key.copy()
val = random.sample(val, n)
m = dict(zip(key, val))

# while False:
flg = True
i = 1
while flg:
    l1 = val[i:]
    for k, v in m.items():
        if k == v:
            # m[k] = random.choice(val)
            k1 = random.choice(l1)
            m[k], m[k1] = m[k1], m[k]
            flg = False
            # print('--', k, v, m)
            break
        i += 1
# print(m)
[print(' - '.join(_)) for _ in m.items()]
