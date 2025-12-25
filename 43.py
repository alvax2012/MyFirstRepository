
from datetime import datetime, date, time, timedelta

# t0 = '%d.%m.%Y'
# t1 = '%d.%m'
# d0 = '14.11.2021'
# d0 = datetime.strptime(d0, t0)
# l = [['Иван Петров', '16.11.1995'], ['Петр Сергеев',
#                                      '14.11.1997'], ['Сергей Романов', '17.11.1994']]
# d0_cnt = (d0 - datetime(year=d0.year, month=1, day=1)).days
# dl = {datetime.strptime(k, t0): v for v, k in l if (datetime.strptime(
#     k, t1) - datetime.strptime(year=datetime.strptime(k, t1).year, month=1, day=1)) > 100}

# print(d0_cnt)

# t0 = '%d.%m.%Y'
# t1 = '%d.%m'
# d0 = '14.11.2021'

# d0 = datetime.strptime(d0, t0)
# # d1 = datetime(year=d0.year, month=d0.month, day=d0.day+7)
# d1 = d0 + timedelta(days=7)

# l = [['Иван Петров', '16.11.1995'], ['Петр Сергеев',
#                                      '14.11.1997'], ['Сергей Романов', '17.11.1994']]
# # d0_cnt = (d0 - datetime(year=d0.year, month=1, day=1)).days
# dl = {datetime.strptime(k, t0): v for v, k in l if (d0 < datetime(year=d0.year, month=datetime.strptime(k, t0).month, day=datetime.strptime(
#     k, t0).day) <= d1) or (d0 < datetime(year=d0.year + 1, month=datetime.strptime(k, t0).month, day=datetime.strptime(k, t0).day) <= d1)}

# print(dl[max(dl)] if dl else 'Дни рождения не планируются')


def choose_plural(amount: int, declensions: tuple):
    p = ((amount // 10) % 10)*10 + (amount % 10)
    if p % 10 == 0:
        i = 2
    elif amount % 10 in range(5, 10) or p in range(11, 20):
        i = 2
    elif amount % 10 == 1:
        i = 0
    elif amount % 10 in range(2, 5):
        i = 1
    return f'{amount} {declensions[i]}'


t0 = '%d.%m.%Y %H:%M'
# d0 = datetime.strptime('16.11.2021 06:30', t0)
# d1 = datetime.strptime('08.11.2022 12:00', t0)

d0 = datetime.strptime('17.11.2021 14:00', t0)
d1 = datetime.strptime('17.11.2021 14:01', t0)

d_cnt = (d1 - d0).days


s_all = (d1 - d0).seconds
h_cnt = s_all // 3600
m_cnt = (s_all // 60) % 60
s_cnt = s_all % 60

if d_cnt < 0:
    print(f'Курс уже вышел!')
elif d_cnt and h_cnt and m_cnt:
    print(
        f'До выхода курса осталось: {choose_plural(d_cnt, ('дней', 'день'))} и {choose_plural(h_cnt, ('часов', 'час'))}')
elif d_cnt and h_cnt == 0:
    print(
        f'До выхода курса осталось: {choose_plural(d_cnt, ('дней', 'день'))}')

elif d_cnt == 0 and h_cnt and m_cnt:
    print(
        f'До выхода курса осталось: {choose_plural(h_cnt, ('часов', 'час'))} и {choose_plural(m_cnt, ('минут', 'минута'))}')
elif d_cnt == 0 and h_cnt and m_cnt == 0:
    print(
        f'До выхода курса осталось: {choose_plural(d_cnt, ('часов', 'час'))}')
elif h_cnt == 0:
    print(
        f'До выхода курса осталось: {choose_plural(m_cnt, ('минут', 'минута'))}')

# elif d_cnt == 0 and h_cnt != 0 and m_cnt != 0:
#     print(f'До выхода курса осталось: {h_cnt} часов и {m_cnt} минут')
# elif d_cnt == 0 and h_cnt != 0 and m_cnt == 0:
#     print(f'До выхода курса осталось: {h_cnt} час')
# elif h_cnt == 0:
#     print(f'До выхода курса осталось: {m_cnt} мин')


print('d_cnt=', d_cnt, 'h_cnt=', h_cnt, 'm_cnt=',
      m_cnt, 's_cnt=', s_cnt, 's_all', s_all)
