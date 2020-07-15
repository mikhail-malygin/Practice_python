#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above() :
        if wall_is_on_the_left() :
            move_right(9)
            move_down(9)
        else :
            move_left(9)
            move_down(9)
    else :
        if wall_is_on_the_right() :
            move_left(9)
            move_up(9)
        else :
            move_right(9)
            move_up(9)



if __name__ == '__main__':
    run_tasks()
