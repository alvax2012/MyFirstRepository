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
