# openpibo-example


## 예제 파일 실행


다음의 코드를 입력하여 예제 파일을 실행할 수 있습니다.

```shell
~ $ git clone https://github.com/themakerrobot/openpibo-examples.git
~ $ cd openpibo-examples/{폴더명}
~/openpibo-examples/{폴더명} $ sudo python3 {파일명}
```

아래는 audio 폴더 내에 있는 play_test.py를 실행하는 예제 코드입니다.

```shell
~ $ cd openpibo-examples/audio
~/openpibo-examples/audio $ sudo python3 play_test.py
```

## 사전 학습

> 예제 파일에 공통으로 들어가는 코드 및 openpibo 라이브러리에 정의되어 있는 함수 사용에 관한 설명입니다.

- **import**

  openpibo의 lib를 import하여 구현합니다. `from openpibo.{module} import {class}`

  아래는 openpibo에 있는 audio의 Audio 클래스를 import하는 예제입니다.

  ```python
  # openpibo-examples/audio/play_test.py
  
  from openpibo.audio import audio

  # openpibo 라이브러리 경로 추가
  import openpibo
  ```

- **함수**

  클래스를 사용하려면 인스턴스를 생성해야 하며, 인스턴스를 통해 해당 클래스의 함수를 호출할 수 있습니다.

  아래는 Audio 클래스의 함수를 호출하여 test.mp3 파일을 재생하는 코드입니다.

  ```python
  # openpibo-examples/audio/play_test.py
  import time
  
  import openpibo
  from openpibo.audio import Audio

  def run():
    o = Audio()  # 인스턴스 생성, obj는 Audio 클래스의 인스턴스
    o.play(filename=openpibo.config['DATA_PATH']+'/audio/test.mp3', out='local', volume=-2000) # '인스턴스.메서드'로 Audio 클래스의 play 호출
    time.sleep(5)
    o.stop()

  if __name__ == '__main__':
    run()
  ```

- **함수의 호출** 

  1. 함수 호출 시, 해당 함수가 요구하는 매개변수(parameter)를 같이 넘겨줘야 합니다.

  2. `out='local'`, `volume='-2000'`처럼 기본 인자 값이 설정되어 있는 경우, 인자(argument)를 넘겨주지 않아도 함수 호출이 가능합니다. 

     (호출 시 인자가 없으면 기본 인자 값이 활용됨)

  3. 함수는 기본적으로 인자를 위치로 판단합니다.

  4. 키워드 인자로 전달시 순서가 바뀌어도 함수 호출이 가능합니다.

  아래는 Audio 클래스 및 함수 호출 예제 코드입니다.

  ```python
  # openpibo/audio.py
  
  import os
  
  class Audio:
      def play(self, filename, out='local', volume='-2000', background=True):
          opt = '&' if background else ''
          os.system(f'omxplayer -o {out} --vol {volume} {filename} {opt}')
      def stop(self):
          os.system('sudo pkill omxplayer')
  ```

  ```python
  # play 함수 호출
  o.play(filename=openpibo.config['DATA_PATH']+'/audio/test.mp3', out='local', volume=-2000) # 방법1
  o.play(filename=openpibo.config['DATA_PATH']+'/audio/test.mp3') # 방법2 (local, volume 기본 인자값이 있으므로 가능)
  o.play(openpibo.config['DATA_PATH']+'/audio/test.mp3', 'local', -2000) # 방법3 (인자의 순서가 맞기 때문에 변수명 안써도 가능)
  o.play(out='local', volume=-2000, openpibo.config['DATA_PATH']+'/audio/test.mp3') # 방법4 (키워드 인자의 경우 순서가 바뀌어도 가능)
  ```

  단, 아래와 같이 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.

  ```python
  o.play(openpibo.config['DATA_PATH']+'/audio/test.mp3', 'local', -2000)  (X)
  ```

- `if __name__ == '__main__'`

  - `__name__`: 현재 모듈의 이름을 담고 있는 내장 변수입니다.
  - 해당 프로그램을 직접 실행했을 경우, 참이 되어 main 함수를 실행합니다.
  - 다른 프로그램에서 import하여 사용할 경우, main 함수는 실행하지 않습니다.

## 참고 사항
더 자세한 설명은 [공식 문서의 EXAMPLES 탭](https://themakerrobot.github.io/openpibo-python/build/html/examples/audio.html)를 참고하시기 바랍니다.
