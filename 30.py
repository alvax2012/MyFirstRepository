athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = 2


com = {1: lambda x: x[0], 2: lambda x: x[1],
       3: lambda x: x[2], 4: lambda x: x[3]}
athletes.sort(key=com[n])
[print(*_) for _ in athletes]
# print(*athletes, sep='\n')


def m1(i):
    t = 4

    def mm2(k):
        return i+t+k
    return mm2


print(m1(2)(5))

mm = m1(2)
print(mm(4))
