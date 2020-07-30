#!/usr/bin/python3

from pyrob.api import *


@task

def task_2_1():
    move_down(2)
    fill_element()
    move_up()
    move_left(3)

def fill_element():
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_right()




if __name__ == '__main__':
    run_tasks()