from openpibo.motion import Motion
from pprint import pprint

motion = Motion()

# res = motion.get_motion('forward1')
# for item in res['pos']:
#   print(item['d'])

motion_list = motion.get_motion()

while True:
  name = input(f'\n{motion_list}\n\n모션 입력 > ')
  print(f'\n{name}')
  pprint(motion.get_motion(name)['pos'])
  
  try:
    motion.set_motion(name)
  except Exception as ex:
    print("모션이 없습니다.")