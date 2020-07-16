from turtle import *

def main():
    square_spiral(10, 10)

def square_spiral(initial_length, increment_length):
    shape('turtle')
    i = 0
    while i < 20 :
        for j in range(4):
            if j < 2 :
                forward(initial_length + i * increment_length)
            else :
                forward(initial_length + (i + 1) * increment_length)
            left(90)
        i += 2

main()



