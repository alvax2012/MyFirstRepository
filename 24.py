s = 'stepik.txt'
with open("forbidden_words.txt", encoding="utf-8") as file, open(s) as infile:
    text = infile.read()
    for f in file.read().strip("\n").split():
        pos = text.lower().find(f)
        while pos > -1:
            text = text[:pos] + "*" * len(f) + text[pos+len(f):]
            pos = text.lower().find(f)
print(text)

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


buf, pos = [None] * 10, 0
with open(s) as f:
    while True:
        s = f.readline().strip()
        if s == '':
            break
        buf[pos], pos = s, (pos + 1) % 10
[print(text) for text in buf[pos:] + buf[:pos] if not text is None]
