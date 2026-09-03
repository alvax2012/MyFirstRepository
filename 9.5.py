from datetime import datetime
from datetime import datetime, UTC
from datetime import date
import time


def f(a):
    def g():
        nonlocal a
        print(a, end=' ')
        a += 1
    return g


g = f(10)
g()
g()
g()
print('==', g())


def outer_function():
    num = 5

    def inner_function():      # определяем вложенную функцию
        nonlocal num
        num += 10
        print(num)
    return inner_function           # вызываем вложенную функцию


a = outer_function()

a()
a()


def outer(x):
    def inner():
        x = 0
        x += 1
        print(x)
    inner()


outer(10)


def power(degree):
    return lambda x: pow(x, degree)


square = power(2)
print(square(5))


def generator_square_polynom(a, b, c):
    def polinom(x):
        return a*x**2 + b*x + c
    return polinom


f = generator_square_polynom(1, 2, 1)
print(f(5))


def sourcetemplate(url):
    def load(*args, **kwargs):
        # url + '?' + '&'.join([f'{i[0]}={i[1]}' for i in sorted(kwargs.values())]) if kwargs else url
        return url + '?' + '&'.join([f'{i[0]}={i[1]}' for i in sorted(kwargs.items())]) if kwargs else url

    return load


url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(1, 2, smartphone='iPhone', notebook='huawei', sale=True))

# https://all_for_comfort_life.com?notebook=huawei&sale=True&smartphone=iPhone


def outer(x):
    def inner():
        return x
    x = None
    return inner


print(outer(10)())


def date_formatter(country_code):
    df = {'ru': '%d.%m.%y',
          'us': 'MM-DD-YYYY',
          'ca': 'YYYY-MM-DD',
          'br': 'DD/MM/YYYY',
          'fr': 'DD.MM.YYYY',
          'pt': 'DD-MM-YYYY'}
    t = df[country_code]
    return lambda d: d.strftime(df[country_code])


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today), today.strftime('%d.%m.%y'))


text = 'Experiment Date 01/28/2005; Time 23:50:13'

dt = datetime.strptime(text, 'Experiment Date %m/%d/%Y; Time %H:%M:%S')

print('dt', dt, dt.strftime('%m'))


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def get_the_fastest_func(*args, arg):

    d = {}
    for f in args:
        start_time = time.monotonic()
        f(arg)
        end_time = time.monotonic()
        d[f] = (end_time - start_time)

    return d


print(get_the_fastest_func(factorial_recurrent, factorial_classic, arg=100))


def sort_priority(num, gr):
    l = []
    for i in gr:
        if i in num:
            num.remove(i)
            l.append(i)
    num.sort()
    l.sort()
    num[0:0] = l
    return num


def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)

# [2, 3, 5, 7, 1, 4, 6, 8]
