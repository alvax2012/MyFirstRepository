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


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times+1

    def __iter__(self):
        return self

    def __next__(self):
        self.times -= 1
        if self.times == 0:
            raise StopIteration
        return self.obj


bee = BoundedRepeater('bee', 2)

print(next(bee))
print(next(bee))


# class Square:
#     def __init__(self, n):
#         self.n = n
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.i += 1
#         if self.i > self.n:
#             raise StopIteration
#         return self.i**2


class Square:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('i=', self.current)
        if self.n == self.current:
            raise StopIteration
        self.current += 1
        print('i1=', self.current)
        return self.current ** 2


squares = Square(2)

print(next(squares))
print(next(squares), squares.current)

print('--')


class Fibonacci:
    def __init__(self):
        self._pre = 0
        self._cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        # if self._pre == 0:
        #     t = self._cur
        #     self._cur = self._pre + self._cur
        #     self._pre = t
        #     return 1
        #     self._cur = 1
        # self._pre = self._cur
        # t = self._cur
        self._pre, self._cur = self._cur, self._pre + self._cur
        # self._pre = t

        return self._cur

# 1,1,2,3,5,8,13,21,34


fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
