def find_key(data, key):
    if key in data:
        return data[key]                # базовый случай

    for v in data.values():
        if type(v) == dict:
            value = find_key(v, key)    # рекурсивный случай
            if value is not None:
                return value


info = {'name': 'Alyson',
        'birthday': {'day': 24, 'month': 'March', 'year': 1974},
        'family':   {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}

print(find_key(info, 'year'))
print(find_key(info, 'father'))


def recursive_sum(n):
    s = 0

    if type(n) == int:
        return n

    for i in n:
        s += recursive_sum(i)
    return s


# my_list = [1, 2, 5]
my_list = [1, [4, 4], 2]

print('==', recursive_sum(my_list))

print()


def linear(my_list):


my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))
