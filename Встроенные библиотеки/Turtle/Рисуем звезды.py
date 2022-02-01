import turtle
from math import sin
from math import pi


def draw_star(radius: float, n: int, m: int):
    """ Drawing n-pointed star. The starting position of the turtle is the center of the circumscribed circle.
        Takes args: radius of the circumscribed circle and
        n - number of sides of regular polygon (points of a star). Attention: works only if n >= 0.
        m - Need to add information about this arg. Attention: works only if m >= 1.
    """

    def draw_regular_polygon(radius, n: int):
        """ Draws a regular polygon.
            Takes arg: n - number of sides of a regular polygon. Attention: works only n >= 3
        """
        polygon_outside_angle = 360 / n
        turtle.left(polygon_outside_angle / 2)
        forward_and_turn(polygon_length(radius, n), polygon_outside_angle, n)

    def outside_angle(n: int):
        """ Returns angle of rotation. This is outside angle of a drawable star.
            Takes arg: n - number of points of a drawable star. Attention: works only if n % != 0
        """
        return n // 2 * 360 / n

    def inner_angle(outside_angle: float):
        """ Returns inner angle of a drawable star.
            Takes arg: outside angle of a drawable star.
        """
        return 180 - outside_angle

    def polygon_length(radius: float, n: int):
        """ Returns length of side of regular polygon.
            Takes arg: radius of the circumscribed circle and n - number of sides of regular polygon.
        """
        return radius * (2 * sin(pi / n))

    def star_distance(polygon_length: float, inner_angle: float):
        """ Returns distance between two points of a drawable star.
            Takes arg: length of side of regular polygon and inner angle of a drawable star.
        """

        return polygon_length / 2 / sin(inner_angle * pi / 360)

    def forward_and_turn(distance: float, angle: float, n: int):
        """ Move the turtle. Takes args: distance between two points,
            angle of rotation and number of sides of regular polygon (points of a star)
        """
        for i in range(1, n + 1):
            turtle.forward(distance)
            turtle.left(angle)

    staring_turtle_angle = turtle.heading()

    # prepare to draw a star, find a start position:
    turtle.penup()
    turtle.setheading(90)
    forward_and_turn(radius, 90, 1)
    turtle.pendown()

    #  turtle.circle(radius)  #  this code to draw the circumscribed circle

    if m == 1:
        draw_regular_polygon(radius, n)
        turtle.penup()
        turtle.setheading(-90)
        # return the turtle to the starting point with the starting angle of rotation:
        turtle.forward(radius)
        turtle.setheading(staring_turtle_angle)
    elif m == 2:
        if n % 2 != 0:
            # set the required rotation angle:
            turtle.left(outside_angle(n) / 2)

            # draw a star:
            forward_and_turn(star_distance(polygon_length(radius, n), inner_angle(outside_angle(n))), outside_angle(n),
                             n)

            # return the turtle to the starting point with the starting angle of rotation:
            turtle.penup()
            turtle.setheading(-90)
            turtle.forward(radius)
            turtle.setheading(staring_turtle_angle)
        elif n == 4:
            turtle.left(outside_angle(n) / 2)
            forward_and_turn(polygon_length(radius, n), inner_angle(outside_angle(n)), outside_angle(n), n)
            turtle.penup()
            turtle.setheading(270)
            forward_and_turn(radius * 2, outside_angle(n) + inner_angle(outside_angle(n)) / 2, 1)
            turtle.pendown()
            forward_and_turn(polygon_length(radius, n), inner_angle(outside_angle(n)), outside_angle(n), n)
            turtle.setheading(90)
            turtle.penup()
            turtle.forward(radius)
            turtle.setheading(staring_turtle_angle)

        elif n % 2 == 0:
            n //= 2
            turtle.left(outside_angle(n) / 2)
            forward_and_turn(star_distance(polygon_length(radius, n), inner_angle(outside_angle(n))), outside_angle(n), n)
            turtle.penup()
            turtle.setheading(270)
            forward_and_turn(radius * 2, outside_angle(n) + inner_angle(outside_angle(n)) / 2, 1)
            turtle.pendown()
            forward_and_turn(star_distance(polygon_length(radius, n), inner_angle(outside_angle(n))), outside_angle(n),
                             n)
            turtle.setheading(90)
            turtle.penup()
            turtle.forward(radius)
            turtle.setheading(staring_turtle_angle)


turtle.shape('turtle')
turtle.speed(10)
turtle.goto(0, 0)

turtle.left(0)
# draw_star(150, 5, 2)


for i in range(5, 25, 2):
    draw_star(150, i, 2)
    turtle.clear()
turtle.exitonclick()
#   turtle.forward(50)
#  turtle.left(36)
