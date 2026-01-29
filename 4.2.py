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


d = {}
with open('deniro.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    print(*rows)
