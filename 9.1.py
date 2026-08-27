# for i in range(97, 123):
#    print(chr(i))

import string


def convert(n):
    d = {1: bin, 2: oct, 3: hex}
    l = []
    # return bin(n)[2:], oct(n)[2:], hex(n)[2:]
    for i in range(1, 4):
        l.append(d[i](n)[2:])

    return tuple(l)


print(convert(-24))


films = {1: {'imdb': 8.8, 'kinopoisk': 8.3},
         2: {'imdb': 7.3, 'kinopoisk': 7.6},
         }
# m = min(sum(v.values()) for v in films.values())
m = min(films, key=lambda i: sum(films[i].values()))
print(m)
# *filter(lambda v: sum(films[v].values()) == m, films),
# t = [k for v in films.values() for k in v.items()]
# print(t)


def dfilm(d):
    p = 20

    def dm(d):
        s = 0
        nonlocal p
        for i in d:
            # s += dfilm(v, s)

            if isinstance(d[i], dict):
                dm(d[i])
                # return s
                # dfilm(v, s)
            else:
                s += d[i]
        if s and s < p:
            p = s
        return s

    dm(d)
    return p


print(dfilm(films))


print(type(repr([1, 2, 3, 4])))


def hash_as_key(data):
    d = {}
    for i in data:
        h = hash(i)

        if h in d:
            if not isinstance(d[h], list):
                d[h] = [d[h]]
            d[h].append(i)
        else:
            d[h] = i
    return d


data = [-1, -2, 3]
# data = [1, 2, 3, 4, 5, 5]
data = [5, 5, 5]

print(hash_as_key(data))


s1 = '[[1, 2], [3, 4], [5, 6]]'
# s1 = "{'Arthur', 'Timur', 'Anri', 'Ruslan', 'Dima'}"
# s1 = "('black', 'blue', 'red', 'orange', 'green', 'gray')"

# res = ''
s = eval(s1)
if isinstance(s, list):
    res = s[-1]
elif isinstance(s, set):
    res = len(s)
else:
    res = s[0]
print(res)


f1 = '2*x**2 + 5*x + 7'
n1 = list(map(int, '-1 5'.split()))
l = []
for x in range(n1[0], n1[1]+1):
    l.append(eval(f1))
    # print(x, eval(f1))

s_out = f'''
Минимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно {min(l)}
Максимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно {max(l)}
'''

print(s_out)

a, b = map(int, '12')

print(a, b)


# анонимные функции являются выражениями, то есть их можно сразу вызывать в момент определения


numbers = filter(lambda x: x > 0, [-3, -2, -1, 0, 1, 2, 3, 1])

if 1 in numbers:
    print('bee')
if 1 in numbers:
    print('geek')


data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [
    1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
# data = [1, 2, '14']
print(*map(int, filter(lambda x: isinstance(x, (int, float)), data)))

numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 9, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396,
           2842, -3879, -3824, -9, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

print((map(lambda x: x**2, filter(lambda x: x % 9 == 0 and x // 100 == 0, numbers))))

dd = [-90, 1, 90]
print(*filter(lambda x: x % 9 == 0 and -100 < x < 100 == 0, dd))
print('==', *filter(lambda x: abs(x) // 100 ==
      0 and abs(x) // 10 > 0 and x % 9 == 0, dd))


l = []

for i in range(3):
    l.append([7]*3)
    print(id(l[i]))

print(l)

l1 = [9]*4

for i in range(3):
    l1[i] = [5]*5
    print(id(l1[i]))

print(l1)

t = [0]*2
print(id([0]*2), id([0]*2), id(t))
print(id([]), id([]))

l2 = [1]
print(id(l2))
l2.append(2)
print(id(l2))

x = 0
print(id(x))
# x = 3
print(id(x))

l3 = [1]
print(id(l3))
l3 = l3 + [2]
print(id(l3))


names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения',
         'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']


print(
    *sorted(filter(lambda x: x[0] in 'АМ' and len(x) > 4, map(str.capitalize, names))))


l = [1, 2]
print(id(l))

# l = [1, 2]
l += [9]
print(id(l), id(l[:]))


def fib(n): return 1 if n == 1 else n*fib(n-1)


print(fib(3))


def print_operation_table(op, row, col):
    l = []
    for i in range(1, row + 1):
        l.append([])
        for j in range(1, col + 1):
            # l[-1].append(op(i, j))
            l[i-1].append(op(i, j))
            print(str(l[i-1][j-1]).rjust(3, ' '), end=' ')
        print()
    print(l)  # op(row, col))


def print_operation_table(op, row, col):
    l = []
    for i in range(1, row+1):
        l.append([i]*col)
        print(*map(lambda i, j: str(op(i, j)).ljust(3, ' '),
              l[i-1], range(1, col+1)))


print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)
print_operation_table(pow, 5, 10)


def verification(login, password, success, failure):
    string.digits
    string.ascii_letters
    string.ascii_lowercase
    string.ascii_uppercase


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


verification('timyrik20', 'Beegeek314', success, failure)
