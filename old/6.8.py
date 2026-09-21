from collections import Counter
import csv
import json
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


columns = ['first_name', 'second_name', 'class_number', 'class_letter']
data = [['Тимур', 'Гуев', 11, 'А'], [
    'Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

# with open('students1.csv', 'w', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(columns)                 # запись заголовков
#     for row in data:                         # запись строк
#         writer.writerow(row)

# with open('students1.csv', encoding='utf-8', newline='') as file:
#     rows = csv.reader(file)
#     for row in rows:
#         print(row)
d = Counter()
with open('name_log.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, quotechar='"')
    d = Counter([line['email'] for line in rows])
    # for row in rows:
    #     # d.update([row['email']])
    #     d += Counter([row['email']])
    #     # print(Counter([row['email']]))


for i in sorted(d):
    print(f'{i}: {d[i]}')

# print(l, d)

print()


def scrabble(symbols, word):
    count_sym = Counter(symbols.lower())
    count_word = Counter(word.lower())
    # print(count_sym, count_word)
    return True if count_sym >= count_word else False


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))


def print_bar_chart(data, mark):
    dc = Counter(data)
    m = max([len(i) for i in dc])
    for i in sorted(dc, key=lambda x: -dc[x]):
        # print(f'{i.ljust(m)} |{mark*dc[i]}')
        print(f'{i:!<{m + 1}}|{mark * dc[i]}')


print_bar_chart('beegeek', '+')
print()
languages = ['java', 'java', 'python', 'C++', 'assembler',
             'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')

print()
pr = Counter()
for k in range(1, 4):
    with open(f'quarter{k}.csv', encoding='utf-8') as file:
        rows = list(csv.reader(file, quotechar='"'))
        del rows[0]
        for nm, *ms in rows:
            pr.update({nm: sum(map(int, ms))})

print(pr, pr)
print('-'*50)

d = Counter()
for i in range(1, 5):
    with open(f'quarter{i}.csv', encoding='utf-8') as file:
        rows = csv.DictReader(file, quotechar='"')
        columns = rows.fieldnames
        for i in rows:
            for col in range(1, 4):
                d.update({i[columns[0]]: int(i[columns[col]])})
                # print({i[columns[0]]: i[columns[col]]}, end='')
            print()
print('==', d)

with open('prices.json', encoding='utf-8') as file:
    data = json.load(file)

for i in d:
    print(i, d[i]*data[i])
    d[i] = d[i]*data[i]
    # print(i, d[i], data[i])
# print('--', data)
print(d, d.total())

print()

with open('quarter1.csv', encoding='utf-8') as fi:
    _, *products = csv.reader(fi)
    # print(_, products)
    products_count = Counter()
    for product in products:
        name, *total_count = product
        print(name, total_count)
        products_count.update({name: sum(map(int, total_count))})

print()

cnt = Counter()
d = Counter()
le = Counter()
l = [['1', '300'], ['1', '250'], ['11', '400'], [
    '1', '300'], ['7', '200'], ['9', '400'], ['7', '250']]
lp = Counter(['1', '1', '11', '9', '5', '5', '7', '9', '9'])

for i in l:
    d.setdefault(i[0], []).append(int(i[1]))
    # cnt.update({i[0]: i[1]})

for k, v in lp.items():
    if type(d[k]) == list:
        le.update({k: sum(d[k][:v])})
    else:
        le.update({k: d[k]})

print(le.total())


books = Counter(s=1, p=10, m=3)
books -= Counter({'s': 2})

print(books)
