from turtle import *

def main():
    spider(12, 100)

def spider(number_paws, length_paws):
    shape('turtle')
    angleFi = 360 / number_paws
    for i in range(number_paws) :
        right(angleFi)
        forward(length_paws)
        stamp()
        penup()
        backward(length_paws)
        pendown()

main()