
def is_function(pairs):
    return len(dict(pairs)) == len(pairs)


def is_function(pairs):
    check_set = set()
    for p in pairs:
        if p[0] in check_set:
            return False
        check_set.add(p[0])
    return True


print(is_function([(1, 3), (2, 5), (1, 7)]))

print()


def is_point_in_rectangle(p: tuple[int, int], rect: list[tuple[int, int], tuple[int, int]]) -> bool:
    if rect[1][0] >= rect[0][0]:
        x1, x2 = rect[0][0], rect[1][0]
    else:
        x2, x1 = rect[0][0], rect[1][0]

    if rect[1][1] >= rect[0][1]:
        y1, y2 = rect[0][1], rect[1][1]
    else:
        y2, y1 = rect[0][1], rect[1][1]
    print(x1, x2, y1, y2)
    return True if x1 < p[0] < x2 and y1 < p[1] < y2 else False


print(is_point_in_rectangle((-2, -2), [(-1, -1), (3, 4)]))

print()


def linear_coefficients(p1, p2):
    x1, y1 = p1
    x2, y2 = p2


def linear_coefficients(a, b):
    x1, y1 = a
    x2, y2 = b
    k = (y2-y1)/(x2-x1)

    b = y2 - k*x2
    return k, b


def equation_of_line(values):
    b = values[0]
    k = values[1] - b
    if all(values[i] == k*i + b for i in range(2, len(values))):
        s1 = str(k) + 'x' if abs(k) != 1 else '-x' if k < 0 else 'x'
        s2 = ''
        if k and b:
            s2 = f' + {abs(b)}' if b > 0 else f' - {abs(b)}'
        elif b == 0 and k:
            pass  # s2 = ''
        elif k == 0 and b:
            s1 = ''
            s2 = f'{b}' if b > 0 else f'{str(b)}'
        else:
            s1 = '0'

        return f'y = {s1}{s2}'


print(equation_of_line([1, 3, 5, 7, 9]))
print(equation_of_line([0, 1, 2, 3, 4]))
print(equation_of_line([0, -1, -2, -3, -4]))
print(equation_of_line([0, -2, -4, -6, -8]))
print(equation_of_line([6, 6, 6, 6, 6]))
print(equation_of_line([1, 2, 3, 5, 7]))

'qq'.lower()
