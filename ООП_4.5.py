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
