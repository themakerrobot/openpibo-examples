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
    url = '{}/stt'.format(URL[args.mode])
    date = str(datetime.datetime.now())
    timeout=5
    filename="test.wav"

    cmd = "arecord -D dmic_sv -c2 -r 16000 -f S32_LE -d {} -t wav -q -vv -V streo test.raw;sox test.raw -c 1 -b 16 {};rm test.raw".format(timeout, filename)
    os.system(cmd)
    files = {'uploadFile':open('./{}'.format(filename), 'rb')}
    r = requests.post(url, files=files, headers={'time':date}, timeout=10)
    j = json.loads(r.text)
    print('Recv: {}:{}'.format(j['type'], j['result']))
    print('Echo data: {}'.format(j['data']))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help='(stg|ops)', default='stg')
    args = parser.parse_args()
    print("Configure: {}".format(args))
    main(args)
