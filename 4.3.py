
import json
from pprint import pprint


countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}

json_data = json.dumps(countries, indent=3, separators=(',', ' - '))


club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

data = [club1, club2, club3]

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
    if isinstance(i, str):
        return i+'!'
    elif isinstance(i, int):
        return i+1
    elif isinstance(i, bool):
        return not i
    elif isinstance(i, list):
        return not i*2
    elif isinstance(i, dict):
        i.update({'newkey': None})
        return i
    elif i == 'null':
        return None
    else:
        return i


with open('data.json') as file:
    data = json.load(file)

# for i in data:
#     print(i)

print(data)
with open('updated_data.json', 'w') as file:
    json.dump(list(map(istype, data)), file, indent=3)
