from operator import mul
from functools import reduce
import random
import operator

s = 'stepik.txt'
with open('forbidden_words.txt', encoding='utf-8') as f_in, open(s, encoding='utf-8') as f_out:
    l_for = f_in.read().split()
    l = f_out.read()  # [_.split() for _ in f_out.read()]
    # l_low = list(map(str.lower, l))

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

                print(j, 'pa=', pa, 'f0=', f0, 'p0=',
                      p0,  'ln=', ln,  '-', sl, s)
                f0 = sl.find(i)
                p0 = f0 + ln

                pa = pa + p0

                # s = s[:f] + r*len(i) + s[f+len(i):]
                # p0 = f0 + len(i)  # s_l[f+len(i):].find(i)
                # if p0 > len(sl):
                #     print(i, p0, f0, '---', sl)
                #     break
                # print(i, p0, '--', sl)

        return s

# print(l_for)
print(l)
# print('wwHelioHeloiop'.find('Hel'))
# s1 = 'лKпhelLo emaIlшOш'
# print(replace_all(l, l_for))
print()
print(' dd   hh '.split())

print(replace_all('0123python4PYTHON5PyThoN56', l_for))
