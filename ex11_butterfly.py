import turtle

turtle.shape('turtle')

def eight(radius):
    turtle.circle(radius)
    turtle.circle(-radius)

number_of_wings = 30

turtle.left(90)

for i in range(0, number_of_wings, 2):
    eight(30 + 5 * i)