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
