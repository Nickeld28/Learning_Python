import turtle

turtle.shape('turtle')
turtle.speed(0)

a = 5

for i in range(1, 50):
    turtle.forward(a * i)
    turtle.left(90)
turtle.done()
