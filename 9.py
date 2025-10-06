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
