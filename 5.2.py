import sys

num2 = [102, 1]
print(id(num2))
num = num2  # [102, 1]
num2.append(3)  # = [102, 1, 7]
print(id(num), id(num2))
print(num, num2)

# num2 = 4
# print(id(num2))
# print(id(num))

num22 = 1  # [102, 1]
print(id(num22))
num11 = num22  # [102, 1]
num22 = 11  # [102, 1]
print(id(num11), id(num22))

print('1=', id(list))


data = ['b', 'e', 'e', 'g', 'e', 'e', 'k']
print(id(data))
data[0] = 'B'
print(id(data))

print(data)


def change_list():
    global nums
    nums = [10]
    return data


nums = [1, 2, 3]
change_list()

print(nums)


data = (1, [10, 20], 'beegeek')

data[1][0] = 40

data[1][1] = 50


print(data)


data = (1, [10, 20], 'beegeek')
data[1].append([40, 50])

print(data)

s = '1'
for i in range(2):
    s += '3'


s = '-31x+52=+67-28x'
l = []

res = []
d = {}
l = s.split('=')


def equ_l(l, flg=False):
    s = l[0]
    k = -1 if flg else 1
    for i in l[1:]:
        if i.isdigit() or i in ['+', '-']:
            s += i
        elif i in ['+', '-']:
            s = i
        elif i.isalpha():
            d[i] = d.get(i, 0) + int(s)*k
            s = ''
    d[None] = d.get(None, 0) + int(s)*k
    return d


# print(equ_l(l[0]))
# print(equ_l(l[1]))


l = [i for i in range(2)]
print(l)


def f1():
    print(7)


def f1(x):
    return 3


print(f1(2))

for i in range(7):
    if i == 3:
        continue
        print(3)
    print(i)


class C:
    def ff():
        print(99)


# c1 = C()
C.ff()

l = []
b = l
print('-', sys.getrefcount([]))

t = 22
print(f'{t}', end='%')

n = True and False + 1
print(n, type(n))

t1 = [1, 2]
t = [1, 2]
l = t*1
print('l=', l)


my_list = [[0] * 3 for _ in range(4)]
my_list[0][0] = 17
print(my_list)


numbers = []
numbers[100:] = (1, 2, 3)
print(numbers[0], numbers[1], numbers[2])  # 1 2 3


numbers = [1, 2, 3, 4]

# numbers.extend([])
numbers.append([])

print(len(numbers), numbers)

numbers = (1.2,)

print(numbers * 2)

numbers = 99, 10

print(numbers)

numbers = tuple([1, 2, 3, 4])

numbers = (100,) + numbers[1:]

print(numbers)      # (100, 2, 3, 4)


my_set = set()

for i in range(3):
    my_set.add(i + 1)
    my_set.discard(i - 1)
    print(i, i + 1, i - 1, my_set)

print(len(my_set))

d = {}
sh = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
s = 'I love Python =)'

for i in range(65, 91):
    d[i] = sh[i-65]

print(d)
out = ''
for i in s:
    if i.isalpha():
        i = d[ord(i.upper())]
    out += i
print(out)
