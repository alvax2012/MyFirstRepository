from math import pi


class Circle():
    def __init__(self, radius):
        self._radius = radius
        self._diameter = self._radius*2
        self._area = pi*self._radius**2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


circle = Circle(1)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))

print()


class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance < amount:
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())

account = BankAccount(100)

try:
    account.withdraw(150)
except ValueError as e:
    print(e)


account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)
except ValueError as e:
    print(e)


print()


class User():
    def __init__(self, name, age):
        # self._name =
        self.set_name(name)
        # self._age =
        self.set_age(age)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, name):
        if not name or not isinstance(name, str) or not name.isalpha():
            raise ValueError('Некорректное имя')
        self._name = name

    def set_age(self, age):
        if age not in range(111):
            raise ValueError('Некорректный возраст')
        self._age = age


user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())

print()

user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
