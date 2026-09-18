import functools


def counter(func, i=2):
    # k = 7
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal k, i
        wrapper.num += 1
        print(f'Вызов {func.__name__}: {wrapper.num}--{k}---{i}')
        val = func(*args, **kwargs)
        k += 1
        i += 1
        return val

    wrapper.num = 0
    k = 1
    return wrapper


@counter
def greet(name):
    return f'Hello {name}!'


print(greet('Timur'))
print(greet('Ruslan'))
print(greet('Arthur'))
print(greet('Gvido'))


s = [100, 25, 505, 481, 1, 2401]
for i in s:
    print(i % 1000 % 10, f"{i} -> {max(str(i), key=int)}")
    # print(i % 100)
