a = '1234'


def aa(i):
    x = i

    def aa1(x):
        print('+++', x)
        return x

    return aa1


p = aa(7)
print('====', p(a))

print(int('-3'))


def process(input_string: str) -> str:
    l = list(map(int, input_string.split()))
    print(l)
    return f'выше нуля: {len(list(filter(lambda x: x > 0, l)))}, ниже нуля: {len(list(filter(lambda x: x < 0, l)))}, равна нулю: {len(list(filter(lambda x: x == 0, l)))}'


input_string = '5 -2 0 0 7 8 -1'
output_string = process(input_string)
print(output_string)


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285,
           5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]


def x(x): return x > 3


print(x(4))

# func_apply = lambda f, s: [f(i) for i in s]

print(map(abs, numbers))
