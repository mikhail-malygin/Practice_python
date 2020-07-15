#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    if wall_is_on_the_right() and wall_is_beneath() :
        fill_cell()
    else :
        number_lines = number_columns = 1
        while wall_is_on_the_right() is False :
            move_right()
            number_columns += 1
        while wall_is_beneath() is False :
            move_down()
            number_lines += 1
        for y in range(number_lines) :
            for x in range(number_columns) :
                fill_cell()
                if y % 2 == 0 and x != number_columns - 1 : move_left()
                elif x == number_columns - 1 and y != number_lines - 1 : move_up()
                elif y % 2 == 1 and x != number_columns - 1 : move_right()
        while wall_is_beneath() is False : move_down()
        if wall_is_on_the_right() : move_left(number_columns - 1)



if __name__ == '__main__':
    run_tasks()
