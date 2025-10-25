import turtle

turtle.speed(10)
turtle.pensize(6)
turtle.hideturtle()

colors = ['green', 'red', 'black', 'blue', 'gold']
x = [50, 100, 0, -100, -50]
y = [-50, 0, 0, 0, -50]

for i in range(5):
    turtle.penup()
    turtle.goto(x[i], y[i])
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(colors[i])
    turtle.circle(47)
    turtle.end_fill()

turtle.penup()
turtle.color('black')
turtle.goto(0, -100)
turtle.write('❤️ Happy Pythoning! 🐍', move=True,
             align='center', font=('Arial', 10, 'bold'))
