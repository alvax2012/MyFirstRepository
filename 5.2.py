

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
r = ''
l = []

res = []
res_p = []

l = s.split('=')
for i in l[0]:
    if not i.isdigit() and i not in ['+', '-']:
        p = i
        break

flg = False
s1 = l[0][0]
for i in l[0][1:]:
    # s1 = l[0][0]
    # res.append(s1)
    if i.isdigit() and flg:  # i not in ['+', '-', '='] and
        s1 += i
        # res.append(s1)
    else:
        if i.isalpha():
            res.append(s1)
            not flg
            # continue
        elif i in ['+', '-']:
            s1 = 0
            not flg
            # res.append(s1)

print(res)
