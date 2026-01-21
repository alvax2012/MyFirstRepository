from operator import mul
from functools import reduce
import random
import operator

s = 'stepik.txt'
with open('forbidden_words.txt', encoding='utf-8') as f_in, open(s, encoding='utf-8') as f_out:
    l_for = f_in.read().split()
    l = f_out.read()

    def replace_all(s: str, l_for: list,  r='*'):
        sl1 = s.lower()
        for i in l_for:
            sl = sl1
            ln = len(i)

            f0 = sl.find(i)
            p0 = f0 + ln

            pa = p0
            j = 0
            # print('i=', i)
            while f0 != -1:
                j += 1
                sl = sl[p0:]
                s = s[:pa-ln] + r*ln + s[pa:]
                # print(j, i,  'pa=', pa, 'p0=', str(p0).ljust(3, ' '),   '-',
                #       'sl=', str(sl).ljust(24, ' '), 'f0=', f0,  '     s=', s)
                f0 = sl.find(i)
                p0 = f0 + ln
                pa = pa + p0
                # print(f0, p0, pa, sl[p0:])
        return s

# print(l)
print()
# print(replace_all('0123python4PYTHON5PyThoN78', l_for))
# for i in l_for:

print(replace_all(l, l_for))


def all_words(word):
    l = [word[0], word[0].swapcase()]
    print(l)
    for char in word[1:]:
        l1, l2 = [chars + char for chars in l], [chars + char.swapcase()

                                                 for chars in l]
        print('cr=', char)
        l = l1 + l2
        print('l=', l)
        print(l1, l2)
    return set(l)


print(all_words('wol'))
