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
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self._s1 = round(-self.b / (2 * self.a), 3)
        self._s2 = round(self.b**2 - 4 * self.a * self.c, 3)

    @property
    def x1(self):
        if self._s2 >= 0:
            return round(self._s1 - self._s2 ** (1/2) / (2 * self.a), 3)

    @property
    def x2(self):
        if self._s2 >= 0:
            return round(self._s1 + self._s2 ** (1/2) / (2 * self.a), 3)

    @property
    def view(self):
        return f'{'' if self.a > 0 else '-'}{abs(self.a)}x^2 {'+' if self.b >= 0 else '-'} {abs(self.b)}x {'+' if self.c >= 0 else '-'} {abs(self.c)}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, t):
        self.a, self.b, self.c = t
        self._s1 = - self.b / (2 * self.a)
        self._s2 = self.b**2 - 4 * self.a * self.c


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

print()
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
print(polynom.coefficients)

print()
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

print()
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

print()
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()
print()
print()
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
