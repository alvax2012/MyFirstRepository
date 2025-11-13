from functools import reduce

c = '905 678123 45612 56'
def t(c): return '*' * 12 + c.replace(' ', '')[-4:]


print(t(c))

print()


def same_parity(l: list):
    y = l[0] % 2
    return list(filter(lambda x: x % 2 == y, l))


print(same_parity([6, 0, 67, -7, 10, -20]))


def same_parity(numbers):
    return reduce(lambda x, y: x + (numbers[0] + y + 1) % 2*[y], numbers, [])


def same_parity1(numbers):
    return reduce(lambda x, y: x + [y], numbers, [])


print(same_parity1([1, 2, 7, 8]))


def is_valid(s: str):
    return all([len(s) in range(4, 7), s.isdigit(), ' ' not in s])


print(is_valid(''))
