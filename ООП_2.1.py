

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
