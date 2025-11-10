from operator import mul
from functools import reduce
import random
import operator

s = 'stepik.txt'
with open('forbidden_words.txt', encoding='utf-8') as f_in, open(s, encoding='utf-8') as f_out:
    l_for = f_in.read().split()
    l = f_out.read()

    def replace_all(s: str, l_for: list,  r='*'):
        sl = s.lower()
        for i in l_for:
            ln = len(i)

            f0 = sl.find(i)
            p0 = f0 + ln

            pa = p0
            j = 0
            while f0 != -1:
                j += 1
                sl = sl[p0:]
                s = s[:pa-ln] + r*ln + s[pa:]
                # print(j, i,  'pa=', pa, 'f0=', f0, 'p0=',
                #      p0,  'ln=', ln,  '-', sl, s)
                f0 = sl.find(i)
                p0 = f0 + ln
                pa = pa + p0
                # print(s)
        return s

# print(l)
print()
# print(replace_all('0123python4PYTHON5PyThoN56', l_for))
# for i in l_for:
print(replace_all(l, l_for))
