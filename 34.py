
t = dict((x, y) for x in [1, 2] for y in [3, 4])
print(t)

l = ['Сергей Карандаш 3',
     'Андрей Тетрадь 5',
     'Юлия Линейка 1',
     'Сергей Ручка 2',
     'Юлия Книга 4',
     'Юлия Книга 4',
     ]

print(l)
d = {}
for i in l:
    x, y, z = i.split()
    # d[x][y] = d.setdefault(x, {}).setdefault(y, 0) + int(z)

    # d.setdefault(x, {})
    d[x] = d.get(x, {})
    d[x][y] = d[x].get(y, 0) + int(z)

    print(x, y, z)
print(d)
