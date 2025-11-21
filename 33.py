import random
from functools import reduce
from operator import *


def index_of_nearest(l: list, n: int):
    l1 = list(map(lambda x: abs(x - n), l))
    return min(enumerate(l1), key=lambda x: x[1])[0] if len(l) > 0 else -1
    # mn = min(l1) if len(l1) > 0 else 0
    # l2 = filter(lambda x: x == mn, l1)
    # ls = '_'.join(map(str, l1))
    # mn = str(min(l1)) if len(l1) > 0 else ' '
    # return l2[0]  # ls.find(mn)


print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([], 17))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
