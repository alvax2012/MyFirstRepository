l = [1, 2, 3]

print(l)

d = 17
print(d)


def aa():
    # global l
    l = []
    l.append(4)
    l[0] = 99
    d = 9
    print('=', l, d)
    # d = 18


aa()

print(l, d)

l = [['Сергей', 'Карандаш', 3], ['Андрей', 'Тетрадь', 5], ['Сергей', 'Тетрадь', 5]]
sales = {}
for _ in l:
    name, item, count = _
    sales[name][item] = sales.setdefault(
        name, {}).setdefault(item, 0) + int(count)

print(sales)


a = [1, 2]
b = [7]*3

l = [a, a, b, b]
b = 7
for i in l:
    print(id(i))
l1 = [2, 3]
print('--', id(l1))
# l1[0] = 7
l1.append(22)
print('--', id([1]*2), id([1]*2))
m = 7
l3 = []
print(l3)


l3 = [1]*2
l3[0] = [1]
l3[1] = [1]
print(',', l3)
for i in l3:
    print(id(i))

l111 = [1, 2]
l222 = [1, 2]
print('--', id(l111), id(l222))
