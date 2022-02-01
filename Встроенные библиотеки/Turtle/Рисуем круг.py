import turtle

turtle.shape('turtle')
turtle.speed(0)
# рисуем круг пошагово циклом
for i in range(72):
    turtle.forward(5)
    turtle.left(5)
# рисуем круг встроенной функцией
turtle.circle(100, 360, 50)
turtle.done()
