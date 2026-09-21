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


# def wtch1(st, en):
#     if st < en:
#         print('*'*st)
#         wtch1(st+1, en)
#         print('*'*st)


# def wtch2(n):

#     if n > 0:
#         print(f'{n}'*n)
#         wtch2(n-1)
#         print(f'{n}'*n)


def wtch(n):
    k = n

    def prn(n):
        if n > 0:
            print(' ' * (k-n)*2, f'{k-n+1}'*n*k, sep='')
        if n > 1:
            prn(n-1)
            print(' ' * (k-n)*2, f'{k-n+1}'*n*k, sep='')
    prn(n)


wtch(4)
# wtch1(1, 4)
print('--')


def print_digits(n):
    # while n:
    #     d, e = n // 10, n % 10
    #     print(e)
    #     n = d
    d, e = n // 10, n % 10
    # print(e)
    if d:
        # print(e)
        print_digits(d)
    print(e)


print_digits(12345)
