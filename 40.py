from datetime import date, time, datetime

fmt = '%d.%m.%Y; %H:%M'
d = {}
with open('diary.txt', encoding='utf-8') as f:

    for i in f:

        try:
            k = datetime.strptime(i.strip(), fmt)
            d.setdefault(k, [])
            # print(datetime.strptime(i.strip(), fmt))
        except ValueError:
            d[k] += [i]
            # print('---')


print(sorted(d.items(), key=lambda x: x[0]))
