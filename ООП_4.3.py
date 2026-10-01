import sys


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


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x**2 + self.y**2)**0.5


vector = Vector()

print(vector.x, vector.y)
print(vector.abs())


vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())


class Numbers:
    def __init__(self):
        self.l = []

    def add_number(self, n):
        self.l.append(n)

    def get_even(self):
        return [i for i in self.l if i not in self.get_odd()]

    def get_odd(self):
        return [i for i in self.l if i % 2]


numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())

print()


class TextHandler:
    def __init__(self):
        self.list_text = []

    def add_words(self, text):
        self.list_text.extend(text.split())

    def get_shortest_words(self):
        min_text = min(map(len, self.list_text), default='')
        return [i for i in self.list_text if len(i) == min_text]
        # if self.list_text:
        #     min_text = min(map(len, self.list_text))
        #     return [i for i in self.list_text if len(i) == min_text]
        # else:
        #     return []

    def get_longest_words(self):
        max_text = max(map(len, self.list_text), default='')
        return [i for i in self.list_text if len(i) == max_text]
        # if self.list_text:
        #     max_text = max(map(len, self.list_text))
        #     return [i for i in self.list_text if len(i) == max_text]
        # else:
        #     return []


texthandler = TextHandler()

# texthandler.add_words('The world will hold my trial for your sins')
# texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())

print()


class Todo:
    def __init__(self):
        self.things = []

    def add(self, *thing):
        self.things.append(thing)
        self.min = min(self.things, key=lambda x: x[1], default=None)[1]
        self.max = max(self.things, key=lambda x: x[1], default=None)[1]

    def get_by_priority(self, n):
        return [i[0] for i in self.things if i[1] == n]

    def get_low_priority(self):
        return self.get_by_priority(self.min)

    def get_high_priority(self):
        return self.get_by_priority(self.max)


todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))

# todo.add('Проснуться', 3)
# todo.add('Помыться', 2)
# todo.add('Поесть', 2)

# print(todo.get_by_priority(2))


# print(todo.things)
# print(todo.get_by_priority(1))
# print(todo.get_low_priority())
# print(todo.get_high_priority())

print()


class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, *s):
        if s not in self.delivery_data:
            self.delivery_data.append(s)

    def get_houses_for_street(self, st):
        res = []
        for i in self.delivery_data:
            if i[0] == st and i[1] not in res:
                res.append(i[1])
        return res

    def get_flats_for_house(self, st, ho):
        res = []
        for s, h, k in self.delivery_data:
            if s == st and h == ho and k not in res:
                res.append(k)
        return res
        # return [k for s, h, k in self.delivery_data if s == st and h == ho] if self.delivery_data else []


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))

print()


class Wordplay:
    def __init__(self, words=[]):
        # self.res = {i: None for i in words}
        # self.words = list(self.res)
        self.words = words[:]

    def add_word(self, word):
        # self.res.update({word: None})
        # self.words = list(self.res)
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]

    def only(self, *args):
        return [i for i in self.words if all(k in args for k in i)]
        # return [i for i in self.res if set(i) == set(args)]

    def avoid(self, *args):
        return [i for i in self.words if all(k not in args for k in i)]


# wordplay = Wordplay(['bee', 'geek', 'cool', 'stepik'])
# wordplay.add_word('python')
# print(wordplay.words)
# print(wordplay.words_with_length(1))
# print(wordplay.only('a', 'b', 'c'))
# print(wordplay.avoid('a', 'b', 'c'))

words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)

print()


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self, chr='N'):
        return chr

    def can_move(self, horizontal, vertical):
        if abs(self.horizontal - horizontal) == 1 and abs(self.vertical - vertical) == 3:
            pass
        elif abs(self.horizontal - horizontal) == 3 and abs(self.vertical - vertical) == 1:
            pass

    def move_to(self):
        pass

    def draw_board(self):
        pass


knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
