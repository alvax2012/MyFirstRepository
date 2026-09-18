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
