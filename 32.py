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

t = 9


def dd(l):
    global t
    l2 = l + [12]
    l += [0, 8]
    t = 1
    return l2


l = [1, 2]
print(dd(l))
print(l, t)


def filter_anagrams(word: str, words: list):
    d = {}
    s = map(lambda x: set(x), words)
    l = []
    for i in words:
        w = frozenset(i)
        d[w] = d.get(w, []) + [i]
    # w = set(word)
    # d = filter(lambda x: set(x) == w, words)
    return d.get(frozenset(word), '---')


word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', [
      'iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))

print(filter_anagrams('стекло', []))
print(filter_anagrams('abba', ['aaab', 'dbcd', 'bdaa', 'badb']))

s = [{k: {v[0]: v[1]}} for k, *v in ['Руслан  Пирог 1123'.split()]]
print(s)


def likes(names: list):
    ls = []

    def sp(s):
        return f'оценил{s} данную запись'

    x, y, z, t = '', '', '', ''

    n = 0
    l = len(names)
    i = l

    if l == 1:
        x, *ls = names
    elif l == 2:
        x, y, *ls = names
    elif l >= 3:
        x, y, z, *ls = names
        n = len(ls)
        i = 3
        t = z if l == 3 else str(n+1) + ' других'

    d = {0: 'Никто не ' + sp(''), 1: f'{x} ' + sp('(а)'),
         2: f'{x} и {y} ' + sp('и'), 3: f'{x}, {y} и {t} ' + sp('и')}

    return d.get(i,  '---')


print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))
