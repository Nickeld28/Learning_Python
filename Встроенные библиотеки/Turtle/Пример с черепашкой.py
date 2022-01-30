import turtle


t = turtle.Turtle()
t.speed(10)
t.color('blue')
t.fillcolor('red')
# Рисует букву S
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.penup()
t.forward(200)
t.pendown()

# Рисует квадрат со сторонами в 100 пикселей
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.forward(200)
t.pendown()

# Рисует окружность с радиусом 100 пикселей
t.circle(100)

t.penup()
t.forward(300)
t.pendown()

# Рисует 10 квадратов внутри друг друга
# range (start, stop, step)
z = int()
for z in range(20, 350, 35):
    t.forward(z)
    t.left(90)
    t.forward(z)
    t.left(90)
    t.forward(z)
    t.left(90)
    t.forward(z)
    t.penup()
    t.right(45)
    t.forward(25)
    t.left(135)
    t.pendown()

t.penup()
t.right(90)
t.forward(200)
t.pendown()

    # Рисует паука с указанным числом лап
# range (start, stop, step)
n = 6
y = int(360/n)

for n in range(y, 361, y):
    t.right(y)
    t.forward(100)
    t.penup()
    t.left(180)
    t.forward(100)
    t.right(180)
    t.pendown()
