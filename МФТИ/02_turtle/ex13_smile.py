from turtle import *

def main(radius_face, radius_eye, height_nose, radius_smile):
    # Подготовка и рисование головы
    shape('turtle')
    penup()
    forward(radius_face)
    pendown()
    face(radius_face)

    # Рисование глаз
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

    # Рисование носа
    penup()
    right(90)
    forward(0.25 * radius_face)
    left(90)
    forward(0.4 * radius_face)
    pendown()
    nose(height_nose)

    # Рисование губ
    penup()
    forward(0.1 * radius_face)
    left(90)
    forward(0.4 * radius_face)
    right(90)
    pendown()
    smile(radius_smile)

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

main(200, 30, 40, 80)


