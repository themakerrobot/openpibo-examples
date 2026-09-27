# 필요한 openpibo 라이브러리를 임포트합니다.
from openpibo.vision import Face   # 얼굴 감지, 학습, 인식 기능
from openpibo.vision import Camera # 카메라 제어
from openpibo.oled import Oled   # OLED 디스플레이 제어 (이 코드에서는 객체만 생성하고 사용하지 않음)

# 얼굴 관련 기능 객체를 생성합니다.
_face = Face()
# 카메라 객체를 생성합니다.
camera = Camera()
# OLED 객체를 생성합니다. (이 코드에서는 사용되지 않습니다)
oled = Oled()

# 기존에 학습된 얼굴 데이터베이스를 불러올 때 사용합니다.
# 여러 사람을 이어서 학습시키거나, 기존 데이터를 유지하며 추가 학습할 때 주석을 해제하고 사용합니다.
# 예: _face.load_db('/home/pi/code/facedb')
# _face.load_db('/home/pi/code/'+'facedb') # 파일 경로는 실제 저장 위치에 맞게 수정해야 합니다.

# 카메라로부터 현재 이미지를 한 장 읽어옵니다.
image = camera.read()
# 읽어온 이미지에서 얼굴을 감지합니다.
face_list = _face.detect_face(image)

# 감지된 얼굴이 없을 경우
if not len(face_list):
  # 이미지 좌측 상단에 "얼굴없음" 텍스트를 검은색으로 표시합니다.
  image = camera.putTextPIL(image, '얼굴없음', (0, 0), 40, '#000000')
# 감지된 얼굴이 있을 경우 (첫 번째 감지된 얼굴을 학습 대상으로 사용)
else:
  # 첫 번째로 감지된 얼굴의 바운딩 박스 정보(x, y, w, h)를 가져옵니다.
  box = face_list[0]
  x = box[0] # 시작 x 좌표
  y = box[1] # 시작 y 좌표
  w = box[2] # 너비
  h = box[3] # 높이

  # 감지된 얼굴 영역(image, box)을 '홍길동'이라는 이름으로 학습시킵니다.
  # 동일한 이름으로 여러 번 학습시키면 해당 인물의 얼굴 데이터가 누적됩니다.
  _face.train_face(image, box, '홍길동')

  # 현재까지 학습된 얼굴 데이터를 파일로 저장합니다.
  # 지정된 경로('/home/pi/code/facedb')에 데이터베이스 파일이 생성되거나 갱신됩니다.
  # 파일 경로는 원하는 위치로 변경 가능합니다.
  _face.save_db('/home/pi/code/' + 'facedb')

  # 학습에 사용된 얼굴 영역 주위에 초록색 사각형을 그립니다.
  image = camera.rectangle(image, (x, y), ((x + w), (y + h)), '#009900', 10)

# 최종 처리된 이미지(얼굴 없음 텍스트 또는 학습된 얼굴 사각형 포함)를 IDE 미리보기 창에 표시합니다.
camera.imshow_to_ide(image)

# (참고) 학습 후에는 이 스크립트를 다시 실행하면 '홍길동' 얼굴 데이터가 누적 학습될 수 있으며,
# 얼굴 인식 스크립트에서 load_db를 통해 저장된 데이터를 불러와 '홍길동'을 인식할 수 있습니다.