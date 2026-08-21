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
print()


def get_value(d, key):
    if key in d:
        return d[key]

    for k in d:
        if isinstance(d[k], dict):
            res = get_value(d[k], key)
            if res:
                return res

    # return res


data = {'firstName': 'Тимур', 'lastName': None, 'birthDate': {'day': 10, 'month': 'October', 'year': 1993}, 'address': {
    'streetAddress': 'Часовая 25, кв. 127', 'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print('res=', get_value(data, 'cityName'))


print()


def get_all_values(d, key):
    m = set()

    def dm(d, key):
        if key in d:
            m.add(d[key])

        for k in d:
            if isinstance(d[k], dict):
                res = dm(d[k], key)
                if res:
                    m.add(d[key])
    dm(d, key)
    return m


my_dict = {

    'Timur': {'hobby': 'math'},
    'Dima': {
        'hobby': 'CS',
        'sister':
        {
            'name': 'Anna',
            'hobby': 'TV',
            'age': 14
        }
    }
}

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))


def get_all_values(data, key):
    values = set()
    if key in data:
        values.add(data[key])
    for item in data.values():
        if isinstance(item, dict):
            values |= get_all_values(item, key)
    return values


print()


def dm(d):
    # res = ''
    if isinstance(d, tuple) and not isinstance(d[1], dict):
        # return f'{d[0]}: {d[1]}\n'
        return f'{d[0]}: {d[1]}'
    elif isinstance(d, tuple) and isinstance(d[1], dict):
        for i in sorted(d[1].items()):
            # res += d[0] + '.' + dm(i)
            print(d[0], dm(i), sep='.')
    else:
        for i in sorted(d.items()):
            res = dm(i)
            if res:
                print(res)
    # print('===', res)
    # return res


def dict_travel1(d):
    res = ''
    k = ''
    if isinstance(d, tuple) and not isinstance(d[1], dict):
        # nonlocal k
        return f'{k}{d[0]}: {d[1]}\n'
    elif isinstance(d, tuple) and isinstance(d[1], dict):

        k += '.' + d[0]
        for i in d[1].items():
            res += dict_travel(i)
        return res
    else:
        k = ''
        for i in d.items():
            res += dict_travel(i)
            # return res
    print(res)


def dict_travel2(d):

    k = ''

    def dm(dct):
        res = ''
        k = ''

        if isinstance(dct, tuple) and not isinstance(dct[1], dict):
            # nonlocal k
            return f'{dct[0]}: {dct[1]}\n'
        elif isinstance(dct, tuple) and isinstance(dct[1], dict):
            return dm((dct[0] + '.', dm(dct[1])))

        for i in dct.items():
            # k = i
            res += dm(i)
        return res

    print(dm(d))


def dict_travel(dct):
    res = {}

    def dm(dct, p=''):
        if not isinstance(dct, dict):
            print(f'{p}: {dct}')
            res[p] = dct
            return

        for i in sorted(dct):
            dm(dct[i], f'{p}.{i}' if p else i)

    dm(dct)
    print(res)


def dict_travel(d):
    res = {}
    pp = []

    def dm(dct):
        nonlocal pp
        # pp = []
        if isinstance(dct, str) or isinstance(dct, int):
            res['.'.join(pp)] = dct
            # p = ''
            return

        for i in sorted(dct):
            pp.append(i)
            dm(dct[i])
            pp.pop()

    dm(d)
    [print(f'{k}: {v}') for k, v in res.items()]


def dict_travel(d):
    p = []

    def dm(dct):
        if isinstance(dct, str) or isinstance(dct, int):
            print('+'.join(p), dct)
            return

        for i in sorted(dct):
            p.append(i)
            dm(dct[i])
            p.pop()

    dm(d)


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}


# data = {'b': 2, 'c': 1,  'a': 1}
# data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

# data = {'a': 111}
dict_travel(data)

# dm(data)
# print(dm(data))

# l = [(3, 4), (1, 5), (3, 2), (7, 5)]
# print(sorted(l, key=lambda x: (-x[1], -x[0])))
