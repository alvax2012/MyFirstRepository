with open('files.txt') as f:
    # l = f.readlines()
    l = [i.split() for i in f]

# print(l)
d = {}
m = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3}
# print(sorted(m))
for i in l:
    nm, count, unit = i
    nm, ext = nm.split('.')
    d[ext][nm] = d.setdefault(ext, {}).setdefault(nm, []) + [int(count), unit]
    # print(nm, ext, count, unit)
# print(d)


for k, v in sorted(d.items()):
    du = {}
    for k1, v1 in sorted(v.items()):
        # print(v1)
        du[v1[1]] = du.get(v1[1], 0) + v1[0]
        print(f'{k1}.{k}')
    print('-'*10)
    m2 = max(du.keys(), key=lambda x: m[x])
    s2 = round(sum([v*(1024**m[k]) for k, v in du.items()]) /
               (1024**m[m2]))
    if s2 // 1024 == 0:
        s1 = s2
        m1 = m2
    else:
        s1 = round(s2 / 1024)
        m1 = ''.join([k for k, v in m.items() if v == m[m2] + 1])
    print('Summary:', s1, m1)
    print()
