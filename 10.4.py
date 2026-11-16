numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

del numbers[4]

print(list(iterator))


numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

del numbers[0]
del numbers[0]

print(next(iterator), numbers)

print()


class list_iterator:
    def __init__(self, data):
        self.data = data
        self.index = -1
        print('id=', id(numbers))

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration
        print('i=', self.index, self.data)
        return self.data[self.index]


numbers = [1, 2, 3, 4, 5]
print(id(numbers))
iterator = list_iterator(numbers)
numbers = [7, 7, 7, 7, 7]
print(id(numbers))

next(iterator)
next(iterator)
del numbers[0]
del numbers[1]
print(next(iterator))


numbers = [1, 2, 3, 4, 5]

for i in numbers:
    del numbers[0]
    print(i)


class Repeater:
    def __init__(self, data):
        self.data = data
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        return self.data
        # self.i += 1
        # if self.i == len(self.data):
        #     raise StopIteration
        # return self.data[self.i]


geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))
