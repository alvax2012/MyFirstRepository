import pickle
import csv
from collections import namedtuple
from datetime import date, time, datetime

l = []

with open('meetings.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    fld = rows.fieldnames
    User = namedtuple('User', fld)
    for i in rows:
        l.append(User._make(i.values()))
l.sort(key=lambda x: (datetime.strptime(
    x[-2], '%d.%m.%Y'), datetime.strptime(x[-1], '%H:%M')))

# for i in l:
#     print(i.surname, i.name)

Device = namedtuple('Device', ['devicetype', 'model'])

# device2 = Device(**{'devicetype': 'keyboard', 'model': 'Logitech G213'})
device2 = Device(devicetype='keyboard', model='LogitechG213')

# device2 = Device(*{'devicetype': 'keyboard', 'model': 'Logitech G213'})
# device2 = Device({'devicetype': 'keyboard', 'model': 'Logitech G213'})
# device2 = Device(1, 2)
# print(device2.devicetype, device2.model)


def null_dec(fanc):
    return fanc


def greet():
    return '123!'


greet1 = null_dec(greet)


Game = namedtuple('Game', ('name', 'developer', 'publisher'))
ExtendedGame = namedtuple(
    'ExtendedGame', Game._fields + ('release_date', 'price'))

Game = Game(1, 2, 3)
# ExtendedGame = ExtendedGame(1, 2, 3, 4, 5)

print(Game.developer)

# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
# with open('data.pkl', 'rb') as file:     # используется файл, полученный на предыдущем шаге
#     obj = pickle.load(file)
# for i in obj:
#     for k, v in i._asdict().items():
#         print(f'{k}: {v}')
#     print()

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

d = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Basic': 4}
l = []
for i in users:
    l.append(i._asdict())

l.sort(key=lambda x: (d[x['plan']], x['email']))
# print(l)

for i in l:
    print(f'{i["name"]} {i["surname"]}\n Email: {i["email"]}\n Plan: {i["plan"]}')
    print()
