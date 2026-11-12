class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()


person = Person('Mike', 'Pondsmith')

print(person.name)
print(person.surname)
print(person.fullname)


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9


class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)


account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)


class QuadraticPolynomial:
    def s1(a, b):
        return round(-b / (2 * a), 3)

    def s2(a, b, c):
        return round(b**2 - 4 * a * c, 3)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def x1(self):
        s2 = QuadraticPolynomial.s2(self._a, self._b, self._c)
        if s2 >= 0:
            return round(QuadraticPolynomial.s1(self._a, self._b) - s2 ** (1/2) / (2 * self._a), 3)

    @property
    def x2(self):
        s2 = QuadraticPolynomial.s2(self._a, self._b, self._c)
        if s2 >= 0:
            return round(QuadraticPolynomial.s1(self._a, self._b) + s2 ** (1/2) / (2 * self._a), 3)

    @property
    def view(self):
        return f'{'' if self._a > 0 else '-'}{abs(self._a)}x^2 {'+' if self._b >= 0 else '-'} {abs(self._b)}x {'+' if self._c >= 0 else '-'} {abs(self._c)}'

    @property
    def coefficients(self):
        return self._a, self._b, self._c

    @coefficients.setter
    def coefficients(self, t):
        self._a, self._b, self._c = t


# print()
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.a, polynom.b, polynom.c = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()


class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        # return f'{int(self.r, 16):X}',  f'{int(self.g, 16):X}',  f'{int(self.b, 16):X}'
        return self._hexcode

    @hexcode.setter
    def hexcode(self, s):
        self._hexcode = s
        self.r, self.g, self.b = int(s[:2], 16), int(
            s[2:4], 16), int(s[4:], 16)


color = Color('0000FF')
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
print()

color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

print()
print(dir(color))
print()
print(color.__dict__)
print('-'*100)

# print(dir(Color))
# print()
# print(Color.__dict__)
