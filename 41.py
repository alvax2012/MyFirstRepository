from datetime import datetime, date
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

for k in sorted(d):
    print(k.strftime(fmt))
    print(*d[k], sep='\n')


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
    return not any([(d1 >= k and d1 <= v) or (d2 >= k and d2 <= v) for k, v in d.items()])


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
