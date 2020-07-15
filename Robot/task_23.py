#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    while wall_is_on_the_right() is False :
        move_right()
        if wall_is_above() is False :
            while wall_is_above() is False :
                move_up()
                fill_cell()
            while wall_is_beneath() is False : move_down()
    while wall_is_beneath() : move_left()







if __name__ == '__main__':
    run_tasks()
