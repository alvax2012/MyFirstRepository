import random
import string


def generate_password(length):
    l = []
    for _ in range(length):
        while True:
            s = random.choice(string.ascii_letters+string.digits)
            if s not in 'lLiIoO0':
                break

        l.append(s)
    return l
    # print(string.ascii_letters)
    # print(string.ascii_uppercase)
    # print(string.ascii_lowercase)
    # print(string.digits)


def generate_passwords(count, length):
    [print(*generate_password(length)) for _ in range(count)]


n, m = 9, 7
generate_passwords(n, m)


n = 10**6       # количество испытаний
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 == 1:
        k += 1

print('pi', (k/n)*s0)
