from operator import mul
from functools import reduce
import random
import operator

s = 'beegeek.txt'
with open('forbidden_words.txt', encoding='utf-8') as f_in, open(s, encoding='utf-8') as f_out:
    l_for = f_in.read().split()
    l = f_out.read()  # [_.split() for _ in f_out.read()]
    # l_low = list(map(str.lower, l))

    def replace_all(s: str, l_for: list,  r='*'):
        s_l = s.lower()
        for i in l_for:
            f = s_l.find(i)
            if f != -1:
                s = s[:f] + r*len(i) + s[f+len(i):]
        return s

# print(l_for)
print(l)
# print('wwHelioHeloiop'.find('Hel'))
# s1 = 'лKпhelLo emaIlшOш'
print(replace_all(l, l_for))

print(' dd   hh '.split())
