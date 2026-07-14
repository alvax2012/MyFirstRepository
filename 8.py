def bee(n):
    if n > 0:
        print(n)
        bee(n - 1)
    print(n)


bee(2)
