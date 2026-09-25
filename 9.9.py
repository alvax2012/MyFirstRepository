from functools import partial
from functools import wraps


def multiply(a, b):
    return a * b


def my_partial(*args_in, **kwargs_in):
    def decorator(func):
        @wraps(func)
        def wripper(*args, **kwargs):
            return func(*args_in, *args, **{**kwargs, **kwargs_in})
        return wripper
    return decorator


double = my_partial(2)(multiply)
basetwo = my_partial(base=2)(int)

# double = partial(multiply, 2)
print(double(3))


print(basetwo('101'))


beegeek = my_partial('beegeek', sep=', ')(print)

beegeek('stepik', 'python')


def f1(a, b):
    print(a, b)


f1(1, 2)
f1(b=2, a=1)
