import string


def draw_graph(f):

    for x in range(10):
        print(end='---\n'*f(x))
        # print('-'*10)
        print('  '*x, '*', sep='')


def f(x):
    # if x <= 5:
    #     return x
    # return x - 2*(x % 5)
    return x


#  draw_graph(f)

# draw_graph(lambda x: x)

print('--')


def rhombus(h, fill_value='!'):

    for i in range(1, h+1):
        if i <= h//2+1:
            s = '*'*(2*i - 1)
        else:
            s = '*'*(2*(h - i)+1)

        print(i, s.center(h, fill_value))

    # for i in range(h, 0):
    #     s = '*'*(2*i - 1)
    #     print(s.center(h, fill_value))


rhombus(5)


def normalize_bits(binary):
    m = len(max(binary, key=lambda x: len(x)))
    return [i.zfill(m) for i in binary]


binary = ['101', '1111101000', '1000']
# print(normalize_bits(binary))

print()
print(repr(string.printable))
# print(string.printable)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

print()


def relate_and_translate(alphabet, text):
    d = str.maketrans(string.ascii_lowercase, alphabet)
    d.update(str.maketrans(string.ascii_uppercase, alphabet))
    return text.translate(d)


alphabet = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢 🅣🅤🅥🅦🅧🅨🅩'
text = 'I love Python =)'
# print(relate_and_translate(alphabet, text))

alphabet = 'xyzabcdefghijklmnopqrstuvw'
text = "Since the discovery and proof Ss"
print(relate_and_translate(alphabet, string.ascii_uppercase),
      alphabet, sep='\n')


print()


def encode(text, step):
    return decode(text, step, 2*step)
    # d = str.maketrans(string.ascii_lowercase,
    #                   string.ascii_lowercase[step:] + string.ascii_lowercase[:step])
    # d.update(str.maketrans(string.ascii_uppercase,
    #          string.ascii_uppercase[step:] + string.ascii_uppercase[:step]))
    # return text.translate(d)


def decode(text, step, t=26):

    d = str.maketrans(string.ascii_lowercase,
                      string.ascii_lowercase[t-step:] + string.ascii_lowercase[:t-step])
    d.update(str.maketrans(string.ascii_uppercase,
                           string.ascii_uppercase[t-step:] + string.ascii_uppercase[:t-step]))
    return text.translate(d)


print(encode('Beegeek', 10))
print(decode('Looqoou', 10))


person = ('Tim', 'Peters')

print('person: %s %s' % person)

name = 'James'
surname = 'Bond'

result = 'My name is %s, %s' % (surname, name)
print(result)
print('person: {} {}'.format(name, surname))

print('person: {} {}'.format('11', '22', name='Tim', surname='Peters'))


class Cat:
    def __init__(self, name, t):
        self.name = name
        self.t = t

    def __str__(self):
        return f'Кот по имени {self.name}'

    def __repr__(self):
        return f"Cat('{self.name}, {self.t}')"


cat = Cat('Кемаль', 7)

print(f'{cat!r}', repr(cat), repr(Cat))
