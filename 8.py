import turtle

turtle.forward(30)
turtle.left(45)

turtle.forward(14)
turtle.left(45)

turtle.forward(30)
turtle.left(45)

turtle.forward(14)
turtle.left(45)

turtle.forward(10)
turtle.right(90)

turtle.forward(60)
turtle.right(90)

turtle.forward(10)
turtle.left(90)

turtle.forward(20)
turtle.left(45)

turtle.forward(28)
turtle.left(45)

turtle.forward(10)
turtle.left(90)

turtle.forward(20)
turtle.left(180)

turtle.forward(20)
turtle.left(90)

turtle.forward(10)
turtle.left(45)

turtle.forward(28)
turtle.left(45)

turtle.forward(20)
turtle.left(90)

turtle.forward(10)
turtle.right(90)

turtle.forward(60)
turtle.right(90)

turtle.forward(10)
turtle.left(45)

turtle.forward(14)
turtle.left(45)

turtle.forward(30)
turtle.left(45)

turtle.forward(14)
turtle.left(45)

turtle.forward(30)

turtle.done()
print('1')


a = 2
b = 3
for _ in '+-*':
    print(f'{a} {_} {b} =', eval(f'{a} {_} {b}'))


numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 +
           9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
number = {abs(_): _ for _ in numbers}
m = max(number)
print(m)
print(number[m])
