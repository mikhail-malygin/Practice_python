import turtle


turtle.shape('turtle')
for i in range(10) :
    turtle.forward(10 + 20 * i)
    turtle.left(90)
    turtle.forward(10 + 20 * i)
    turtle.left(90)
    turtle.forward(10 + 20 * i)
    turtle.left(90)
    turtle.forward(10 + 20 * i)
    turtle.right(45)
    if i != 9 :
        turtle.penup()
        turtle.forward(10 * 2**0.5)
        turtle.pendown()
        turtle.left(135)


