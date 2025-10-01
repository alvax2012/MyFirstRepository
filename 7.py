from decimal import *
import random
import string
from decimal import *


def generate_password(length):
    l = []
    for _ in range(length):
        while True:
            s = random.choice(string.ascii_letters+string.digits)
            if s not in 'lLiIoO0':
                break

        l.append(s)
    return l
    # print(string.ascii_letters)
    # print(string.ascii_uppercase)
    # print(string.ascii_lowercase)
    # print(string.digits)


def generate_passwords(count, length):
    [print(*generate_password(length)) for _ in range(count)]


n, m = 9, 7
generate_passwords(n, m)

print()

n = 10      # количество испытаний
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # print('--', x, y)
    if x**2 + y**2 <= 1:
        k += 1
        print(x, y)

print('pi', (k/n)*s0)

# abs = 3
l = [[1, 2, 3]]*3
l[0][0] = 9
print(l)

a = 13
if a > 10:
    t = 1

if a > 2:
    t = 2
else:
    t = 3
print(t)

for i in 1, 2, '3':
    print(i, end='')


x = 3


num = 0.1 + 0.1 + 0.1
a = float(0.3)
b = float(0.3)
if num == b:
    print('YES')
else:
    print('NO')
print(num, -7 // 4)

s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
s = [Decimal(_) for _ in s.split()]
print(sum(s))
s.sort(reverse=True)
print(*s[:6])


num = Decimal('0.1244354689')
t = num.as_tuple()
if abs(t[2]) < len(t[1]):
    print(max(t[1])+min(t[1]))
else:
    print(max(t[1]), t)
