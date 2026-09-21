class Gun:
    def shoot(self):
        print('pif')


gun = Gun()
gun.shoot()

Gun().shoot()

Gun.shoot(gun)

Gun.shoot(Gun())


class User:
    def __init__(self, name, friends=0):
        self.name = name
        self.friends = friends

    def add_friends(self, i):
        self.friends += i


user = User('Timur')

user.add_friends(2)
user.add_friends(2)
user.add_friends(3)

print(user.friends, user.__dict__, User.__dict__, sep='\n')

print()


class D:
    def __init__(self, role="guest"):
        if role not in {"guest", "admin", "moder"}:
            print('==', role)  # raise ValueError(role)
        self.role = role


d = D("admin")
print('1=', d.role)
d.role = 'sss'
print('2=', d.role)


class House:
    def __init__(self, color='', rooms=0):
        self.color = color
        self.rooms = rooms

    def paint(self, color):
        self.color = color

    def add_rooms(self, n):
        self.rooms += n


house = House('white', 4)

house.paint('black')
house.add_rooms(1)

print(house.color)
print(house.rooms)

print()


class Circle:
    from math import pi

    def __init__(self, radius=0):

        self.radius = radius
        self.diameter = self.radius*2
        self.area = self.pi*self.radius**2

    diam = 2


circle = Circle(5)

print(circle.radius)
print(circle.diameter)
circle.diam2 = 3
print(circle.area, circle.diam, circle.diam2, circle.__dict__)
