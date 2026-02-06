
import json
import csv
from pprint import pprint
from datetime import datetime, time

# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

# json_data = json.dumps(countries, indent=3, separators=(',', ' - '))


# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

# data = [club1, club2, club3]

# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=3)


# specs = {
#     'Модель': 'AMD Ryzen 5 5600G',
#     'Год релиза': 2021,
#     'Сокет': 'AM4',
#     'Техпроцесс': '7 нм',
#     'Ядро': 'Cezanne',
#     'Объем кэша L2': '3 МБ',
#     'Объем кэша L3': '16 МБ',
#     'Базовая частота': '3900 МГц'
# }

# specs_json = json.dumps(specs, ensure_ascii=0, indent=3)


# def is_correct_json(data):
#     try:
#         json.loads(data)
#         return True
#     except ValueError:
#         return False


# data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

# print(is_correct_json(data))
# print(is_correct_json('number = 17'))


def istype(i):
    if isinstance(i, bool):
        return not i
    elif isinstance(i, str):
        return i+'!'
    elif isinstance(i, int):
        return i+1
    elif isinstance(i, list):
        return i*2
    elif isinstance(i, dict):
        i.update({'newkey': None})
        return i
    else:
        pass


# with open('data.json', encoding='utf-8') as file:
#     data = json.load(file)

# # l1 = [(1, 2), 1, 'ww', [1, 2], {1: 3}, False, None]
# # print([istype(i) for i in l1 if i != None])

# print(type(data))
# data = [istype(i) for i in data if i != None]
# with open('updated_data.json', 'w', encoding='utf-8') as file:
#     # json.dump([1, 3], file)
#     json.dump(data, file, indent=3)

# res = []
# d = {}
# with open('people.json', encoding='utf-8') as file:
#     data = json.load(file)


# for i in data:
#     d.update(i)

# print(d.keys())

# [i.update({k: None}) for i in data for k in d if k not in i]


# #print(data)
# with open('updated_people.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=3)

l = [1, 2]
for i in l:
    i = 111
print(l)


# d = {}
# with open('countries.json', encoding='utf-8') as file:
#     data = json.load(file)

# for i in data:
#     v, k = i.values()
#     d.setdefault(k, []).append(v)

# print(d)
# with open('religion.json', 'w', encoding='utf-8') as file:
#     json.dump(d, file, indent=3)

# d = {}
# with open('playgrounds.csv', encoding='utf-8') as in_file:
#     reader = csv.DictReader(in_file, delimiter=';')
#     col = reader.fieldnames
#     rows = list(reader)

# # print(col)
# # print(rows)


# for i in rows:
#     d.setdefault(i[col[1]], {}).setdefault(i[col[2]], []).append(i[col[3]])

# print(d)
# with open('addresses.json', 'w', encoding='utf-8') as file:
#     json.dump(d, file, indent=3, ensure_ascii=0)


# d = {}
# with open('students.json', encoding='utf-8') as file:
#     data = json.load(file)
# col = ['name', 'phone']


# res = [{'name': i['name'], 'phone': i['phone']}
#        for i in data if i['age'] >= 18 and i['progress'] >= 75]
# res.sort(key=lambda x: x['name'])
# print(res)
# with open('data.csv', 'w', encoding='utf-8', newline='') as out_file:
#     writer = csv.DictWriter(out_file, fieldnames=col)
#     writer.writeheader()
#     writer.writerows(res)


# d = {}
l = []
with open('pools.json', encoding='utf-8') as file:
    data = json.load(file)

for i in data:
    adr = i['Address']
    work = i['WorkingHoursSummer']['Понедельник'].split('-')
    # datetime.strptime(work[0], '%H:%M')
    d1 = time(hour=int(work[0].split(':')[0]))
    d2 = time(hour=int(work[1].split(':')[0]))
    dim = i['DimensionsSummer']
    if d1.hour <= 10 and d2.hour >= 12:
        l.append((adr,   dim['Length'], dim['Width']))

l.sort(key=lambda x: (-x[1], -x[2]))
res = l[0]
print(f'{res[1]}x{res[2]}', res[0], sep='\n')
