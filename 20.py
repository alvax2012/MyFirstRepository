from operator import mul
from functools import reduce
import random
p1 = 'c:/1/'

with open(p1 + 'nums.txt', encoding='utf-8') as f:
    print(sum([sum(map(int, ''.join(map(lambda x: x if x.isdigit() else ' ', i)).split()))
          for i in f]))

with open(p1 + 'nums.txt', encoding='utf-8') as f:
    s = reduce(lambda a, b: a + (b if b.isdigit() else ' '), f.read(), '')
    print(sum(map(int, s.split())))


with open(p1 + 'nums.txt', encoding='utf-8') as f:
    print(sum(map(int, reduce(lambda x, y: x + y if y.isdigit()
          else x + ' ', f.read(), '').split())))


with open(p1 + 'nums.txt', encoding='utf-8') as f:
    print(reduce(lambda x, y: x + y if y < 2
                 else x + 10, [1, 3, 4]))


with open(p1 + 'file1.txt', encoding='utf-8') as f:
    fl = f.read()
    print(reduce(lambda x, y: x + (1 if y.isalpha() else 0), fl, 0), 'letters')
    print(reduce(lambda x, y: x + 1 if y in ' \n' else x, fl, 0) + 1, 'words')
    print(reduce(lambda x, y: x + 1 if y == '\n' else x, fl, 0) + 1, 'lines')

    print(len(list(filter(str.isalpha, fl))))
    print(len(fl.split()))
    print(len(fl.split('\n')))

t = 're\n'
print(t.count('\n'), len(t), 'a'.isalpha())


with open(p1 + 'first_names.txt', encoding='utf-8') as f:
    fl = f.readlines()
    c1 = [random.choice(fl).strip() for _ in range(3)]
    print(c1)
with open(p1 + 'last_names.txt', encoding='utf-8') as f:
    fl = f.readlines()
    c2 = [random.choice(fl).strip() for _ in range(3)]
    print(c2)
[print(f'{_[0]} {_[1]}') for _ in zip(c1, c2)]


with open(p1 + 'population.txt', encoding='utf-8') as f:
    fl = f.read().strip()
    print(*map(lambda x: x[0], filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500000,
          [_.split('\t') for _ in fl.split('\n')])), sep='\n')


def read_csv():
    # l = []
    with open(p1 + 'data.csv', encoding='utf-8') as f:
        fl = f.readlines()
        # d = dict.fromkeys(fl[0].strip().split(','))
        # h1 = enumerate(fl[0].strip().split(','))
        h = fl[0].strip().split(',')
        # l = [dict(zip(h, fl[1:].split(',')))]
        # for i in fl[1:]:
        #     print(i.strip().split(','))

        # for i in fl[1:]:
        #     l.append(dict(zip(h, i.strip().split(','))))
        l = [dict(zip(h, i.strip().split(','))) for i in fl[1:]]
    return l


print(read_csv())
print('1')
colors = ['red', 'green', 'blue']

# for pair in enumerate(colors):
print(*enumerate(colors))


with open(p1 + 'words.txt', 'w') as output:
    print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
    print('python', file=output)


s = 'input()'
with open(p1 + 'output.txt', 'w') as f:
    f.write(s)


with open('random2.txt', 'w') as f:
    f.writelines(['559\n', '375\n'])


l = list(range(111, 778))
with open('random1.txt', 'w') as f:
    # t = enumerate(range(111, 778))
    for _ in range(25):
        print(l[random.randrange(777-111)], sep='\n', file=f)


# print([str(random.randint(111, 777))+'\n' for _ in range(25)])

with open(p1 + 'input.txt') as f_in, open(p1 + 'output.txt', 'w') as f_out:
    fl = f_in.readlines()
    # f_out.writelines([f'{_[0]}) {_[1]}' for _ in enumerate(fl, 1)])
    print(*[f'{_[0]}) {_[1]}' for _ in enumerate(fl, 1)], file=f_out, sep='')


# with open(p1 + 'class_scores.txt', encoding='utf-8') as f_in, open(p1 + 'new_scores.txt', 'w', encoding='utf-8') as f_out:
#     print(*[f'{reduce(lambda x, y: x + " " + str(int(y)+5) if int(y) <= 95 else x + ' 100', i.strip().split())}' for i in f_in],
#           file=f_out, sep='\n')


with open(p1 + 'goats.txt') as f_in, open(p1 + 'answer.txt', 'w') as f_out:
    l1, l2 = f_in.read().split('GOATS')
    l1, l2 = l1.strip().split('\n')[1:], l2.strip().split('\n')
    n = len(l2)
    d = {}
    for i in l2:  # d.keys():
        d[i] = d.get(i, 0) + 1
    print('d=', d)
    [print(f'{i[0]}')
     for i in sorted(filter(lambda i: i[1] / n > 0.07, d.items()))]
