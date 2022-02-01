import turtle


turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)


for i in range(3, 11):
    turtle.pendown()
    turtle.circle(20 * (i-2), 360, i)
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.done()
