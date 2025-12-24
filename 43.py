
from datetime import datetime, date, time, timedelta

t0 = '%d.%m.%Y'
t1 = '%d.%m'
d0 = '14.11.2021'
d0 = datetime.strptime(d0, t0)
l = [['Иван Петров', '16.11.1995'], ['Петр Сергеев',
                                     '14.11.1997'], ['Сергей Романов', '17.11.1994']]
d0_cnt = (d0 - datetime(year=d0.year, month=1, day=1)).days
dl = {datetime.strptime(k, t0): v for v, k in l if (datetime.strptime(
    k, t1) - datetime.strptime(year=datetime.strptime(k, t1).year, month=1, day=1)) > 100}

print(d0_cnt)
