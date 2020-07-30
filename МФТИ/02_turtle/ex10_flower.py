from turtle import *

def main():
    number_of_petals = 16
    stem(300)
    pensize(1)
    pencolor("Red")
    for i in range(0, number_of_petals, 2):
        if i == 0:
            eight(50)
        else:
            left(360 / number_of_petals)
            eight(50)

def stem(length):
    shape('turtle')
    right(90)
    pensize(5)
    pencolor("Green")
    forward(length)
    penup()
    right(180)
    forward(length)
    right(90)
    pendown()

def eight(radius):
    shape('turtle')
    circle(radius)
    circle(-radius)

main()











