from turtle import *
from math import *


def main(R,  number_of_right_polygons):
    '''
    R - радиус описанной окружности треугольника
    number_of_right_polygons - число вписанных правильных многоугольников
    '''

    shape('turtle')
    delay(10)
    delta = 1.5 # delta - коэффициент прироста радиуса описанной окружности
    R_polygons = [R]
    for i in range(1, 10):
        # радиусы описанных окружностей правильного многоугольника
        if i > 5 : delta -= 0.1
        R_polygons.append(delta * R_polygons[i - 1])


    for i in range(number_of_right_polygons):
        R_current = R_polygons[i]
        penup()
        forward(R_current)
        pendown()
        right_polygon(i + 3, R_current)


def right_polygon(number_of_sides, R_current):
    side =  2 * R_current * sin(pi / number_of_sides)
    angleFi = 180 * (number_of_sides - 2) / number_of_sides
    for j in range(number_of_sides):
        if j == 0:
            left(180 - angleFi / 2)
            forward(side)
        else:
            left(180 - angleFi)
            forward(side)
            if j == number_of_sides - 1:
                right(angleFi / 2)
                penup()
                backward(R_current)
                pendown()


main(10, 10)








