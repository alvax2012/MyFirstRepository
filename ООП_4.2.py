class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        self.night_vision = True

    name1 = 111                    # способность видеть в темноте


cat1 = Cat('Британский', 'Кемаль')
cat2 = Cat('Манчкин', 'Роджер')
cat2.night_vision = True

print(cat1.night_vision, cat1.__dict__)
print(cat2.night_vision, cat1.__dict__)

print(Cat.__dict__)

print()


class C:
    def f():
        pass


class D():
    def f(self):
        pass


class E(D, C):
    def f(self):
        super().f()


E().f()
