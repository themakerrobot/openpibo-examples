from openpibo.motion import Motion

motion = Motion()

# 내모션 Tools에서'weather' 모션을 생성 후, 실행
# print(motion.get_motion(path='/home/pi/mymotion.json'))
# motion.set_mymotion('weather', 3)
# motion.stop()


# 내장 모션
print(motion.get_motion())
motion.set_motion('clapping1', 1)
motion.stop()