from math import pi, sin, cos
import turtle

turtle.shape('turtle')
length = 10
i = 0

while i < 20 :
    turtle.forward(10 + i * length)
    turtle.left(90)
    turtle.forward(10 + i * length)
    turtle.left(90)
    turtle.forward(10 + (i + 1) * length)
    turtle.left(90)
    turtle.forward(10 + (i + 1) * length)
    turtle.left(90)
    i += 2





'''for i in range(200):
    t = i / 10 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)'''