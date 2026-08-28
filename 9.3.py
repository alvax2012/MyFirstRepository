import string


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

    if not any(filter(str.isalpha, password)):
        return failure(login, d[1])
    elif not any(filter(str.isupper, password)):
        return failure(login, d[2])
    elif not any(filter(str.islower, password)):
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
