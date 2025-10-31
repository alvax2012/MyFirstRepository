from operator import mul
from functools import reduce
f = open('c:/1/nums.txt', encoding='utf-8')
# print(sum(map(int, list(f))))
# print(list(f))

# print(reduce(lambda x, y: x + int(y) if y != '' else 0,map(lambda x: x.strip(), f.readlines()), 0))

# print(sum(list(map(lambda x: int(x) if x != '' else 0,map(lambda x: x.strip(), f.readlines())))))

print(sum(list(map(int, filter(None, map(str.strip, f.readlines()))))))

# print(sum(map(int, f.read().split())))

# print(sum(list(map(lambda x: int(x) if x != '' else 0, list(f.read().split())))))
f.close()

print(str('') or 0)


with open('c:/1/nums1.txt') as f:
    print(sum(int(line.strip()) for line in f if not line.isspace()))
f.close()


with open('c:/1/nums1.txt') as f:
    print(type(int(w) for line in f for w in line.split() if w.isdigit()))
f.close()


f = open('c:/1/prices.txt', encoding='utf-8')
print(sum(map(lambda x: int(x[1])*int(x[2]), (l.split() for l in f))))
f.close()

f = open('c:/1/prices.txt', encoding='utf-8')
print(reduce(lambda x, y: x + int(y[1])*int(y[2]), map(str.split, f), 0))
f.close()

with open('c:/1/prices.txt') as file:
    print(sum(map(lambda line: mul(*map(int, line.split()[1:])), file)))
file.close()

p1 = 'c:/1/prices.txt'
with open(p1) as f:
    print(sum(eval('*'.join(s.split()[1:])) for s in f))
f.close()


l = [1, 1, 3, 4, 4]

# d = dict(zip(range(len(l)), l))
# print(d)
d = {}

for _ in l:
    d[_] = d.get(_, 0) + _

print({})

file = open('c:/1/seek.txt', 'r', encoding='utf-8')
print(file.tell())
line1 = file.readline()
print(file.tell())

file.close()

p1 = 'c:/1/'
print('-'*50)
file = open(p1 + 'lines.txt', encoding='utf-8')

# file.seek(0)
# print('1.', file.readline())
t = file.readline()
print('-', file.tell(), t)
file.close()


with open(p1 + '1.txt', encoding='utf-8') as file:
    print('Repeat after me:', file.readline().strip())
    for line in file:
        print(line.strip() + '!')

print('--')

with open(p1 + 'text.txt', encoding='utf-8') as f:
    print(*[list(map(lambda x: x[::-1], l.split()))[::-1]
          for l in f], sep='\n')
    # [print(' '.join(l.split()[::-1])) for l in f]
print('-')

with open(p1 + 'text.txt') as f:
    print(f.read()[::-1])

with open(p1+'text.txt') as file:
    print(*[i[::-1] for i in file.readline().split()[::-1]])


with open(p1+'data.txt') as f:
    print(*f.readlines()[::-1], sep='')

with open(p1 + 'lines.txt', encoding='utf-8') as f:
    print([l for l in filter(lambda x: x, f)])
