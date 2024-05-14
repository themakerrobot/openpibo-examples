from openpibo.device import Device
import time

device = Device()

device.eye_on(255,255,255)
time.sleep(2)
device.eye_on(255,0,0,0,0,255)
time.sleep(2)
device.eye_off()

print(device.get_dc(True))
print(device.get_battery(True))
print(device.get_pir())
print(device.get_touch())
print(device.get_button())