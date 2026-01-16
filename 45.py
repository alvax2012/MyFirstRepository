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
