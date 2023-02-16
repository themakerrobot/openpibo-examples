from openpibo.audio import Audio
import os

def run():
  audio = Audio()
  cmd = "arecord -D dmic_sv -c2 -r 16000 -f S32_LE -d 3 -t wav -q -vv -V streo stream.raw;sox stream.raw -c 1 -b 16 stream.wav;rm stream.raw"
  os.system(cmd)
  audio.play(filename="stream.wav", volume=100, background=False)
  os.remove("stream.wav")

# Main loop
if __name__ == "__main__":
  run()