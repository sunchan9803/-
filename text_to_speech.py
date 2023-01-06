# TTS(TEXT TO SPEECH)
from gtts import gTTS # Google text to speech
from playsound import playsound

file_name = 'sample.mp3'

#한글 문장
text = '안녕하세요' #음성으로 출력하고 싶은 텍스트 작성
tts_ko = gTTS(text=text, lang='ko') #언어 지정
tts_ko.save(file_name) #파일을 저장
playsound(file_name) #저장된 파일을 mp3로 실행
