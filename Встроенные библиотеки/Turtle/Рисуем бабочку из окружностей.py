import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.right(90)

for i in range(20):
    turtle.left(180)
    turtle.circle(38 + i * 3.5)
turtle.done()
