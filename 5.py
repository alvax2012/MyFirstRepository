

def c(j):
    k = 2
    print(j)
    print(k)

    def f(x):
        nonlocal k, j
        x += k + j
        k += 1
        j += 1
        return x

    return f


t = c(5)
print(t.__closure__,  t(5))
for var in t.__closure__:
    print('var=', var.cell_contents)
print()


def f(a):
    print(999)

    def g(k=17):
        nonlocal a
        print(a, end=' ')
        a += 1
    return g


g = f(10)
print(g.__closure__, g.__defaults__)
g()
g()

print(777)
print()


def f2(x):
    x += 1
    return x


def cf(f1):
    def wripper(*args):
        return f1(*args)

    return wripper


cf = cf(f2)
print(cf.__closure__, cf(4))


# def cf(x):
#     # def wripper(*args):
#     #     return f1(*args)

#     return f2(x)


# f = cf(f2)
# print(cf.__closure__, f(4))


def ff(*args, **kwarg):
    print(*args, **kwarg)
    return args, kwarg


print(ff(1, 2, 3, sep='--'))


a = [1, 2]
print(id(a))
for i in a:
    # i = 7
    print(id(i))
print(id(i), id(7))

i = [1, 2]
print(id(i))

i1 = [1, 2]
print(id(i1))
