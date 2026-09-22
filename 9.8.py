from functools import wraps
import functools


def counter(func, i=2):
    k = 7

    @functools.wraps(func)
    def wrapper(*args, t=10,  **kwargs):
        nonlocal k, i
        wrapper.num += 1
        print(f'Вызов {func.__name__}: {wrapper.num}--{k}---{i}   {t}')
        val = func(*args, **kwargs)
        k += 1
        i += 1
        t += 1
        return val

    wrapper.num = 0
    k = 3
    return wrapper


@counter
def greet(name):
    return f'Hello {name}!'


print(greet('Timur'))
print(greet('Ruslan'))
print(greet('Arthur'))
print(greet('Gvido'))


s = [100, 25, 505, 481, 1, 2401]
for i in s:
    print(i % 1000 % 10, f"{i} -> {max(str(i), key=int)}")
    # print(i % 100)


def wrapper1(t=10):
    t += 2
    print(f'Вызов  {t}')


def wrapper1(t=100):
    t += 2
    print(f'Вызов  {t}')


wrapper1()
wrapper1()
print(wrapper1.__defaults__)


class ElectricCar:
    """111"""

    def __init__(self, color, owner):

        self.color = color
        self.owner = owner
        return None


car = ElectricCar('yellow', 'Gvido')

print(car.color, car.__dict__)
print(car.owner, ElectricCar.__dict__)

print()


class A:
    def method(self, x):
        print(type(self), self, x)


a = A()

a.method(10)       # self = a (экземпляр), x = 10
A.method(a, 10)    # то же самое: self = a, x = 10
A.method(10, 20)   # self = 10, x = 20 — работает, но self не экземпляр


print()


def square(func):
    @functools.wraps(func)
    def wripper(*args, **kwargs):

        return func(*args, **kwargs)
    return wripper


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b


print(add(1, 1))
print(add.__name__)
print(add.__doc__)

print()


def returns_string(func):

    @functools.wraps(func)
    def wripper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not isinstance(res, str):
            raise TypeError
        return res
    return wripper


@returns_string
def add(a, b):
    return a + b


try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))


@returns_string
def beegeek():
    '''documentation'''
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)

print('----')


def trace(func):
    @wraps(func)
    def wripper(*args, **kwargs):
        res = func(*args, **kwargs)

        print(
            f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}\nTRACE: возвращаемое значение {func.__name__}(): {repr(res)}")
        return res
    return wripper


@trace
def say(name, line):
    '''прекрасная функция'''
    return f'{name}: {line}'


# print(say.__name__)
# print(say.__doc__)
# say('Jane', 'Hello, World')


@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)

print()

# Обычный пример
s = "Hello"
print(repr("Hello"), s)  # Вывод: 'Hello'

# Можно воссоздать объект
l = [1, 2, 3]
code = repr(l)
new_obj = eval(code)


print(l, repr(l), eval(code), eval('1+2'), repr(4))  # Вывод: [1, 2, 3]


def repeater(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции.')
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator


@repeater(repeat=5)
def beegeek():
    print('beegeek')


print(beegeek())


print()


def decor1(func):
    print('Применяется декоратор 1')

    def wrapper():
        print('Запущена обертка декоратора 1')
        return func().upper()
    print('Возвращаем обертку декоратора 1')
    return wrapper


def decor2(func):
    print('Применяется декоратор 2')

    def wrapper():
        print('Запущена обертка декоратора 2')
        return func()[1:]
    print('Возвращаем обертку декоратора 2')
    return wrapper


def decor3(func):
    print('Применяется декоратор 3')

    def wrapper():
        print('Запущена обертка декоратора 3')
        return func()[::-1]
    print('Возвращаем обертку декоратора 3')
    return wrapper


@decor3
@decor2
@decor1
def beegeek():
    print('Запущена декорируемая функция')
    return 'beegeek'


print('Выводим', beegeek())
print()


def prefix(string, to_the_end=False):

    def set_prefix(func):
        @functools.wraps(func)
        def wripper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            else:
                return string + func(*args, **kwargs)
        return wripper
    return set_prefix


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())


print()


def make_html(tag=None):
    def decorator(func):
        @wraps(func)
        def wripper(*args, **kwargs):
            return (func(*args, **kwargs), f'<{tag}>{func(*args, **kwargs)}</{tag}>')[bool(tag)]
        return wripper
    return decorator


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))

print()


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wripper(*args, **kwargs):
            for i in range(times-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wripper
    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')


say_beegeek()

print()


def strip_range(start=0, end=0, char='.'):
    def decorator(func):
        @wraps(func)
        def wripper(*args, **kwargs):
            res = func(*args, **kwargs)
            if (end - start) < len(res) - 1:
                l = end
                char1 = char*(end - start)
            else:
                l = len(res)
                char1 = char*(l - start)

            return res.replace(res[start: l], char1)
        return wripper
    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())


s = "print(calculate('xyz', [1, 2, 3], 'x-y+z'))             # 1 - 2 + 3 = 2"


def calculate(var, val, exp):
    locals_dict = {k: v for k, v in zip(var, val)}
    res = 0
    coef = 1
    for char in exp:
        if char == '-':
            coef = -1
        if char == '+':
            coef = 1

        res += coef * locals_dict.get(char, 0)
    return res  # eval(exp, locals_dict)


print(calculate('xyz', [1, 2, 3], 'x-y+z'))

# locals_dict = {"y": 10, "x": 5}
# print(eval('x+y', locals_dict))

print()


def takes(*arg_type):

    def decorator(func):
        @wraps(func)
        def wripper(*args, **kwargs):
            if all(type(j) == i for i in arg_type for j in args) and all(type(j) == i for i in arg_type for j in kwargs.values()):
                return func(*args, **kwargs)
            else:
                raise TypeError
        return wripper
    return decorator


@takes(list, bool, str, int)
def repeat_string(string, times):
    pass
    # return string * times


try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))


print(str(type(2)), repr(type(2)))
