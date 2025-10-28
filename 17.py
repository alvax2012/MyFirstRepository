class Person:

    def __init__(self, dt1, name1, cnt1):
        self.name = name1
        self.dt = dt1
        self.cnt = int(cnt1)

    def display_info(self):
        l = int(self.dt.split('-')[1])
        q = 0
        if l == 6:
            q = 7
        elif l == 3:
            q == 4
        else:
            q == 3
        return q


# tom = Person("Tom", 22)
# tom.display_info()


def report1(s):
    m = []
    d = {}
    l = list(map(lambda x: x.split(':'), s.split(';')))
    # d = d.setdefault
    for i in l:
        # print(i)
        p = Person(i[0], i[1], i[2])
        m.append(
            f'Q: {p.display_info()}\n Наименование: {p.name} \n Количество: {p.cnt}')
        d[i[0]] = d.setdefault(i[0], 0) + 1
    print(d)
    return m


s = '2025-06-01:ручка:3;2025-06-01:стол:3;2025-03-02:стол:5'
tt = report1(s)
print(report1(s))

for i in tt:
    print(i)
