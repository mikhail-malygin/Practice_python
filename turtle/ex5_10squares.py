from turtle import *

def main():
    nested_squares(10, 10, 20)

def nested_squares(number_of_squares, initial_length, increment_length):
    shape('turtle')
    for i in range(number_of_squares) :
        for j in range(4):
            forward(initial_length + increment_length * i)
            left(90) if j != 3 else right(45)
        if i != number_of_squares - 1:
            penup()
            forward(10 * 2**0.5)
            pendown()
            left(135)

main()
