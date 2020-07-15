from turtle import *

shape('turtle')

def face(radius_face):
    color('black', 'yellow')
    begin_fill()
    left(90)
    circle(radius_face)
    end_fill()

def eyes(radius_eye):
    color('black', 'blue')
    begin_fill()
    circle(radius_eye)
    end_fill()

def nose(height_nose):
    width(5)
    forward(height_nose)

def smile(radius_smile):
    width(5)
    pencolor('Red')
    circle(-radius_smile, 180)


radius_face = 200
radius_eye = 30
height_nose = 0.2 * radius_face
radius_smile = 80

face(radius_face)
left(90)
penup()
forward(1.25 * radius_face)
right(90)
forward(0.5 * radius_face)
pendown()
eyes(radius_eye)
right(90)
penup()
forward(0.5 * radius_face)
right(90)
pendown()
eyes(radius_eye)
penup()
right(90)
forward(0.25 * radius_face)
left(90)
forward(0.4 * radius_face)
pendown()
nose(height_nose)
penup()
forward(0.1 * radius_face)
left(90)
forward(0.3 * radius_face)
right(90)
pendown()
smile(radius_smile)


