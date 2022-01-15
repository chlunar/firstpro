from cs1robots import *
import time

load_world("../worlds/amazing2.wld")
hubo = Robot(beepers = 10)
hubo.set_trace("blue")
sleep_time = 0.5

def turn_right():
  for i in range(3):
    hubo.turn_left()

#---------------------------------------------------

time.sleep(sleep_time)
hubo.drop_beeper()

while not hubo.front_is_clear():
  time.sleep(sleep_time)
  hubo.turn_left()
  
time.sleep(sleep_time)
hubo.move()

while not hubo.on_beeper():
  if hubo.right_is_clear():
    time.sleep(sleep_time)
    turn_right()
    time.sleep(sleep_time)
    hubo.move()
  elif hubo.front_is_clear():
    time.sleep(sleep_time)
    hubo.move()
  else:
    time.sleep(sleep_time)
    hubo.turn_left()
  
