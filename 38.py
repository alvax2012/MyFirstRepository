
from datetime import date

my_date = date(2020, 6, 17)
my_date = my_date.replace(month=9, day=29)

print(my_date)

d = {}
k = 22
i = 8
# d.setdefault(k, []).append(2)

d.setdefault(k, {}).update({8: 7})
# d[k][i] = d.setdefault(k, {8: 0}).get(i, 0) + 2

print(d)
