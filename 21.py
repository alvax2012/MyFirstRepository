from operator import mul
from functools import reduce
import random
import operator
s = 'words1.txt'
with open('forbidden_words.txt', encoding='utf-8') as f_in, open(s, encoding='utf-8') as f_out:
    l_for = f_in.read().split()
    l = f_out.read().split(' ')
    l_low = list(map(str.lower, l))
    print(l)
    print(l_low)
    # l = map(lambda x:  x  if x.replace(.lower(), '*'*len(w)), l_out)
    # l = [i if i not in l_out else i for i in l_out]\

    def cmp(s, sf):
        l = list(sf)
        ls = list(s)
        for i in range(len(l)):
            if l[i] != '*':
                l[i] = ls[i]
        return ''.join(l)

    for i in range(len(l_low)):
        i1 = l_low[i]
        for j in l_for:
            if j in i1:
                l_low[i] = cmp(l[i], i1.replace(j.lower(), '*'*len(j)))

    print(*l_low)
