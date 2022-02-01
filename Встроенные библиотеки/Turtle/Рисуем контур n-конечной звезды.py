import turtle as t

t.speed(10)

def draw_star(size, points):
    tipcorner = 20
    cavity = (360 + points * tipcorner) / points  # get corner between tips
    for x in range(points * 2):
        t.forward(size)
        if x % 2 == 0:
            t.left(180 - tipcorner)
        else:
            t.right(180 - cavity)


draw_star(50, 20)
t.done()
