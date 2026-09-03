

def quantify(num, pred):
    if pred is None:
        pred = bool
    return sum([pred(i) for i in num])


numbers = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x > 1))
print(quantify(numbers, None))


def is_integer(n):
    s = '0123456789'
    sig = 1
    if n[0] == '-':
        sig = -1
        n = n[1:]

    for i in n:
        if i not in s:
            return False

    return bool(sig*int(n)) if not int(n) else False


print(is_integer('-199'))


def is_decimal(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


print(is_decimal('.-2'))


def is_fraction(x):
    def is_integer(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    res = x.split('/')
    print(res)
    if len(res) != 2:
        return False
    elif is_integer(res[0]) and is_integer(res[1]) and int(res[1]) > 0:
        return True
    else:
        return False


print('--', is_fraction('1/-2'))


def intersperse(iterable, delimiter):
    return delimiter.join(iterable)


print(*intersperse([1, 2, 3], '-'))
