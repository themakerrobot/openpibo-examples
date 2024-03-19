import requests
import datetime
import json
import base64
import argparse
import os

URL = {
  #'stg':'http://192.168.2.254:58821',
  'stg':'https://stg-neapi.circul.us',
  #'ops':'http://192.168.3.254:59821',
  'ops':'https://ops-neapi.circul.us',
}

def main(args):
    url = '{}/tts'.format(URL[args.mode])
    date = str(datetime.datetime.now())
    volume = -1000
    msg = "안녕하세요. 반갑습니다."
    filename = "test.wav"
    r = requests.post(url, headers={'time':date}, params={'msg':msg}, timeout=10)
    j = json.loads(r.text)
    print('Recv: {}:{}'.format(j['type'], j['result']))
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(j['data']))
    cmd = "omxplayer -o local --vol {} {}".format(volume, filename)
    os.system(cmd)
    print('Save file ok, {}'.format(filename))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='(stg|ops)', default='stg')
    args = parser.parse_args()
    print("Configure: {}".format(args))
    main(args)
