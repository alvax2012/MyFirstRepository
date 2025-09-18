import random
import string
m1 = random.sample(range(1, 76), 25)
# print(len(m) == len(set(m)))
# m = [*range(1, 76)]
# random.shuffle(m)
# m = m[:26]
# print(m1)
s12 = [m1[_*5:_*5+5] for _ in range(5)]
# s[2][2] = 0
# print('-', s12)

# s12 = [['0'.ljust(2) if row == 2 and col == 2 else str(s12[row][col]).ljust(1)
#        for row in range(5)] for col in range(5)]
print('--', s12)
[print(*row, sep=' ') for row in s12]
