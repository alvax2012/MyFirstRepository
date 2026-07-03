import json


def d1():
    try:
        1 / 0
    except:
        # pass
        raise


# try:
#     d1()
# # записываем сгенерированное исключение в переменную err
# except Exception as err:
#     print(err)
#     print(type(err))


# try:
#     with open('prices.json', encoding='utf8') as file:
#         try:
#             out = json.load(file)
#         except ValueError:
#             out = 'Ошибка при десериализации'
# except FileNotFoundError:
#     out = 'Файл не найден'

# print(out)

class ValueShortLen(Exception):
    pass


def is_good_password1(s):
    length_ok = len(s) >= 9
    return all((any(i.isdigit() for i in s), any(i.isupper() for i in s), any(i.islower() for i in s), length_ok))
    # if len(s) < 9:
    #     return not res
    # elif s.isalnum():
    #     return res
    # elif s.isalpha():
    #     return not res
    # elif s.isdecimal():
    #     res = not res
    # elif s.isupper():
    #     res = not res
    # elif s.islower():
    #     res = not res

    # else:
    #     return not res

    # return res


def is_good_password(string):
    if len(string) < 9:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for c in string:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True

    return all([has_upper, has_lower, has_digit])


print()

# print(is_good_password('abc!@#%$#%#$%^&dABC8'))
print(is_good_password1('!@#$%^&*()_+1'))
# print(is_good_password('МойПарольСамыйЛучший111'))
# print(is_good_password('HELLO1234'))
# print(is_good_password('sss1234567890'))
# print(is_good_password('qwertyтимур696969'))

# TEST_11:
# print(is_good_password('1234567890'))

# TEST_12:
# print(is_good_password('HELLO1234'))
#


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password2(s):
    try:
        t = 1/0
    except:
        # pass
        raise

    if len(s) < 9:
        raise LengthError()

    if not all((any(i.isupper() for i in s), any(i.islower() for i in s))):
        raise LetterError()
    if not any(i.isdigit() for i in s):
        raise DigitError()


print()

try:
    print(is_good_password2('qqqqqqqqqqqqqWW'))
except Exception as err:
    try:
        l = [1, 2]
        t = l[4]
    except:
        # pass
        raise
    print(err)
    print(type(err))
