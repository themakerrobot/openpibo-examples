from openpibo.motion import Motion
import time

motion = Motion()

print(motion.get_motion())
motion.set_motion('wave1', 1)

# print(motion.get_motion(path='/home/pi/mymotion.json'))
# motion.set_mymotion('test', 1)

while True:
  motion.set_speed(4, 100)
  motion.set_acceleration(4, 5)
  motion.set_motor(4, (-40))
  time.sleep(1)
  motion.set_speed(4, 100)
  motion.set_acceleration(4, 40)
  motion.set_motor(4, 40)
  time.sleep(1)