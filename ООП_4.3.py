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


class Bee:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n


print()


class Gun:
    def __init__(self):
        self.flag = True

    def shoot(self):
        if self.flag:
            print('pif')
        else:
            print('paf')
        self.flag = not self.flag


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()

print()


class Gun:
    counter = 0

    def shoot(self):
        pass
        if self.counter % 2 == 0:
            print('pif')
            self.counter += 1
        else:
            print('paf')
            self.counter += 1


gun = Gun()
# print(Gun.__dict__)
# print(gun.__dict__)    # {}

# gun.shoot()
# print(gun.__dict__)    # {'counter': 1}

# print('888')
# print(Gun.__dir__(Gun))
# print(gun.__dir__())
# print()
# print(dir(Gun))
# print(dir(gun))


class Gun:
    def __init__(self):
        self.cnt = 0

    def shoot(self):
        # print('paf' if self.cnt % 2 else 'pif')
        print(('pif', 'paf')[self.cnt % 2])
        self.cnt += 1

    def shots_count(self):
        return self.cnt

    def shots_reset(self):
        self.cnt = 0


gun = Gun()

print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())


class Scales:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n

    def get_result(self):
        if self.left > self.right:
            return 'Левая чаша тяжелее'
        elif self.left < self.right:
            return 'Правая чаша тяжелее'
        else:
            return 'Весы в равновесии'


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)


print(scales.get_result())
