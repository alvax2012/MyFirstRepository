import calendar
import datetime

print(calendar.isleap(2024))
print(calendar.isleap(2027))


print(*[calendar.isleap(_)
      for _ in (2007, 1993, 1994, 1992, 1991)], sep="\n")

print(list(calendar.month_abbr).index('Dec'))

d = datetime.datetime.strptime('2021-11-02', '%Y-%m-%d')
# datetime.strptime(dt, '%Y%m%d')
print(d.weekday())
