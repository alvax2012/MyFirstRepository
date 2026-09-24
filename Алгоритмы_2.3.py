
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
