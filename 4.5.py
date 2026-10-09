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
