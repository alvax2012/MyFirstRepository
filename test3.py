from collections import defaultdict
import pandas as pd


def null_dec(func):
    y = 123
    return func(y)


def greet(y):
    print('123!')
    return '222!' + str(y)


greet1 = null_dec(greet)

print(greet1)

d = {'sep1': '\n'}
print('123-', '-321', **{'sep': '\n', 'end': '!'})

print()
l = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
sr = sum(l)/len(l)
l1 = sum([(i-sr)**2 for i in l])/(len(l)-1)
print(l1**(0.5))

sample = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]

sr = pd.Series(sample)

print(sr.median())


my_dict = defaultdict(list)


result = True | False
print(result)      # 1
print(type(result))


l = dict(a1=2, b1=4)
print(l)

for i in l.keys():
    print(i)


letters1 = dict(a=1, b=2, c=3, d=4)
letters2 = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
letters3 = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print(letters1)
print(letters2)
print(letters3)
