from turtle import *
from math import *



shape('turtle')
delay(10)


R = 10 # радиус описанной окружности треугольника
delta = 15 # прирост радиуса описанной окружности
number_of_right_polygons = 10


penup()
forward(R)
pendown()
for i in range(number_of_right_polygons):
    number_of_sides = i + 3
    side = i * delta + 2 * R * sin(pi / number_of_sides)
    angleFi = 180 * (number_of_sides - 2) / number_of_sides
    for j in range(number_of_sides):
        if j == 0:
            left(180 - angleFi / 2)
            forward(side)
        else:
            left(180 - angleFi)
            forward(side)
            if j == number_of_sides - 1 : right(angleFi / 2)
    if i != number_of_right_polygons - 1 :
        penup()
        forward(delta)
        pendown()









