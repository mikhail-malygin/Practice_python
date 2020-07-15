import turtle

turtle.shape('turtle')

def eight(radius):
    turtle.circle(radius)
    turtle.circle(-radius)

def stem(length):
    turtle.right(90)
    turtle.pensize(5)
    turtle.pencolor("Green")
    turtle.forward(length)
    turtle.penup()
    turtle.right(180)
    turtle.forward(length)
    turtle.right(90)
    turtle.pendown()



number_of_petals = 16

stem(300)
turtle.pensize(1)
turtle.pencolor("Red")

for i in range(0, number_of_petals, 2):
    if i == 0 :
        eight(50)
    else :
        turtle.left(360 / number_of_petals)
        eight(50)



