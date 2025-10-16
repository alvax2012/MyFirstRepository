def matrix(n=1, m=None, value=0):
    s = []
    if not m:
        m = n
        matrix.__defaults__
    for i in range(n):
        s.append([])
        for j in range(m):
            s[-1].append(value)
    m = 0
    # print('--' if m else n)
    return s


print(matrix(4, 3, 9))

print()


def greet(nm, *args):
    args = list(args)
    args.insert(0, nm)
    print(args)
    return f'Hello, {' and '.join(args)}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))

print()


def print_products(*args):
    val = tuple(_ for _ in args if type(_) is str and _)
    d = dict(zip((_ for _ in range(len(val))), val))
    [print(f'{key + 1}) {val}')
     for key, val in d.items()] if val else print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',),
               'Яблоки', '', 'Макароны', 5, True)
print()
print_products([4], {}, 1, 2, {'Beegeek'}, '')


def info_kwargs(**kwargs):
    [print(key, ': ', val, sep='') for key, val in sorted(kwargs.items())]


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

print(type(sum))
print(sum)

numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10,
                                                                                                            20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]


def sr(num):
    return sum(num) / len(num)


# print(sr(numbers[0]))
print('-', min(numbers, key=sr), max(numbers, key=sr), sep='\n')

# cnt = 1
# cnt1 = 3
# # cnt2 = 0
# # cnt3 = 6
# for i in range(3, 7):
#     # cnt1 += 1
#     cnt2 = 0
#     for j in range(5):
#         # cnt2 += 1
#         # print('cnt1', cnt1, 'cnt2', cnt2)
#         cnt3 = 7
#         for k in range(7, 10):
#             print('cnt1', cnt1, i, 'cnt2', cnt2, j, 'cnt3', cnt3, k, cnt)
#             cnt3 += 1
#             cnt += 1
#             # print('cnt1', cnt1, 'cnt2', cnt2, 'cnt3', cnt3)
#         cnt2 += 1
#     cnt1 += 1
# print('cnt=', cnt, cnt1, cnt2, cnt3)

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100),
           (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]


def mm(num: tuple):
    return min(num) + max(num)


numbers.sort(key=mm)


print(numbers)


l = 'a'
print(l[::-1])


def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a * x**2 + b * x + c

    return square_polynom


print()
numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013,
           23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def rnd(a):
    def rn(x):
        return round(x, a)
    return rn


f = rnd(a=2)


def get_round(x):
    return round(x, 2)


print(*map(f, numbers))
print(*map(get_round, numbers))


def map1(fun, i):
    l = []
    for _ in i:
        l.append(fun(_))
    return l


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


def filter1(fun, i):
    l = []
    for _ in i:
        if fun(_):
            l.append(_)
    return l


def is_pr(i):
    return i % 5 == 2 and len(str(i)) == 3


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394,
           560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]


def pw3(x):
    return pow(x, 3)


print(*map1(pw3, filter1(is_pr, numbers)), sep='\n')
