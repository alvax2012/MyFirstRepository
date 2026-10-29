

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


draw_graph(f)

# draw_graph(lambda x: x)


def rhombus(h, fill_value='!'):

    for i in range(1, h+1):
        s = '*'*i
        print(s.center(i, '!'))


rhombus(5)
