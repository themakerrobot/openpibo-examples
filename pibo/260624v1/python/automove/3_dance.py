from openpibo.motion import Motion
from openpibo.audio import Audio
import time

motion = Motion()
audio = Audio()

print(motion.get_motion())
#print(motion.get_motion(path='/home/pi/mymotion.json'))

audio.play('/home/pi/openpibo-files/audio/music/exercise.mp3', 80)

#motion.set_mymotion('test', 3)
time.sleep(1)
motion.set_motion('wave1', 1)

audio.stop()
motion.set_motion('stop')