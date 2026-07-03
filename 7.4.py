from sys import exc_info
import sys
import calendar
import locale

# print(issubclass(IndexError, LookupError))
# print(issubclass(LookupError, IndexError))

# try:
#     nums = [10, 5, 20, 25]
#     print(nums[100])
# except BaseException as err:    # записываем сгенерированное исключение в переменную err
#     print(err)
#     print(type(err))


# try:
#     х = 1 / 0
# except Exception as err:
#     print(exc_info())

# while True:
#     print(input())

# data = sys.stdin.read()
# print(data)

# for line in sys.stdin:
#     print(line.strip('\n'))


# def sub(n):
#     if n < 0:
#         raise ValueError('Число должно быть натуральным')
#     return 1 / n


# print('-'*50)

# try:
#     n = 0
#     print(sub(n))
# except ZeroDivisionError as e:
#     try:
#         print(sub(-10))
#     except ValueError:
#         raise
# print('pass')

# try:
#     х = 1 / 0
# except Exception as err:
#     # каким-то образом обработали перехваченное исключение
#     # d = 1 / 0
#     print('--', err)
#     raise                       # пробрасываем исключение выше

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(n):
    days = list(calendar.day_name)
    if not isinstance(n, int):
        raise TypeError('Аргумент не является целым числом')
        print(n)
    if n < 1 or n > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return days[n-1]


try:
    print(get_weekday('20'))
except Exception as err:
    print(err)
    print(type(err))

print()


# def get_id(names, name):
#     if not isinstance(name, str):
#         raise TypeError('Имя не является строкой')
#     if not (name.isalpha() and name.istitle()):
#         raise ValueError('Имя не является корректным')
#         # print('lf')
#     return len(names) + 1


# names = ['Timur', 'Anri', 'Dima', 'Arthur']
# name = 'Ruslan1337'

# try:
#     print(get_id(names, name))
# except ValueError as e:
#     print(e)

num = 7
if not (4 < num < 8):
    print(num)


class NumberNotInRangeError(Exception):
    pass


try:
    number = int('3999')
    if not 4000 < number < 8000:
        raise NumberNotInRangeError('Число из недопустимого диапазона')
    print(number)
except NumberNotInRangeError as e:
    print(e)
