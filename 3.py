import functools
import time


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__}")  # Код до вызова
        result = func(*args, **kwargs)          # Вызов оригинальной функции
        print(f"Функция {func.__name__} завершилась")  # Код после вызова
        t = True
        return result
    return wrapper


t = False


@log_decorator
def say_hello(name):
    return f"Привет, {name}!"


# print(say_hello("Мир"))


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


# beegeek()


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


# @decor3
# @decor2
# @decor1
def beegeek():
    print('Запущена декорируемая функция')
    return 'beegeek'


beegeek = decor1(beegeek)
beegeek = decor2(beegeek)

print()
print('Выводим', beegeek())

print('---')


def repeater(repeat=1):
    def decorator(func):
        print('Применяется декоратор repeater')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Запущена обертка декоратора repeater')
            for i in range(1, repeat + 1):
                print(f'{i}-й запуск функции.')
                value = func(*args, **kwargs)
            return value
        print('Возвращаем обертку декоратора repeater')
        return wrapper
    return decorator


def delayed(delay=2):
    def decorator(func):
        print('Применяется декоратор delay')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('Запущена обертка декоратора delay')
            print(f'Спим {delay} сек.')
            time.sleep(delay)
            value = func(*args, **kwargs)
            return value
        print('Возвращаем обертку декоратора delay')
        return wrapper
    return decorator


# @delayed(delay=1)
# @repeater(repeat=5)
def monitor(url):
    print(f'Проверка {url} на доступность.')
    return f'Проверка {url} на доступность.'


monitor = repeater(repeat=5)(monitor)
monitor = delayed(delay=1)(monitor)

print()
print(monitor('https://stepik.org/'))
# delayed(delay=1)(repeater(repeat=5)(monitor('https://stepik.org/')))

print()


def make_upper(func):
    def wrapper():
        t = func().upper()
        print(t, 1)
        return t
    return wrapper


def del_first_char(func):
    def wrapper():
        t = func()[1:]
        print(t, 2)
        return t
    return wrapper


def reverse(func):
    def wrapper():
        t = func()[::-1]
        print(t, 3)
        return t
    return wrapper


# @reverse
# @del_first_char
# @make_upper
def beegeek():
    return 'beegeek'


beegeek = reverse(del_first_char(make_upper(beegeek)))

print(beegeek())
