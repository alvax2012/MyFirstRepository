from datetime import datetime, date, timedelta
from math import ceil

fmt = '%d.%m.%Y; %H:%M'
d = {}
with open('diary.txt', encoding='utf-8') as f:
    for i in f:
        try:
            k = datetime.strptime(i.strip(), fmt)
            d.setdefault(k, [])
        except ValueError:
            d[k] += [i.strip()]
l = sorted(d.items(), key=lambda x: x[0])
d[k] += ['']

# for k in sorted(d):
#     print(k.strftime(fmt))
#     print(*d[k], sep='\n')


print('111')


def is_available_date(booked_dates, date_for_booking):
    d = {}
    fmt = '%d.%m.%Y'
    for i in booked_dates:
        if '-' not in i:
            d.setdefault(datetime.strptime(i, fmt), datetime.strptime(i, fmt))
        else:
            d.setdefault(datetime.strptime(
                i.split('-')[0], fmt), datetime.strptime(i.split('-')[1], fmt))

    if '-' in date_for_booking:
        d1 = datetime.strptime(date_for_booking.split('-')[0], fmt)
        d2 = datetime.strptime(date_for_booking.split('-')[1], fmt)
    else:
        d1 = datetime.strptime(date_for_booking, fmt)
        d2 = d1
    print(d, d1, d2)
    return not any([any(((d1 >= k and d1 <= v), (d2 >= k and d2 <= v), (k >= d1 and k <= d2), (v >= d1 and v <= d2))) for k, v in d.items()])


dates = ['01.11.2021', '05.11.2021-09.11.2021',
         '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))


ans = datetime.now() + timedelta(days=ceil(timedelta(hours=93) / timedelta(hours=5)))
print(ans.strftime('Приблизительная дата окончания курса: %d.%m.%Y %H:%M'))


dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))


today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = abs(today-birthday).days

print(days)


d1 = datetime.strptime('04.11.2021', '%d.%m.%Y')
d0 = datetime.strftime(d1+timedelta(days=-1), '%d.%m.%Y')
d2 = datetime.strftime(d1+timedelta(days=1), '%d.%m.%Y')
print(d0, d2, sep='\n')


ts = '%H:%M:%S'
d1 = datetime.strptime('00:01:01', ts)
d0 = datetime.strptime('00:00:00', ts)
print((d1-d0).seconds)


ts = '%H:%M:%S'
d1 = datetime.strptime('09:00:00', ts)
n = 90  # int(input())

print(datetime.strftime(d1 + timedelta(seconds=n), ts))
