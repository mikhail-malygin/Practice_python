#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    counter = 0
    the_previous_cell_is_filled = False
    while wall_is_on_the_right() is False and counter < 3 :
        if cell_is_filled()	is False :
            the_previous_cell_is_filled = False
            counter = 0
            move_right()
        else :
            if the_previous_cell_is_filled is False : the_previous_cell_is_filled = True
            counter += 1
            if counter != 3 : move_right()








if __name__ == '__main__':
    run_tasks()
