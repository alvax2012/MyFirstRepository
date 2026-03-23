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
