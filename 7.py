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
