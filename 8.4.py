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


my_list = [1, 2, 5]
# my_list = [1, [4, 4], 2]

print('==', recursive_sum(my_list))

print()

# l_out = []


def linear(n):
    l_out = []

    def lsn(n):
        if isinstance(n, int):
            return n

        for i in n:
            k = lsn(i)
            if k:
                l_out.append(k)
    lsn(n)
    return l_out


def linear(li):
    res = []
    print(id(res))
    for elem in li:
        if isinstance(elem, list):
            res.extend(linear(elem))
        else:
            res.append(elem)
    return res


def linear(data):
    total = []

    def loc(data):
        if type(data) == int:
            total.append(data)
            return
        if type(data) == list:
            for i in data:
                loc(i)              # рекурсивный случай
    loc(data)
    return total


# my_list = [[3, 2, 5345, 65, 7, 777, 0, 43, 65, 754, 3, 1, 2]]
my_list = [3, 1, [4, 2]]
# my_list = [3, [4], [5, [6, [7, 8]]]]

print('=', linear(my_list))


# def tt1(l):
#     return l

# l = [1, 2]
# print(id(l), id(tt1(l)))

print()


def get_value(d, key):
    res = ''
    if key in d:
        res = d[key]
        return res

    for k in d:
        if isinstance(k, dict):
            get_value(k, key)

    return res


data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {
    'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print('res=', get_value(data, 'cityName'))
