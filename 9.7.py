

import itertools
x = 10


def f(x):
    c = x
    return c


b = f(x)

print(id(x), id(b), id(f(x)), id(f))


def print_given(*args, **kwargs):
    for i in args:
        print(f'{i} {type(i)}')
    for i in kwargs:
        print(f'{i} {kwargs[i]} {type(kwargs[i])}')


print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two=2, one=1, three=3)

number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
print(*sorted(number_names, key=lambda x: number_names[x]))

print()


def make_greeter(prase):
    prefix = ''  # prase + f', - '
    n = 1

    def greeter(name):
        nonlocal n
        n += 1
        return prase + name + '--' + str(n)

    return greeter


a = make_greeter('aa')
b = make_greeter('bb')


print(a('1'), a.__closure__)
print(a('2'), a.__closure__)

# print(make_greeter('aa')('1'), make_greeter('aa').__closure__)
# print(make_greeter('aa')('2'), make_greeter('aa').__closure__)

print(id(a))
print(id(b))

print()


# def f1(x):
#     return x


# def f2(x):
#     return x


# print(id(f(2)))
# print(id(f(3)))


def composition(f, g):
    def h(*x):
        return f(g(*x))
    return h


# h = composition(lambda x: x**2, lambda x: x + 1)
# print(h(5))

h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print('=', h(5))


print(list(itertools.starmap(lambda x, y, z: x+y+z, [(1, 2, 3), (2, 3, 4)])))

# i = (str, str)
# print(list(itertools.starmap(composition(*i), [(1, 2), (2, 3)])))


# def sandwich(f):
#     def wrapper(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         p = f(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')

#         return p
#     return wrapper


def sandwich(func):
    def wrapper(*args, **kwargs):
        try:
            print('---- Верхний ломтик хлеба ----')
            return func(*args, **kwargs)
        finally:
            print('---- Нижний ломтик хлеба ----')

    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
print()


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())

# def add_ingredients(*args):
#     print('--', args)
#     print(*args)


# add_ingredients('томат', 'салат', 'сыр', 'бекон')
# add_ingredients(*['томат', 'салат', 'сыр', 'бекон'])

def prn_upper(f):
    def wrapper(*args, **kwargs):
        print(*map(lambda i: str(i).upper(), args),
              sep=f'{kwargs['sep'].upper() if kwargs.get('sep') else ''}', end=f'{kwargs['end'].upper() if kwargs.get('end') else ''}')
    return wrapper


prn = prn_upper(print)


prn('aaa', 222, 333, sep='xxx', end='t')
