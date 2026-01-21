from datetime import date, time, datetime

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(
    2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

d = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4}

# [print(f'{i.year}-Q{d[i.month]}') for i in dates]


def get_min_max(dates):
    if dates == []:
        return ()
    print(min(dates), max(dates))


dates = [date(2021, 10, 5), date(1992, 6, 10),
         date(2012, 2, 23), date(1995, 10, 12)]

print(get_min_max(dates))


def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end)+1)]


date1 = date(2025, 12, 25)
date2 = date(2026, 1, 5)

# print(date2 - date1)
print(get_date_range(date1, date2))


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    # return len([date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end)+1) if date.fromordinal(i).weekday() == 6])
    return sum(date.fromordinal(i).weekday() == 5 for i in range(start.toordinal(), end.toordinal() + 1))


date1 = date(2010, 6, 13)
date2 = date(2011, 7, 14)
print(saturdays_between_two_dates(date1, date2))


def saturdays_between_two_dates(date1, date2):
    return (max(date1, date2).toordinal() - min(date1, date2).toordinal() - (8 - min(
        date1, date2).isoweekday()) - max(date1, date2).isoweekday() + 1) // 7 + 1 - min(date1, date2).isoweekday() // 7 + max(date1, date2).isoweekday() // 6


date2 = date(2023, 11, 5)
date1 = date(2023, 11, 24)


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    delta = end.toordinal() - start.toordinal()
    print(delta//7, start.weekday(), delta % 7)
    return delta//7 + (start.weekday() % 6+delta % 7 >= 5)


d1 = date(1992, 8, 24)
print(d1.strftime('%j'))


andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(type(andrew))   # выводим дату в формате month_name (YYYY)
# выводим дату в формате YYYY-day_number
print(type(andrew.day))


def print_good_dates(d: date):
    d1 = sorted(d)
    for i in d:
        if i.year == 1992:
            print(i.strftime('%B %d, %Y'))


dates = [date(1992, 1, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)


s = 'end'
while True:
    if s == 'end':
        print('117')
        break
    print('11')

print('-'*50)


def is_correct(d, m, y):
    try:
        date(y, m, d)
        return True
    except ValueError:
        return False


l = [
    '29.02.2016',
    'end']
i = 0
k = 0
s1 = l[i]
while s1 != 'end':
    print('--', s1)
    i += 1
    s1 = l[i]

print(k)


def ff1(x):
    print(x)
    return x*x


t = ff1(2)

print(ff1(2))


d = datetime.strptime('9:00', '%H:%M')
print(d)

print(type(d.isoformat()))


text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'

dt = datetime.strptime(
    text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')

print(dt)


times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(
                          2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(
                          2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(
                          2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(
                          2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(
                          2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(
                          2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(
                          2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(
                          2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(
                          2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(
                          2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(
                          2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(
                          2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
l = map(lambda d: d.hour > 12, times_of_purchases)
print(sum(l))

dts = [d.strftime('%p') for d in times_of_purchases]
print(dts)

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(
             167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
# dt = datetime.combine(dates, times)
for i in sorted(zip(dates, times), key=lambda x: x[1].second):
    print(datetime.combine(i[0], i[1]))

l = [1, 2]
l1 = map(lambda x: x, l)
print(l1)
print(list(l1))

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

print(max(((k, datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S') - datetime.strptime(
    v[0], '%d.%m.%Y %H:%M:%S')) for k, v in data.items()), key=lambda x: x[1])[0])

fmt = '%d.%m.%Y %H:%M:%S'
fastest = min(data, key=lambda x: dt.strptime(
    data[x][1], fmt) - dt.strptime(data[x][0], fmt))
print(fastest)
