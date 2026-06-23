from collections import ChainMap

fruits = ChainMap({'apple': 10, 'banana': 20},
                  {'lemon': 10, 'pineapple': 15},
                  {'kiwi': 15, 'lime': 5})

fruits.maps.append({'mango': 20, 'melon': 20})

del fruits.maps[0]
del fruits.maps[1]

print(fruits)


def get_all_values(chainmap: ChainMap, key):
    s = set()
    l = chainmap.maps
    for i in chainmap.maps:
        if i.get(key):
            s.add(i[key])
    return s


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

result = get_all_values(chainmap, 'name')

print(result)
print(*sorted(result))

print()


def deep_update(chainmap: ChainMap, key, value):
    if not chainmap.get(key):
        chainmap[key] = value
    print(chainmap)
    for i in chainmap.maps:
        if i.get(key):
            i[key] = value
        # .setdefault(key, value)
        # print(i)


chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
chainmap = ChainMap({'name1': 'Tanya'}, {
                    'name2': 'Arthur'}, {'name1': 'Timur'})
# deep_update(chainmap, 'name', 'Dima')

# print(chainmap['name'] if 'name1' in chainmap else '---')
chainmap['name12'] = '00'

print(chainmap)
for i in chainmap:
    print(i)


def get_value(chainmap: ChainMap, key, from_left=True):
    if key in chainmap:
        if not from_left:
            chainmap.maps.reverse()

        return chainmap[key]


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

# print(get_value(chainmap, 'name'))
s = 0
t = '2.6'
try:
    s += int(t)
    print(111)
except ValueError:
    print(222)
except ValueError:
    print(333)
