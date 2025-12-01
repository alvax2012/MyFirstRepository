
d = {}
k = 22
i = 8
# d.setdefault(k, []).append(2)

d.setdefault(k, {}).update({8: 7})
# d[k][i] = d.setdefault(k, {8: 0}).get(i, 0) + 2

print(d)
