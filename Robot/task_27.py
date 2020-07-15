#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    counter = 0
    i = 0
    interval_is_not_null = False
    flag = 0
    while wall_is_on_the_right() is False :
        move_right()
        if interval_is_not_null is False and flag == 0 :
            fill_cell()
            flag = 1
        elif interval_is_not_null is False and flag != 0 :
            fill_cell()
            interval_is_not_null = True
            counter += 1
            i = counter
        elif interval_is_not_null and i != 0 : i -= 1
        elif interval_is_not_null and i == 0 :
            fill_cell()
            counter += 1
            i = counter



if __name__ == '__main__':
    run_tasks()
