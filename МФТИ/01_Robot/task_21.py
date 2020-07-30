#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for y in range(13) :
        for x_right in range(y + 1) :
            fill_cell()
            move_right()
        for x_left in range(y + 1) : move_left()
        move_down()




if __name__ == '__main__':
    run_tasks()
