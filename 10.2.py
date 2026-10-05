numbers = [4, 8, 15, 16, 23, 42]

iterator = iter(numbers)              # создаем итератор на основе списка

print(15 in iterator)
# print(23 in iterator)

x, *y = iterator
print(x, y)
