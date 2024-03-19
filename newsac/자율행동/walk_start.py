from openpibo.motion import Motion

motion = Motion()

res = motion.get_motion('forward1')

print(res)

for item in res['pos']:
  print(item['d'], item['seq'])
  