from turtle import *


def main(length):
    shape('turtle')
    delay(10)

    star(length, 5)
    penup()
    forward(2 * length)
    pendown()
    star(length, 11)


def star(length, number):
    for i in range(number):
        forward(length)
        right(180 - 360 / (2 * number))

main(100)