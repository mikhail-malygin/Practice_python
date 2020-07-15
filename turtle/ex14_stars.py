from turtle import *
from math import *

shape('turtle')
delay(10)



def star(length, number):
    for i in range(number):
        forward(length)
        right(180 - 360 / (2 * number))

star(100, 5)
penup()
forward(200)
pendown()
star(100, 11)