from cs1robots import *
load_world('p2.wld')
gshs=Robot()
gshs.set_trace(color='blue')
gshs.set_pause(0.1)

for i in [10, 8, 6, 4, 2]:
    for j in range(i):
        gshs.move()
    gshs.turn_left()
    for j in range(i):
        gshs.move()
    gshs.turn_left()
    for j in range(i):
        gshs.move()
    gshs.turn_left()
    for j in range(i-1):
        gshs.move()
    gshs.turn_left()
    gshs.move()
gshs.pick_beeper()