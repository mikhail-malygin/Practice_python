#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_9_3():
    size_of_field = 1


    while wall_is_beneath()	is False :
        size_of_field += 1
        move_down()

    for y in range(size_of_field) :
        for x in range(size_of_field) :
           if (x == y or x + y == size_of_field - 1) is False : fill_cell()
           if y % 2 == 0 and (x != size_of_field - 1) : move_right()
           elif y % 2 != 0 and (x != size_of_field - 1) : move_left()
           elif (y != size_of_field - 1) and (x == size_of_field - 1) : move_up()


    move_down(size_of_field - 1)
    move_left(size_of_field - 1)



if __name__ == '__main__':
    run_tasks()
