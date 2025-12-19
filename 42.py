from datetime import datetime, date, time, timedelta

weekdays_count = [0] * 7
print(weekdays_count)
for year in range(1, 10000):
    for month in range(1, 13):
        day_of_week = date(year, month, 13).weekday()
        weekdays_count[day_of_week] += 1

print(weekdays_count, sep='\n')

for i in range(7):
    d1 = date(2025, 12, i+8)
    print(d1.weekday(), d1.strftime("%A"))


d0 = datetime.strptime('01.11.2021 17:35', '%d.%m.%Y %H:%M')
print(d0.day, d0.month, d0.year)
t1 = 9
t2 = 21
if d0.weekday() in (5, 6):
    t1 = 10
    t2 = 18

print(d0.weekday(), t1, t2)
# if t1 <= d0 <= t2:

if d0.time() > time(hour=t2) or d0.time() < time(hour=t1):
    print('Магазин не работает')
else:
    dd = datetime.strptime(f'{t2}:00', '%H:%M')
    print(int((dd-d0).seconds/60))
    # print(datetime(hour=9, year=2021, month=11, day=1)-d0)
    # print(d0.time().hour-time(hour=21).hour, d0.time().minute -time(hour=21).minute)  # time(hour=t1))

    # print(d0.time(), time(hour=21))

# print((d0-timedelta(hours=21)).minute, '----',
    # type(d0.time().hour), '--', d0.time().minute)

print(d0.time() > time(hour=21))


td = timedelta(hours=d0.hour, minutes=d0.minute)

if d0.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
    print(int((timedelta(hours=21) - td).total_seconds() // 60))
elif d0.weekday() > 4 and timedelta(hours=10) <= td < timedelta(hours=18):
    print(int((timedelta(hours=18) - td).total_seconds() // 60))
else:
    print('Магазин не работает')

t0 = '%d.%m.%Y'
# d0, d1 = datetime.strptime('07.03.2021', t0), datetime.strptime('13.03.2021', t0)
d0, d1 = datetime.strptime(
    '01.11.2021', t0), datetime.strptime('10.11.2021', t0)
if (d0.month + d0.day) % 2 == 0:
    d0 += timedelta(days=1)

while d0 < d1:
    if d0.weekday() not in (0, 3):
        print(d0.strftime(t0))
    d0 += timedelta(days=3)


# print(d0.strftime(t0))

# for i in range(0, (d1-d0).days+1, 3):
#     d0 += timedelta(days=3)
#     if d0.weekday() not in (0, 3):
#         print(d0.strftime(t0))

# print(d0, d1)
