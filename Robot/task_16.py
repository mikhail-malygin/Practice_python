#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while wall_is_above() is False :
        move_up()
    if wall_is_on_the_right() :
        while wall_is_on_the_left() is False :
            move_left()
    else :
        while wall_is_on_the_right() is False :
            move_right()



if __name__ == '__main__':
    run_tasks()
