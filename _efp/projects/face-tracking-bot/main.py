# numbers 모듈에서 Number 클래스를 임포트합니다. 변수가 숫자인지 확인하는 데 사용됩니다.
from numbers import Number
# openpibo 라이브러리에서 Motion, Camera, Face 클래스를 임포트합니다.
from openpibo.motion import Motion # 로봇 모션 제어 (모터 제어)
from openpibo.vision import Camera # 카메라 제어
from openpibo.vision import Face   # 얼굴 감지 기능
import os # 운영체제 관련 기능 (이 코드에서는 사용되지 않음)

# 전역 변수 초기화 (None으로 설정하여 사용 전 할당 확인 가능)
mt = None # 목 틸트(위아래) 모터(5번)의 목표 각도
mp = None # 목 팬(좌우) 모터(4번)의 목표 각도
cx = None # 감지된 얼굴의 중심 x 좌표
image = None # 카메라에서 읽어온 이미지 프레임
cy = None # 감지된 얼굴의 중심 y 좌표
items = None # 얼굴 감지 결과 (감지된 얼굴들의 정보 리스트)
item = None # 현재 처리 중인 얼굴 정보 (items 리스트의 첫 번째 요소)

# 모션 제어 객체를 생성합니다.
motion = Motion()

# 이 함수는 감지된 얼굴의 중심 좌표(cx, cy)를 기준으로
# 로봇의 목(팬, 틸트) 모터 각도(mp, mt)를 조절하여 얼굴을 추적하도록 합니다.
def move():
  # 함수 내에서 전역 변수 mt, mp, cx, image, cy, items, item을 사용하고 수정할 것을 선언합니다.
  global mt, mp, cx, image, cy, items, item

  # --- 목 팬(좌우) 모터 제어 ---
  # 얼굴 중심 x좌표(cx)가 화면 왼쪽 영역(270 미만)에 있고, 현재 팬 각도(mp)가 최대 오른쪽 각도(40) 미만일 때
  if cx < 270 and mp < 40:
    # 팬 각도(mp)를 4 증가시킵니다 (오른쪽으로 이동). mp가 숫자가 아니면 0으로 간주하고 4를 더합니다.
    mp = (mp if isinstance(mp, Number) else 0) + 4
  # 얼굴 중심 x좌표(cx)가 화면 오른쪽 영역(370 초과)에 있고, 현재 팬 각도(mp)가 최대 왼쪽 각도(-40) 초과일 때
  elif cx > 370 and mp > -40:
    # 팬 각도(mp)를 4 감소시킵니다 (왼쪽으로 이동). mp가 숫자가 아니면 0으로 간주하고 -4를 더합니다.
    mp = (mp if isinstance(mp, Number) else 0) + -4

  # --- 목 틸트(위아래) 모터 제어 ---
  # 얼굴 중심 y좌표(cy)가 화면 아래 영역(290 초과)에 있고, 현재 틸트 각도(mt)가 최대 위쪽 각도(16) 미만일 때
  if cy > 290 and mt < 16:
    # 틸트 각도(mt)를 4 증가시킵니다 (위쪽으로 이동). mt가 숫자가 아니면 0으로 간주하고 4를 더합니다.
    mt = (mt if isinstance(mt, Number) else 0) + 4
  # 얼굴 중심 y좌표(cy)가 화면 위쪽 영역(190 미만)에 있고, 현재 틸트 각도(mt)가 최대 아래쪽 각도(-16) 초과일 때
  elif cy < 190 and mt > -16:
    # 틸트 각도(mt)를 4 감소시킵니다 (아래쪽으로 이동). mt가 숫자가 아니면 0으로 간주하고 -4를 더합니다.
    mt = (mt if isinstance(mt, Number) else 0) + -4

  # 계산된 목표 각도로 목 팬(4번) 모터와 틸트(5번) 모터를 설정합니다.
  motion.set_motor(4, mp) # 4번 모터(팬) 각도 설정
  motion.set_motor(5, mt) # 5번 모터(틸트) 각도 설정

# 카메라 객체를 생성합니다.
camera = Camera()
# 얼굴 감지 객체를 생성합니다.
_face = Face()

# 목 틸트(mt)와 팬(mp) 모터의 초기 각도를 0으로 설정합니다.
mt = 0
mp = 0

# 메인 루프 시작: 얼굴 감지 및 추적을 계속 반복합니다.
while True:
  # 카메라로부터 현재 이미지를 읽어옵니다.
  image = camera.read()
  # 읽어온 이미지에서 얼굴을 감지합니다. 결과는 감지된 얼굴 정보(x, y, 너비, 높이)의 리스트입니다.
  items = _face.detect_face(image)
  # 감지된 얼굴 정보를 콘솔에 출력합니다. (디버깅용)
  print(items)

  # 감지된 얼굴이 없을 경우
  if not len(items):
    # 콘솔에 '-'를 출력하여 얼굴이 없음을 나타냅니다.
    print('-')
  # 감지된 얼굴이 있을 경우
  else:
    # 첫 번째로 감지된 얼굴 정보(item)를 가져옵니다. (리스트의 첫 번째 요소)
    item = items[0]
    # 얼굴 정보(x, y, 너비 w, 높이 h)를 사용하여 얼굴의 중심 좌표(cx, cy)를 계산합니다.
    # cx = 시작 x좌표 + 너비의 절반
    cx = item[0] + item[2] / 2
    # cy = 시작 y좌표 + 높이의 절반
    cy = item[1] + item[3] / 2
    # 계산된 얼굴 중심 x, y 좌표를 콘솔에 출력합니다. (디버깅용)
    print(cx)
    print(cy)
    # 계산된 얼굴 중심 좌표에 빨간색 원을 그립니다. (시각화용)
    image = camera.circle(image, (int(cx), int(cy)), 5, '#ff0000', 10)
    # move 함수를 호출하여 얼굴 중심 좌표(cx, cy)에 따라 목 모터를 조절합니다.
    move()

  # 이미지 위에 추적 목표 영역(중앙 사각형)을 초록색으로 그립니다. (시각화용)
  # 얼굴 중심이 이 사각형 안에 들어오도록 모터가 제어됩니다.
  image = camera.rectangle(image, (270, 190), (370, 290), '#33cc00', 5)
  # 처리된 이미지(얼굴 중심 원, 목표 영역 사각형 포함)를 IDE 미리보기 창에 표시합니다.
  # 0.5는 프레임 간의 지연 시간(초)이 아니라, imshow_to_ide 함수의 내부 처리와 관련된 값일 수 있습니다(확인 필요). 보통은 지연 시간이 아닙니다.
  camera.imshow_to_ide(image, 0.5)