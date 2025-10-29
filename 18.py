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
    print(sum(int(w) for line in f for w in line.split() if w.isdigit()))
f.close()


f = open('c:/1/prices.txt', encoding='utf-8')
print(sum(map(lambda x: int(x[1])*int(x[2]), (l.split() for l in f))))
f.close()

f = open('c:/1/prices.txt', encoding='utf-8')
print(reduce(lambda x, y: x + int(y[1])*int(y[2]), map(str.split, f), 0))
f.close()
