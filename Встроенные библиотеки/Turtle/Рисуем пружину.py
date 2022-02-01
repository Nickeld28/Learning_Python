import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.penup()
turtle.goto(-250, 0)
turtle.left(90)
turtle.pendown()

for i in range(6):
    turtle.circle(-50, 180)
    if i < 5:
        turtle.circle(-10, 180)
    else:
        break
turtle.done()
