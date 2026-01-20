import calendar
# import datetime
from datetime import datetime, date

print(calendar.isleap(2024))
print(calendar.isleap(2027))


print(*[calendar.isleap(_)
      for _ in (2007, 1993, 1994, 1992, 1991)], sep="\n")

print(list(calendar.month_abbr).index('Dec'))

d = datetime.strptime('2021-11-02', '%Y-%m-%d')
# datetime.strptime(dt, '%Y%m%d')
print(d.weekday())


def get_days_in_month(y, m):
    l = []
    m_index = list(calendar.month_name).index(m)
    for i in range(1, calendar.monthrange(y, m_index)[1]+1):
        # l.append(date(y, m_index, i))
        l.append(datetime(day=i, month=m_index, year=y).date())
    return l


print(get_days_in_month(2021, 'December'))


def get_all_mondays(y):
    l = []
    for i in list(calendar.month_name)[1:]:
        l.extend(filter(lambda d: calendar.weekday(
            d.year, d.month, d.day) == 0, get_days_in_month(y, i)))
    return l


print()
# print(get_all_mondays(2021))

# for week in calendar.monthcalendar(2021, 9):
#     monday = week[0]
#     print(week)
#     if monday:
#         print(monday)

print('-'*30)


def get_tcm(y):
    l = []
    for i in range(1, 13):
        d = calendar.monthrange(y, i)[0]
        cnt = 7
        wd = 4
        if 3-d < 0:
            n = 2
        elif 3-d >= 0:
            n = 1
        d_out = (n*cnt + wd) + (cnt - d)
        print(date(day=d_out, year=y, month=i).strftime('%d.%m.%Y'))


get_tcm(2021)
