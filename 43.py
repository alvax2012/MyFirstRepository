
from datetime import datetime, date, time, timedelta

t0 = '%d.%m.%Y'
t1 = '%d.%m'
d0 = '14.11.2021'

d0 = datetime.strptime(d0, t0)
# d1 = datetime(year=d0.year, month=d0.month, day=d0.day+7)
d1 = d0 + timedelta(days=7)

l = [['Иван Петров', '16.11.1995'], ['Петр Сергеев',
                                     '14.11.1997'], ['Сергей Романов', '17.11.1994']]
# d0_cnt = (d0 - datetime(year=d0.year, month=1, day=1)).days
dl = {datetime.strptime(k, t0): v for v, k in l if (d0 < datetime(year=d0.year, month=datetime.strptime(k, t0).month, day=datetime.strptime(
    k, t0).day) <= d1) or (d0 < datetime(year=d0.year + 1, month=datetime.strptime(k, t0).month, day=datetime.strptime(k, t0).day) <= d1)}

print(dl[max(dl)] if dl else 'Дни рождения не планируются')
