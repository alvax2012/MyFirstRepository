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


def num_of_sundays(y):
    d1 = datetime(year=y, month=12, day=31)
    d0 = datetime(year=y, month=1, day=1)
    return datetime.strftime(d0, '%j'), d0.weekday(), datetime.strftime(d0, '%U'), datetime.strftime(d1, '%j'), d1.weekday(), datetime.strftime(d1, '%U')


print(num_of_sundays(2000))


dt = datetime(2021, 11, 4) + timedelta(days=3)

print(dt)

print('---')
t1 = '%d.%m.%Y'
d1 = datetime.strptime('20.12.2021', t1)
print(datetime.strftime(d1, t1))
for i in range(2, 11):
    d1 += timedelta(days=i)
    # print(datetime.strftime(d1, t1))
    print(d1.strftime(t1), datetime(2021, 12, 20 + i).strftime(t1))


t1 = '%d.%m.%Y'
s = '05.10.2021 06.10.2021 07.10.2021 08.10.2021 09.10.2021'
l = s.split()
l_out = []
# print(l)
for i in range(1, len(l)):
    l_out.append(abs(datetime.strptime(
        l[i-1], t1)-datetime.strptime(l[i], t1)).days)
print(l_out)


def fill_up_missing_dates(dates):
    t1 = '%d.%m.%Y'
    l_out = []
    l = sorted(map(lambda d: datetime.strptime(d, t1), dates))
    print(l)
    # l_out.append(l[0])
    for i in range(1, len(l)):
        l_out.append(l[i-1].strftime(t1))
        print((l[i], l[i-1]))
        for j in range((l[i]-l[i-1]).days - 1):
            l_out.append((l[i-1] + timedelta(days=j+1)).strftime(t1))
    l_out.append(l[i].strftime(t1))
    return l_out


dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']

print(fill_up_missing_dates(dates))
print(dates)

t1 = '%H:%M'
d0, d1 = datetime.strptime('09:00', t1), datetime.strptime('11:00', t1)
d = d0 - timedelta(minutes=10)
while d < d1 - timedelta(minutes=45):
    d += timedelta(minutes=10)
    print(d.strftime(t1), end=' - ')
    d += timedelta(minutes=45)
    print(d.strftime(t1))

t1 = '%H:%M'
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

l = sum(map(lambda d: (datetime.strptime(
    d[1], t1)-datetime.strptime(d[0], '%H:%M')).total_seconds() // 60, data))

print(*((datetime.strptime(
    t[1], '%H:%M') - datetime.strptime(t[0], '%H:%M')).seconds for t in data))

print(l)

t0 = '%d.%m.%Y'
d0 = datetime.strptime('01.01.0001', t0)
d1 = datetime.strptime('31.12.9999', t0)
dn = {}
# for _ in range(7):
#     d0 += timedelta(days=1)
#     print(d0.strftime('%w'), d0.weekday(), d0.strftime("%A"), d0)

d = d0
j = 0
while d < d1:
    d += timedelta(days=1)
    if d.day == 13:
        dn[d.weekday()] = dn.get(d.weekday(), 0) + 1
        # print(j, 'd=', d.day, d.weekday(), d.strftime("%A"))
[print(i[1]) for i in sorted(dn.items())]
