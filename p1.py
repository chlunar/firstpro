from cs1robots import *
load_world('myworld.wld')
gshs=Robot()
gshs.set_trace(color='blue')
gshs.set_pause(0.1)

def turn_right():
    for i in range(3):
        gshs.turn_left()

def turn_around():
    gshs.turn_left()
    gshs.turn_left()

def move_around():
    while not gshs.right_is_clear():
        gshs.move()
    turn_right()
    gshs.move()
    turn_right()
    while gshs.front_is_clear():
        gshs.move()
    turn_around()
    if gshs.on_beeper():
        gshs.pick_beeper()


gshs.turn_left()
for i in range(9):
    move_around()
