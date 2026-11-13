class Counter:
    # конструктор принимает два аргумента low и high (помимо self)
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.low > self.high:
            raise StopIteration
        else:
            t = self.low
            self.low += 1
            return t  # self.low - 1


# создаем итератор Counter, передавая значения low=3, high=10
counter1 = Counter(3, 10)

for i in counter1:                # неявно вызываем функцию next()
    print(i)

# создаем итератор Counter, передавая значения low=100, high=103
counter2 = Counter(100, 103)
print(next(counter2))             # явно вызываем функцию next()
print(next(counter2))             # явно вызываем функцию next()
