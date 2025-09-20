import random
import string

key = ['Владимир Смолов',
     'Тагир Хан',
     'Давид Лавров',
     'Арина Приходько',
     'Глеб Анисимов']

# n = 5
# key = [input() for _ in range(int(input()))]
# print(key)
n = len(key)
val = key.copy()
val = random.sample(val, n)
m = dict(zip(key, val))

while False:
    # flg = False
    for k, v in m.items():
        if k == v:
			val = random.sample(val, n)
    		m = dict(zip(key, val))
			flg = True
           	break
    
print(m)
#[print(' - '.join(_)) for _ in m.items()]