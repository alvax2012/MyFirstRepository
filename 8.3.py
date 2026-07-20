def fib(n):
    if n <= 2:
        return 1                             # базовый случай
    else:
        return fib(n - 1) + fib(n - 2)       # рекурсивный случай


# ключ - номер числа, значение - число Фибоначчи
cache = {1: 1, 2: 1}


def fib(n):
    result = cache.get(n)
    if result is None:
        result = fib(n - 2) + fib(n - 1)
        cache[n] = result
    return result


print(fib(6))
