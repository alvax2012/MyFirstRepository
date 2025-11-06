from operator import mul
from functools import reduce
import random
import operator
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


print()
l_in = ['f1.txt', 'f2.txt']
l_out = []
with open('output.txt', 'w') as f_out:
    for _ in l_in:
        with open(_) as f_in:
            s = f_in.read()
            l_out.append(s)
    f_out.writelines(l_out)

print(l_out)

print('--')
with open(p1 + 'logfile.txt', encoding='utf-8') as f_in, open(p1 + 'output11.txt', 'r', encoding='utf-8') as f_out, open(p1 + 'output22.txt', 'w', encoding='utf-8') as f_out1:
    # fl1 = [i.strip().split(',') for i in f_in.readlines()]
    # l_out = map(lambda x: x[0].strip() + '\n', filter(lambda x: ((int(x[2].strip()[:2])*60 + int(x[2].strip()[-2:]))) - (
    #     int(x[1].strip()[:2])*60 + int(x[1].strip()[-2:])) >= 60, fl1))

    # f_in.seek(0)
    # f_out.seek(0)

    # print(reduce(operator.add, [int(_.strip().split()[1])
    #       for _ in f_out.readlines()[:-1]]))

    # print(*map(lambda x: int(x.strip().split()
    #       [1]) > 3, f_out.readlines()[:-1]))

    # print(max(f_out.readlines(), key=lambda x: len(x.strip())))
    # print(max(map(lambda x: len(x.strip()), f_out.readlines())))

    # print(*map(lambda x: '*'*len(x) if x.strip()
    #       in ('214') else x, f_out.readlines()))

    d1 = {'ф': 'f', 'л': 'l', 'р': 'r', 'у': 'u'}

    print(reduce(lambda x, y: x + y,
          list(map(lambda x: d1.get(x, '0') if x not in ('\n') else x, f_out.read()))), file=f_out1, sep='--')
