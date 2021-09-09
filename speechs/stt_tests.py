from openpibo.speech import Speech

obj = Speech()
# 음성 언어를 문자 데이터로 변환하여 출력
ret = obj.stt()
print(ret)
