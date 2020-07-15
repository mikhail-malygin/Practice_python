#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while wall_is_on_the_right() is False:
        if wall_is_above() is False and wall_is_beneath() :
            move_up()
            fill_cell()
            move_down()
        elif wall_is_above() and wall_is_beneath() is False :
            move_down()
            fill_cell()
            move_up()
        elif wall_is_above() is False and wall_is_beneath() is False :
            move_down()
            fill_cell()
            move_up(2)
            fill_cell()
            move_down()
        move_right()
    if wall_is_above() is False and wall_is_beneath() :
        move_up()
        fill_cell()
        move_down()
    elif wall_is_above() and wall_is_beneath() is False :
        move_down()
        fill_cell()
        move_up()
    elif wall_is_above() is False and wall_is_beneath() is False :
        move_down()
        fill_cell()
        move_up(2)
        fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
