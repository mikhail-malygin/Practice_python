#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_down()
    for y in range(5) :
        for x in range(10) :
            fill_element_left_to_right() if y % 2 == 0 else fill_element_right_to_left()
            if x != 9 and y % 2 == 0 : move_right(2)
            elif x != 9 and y % 2 != 0 : move_left(2)
            elif x == 9 and y != 4 : move_down(4)
            elif x == 9 and y == 4 :
                move_up()
                while wall_is_on_the_left() is False : move_left()


def fill_element_left_to_right():
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()

def fill_element_right_to_left():
    fill_cell()
    move_left()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_left()
    fill_cell()


if __name__ == '__main__':
    run_tasks()
