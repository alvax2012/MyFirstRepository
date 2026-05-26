from collections import Counter
import csv
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
print()

d = Counter()
for i in range(1, 2):
    with open(f'quarter{i}.csv', encoding='utf-8') as file:
        rows = csv.DictReader(file, quotechar='"')
        columns = rows.fieldnames
        for i in rows:
            for col in columns:
                # d.update({col: int(i[col])})
                print({col: i[col]}, end='')
            print()


print('--', d)
