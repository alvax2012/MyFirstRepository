

def draw_graph(f):

    for x in range(10):
        print(end='---\n'*f(x))
        # print('-'*10)
        print('  '*x, '*', sep='')


def f(x):
    # if x <= 5:
    #     return x
    # return x - 2*(x % 5)
    return x


#  draw_graph(f)

# draw_graph(lambda x: x)

print('--')


def rhombus(h, fill_value='!'):

    for i in range(1, h+1):
        if i <= h//2+1:
            s = '*'*(2*i - 1)
        else:
            s = '*'*(2*(h - i)+1)

        print(i, s.center(h, fill_value))

    # for i in range(h, 0):
    #     s = '*'*(2*i - 1)
    #     print(s.center(h, fill_value))


rhombus(5)


def normalize_bits(binary):
    m = len(max(binary, key=lambda x: len(x)))
    return [i.zfill(m) for i in binary]


binary = ['101', '1111101000', '1000']
print(normalize_bits(binary))
