s = 'o1.txt'
ls = []
with open(s, encoding='utf-8-sig ') as f_in:
    l = [i for i in f_in.readlines()[::-1]]
    n = range(len(l))
    for i in n:
        # print('i=', i, l[i])
        if i != max(n):
            if ('def ' in l[i]) and ('#' not in l[i+1]):
                ls.append(l[i][4:l[i].find('(')]+'\n')
        else:
            if 'def ' in l[i]:
                ls.append(l[i][4:l[i].find('(')]+'\n')

[print(_, end='')
 for _ in ls[::-1]] if len(ls) > 0 else print('Best Programming Team')
