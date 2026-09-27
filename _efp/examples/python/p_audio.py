from openpibo.audio import Audio
import time

audio = Audio()

audio.play('/home/pi/openpibo-files/audio/music/classic.mp3', 80)
time.sleep(5)
audio.stop()

audio.record('/home/pi/myaudio/test.wav', 5, False)
audio.play('/home/pi/myaudio/test.wav', 80)