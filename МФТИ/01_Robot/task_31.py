#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.01)
def task_8_30():

    current_number_of_apperture = 0
    #width = 1
    counter = 1

    while 1 :
        while wall_is_beneath() is False :
            move_down()
            if wall_is_beneath() : current_number_of_apperture = counter = 0

        while wall_is_on_the_left() is False :
            move_left()
            counter += 1
            if wall_is_beneath() is False :
                current_number_of_apperture = counter
                break

        if current_number_of_apperture == 0 :
            counter = 0
            while wall_is_on_the_right() is False :
                move_right()
                counter += 1
                if wall_is_beneath() is False :
                    current_number_of_apperture = counter
                    break

        if current_number_of_apperture == 0 :
            while wall_is_on_the_left() is False : move_left()
            break









if __name__ == '__main__':
    run_tasks()
