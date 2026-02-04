import csv
from datetime import datetime

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

# text = '''name,grade
# Timur,5
# Arthur,4
# Anri,5'''

# with open('grades.csv', 'w') as file:
#     file.write(text)


# def csv_columns(filename):
#     res = {}
#     with open(filename, encoding='utf-8') as file:
#         rows = csv.DictReader(file, delimiter=';')
#         for row in rows:
#             for k, v in row.items():
#                 # res[k] = res.get(k, []) + [v]

#                 res.setdefault(k, []).append(v)

#                 # res.setdefault(k, [])
#                 # res[k].append(v)

#     return res


# print(csv_columns('grades.csv'))

# res = {}
# with open('data.csv', encoding='utf-8') as in_file, open('domain_usage.csv', 'w', encoding='utf-8', newline='') as out_file:
#     rows = csv.DictReader(in_file)
#     columns = rows.fieldnames
#     print(columns)
#     for row in rows:
#         ml = row[columns[2]].split('@')[1]
#         res[ml] = res.get(ml, 0) + 1

#     columns_out = ['domain', 'count']
#     res_out = [{columns_out[0]: k, columns_out[1]                : int(v)} for k, v in res.items()]
#     writer = csv.DictWriter(out_file, fieldnames=columns_out)
#     writer.writeheader()                 # запись заголовков
#     writer.writerows(sorted(res_out, key=lambda i: (
#         i[columns_out[1]], i[columns_out[0]])))

# out_file.write('1\n')

# print(sorted(res_out, key=lambda i: (i[columns_out[1]], i[columns_out[0]])))
# print(res_out)
print('-'*50)
# res = {}
# with open('wifi.csv', encoding='utf-8') as in_file:
#     rows = csv.DictReader(in_file, delimiter=';')
#     columns = rows.fieldnames
#     ml = columns[1]
#     for row in rows:
#         res[row[ml]] = res.get(row[ml], 0) + int(row[columns[-1]])

# for i in sorted(res.items(), key=lambda x: (-x[1], x[0])):
#     print(f'{i[0]}: {i[1]}')

# res = {}
# with open('titanic.csv', encoding='utf-8') as in_file:
#     rows = csv.DictReader(in_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     columns = rows.fieldnames
#     res = list(filter(lambda i: i[columns[0]], rows))
# res.sort(key=lambda x: x[columns[2]], reverse=True)
# for i in res:
#     print(i[columns[1]])

# res_out = {}
# ds = '%d/%m/%Y %H:%M'
# with open('name_log.csv', encoding='utf-8') as in_file:
#     rows = csv.DictReader(in_file)
#     columns = rows.fieldnames
#     for row in rows:
#         res_out.setdefault(row[columns[1]], []).append(
#             (datetime.strptime(row[columns[2]], ds), row[columns[0]]))


# res = []
# for i in sorted(res_out.items(), key=lambda x: x[0]):
#     dm = max(i[1], key=lambda x: x[0])
#     # print(dm[0])
#     res.append({columns[0]: dm[1],  columns[1]: i[0],
#                columns[2]: dm[0].strftime(ds)})
#     # res.append((dm[1], i[0], dm[0].strftime(ds)))

# print(res)


# with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as out_file:
#     writer = csv.DictWriter(
#         out_file, fieldnames=columns)
#     writer.writeheader()                 # запись заголовков  , quoting=csv.QUOTE_NONE
#     writer.writerows(res)

# text = '''01,Title,Ran So Hard the Sun Went Down
# 02,Title,Honky Tonk Heroes (Like Me)'''


# with open('data.csv', 'w', encoding='utf-8') as file:
#     file.write(text)


# def condense_csv(filename, id_name):
#     res = []
#     columns = []
#     with open(filename, encoding='utf-8') as in_file:
#         rows = csv.reader(in_file)

#         columns.append(id_name)
#         d = {}
#         # print(*rows)
#         for i, k, v in rows:
#             # d = {}
#             if k not in columns:
#                 columns.append(k)

#             d[i][k] = d.setdefault(i, {}).setdefault(k, v)
#             # d.append({id_name: i, k: v})

#         print(columns, d)
#         for i in d:
#             d1 = {id_name: i}
#             for k, v in d[i].items():
#                 d1[k] = v
#             res.append(d1)
#         # res = [{id_name: k}.setdefault(i[0], i[1])
#         #        for k, v in d.items() for i in v.items()]

#         print(res)

#         with open('condensed.csv', 'w', encoding='utf-8', newline='') as out_file:
#             writer = csv.DictWriter(out_file, fieldnames=columns)
#             writer.writeheader()                 # запись заголовков  , quoting=csv.QUOTE_NONE
#             writer.writerows(res)


# condense_csv('data.csv', id_name='ID')

# res = []
# with open('student_counts.csv', encoding='utf-8') as in_file:
#     rows = csv.DictReader(in_file)
#     col = rows.fieldnames[:1] + sorted(rows.fieldnames[1:],
#                                        key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))

#     rows = list(rows)
# print(col)

# with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as out_file:
#     writer = csv.DictWriter(out_file, fieldnames=col)
#     writer.writeheader()
#     writer.writerows(rows)

d = {}
with open('prices.csv', encoding='utf-8') as in_file:
    rows = csv.DictReader(in_file, delimiter=';')
    col = rows.fieldnames
    for row in rows:
        m = row[col[0]]

        del row[col[0]]
        mx = sorted(row.items(), key=lambda i: (int(i[1]), i[0]))[0]
        d[m] = mx
        # print(m, mx)

res = sorted(d.items(), key=lambda i: (i[1][1], i[1][0], i[0]))[0]
# print(res)
print(f'{res[1][0]}: {res[0]}')
