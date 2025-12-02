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
    return date.toordinal(end - start)  # [i for i in range(end - start)]


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(date2 - date1)
print(get_date_range(date1, date2), sep='\n')
