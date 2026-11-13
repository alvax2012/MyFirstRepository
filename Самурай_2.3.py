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
