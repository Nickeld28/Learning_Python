import turtle

turtle.shape('turtle')
turtle.speed(0)
# рисуем вложенные квадраты
def turtle_square(a):
    """draw square with turtle"""

    turtle.forward(a)
    for i in range(3):
        turtle.left(90)
        turtle.forward(a)
    turtle.left(90)

for i in range(1, 11):
    turtle_square(i * 20)
    turtle.penup()
    turtle.goto(- i * 10, - i * 10)
    turtle.right(0)
    turtle.pendown()
turtle.done()
