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


def wtch1(st, en):
    if st < en:
        print('*'*st)
        wtch1(st+1, en)
        print('*'*st)


def wtch2(n):

    if n > 0:
        print(f'{n}'*n)
        wtch2(n-1)
        print(f'{n}'*n)


def wtch1(en, k):
    if en > 0:
        print(f'{en}'*en*k)
        wtch1(k, en-1)
        print(f'{en}'*en)


wtch1(4, 4)
# wtch1(1, 4)
