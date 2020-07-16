from turtle import *

def main(number_wings):
    shape('turtle')
    left(90)
    for i in range(0, number_wings, 2):
        eight(30 + 5 * i)

def eight(radius):
    circle(radius)
    circle(-radius)

main(30)


