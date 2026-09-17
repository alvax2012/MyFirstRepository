
import sys
import itertools
import time

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
        # print('1=', args, kwargs)
        # print('2=', *args, **kwargs)
        # f(*args, sep=f'{kwargs['sep'].upper() if kwargs.get('sep') else ''}',
        #   end=f'{kwargs['end'].upper() if kwargs.get('end') else ''}')
        f(*map(lambda i: str(i).upper(), args),
          sep=f'{kwargs['sep'].upper() if kwargs.get('sep') else ''}', end=f'{kwargs['end'].upper() if kwargs.get('end') else ''}')
    return wrapper

# f(*map(lambda i: str(i).upper(), args),
#           sep=f'{kwargs['sep'].upper() if kwargs.get('sep') else ''}', end=f'{kwargs['end'].upper() if kwargs.get('end') else ''}')


prn = prn_upper(print)


prn('aaa', 222, 333, sep='xxx', end='t')
print()


# for i in range(5):
#     print(i, end=" ")
#     sys.stdout.flush()  # Явно сбрасываем буфер после каждой печати
#     time.sleep(1)


def decorator(func):
    def wrapper(*args, **kwargs):
        new_args = map(lambda x: x.upper() if isinstance(x, str) else x, args)
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        func(*new_args, **kwargs)
    return wrapper


old_print = print


@decorator
def print(*args, **kwargs):
    old_print(*args, **kwargs)


print()
print('bbb', 222, 333, sep='xxx', end='t')
print = old_print
print()
print()
print('==')


def decorator(func):
    def wrapper(*args, **kwargs):
        args = [str(arg).upper() for arg in args]
        kwargs = {k: v.upper()
                  for k, v in kwargs.items() if k in ['end', 'sep']}
        func(*args, **kwargs)
    return wrapper


print = decorator(print)
print()
print('ccc', 222, 333, sep='xxx', end='t', end1='t')

print = old_print
print()


def introduce(f):
    def wrapper(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return wrapper


@introduce
def f1(a):
    return a


print(f1(10), f1.__name__)
print()


def do_twice(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return f(*args, **kwargs)
    return wrapper


@do_twice
def beegeek():
    print('beegeek')
    return 'beegeek'


print(beegeek())


print()


def reverse_args(f):
    def wrapper(*args, **kwargs):

        return f(*args[::-1], **{i: kwargs[i] for i in sorted(kwargs, reverse=True)})
    return wrapper


# @reverse_args
# def power(a, n):
#     return a ** n

# print(power(2, 3))

@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))


@reverse_args
def operation(a, b, name):
    return a // b + name


print(operation(10, 90, name=1))

print()

s = [100, 25, 505, 481, 1, 2401]
for i in s:
    print(i % 100, i % 100 % 10, f"{i} -> {max(str(i), key=int)}",
          max(str('123'), key=int))
    # print(i % 100)


def exception_decorator(f):
    def wrapper(*args, **kwargs):

        try:
            return f(*args, **kwargs), 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


@exception_decorator
def f(x):
    return x**2 + 2*x + 1


print(f(7))


def takes_positive(f):
    def wrapper(*args, **kwargs):
        if not all([isinstance(i, int) for i in args]) or not all([isinstance(i, int) for i in kwargs.values()]):
            raise TypeError  # (' аргумент не является целым числом')
        if not all([i > 0 for i in args]) or not all([i > 0 for i in kwargs.values()]):
            # ('аргумент является целым числом, но отрицательным или равным нулю')
            raise ValueError
        return f(*args, **kwargs)
    return wrapper


# @takes_positive
# def positive_sum(*args):
#     return sum(args)


# print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, -10))


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


try:
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
except Exception as err:
    print(type(err))

try:
    x, y = 10, 0
    if y == 0:
        raise ZeroDivisionError('Произошло деление на ноль.')
except ZeroDivisionError as err:
    print(err)
    print(err.args)
    print(type(err.args))


try:
    x = 1 / 0
except Exception as err:
    # каким-то образом обработали перехваченное исключение
    print(err)
    # raise


class ElectricCar:
    pass


car = ElectricCar()

print(getattr(car, 'owner', 11))


def optional_introduce(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('introduce'):
            print(f.__name__)
        return f(*args)
    return wrapper


@optional_introduce
def identity(x):
    return x


print(identity(20))
print(identity(42, introduce=True))
