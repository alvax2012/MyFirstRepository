from datetime import date

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
print(type(andrew.year))


def print_good_dates(d: date):
    d1 = sorted(d)
    for i in d:
        if i.year == 1992:
            print(i.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)
