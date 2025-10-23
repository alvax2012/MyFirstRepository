from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88,
          4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo',
         'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

# Исправьте этот код
i = len(floats)
map_result = list(map(round, map(pow, floats, [2] * i), [1]*i))
filter_result = list(filter(lambda name: len(
    name) > 4 and name == name[::-1], words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)


data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]


l = list(sorted(map(lambda x: x[0], filter(
    lambda x: x[1] > 10**7 and x[2] == 'primary', data)), key=lambda x: x))


print(reduce(lambda x, y: f'{x} {y},', l, 'Cities:')[:-1])

print('---')


is_non_negative_num1 = (lambda x:  ''.join(
    [_ for _ in x if _ in '.' or 48 <= ord(_) <= 57]).replace('.', '', 1))('123')
print('+++', is_non_negative_num1)


def is_non_negative_num(x): return x.replace('.', '', 1).isdigit()


print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))


words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware',
         'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

print(*sorted(filter(lambda x: len(x) == 6, words), key=lambda x: x))


numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35,
           64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]

print(*map(lambda x: x // 2 if not x % 2 else x, filter(lambda x: not x %
      2 or x <= 47, numbers)))
# print(*filter(lambda x: not x % 2, numbers))


data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'),
        (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]


def fs(x): return x[1][-1]


print(fs, id(fs), type(fs), sep='\n')

# print(*map(lambda x: f'{x[1]}: {x[0]}',
#      sorted(data, reverse=True, key=lambda x: x[1][-1])), sep='\n')

data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом',
        'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

print(sorted(sorted(data), key=lambda x: len(x)))


mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772,
              'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

print(max(mixed_list,  key=lambda x: x if isinstance(x, (int, float)) else 0))
print(*sorted(filter(lambda x: isinstance(x, int), mixed_list)))
print(max(mixed_list, key=lambda x: (isinstance(x, int), x)))


mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse',
              78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]

print(sorted(mixed_list, key=lambda x: (type(x) == str, x)))

print(sorted(mixed_list, key=lambda x: (True, x) if type(x) is str else (False, x)))

print()
s = '244 11 120'
# s = (int(_) for _ in s.split())
# s = map(int, s)
print(s)
m = 255
print(*map(lambda x: m-x, map(int, s.split())))

s = '2 4 3'
l = list(map(int, s.split()))
x = 10
l1 = list(map(int, s.split()))[::-1]
d = tuple(zip(range(len(l)), l1))


def mn(l):
    # mmn1 = map((lambda y: y*x), l)
    # mmn = mmn1(x)
    def mmn(x):
        return map(lambda y: x*y, l)
    return mmn


# f = mn(l)
# print(*f(x))

print(l)
# print(*d)


def evaluate(x, d):
    return reduce(lambda x, y: x + y, map(lambda y: y[1]*pow(x, y[0]), d), 0)
    # return map(lambda y: y*pow(y, x), l)


print('--+', evaluate(x, d),  l)
print(d)
