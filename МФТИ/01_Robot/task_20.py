#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for y in range(12) :
        for x in range(27) :
            fill_cell()
            if y % 2 == 0 and x != 26 : move_right()
            elif x == 26 : move_down()
            elif y % 2 == 1 and x != 26 : move_left()




if __name__ == '__main__':
    run_tasks()
