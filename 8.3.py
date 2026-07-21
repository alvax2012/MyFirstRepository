def fib(n):
    if n <= 2:
        return 1                             # базовый случай
    else:
        return fib(n - 1) + fib(n - 2)       # рекурсивный случай


# ключ - номер числа, значение - число Фибоначчи
cache = {1: 1, 2: 1}


def fib1(n):
    result = cache.get(n)
    if result is None:
        result = fib(n - 2) + fib(n - 1)
        cache[n] = result
    return result


print(fib(6))


n = 541


def ndig(n):
    if not n:
        return n % 10
    else:
        # d, e = n // 10, n % 10
        # d = n
        # e = ndig(n-1)

        return n % 10 + ndig(n // 10)


print(ndig(n))


def number_of_frogs(y):
    if y == 1:
        return 77
    return 3*(number_of_frogs(y-1)-30)


print(number_of_frogs(2))


def range_sum(num, start, end):
    if start == end:
        return num[end]
    return num[end] + range_sum(num, start, end - 1)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))


def get_pow(a, n):
    if not n:
        return 1
    return a*get_pow(a, n-1)


print(get_pow(5, 2))


def get_fast_pow(a, n):
    if n == 1:
        return a
    elif n % 2:
        return (a**2)*(n/2)
    else:
        return a*(a**(n-1))


print(get_fast_pow(5, 2))
