
x = 10


def f(x):
    c = x
    return c


b = f(x)

print(id(x), id(b), id(f(x)), id(f))
