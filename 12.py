a = '1234'


def aa(i):
    x = i

    def aa1(x):
        return x
    print(i)
    return aa1


p = aa(7)
print(p(a))
