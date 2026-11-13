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
print(normalize_bits(binary))

print()
print(repr(string.printable))
print(string.printable)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

print()


def relate_and_translate(alphabet, text):
    text = text.translate(str.maketrans(string.ascii_uppercase, alphabet))
    return text.translate(str.maketrans(string.ascii_lowercase, alphabet))


alphabet = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
text = 'I love Python =)'
print(relate_and_translate(alphabet, text))

alphabet = 'xyzabcdefghijklmnopqrstuvw'
text = """Since the discovery and proof of Copernicus' law, the mere recognition that it is not the sun but the earth that moves has destroyed the entire cosmography of the ancients. By refuting the law, it was possible to retain the old view of the movements of bodies, but without refuting it, it seemed impossible to continue studying the Ptolemaic worlds. But even after the discovery of Copernicus' law, the Ptolemaic worlds continued to be studied for a long time.
Since the first man said and proved that the number of births or crimes obeys mathematical laws, and that certain geographical and political-economic conditions determine one way or another of government, that certain relations of the population to the land produce the movements of the people, since then the foundations on which history was built have been destroyed.
By refuting the new laws, it was possible to maintain the old view of history, but without refuting them, it seemed impossible to continue studying historical events as
"""
print(relate_and_translate(alphabet, text))
