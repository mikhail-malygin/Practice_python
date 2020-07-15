#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(2)
    for x in range(5) :
        fill_element()
        if x != 4 : move_right(2)
    move_up()
    move_left(2)

def fill_element():
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


if __name__ == '__main__':
    run_tasks()
