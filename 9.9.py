from functools import lru_cache
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

s = 'tutorial'


@lru_cache()
def eng_per(s):
    return ''.join(sorted(s))


print(eng_per(s))

print()


# @lru_cache()
def ways(n):
    t = (1, 3, 4)
    l = []

    def ways_rec(p=1):
        for i in t:
            if p < n:
                p += i
                # ways_rec()
            elif i > n:
                continue
            else:
                l.append(n)
                return l
            ways_rec(p)
    return ways_rec()


print(ways(5))
