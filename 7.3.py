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
