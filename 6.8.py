from collections import Counter
s = 'Любимой песни слог Знакомый ритм слов Панацея от всего'.lower().split()

cnt1 = Counter(s)  # .most_common()
print(cnt1)
m = max(cnt1.values())
l = sorted([i[0] for i in filter(lambda x: x[1] == m, cnt1.items())],
           key=lambda x: x[0], reverse=True)
print(l[0])

most_common_word = max(cnt1, key=lambda x: (cnt1[x], x))
# print(l if len(l) == 1 else ', '.join(l))
print(most_common_word)

print()

cnt1 = sorted(Counter([len(i) for i in s]).items(), key=lambda x: x[1])
for i in cnt1:
    print(f'Слов длины {i[0]}:', i[1])
print(cnt1)
