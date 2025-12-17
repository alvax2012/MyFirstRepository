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

d0 = datetime.strptime('01.11.2021 20:45', '%d.%m.%Y %H:%M')

t1 = timedelta(hours=9)
t2 = timedelta(hours=21)
if d0.weekday() == 5 or 6:
    t1 = timedelta(hours=10)
    t2 = timedelta(hours=18)

# if t1 <= d0 <= t2:
print(d0-timedelta(hours=21))
