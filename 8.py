def bee(n):
    if n > 0:
        print(n)
        bee(n - 1)
    print(n)


bee(2)


def triangle(n):
    i = 1

    def prn(i):
        if i <= n:
            print('*'*i)
            prn(i+1)
    prn(i)


# triangle(3)

def triangle(n):
    if n > 0:
        triangle(n-1)
    print('*'*n)


def triangle(h):
    if h > 1:
        triangle(h - 1)
    print('*' * h)


print()
triangle(5)

print('--')


def wtch(n):
    if n > 0:
        print('*'*n)
        wtch(n-1)
        print('*'*n)


wtch(4)
