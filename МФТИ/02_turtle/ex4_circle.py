from turtle import *

def main():
    circle(10, 30)

def circle(side, number_of_sides):
    shape('turtle')
    angleFi = 180 * (number_of_sides -2) / number_of_sides
    for i in range(number_of_sides):
        left(180 - angleFi / 2) if i == 0 else left(180 - angleFi)
        forward(side)

main()