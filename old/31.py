import random
from functools import reduce
from operator import *


def foo(*args, **kwar):
    return args[0]+args[1]


print(foo(1, 2))

print('---')


def print_given(*args, **kwargs):
    [print(i, type(i)) for i in args]
    [print(i[0], i[1], type(i[1])) for i in sorted(kwargs.items())]


print_given(1, [1, 2, 3], 'three', two=2)


def convert(s: str):
    l = list(filter(str.isalpha, list(s)))
    l_l = len(list(filter(str.islower, l)))
    l_u = len(list(filter(str.isupper, l)))
    return s.upper() if l_u > l_l else s.lower()


print(convert.__defaults__)


# [l11.append(i) for i in [1, 2, 7]]
# print(l11)
