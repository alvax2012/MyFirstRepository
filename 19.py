from operator import mul
from functools import reduce
p1 = 'c:/1/'
print(p1 + 'lines.txt')

with open(p1 + 'lines.txt', encoding='utf-8') as f:
    l1 = f.readlines()
    m = len(max(l1, key=lambda x: len(x)))
    # print(m)
    # f.seek(0)
    # print('reduce1=', *filter(lambda x: len(x) == m, l), sep='')
    # print(*map(lambda x: (x.strip(), len(x)), l1))
    # print(*filter(lambda x: len(x) >= 19, l1))
    # l2 = ['1', '33', '444']
    # l2 = [_.replace(' ', '_').strip() for _ in f.readlines() if len(_) > 17]
    # print(l2)
    # print(reduce(lambda x, y: x + y if len(y) == m else x, l1))

print()
with open(p1 + 'nums.txt', encoding='utf-8') as f:
    print(sum([sum(map(int, ''.join(map(lambda x: x if x.isdigit() else ' ', i)).split()))
          for i in f]))
# l1 = f.readlines()
# m = len(max(l1, key=lambda x: len(x)))
# print(m)
# f.seek(0)

# print(*map(lambda x: sum(list(map(int, x.strip().split()))), f.readlines()), sep='\n')

# print(*map(lambda x: sum(list(map(int, x.strip().split()))), f.readlines()), sep='\n')
# print(*filter(lambda x: len(x) >= 19, l1))
# l2 = ['1', '33', '444']
# l2 = [_.replace(' ', '_').strip() for _ in f.readlines() if len(_) > 17]
# print(l2)
# print(reduce(lambda x, y: x + y if len(y) == m else x, l1))
print()
print()
with open(p1 + 'nums.txt', encoding='utf-8') as f:
    print((reduce(lambda x, y: x + y if y.isdigit() else x + '_', i, ''))
          for i in f.readlines())


l = ' 12  45 456   3 \n'

print('str=', str(reduce(lambda x, y: x + y if y.isdigit()
      else x + ' ', '  12  23  12   2 ', ' ')).split(),  reduce(lambda x, y: x + y if y < 2
      else x + 10, [1, 3, 4]))
