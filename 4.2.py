import csv


# with open('sales.csv', encoding='utf-8') as fl:
#     rows = csv.reader(fl, delimiter=';')
#     for index, item in enumerate(rows):
#         if index and item[2] < item[1]:
#             print(item[0])


# with open('sales.csv', encoding='utf-8') as fl:
#     rows = csv.DictReader(fl, delimiter=';')
#     for row in rows:
#         if int(row['new_price']) < int(row['old_price']):
#             print(row)

# d = {}
# with open('salary_data.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';')
#     for row in rows:
#         name = row['company_name']
#         d[name] = d.get(name, []) + [int(row['salary'])]

# print(*sorted(d, key=lambda i: (sum(d[i])/len(d[i]), i)), sep='\n')

# n = 1  # int(input())
# d = {}
# columns = ['1', '2', '3']
# with open('deniro.csv', encoding='utf-8') as file:
#     rows = csv.reader(
#         file,  delimiter=',')
#     res = map(lambda i: [int(i[k]) if i[k].isdigit()
#               else i[k] for k in range(3)], rows)

#     [print(*i, sep=', ') for i in sorted(res, key=lambda i: i[n-1])]

text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('grades.csv', 'w') as file:
    file.write(text)


def csv_columns(filename):
    res = {}
    with open(filename, encoding='utf-8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            for k, v in row.items():
                # res[k] = res.get(k, []) + [v]

                res.setdefault(k, []).append(v)

                # res.setdefault(k, [])
                # res[k].append(v)

    return res


print(csv_columns('grades.csv'))

res = {}
with open('data.csv', encoding='utf-8') as in_file, open('domain_usage.csv', 'w', encoding='utf-8', newline='') as out_file:
    rows = csv.DictReader(in_file)
    columns = rows.fieldnames
    print(columns)
    for row in rows:
        ml = row[columns[2]].split('@')[1]
        res[ml] = res.get(ml, 0) + 1

    columns_out = ['domain', 'count']
    res_out = [{columns_out[0]: k, columns_out[1]
        : int(v)} for k, v in res.items()]
    writer = csv.DictWriter(out_file, fieldnames=columns_out)
    writer.writeheader()                 # запись заголовков
    writer.writerows(sorted(res_out, key=lambda i: (
        i[columns_out[1]], i[columns_out[0]])))

    # out_file.write('1\n')

# print(sorted(res_out, key=lambda i: (i[columns_out[1]], i[columns_out[0]])))
# print(res_out)
res = {}
with open('wifi.csv', encoding='utf-8') as in_file:
    rows = csv.DictReader(in_file)
    columns = rows.fieldnames[0].split(';')
    print(columns[1])
    for row in rows:
        ml = row[columns[1]]
        res[ml] = res.get(ml, 0) + 1

    print(res)
