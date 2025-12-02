en = 'AaBCcEeHKMOoPpTXxy'

ru = 'АаВСсЕеНКМОоРрТХху'


s1, s2, s3 = 'Р', 'О', 'А'
l = (s1, s2, s3)
print(any(map(lambda x: x in en, l)))

t = [1, 2].reverse()
print([1, 2][::-1], t)


n, x, y, a, b = [9, 3, 6, 5, 8]
l = [int(_) + 1 for _ in range(n)]
# l = l[:x-1] + l[x-1:y][::-1] + l[y:]

# l = l[: y] + l[y:][::-1]

l = l[:x-1] + l[x-1:y][::-1] + l[y:]
l = l[:a-1] + l[a-1: b][::-1] + l[b:]
print(*l)

nums = list(range(1, n + 1))

nums[x - 1:y] = reversed(nums[x - 1:y])
# nums[a - 1:b] = reversed(nums[a - 1:b])

nums[x - 1:y] = [9, 9]
d = nums[x - 1:y]

print(*nums, d)

s = '3 1 3 2 3 11 4 3 5 3 6 3 7 3 8 3 9 3 10 3 11 3 3 12 13 1'
t = s.split()
l = map(int, t)
d = {}
for i in l:
    d[i] = d.get(i, 0) + 1


print(sorted(map(lambda x: x[0], filter(lambda i: i[1] > 1, d.items()))))

print(sorted([key for key, val in d.items() if val > 1]))

n = 20
# l = []
print(l)
d = {}
d1 = {}
for i in list(range(1, n+1)):
    k = sum(map(int, list(str(i))))
    d[k] = d.get(k, []) + [i]
    d1[k] = d1.get(k, 0) + 1

l = max(len(i) for i in d.values())

print(d, d1)

print(len((max(d.values(), key=len))))

print(max(d1.values()))


def sm(n):
    s = 0
    while n > 0:
        l = n % 10
        n //= 10

        s += l
        print('n, l, s =', n, l, s)
    return (s)


print('sm=',  sm(1274))


n = 6


l = ['испанский, португальский, эсперанто, французский',
     'французский, испанский, эсперанто',
     'португальский, эсперанто, французский, испанский',
     'французский, английский, болгарский, испанский, эсперанто',
     'эсперанто, английский, русский, испанский, французский',
     'python, испанский, эсперанто, латышский, польский, французский']

m = set(l[0].split(', '))
# m &= set(l[1].split(', '))

for _ in l[1:]:
    m &= set(_.split(', '))

if m:
    print(*sorted(m), sep=', ')
else:
    print('Фильм снять не удастся')
print(m)


def max_rn(l: list):
    res = 0
    if l[0] != 0:
        return 0
    for i in range(1, len(l)):
        res = l[i]
        if abs(res-l[i-1]) > 1:
            res = l[i-1]
            # print(res, l[i-1])
            break

    return res+1
    # print(i-1, i, l[i-1], l[i])


l = [2, 5, 6, 7, 8]

print(max_rn(l))

l = [1, 2]


def tt(l: list):
    l = l + [9]
    # l[0] = 8


t = 'qwe123'
t1 = ''.join(i for i in t if i.isalpha())
print(l, tt(l), t1)

d = {1: 2, 2: 3}
if d.setdefault(2):
    print('+', d)
print(d)
