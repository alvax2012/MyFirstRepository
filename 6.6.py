from collections import OrderedDict

# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
#                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
data = OrderedDict(key1='value1', key2='value2', key3='value3')
print('---', data)
for k in list(data):
    data.move_to_end(k, last=False)
    # print(k)
# data.sorted_keys = lambda: sorted(data.keys(), reverse=True)
# data.sorted_keys()
print('===', data)

print()

letters = OrderedDict(e=2, d=4, a=1, c=3)

letters.sorted_keys = lambda: sorted(letters.keys())

print(letters)
print(letters.sorted_keys())

letters['b'] = 5
print(letters)
print(letters.sorted_keys())

# for key in letters.sorted_keys():
#     print(key, '->', letters[key])


print(letters.__dict__)
print(letters)


print()

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                   'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

l = list(data)
n = len(l)
for i in range(int(n/2)):
    print(l[i], l[n-i-1])
    data.move_to_end(l[i])
    data.move_to_end(l[n-i-1])

print(data)


print()

# TEST_2:  ('Mercury', 1) ('Venus', 2) ('Earth', 3) ('Mars', 4)


def custom_sort(data, by_values=False):
    if by_values:
        for k, v in sorted(data.items(), key=lambda x: (x[1], x[0])):
            data.move_to_end(k)
            # print(k)
    else:
        for i in sorted(data):
            data.move_to_end(i)


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data)

print(*data.items())
