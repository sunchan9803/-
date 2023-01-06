import os
import time

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

#스크래핑 클래스 불러오기
import scrape.naver_exchange_rate as nex
import scrape.naver_fortune_mouse as nfrm
import scrape.naver_fortune_tiger as nfrt
import scrape.naver_fortune_dragon as nfrd
import scrape.naver_fortune_horse as nfrh
import scrape.naver_fortune_monkey as nfrmk
import scrape.naver_fortune_dog as nfrdg
import scrape.naver_fortune_cow as nfrc
import scrape.naver_fortune_rabbit as nfrr
import scrape.naver_fortune_snake as nfrsn
import scrape.naver_fortune_sheep as nfrsh
import scrape.naver_fortune_chicken as nfrch
import scrape.naver_fortune_pig as nfrp
import scrape.naver_weather as nwh
import scrape.naver_covid as ncovid



 # 음성 인식(듣기,STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[사용자] : ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') #음성 인식 실패한 경우
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))     #API key 오류, 네트워크 단절 등

#대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        wh = nwh.Weather()
        answer_text = '{}, 날씨 상태는 {} 입니다. 그리고 오늘의 {}, {} 입니다.'.format(wh.curr_temp, wh.weather_con, wh.min_temp, wh.max_temp)
    elif '환율' in input_text:
        ex = nex.Exchange()
        answer_text = '현재 원 달러 환율은 {} 입니다. \n 등락률은 {} 입니다.'.format(ex.curr_exchange, ex.ex_rate) 
    elif '쥐띠' in input_text:
        fr = nfrm.Fortune_Mouse()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune)    
    elif '호랑이띠' in input_text:
        fr = nfrt.Fortune_Tiger()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '용띠' in input_text:
        fr = nfrd.Fortune_Dragon()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '말띠' in input_text:
        fr = nfrh.Fortune_Horse()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '원숭이띠' in input_text:
        fr = nfrmk.Fortune_Monkey()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '개띠' in input_text:
        fr = nfrdg.Fortune_Dog()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '소띠' in input_text:
        fr = nfrc.Fortune_Cow()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '토끼띠' in input_text:
        fr = nfrr.Fortune_Rabbit()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '뱀띠' in input_text:
        fr = nfrsn.Fortune_Snake()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '양띠' in input_text:
        fr = nfrsh.Fortune_Sheep()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '닭띠' in input_text:
        fr = nfrch.Fortune_Chicken()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '돼지띠' in input_text:
        fr = nfrp.Fortune_Pig()
        answer_text = '오늘의 운세입니다. {}'.format(fr.curr_fortune) 
    elif '코로나' in input_text:
        nc = ncovid.Covid()
        answer_text = '오늘의 일일 확진자는 {} 명 입니다.'.format(nc.today_covid)
    elif '고마워' in input_text:
        answer_text = '별 말씀을요'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop=False) 
    else:
        answer_text = '다시 말씀 해주시겠어요?'   
    speak(answer_text)            

#소리내어 읽기(TTS)
def speak(text):
    print('[인공지능] : ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)
