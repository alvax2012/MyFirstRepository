import time
from math import factorial


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def add1(a):
    time.sleep(3)
    return a


def calculate_it(fanc, *args):
    start_time = time.monotonic()
    res = fanc(*args)
    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    return res, elapsed_time


print(calculate_it(add, 1, 2, 3))


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


fancs = [factorial_recurrent, factorial_classic, factorial]


def get_the_fastest_func(fancs: list, arg=None):

    d = {}
    for f in fancs:
        start_time = time.monotonic()
        if arg:
            f(arg)
        else:
            f
        end_time = time.monotonic()

        d[f] = d.get(f, 0) + (end_time - start_time)
        print(f, d[f], end_time - start_time)

    return min(d, key=lambda x: d[x])


print(get_the_fastest_func(fancs, 3))


def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


fancs = [for_and_append, list_comprehension]

print(get_the_fastest_func(fancs))


def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable)


fancs = [for_and_append, list_comprehension, list_function]
print()
print(get_the_fastest_func(fancs, range(100_000)))
