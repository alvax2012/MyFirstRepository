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
    bd = []
    b_d = {}
    fmt = '%d.%m.%Y'
    for i in booked_dates:
        if '-' not in i:
            bd.append([i])
            b_d.setdefault(datetime.strptime(i, fmt), 1)
        else:
            bd.append(i.split('-'))
            b_d.setdefault(datetime.strptime(i.split(
                '-')[0], fmt), (datetime.strptime(i.split('-')[1], fmt) - datetime.strptime(i.split('-')[0], fmt)).days+1)

    res = 0
    date_for_booking_dt = datetime.strptime(date_for_booking, fmt)
    date_for_booking_cnt = 1
    for k, v in sorted(b_d.items(), key=lambda x: x[0]):
        print(k, v)
        if date_for_booking_dt >= k and date_for_booking_cnt <= v:
            res = date_for_booking, k, v
            break
    return res


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '05.11.2021'
print(is_available_date(dates, some_date))
