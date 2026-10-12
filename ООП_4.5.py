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
