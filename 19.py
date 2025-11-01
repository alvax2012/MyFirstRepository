from operator import mul
from functools import reduce
p1 = 'c:/1/'
print(p1 + 'lines2.txt')

with open(p1 + 'lines2.txt', encoding='utf-8') as f:
    l1 = f.readlines()
    m = len(max(l1, key=lambda x: len(x)))
    # print(m)
    # f.seek(0)
    # print('reduce1=', *filter(lambda x: len(x) == m, l), sep='')
    # print(*map(lambda x: (x.strip(), len(x)), l1))
    # print(*filter(lambda x: len(x) >= 19, l1))
    # l2 = ['1', '33', '444']
    l2 = [_.replace(' ', '_').strip() for _ in f.readlines() if len(_) > 17]
    # print(l2)
    print(reduce(lambda x, y: x + y if len(y) == m else x, l1))

with open(p1 + 'nums3.txt', encoding='utf-8') as f:
    # l1 = f.readlines()
    # m = len(max(l1, key=lambda x: len(x)))
    # print(m)
    # f.seek(0)

    print(*map(lambda x: sum(list(map(int, x.strip().split()))), f.readlines()), sep='\n')

    # print(*map(lambda x: sum(list(map(int, x.strip().split()))), f.readlines()), sep='\n')
    # print(*filter(lambda x: len(x) >= 19, l1))
    # l2 = ['1', '33', '444']
    # l2 = [_.replace(' ', '_').strip() for _ in f.readlines() if len(_) > 17]
    # print(l2)
    # print(reduce(lambda x, y: x + y if len(y) == m else x, l1))
