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


sample = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]

sr = pd.Series(sample)

print(sr.median())


my_dict = defaultdict(list)

for i in sample:
    # if i == 4:
    my_dict[i].append(i)


print(my_dict)
