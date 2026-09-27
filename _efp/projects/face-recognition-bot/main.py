# 필요한 openpibo 라이브러리를 임포트합니다.
from openpibo.vision import Face   # 얼굴 감지 및 인식 기능
from openpibo.vision import Camera # 카메라 제어

# 에러 결과를 저장할 전역 변수 초기화 (사용 방식에 개선 여지가 있음)
errorResult = None

# 얼굴 관련 기능 객체를 생성합니다.
_face = Face()
# 카메라 객체를 생성합니다.
camera = Camera()

# 이 함수는 감지된 얼굴의 바운딩 박스(x, y, w, h)가
# 이미지 경계(640x480 가정)를 벗어나는지 확인합니다.
# 주의: x, y, w, h 변수를 파라미터로 받지 않고 전역 변수에 의존하고 있어,
# 코드의 명확성과 재사용성이 떨어집니다.
def errorCheck():
  # 전역 변수 errorResult를 함수 내에서 사용/수정함을 명시 (하지만 반환값도 사용)
  global errorResult
  # 바운딩 박스의 x좌표가 0보다 작거나, x+너비가 640(이미지 너비)보다 크면 경계 벗어남
  if x < 0 or x + w > 640:
    errorResult = False # 에러 상태 (경계 벗어남)
  # 바운딩 박스의 y좌표가 0보다 작거나, y+높이가 480(이미지 높이)보다 크면 경계 벗어남
  elif y < 0 or y + h > 480:
    errorResult = False # 에러 상태 (경계 벗어남)
  # 위의 조건에 해당하지 않으면, 바운딩 박스는 이미지 경계 내에 있음
  else:
    errorResult = True  # 정상 상태 (경계 내)
  # 계산된 에러 상태를 반환합니다.
  return errorResult

# 미리 저장된 얼굴 데이터베이스를 로드하는 부분 (현재 주석 처리됨)
# 사용하려면 주석을 해제하고 실제 데이터베이스 경로를 지정해야 합니다.
_face.load_db('/home/pi/code/'+'facedb')

# 메인 루프 시작: 얼굴 감지 및 인식 과정을 계속 반복합니다.
while True:
  # 카메라로부터 현재 이미지를 읽어옵니다.
  image = camera.read()
  # 읽어온 이미지에서 얼굴을 감지합니다. 결과는 감지된 얼굴 정보(x, y, w, h)의 리스트입니다.
  face_list = _face.detect_face(image)

  # 감지된 얼굴 리스트를 콘솔에 출력합니다. (디버깅용)
  print(face_list)

  # 감지된 얼굴이 없을 경우
  if not len(face_list):
    # 이미지 좌측 상단에 "얼굴없음" 텍스트를 검은색으로 표시합니다.
    image = camera.putTextPIL(image, '얼굴없음', (0, 0), 40, '#000000')
  # 감지된 얼굴이 있을 경우
  else:
    # 첫 번째로 감지된 얼굴의 바운딩 박스 정보(x, y, w, h)를 가져옵니다.
    box = face_list[0]
    x = box[0] # 시작 x 좌표
    y = box[1] # 시작 y 좌표
    w = box[2] # 너비
    h = box[3] # 높이

    # 감지된 얼굴 주위에 초록색 사각형을 그립니다.
    image = camera.rectangle(image, (x, y), ((x + w), (y + h)), '#009900', 10)

    # errorCheck() 함수를 호출하여 얼굴 바운딩 박스가 이미지 경계 내에 있는지 확인합니다.
    # 이 때 errorCheck 함수는 현재 범위의 x, y, w, h 변수를 사용합니다.
    if errorCheck():
      # 바운딩 박스가 경계 내에 있을 경우, 얼굴 인식을 시도합니다.
      # 인식 대상 이미지(image)와 인식할 영역(box)을 전달합니다.
      result = _face.recognize(image, box)
      # 인식 결과에서 'name' 키의 값(인식된 사람 이름 또는 'Guest')을 가져옵니다.
      name = result['name']
      # 인식된 이름이 'Guest'가 아닐 경우 (등록된 사용자일 경우)
      if name != 'Guest':
        # 이미지 좌측 상단에 인증 완료 메시지를 표시합니다.
        image = camera.putTextPIL(image, (str(name) + ' 님, 인증되었습니다.'), (0, 0), 40, '#000000')
      # 인식된 이름이 'Guest'일 경우 (등록되지 않은 사용자일 경우)
      else:
        # 이미지 좌측 상단에 인증 거절 메시지를 표시합니다.
        image = camera.putTextPIL(image, '인증이 거절되었습니다.', (0, 0), 40, '#000000')
    # else: # 바운딩 박스가 경계를 벗어난 경우 (errorCheck()가 False 반환) - 필요시 추가 처리
    #   image = camera.putTextPIL(image, '얼굴 경계 벗어남', (0, 0), 40, '#FF0000')

  # 최종 처리된 이미지를 IDE 미리보기 창에 표시합니다.
  camera.imshow_to_ide(image)