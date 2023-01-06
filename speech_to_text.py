import speech_recognition as sr #설치한 모듈 불러오기


r = sr.Recognizer()
#마이크로부터 들려온 음성 인식
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source)    # 마이크로부터 음성 듣기
try:
    # 구글 API로 인식 (하루 50회)
    text = r.recognize_google(audio, language='ko') 
    # 들려온 음성을 text로 변환
    print(text)
    # 예외 처리 방식
except sr.UnknownValueError:
    print('인식 실패') #음성 인식 실패한 경우
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) #API key 오류, 네트워크 단절 등
