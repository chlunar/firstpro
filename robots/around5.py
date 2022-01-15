# This program lets the robot go around its world
# counter clockwise, stopping when it returns
# to the starting point.

from cs1robots import *
import time

load_world("../worlds/amazing2.wld")
hubo = Robot(beepers = 1)
hubo.set_trace("blue")
sleep_time = 0.5

def turn_right():
  for i in range(3):
    hubo.turn_left()

def mark_starting_point_and_move():
    time.sleep(sleep_time)
    hubo.drop_beeper()
    while not hubo.front_is_clear():
        time.sleep(sleep_time)
        hubo.turn_left()
    time.sleep(sleep_time)
    hubo.move()

def follow_right_wall():
    if hubo.right_is_clear():
        # Keep to the right
        time.sleep(sleep_time)
        turn_right()
        time.sleep(sleep_time)
        hubo.move()
    elif hubo.front_is_clear():
        # move following the right wall
        time.sleep(sleep_time)
        hubo.move()
    else:
        # follow the wall
        time.sleep(sleep_time)
        hubo.turn_left()    


# ---- end of definitions, begin solution ------

mark_starting_point_and_move()

while not hubo.on_beeper():
    follow_right_wall()
  
