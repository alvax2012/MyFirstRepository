
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
    b = (y2-y1)/(x2-x1)

    k = (y2 - b)/x2
    return k, b


print(linear_coefficients((0, 0), (1, 5)))
