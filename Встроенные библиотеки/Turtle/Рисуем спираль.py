import turtle

turtle.shape('turtle')
turtle.speed(0)
# рисуем спираль
for i in range(300):
    turtle.forward(1 + i / 15)
    turtle.left(10)
turtle.done()
