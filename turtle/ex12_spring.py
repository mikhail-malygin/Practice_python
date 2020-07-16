from turtle import *

def main(number_loops, big_radius, small_radius):
    left(90)
    for i in range(number_loops):
        semicircle(big_radius)
        semicircle(small_radius)

def semicircle(radius):
    shape('turtle')
    circle(-radius, 180)

main(10, 25, 5)