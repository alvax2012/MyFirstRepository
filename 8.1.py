def message(times):
    if times > 0:
        print('Это рекурсивная функция.',  times, id(times))
        message(times - 1)
        print(times, id(times))


print(id(5))
message(5)
