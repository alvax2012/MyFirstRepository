import string
import sys


def print_operation_table(op, row, col):
    l = []
    for i in range(1, row + 1):
        l.append([])
        for j in range(1, col + 1):
            # l[-1].append(op(i, j))
            l[i-1].append(op(i, j))
            print(str(l[i-1][j-1]).rjust(3, ' '), end=' ')
        print()
    print(l)  # op(row, col))


def print_operation_table(op, row, col):
    l = []
    for i in range(1, row+1):
        l.append([i]*col)
        print(*map(lambda i, j: str(op(i, j)).ljust(3, ' '),
              l[i-1], range(1, col+1)))


print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)
print_operation_table(pow, 5, 10)


def verification(login, password, success, failure):
    # string.digits
    string.ascii_letters
    # string.ascii_lowercase
    # string.ascii_uppercase

    d = {
        1: 'в пароле нет ни одной буквы',
        2: 'в пароле нет ни одной заглавной буквы',
        3: 'в пароле нет ни одной строчной буквы',
        4: 'в пароле нет ни одной цифры'}

    print(*filter(lambda x: not (x in string.ascii_letters), password))

    if not any(filter(lambda x:  x in string.ascii_letters, password)):
        return failure(login, d[1])
    elif not any(filter(lambda x:  x in string.ascii_uppercase, password)):
        return failure(login, d[2])
    elif not any(filter(lambda x:  x in string.ascii_lowercase, password)):
        return failure(login, d[3])
    elif not any(filter(str.isdigit, password)):
        return failure(login, d[4])
    else:
        return success(login)


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


verification('timyrik20', 'Beegeek314', success, failure)
verification('Arthur_Davletov', 'мойпароль123', success, failure)

verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)

# анонимные функции являются выражениями, то есть их можно сразу вызывать в момент определения


def bee():
    return 'bee'


def geek():
    return 'geek'


# bee, geek = geek, bee

bee = geek
geek = bee

print(bee())
print(geek())


def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    return sum(filter(lambda x: isinstance(x, (int, float)), elems))


print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum(['beegeek', 11, 'stepik', 28.5,
      '100', 11.2]), numbers_sum.__doc__)


def prn(*args, **kwargs):
    s = f'{kwargs.get('sep', ', ')}'.upper().join(map(lambda x: x.upper() if type(
        x) == str else str(x), args)) + f'{kwargs.get('end', '\n')}'.upper()
    sys.stdout.write(s)
    sys.stdout.write(
        '-'.join(map(lambda x: x.upper() if isinstance(x, str) else str(x), args)))


pr = print
print = prn

words = (1, 'black', 'white', 'grey', 'black-1', 'white-1', 'python')
# print(*words)
print(*words, sep=' to ', end=' LOVE')
print('beegeek', [1, 2, 3], 4)
print = pr

print('qw')
