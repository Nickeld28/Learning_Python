import turtle

turtle.shape('turtle')
turtle.speed(0)

def turtle_ray(a, b):
    """draw ray with turtle"""

    turtle.pendown()
    turtle.right(a)
    turtle.forward(b)
    turtle.penup()
    turtle.left(180)
    turtle.forward(b)
    turtle.left(180)


n = 20
a = 200
for i in range(1, 361, 360 // n):
    turtle_ray(360 // n, a)
turtle.done()
