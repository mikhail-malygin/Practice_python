from math import *
from turtle import *

def main():
    spiral()

def spiral():
    shape('turtle')
    for i in range(200):
        t = i / 10 * pi
        dx = t * cos(t)
        dy = t * sin(t)
        goto(dx, dy)

main()


