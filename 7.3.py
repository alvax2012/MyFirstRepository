try:
    x = 10 / 10
    print(x)
finally:
    print('Блoк finally')


def f1():
    try:
        x = 10
        return x
    finally:
        x = 20


def f2():
    try:
        return 10
    except:
        pass
    else:
        return 20


def f():
    try:
        x = [10]
        return x
    finally:
        x.append(20)


print(f1())

print()

try:
    numbers = (1, 2, 3)
    print(numbers + (4))
except:
    print('Произошла ошибка')
finally:
    print('Завершение программы')


t1 = (1, 2, 3)
t2 = (4,)
t1 = t1 + t2
print(t1)

numbers = list(filter(int, ['1', '2', '3', '4', '5']))
print(numbers)


s = '111'

months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
               7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


try:
    s_out = months_dict[int(s)]
except KeyError:
    s_out = 'Введено число из недопустимого диапазона'
except ValueError:
    s_out = 'Введено некорректное значение'
# except KeyError:
#     s_out = 'Введено число из недопустимого диапазона'

print(s_out)
