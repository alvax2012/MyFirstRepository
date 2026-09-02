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
