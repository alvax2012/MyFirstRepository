class ElectricCar:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    color = property(fget=get_color)


car = ElectricCar('black')

# car.color = 'yellow'

print(car.color)

print()


class ElectricCar:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    color = property(get_color, set_color)


car = ElectricCar('black')

print(type(car.color), type(ElectricCar.color))

print()


class ElectricCar:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    color = property(get_color, set_color)


car = ElectricCar('black')

print(ElectricCar.color.fget(car))

print()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return self.length*2 + self.width*2

    def get_area(self):
        return self.length * self.width

    perimeter = property(fget=get_perimeter)
    area = property(fget=get_area)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)

<<<<<<< Updated upstream
print()


class Cat:
    def __init__(self, name):
        self._name = name                               # имя кошки

    @property
    def name(self):                                     # геттер свойства name
        return self._name

    @name.setter
    def get_name(self, name):                               # сеттер свойства name
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    @name.deleter
    def del_name(self):                                     # делитер свойства name
        del self._name


print(Cat.name.fget)
print(Cat.name.fset)
print(Cat.name.fdel)
=======

class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if hours in range(1, 13):
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)


print()


class C:
    def f():
        print('888')


class D():
    def f(self):
        pass


class E(D, C):
    def f(self):
        super().f()


E().f()
C.f()
print(E.__mro__)
# cc = C()
# cc.f()


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)


person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)

person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)
>>>>>>> Stashed changes
