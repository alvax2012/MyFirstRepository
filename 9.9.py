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
# def ways(n):
#     t = (1, 3, 4)
#     l = []

#     def ways_rec(p=1):
#         for i in t:
#             if p < n:
#                 p += i
#                 # ways_rec()
#             elif i > n:
#                 continue
#             else:
#                 ways_rec.res.append(n)
#                 return l
#             ways_rec(p)
#         ways_rec.res = []
#     return ways_rec()


# print(ways(5))

def dict_travel(nested_dicts):
    def traverse(d, prefix=''):
        for key, value in sorted(d.items()):
            path = f'{prefix}.{key}' if prefix else key
            if isinstance(value, dict):
                traverse(value, path)
            else:
                print(f'{path}: {value}')
    traverse(nested_dicts)


def dict_travel(d):
    p = []

    def dm(dct):
        if isinstance(dct, str) or isinstance(dct, int):
            print('.'.join(p), dct, sep=': ')
            return

        for i in sorted(dct):
            p.append(i)
            dm(dct[i])
            p.pop()

    dm(d)


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)


# @lru_cache()
def ways(n):
    t = (1, 3, 4)
    l = [[]]

    def ways_rec(p=1):

        if len(l[-1]) == 3:
            l.append([])
            return

        # ways_rec.res = []

        for i in t:
            l[-1].append(i)
            ways_rec(i)
            # p.pop()
        return

    return ways_rec()


print(ways(5))
