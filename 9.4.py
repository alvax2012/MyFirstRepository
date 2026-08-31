def my_func():
    return 17


# k = input
# input = my_func
# num = input()
# print(num)

# input = k

# n = input()
# print(n)


# s = '''
# ffg
# jklj
# q
# '''
# print(s)

def append(element, seq=[1, 2]):
    seq.append(element)


def append(element, seq=[177, 2]):
    seq.append(element)


print(append.__defaults__)


def f(a):
    def g():
        nonlocal a

        print(a)
        a += 1

    return g


g = f(10)
g()
g()
# g(3)
# print('==', g(4))
