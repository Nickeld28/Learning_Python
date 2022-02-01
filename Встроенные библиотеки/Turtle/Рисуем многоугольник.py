import turtle

turtle.shape('turtle')
turtle.speed(1)

def draw_n_angle(l, n:int):
    """drawing n-angle, l - length of edge"""

    for i in range(1, n + 1):
        turtle.forward(l)
        turtle.left(360 // n)

draw_n_angle(100, 7)
turtle.done()
