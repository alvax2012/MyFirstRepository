def matrix(n=1, m=None, value=0):
    s = []
    if not m:
        m = n
        matrix.__defaults__
    for i in range(n):
        s.append([])
        for j in range(m):
            s[-1].append(value)
    m = 0
    # print('--' if m else n)
    return s


print(matrix(4, 3, 9))

print()


def greet(nm, *args):
    args = list(args)
    args.insert(0, nm)
    print(args)
    return f'Hello, {' and '.join(args)}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))

print()


def print_products(*args):
    val = tuple(_ for _ in args if type(_) is str and _)
    d = dict(zip((_ for _ in range(len(val))), val))
    [print(f'{key + 1}) {val}')
     for key, val in d.items()] if val else print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',),
               'Яблоки', '', 'Макароны', 5, True)
print()
print_products([4], {}, 1, 2, {'Beegeek'}, '')


def info_kwargs(**kwargs):
    [print(key, ': ', val, sep='') for key, val in sorted(kwargs.items())]


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
