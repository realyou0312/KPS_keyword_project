import re
import requests

def get_translate(text):
    client_id = "MiYJWifswyflknKc75an"
    client_secret = "p3WJ5nuZ2h"

    data = {'text' : text,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)

def start_trans(input_text):
    ENGS = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E',
            'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J',
            'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O',
            'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T',
            'u', 'U', 'v', 'V', 'w', 'W', 's', 'S', 'y', 'Y',
            'z', 'Z']

    KORS = ['에이', '에이', '비', '비', '씨', '씨', '디', '디', '이', '이',
            '에프', '에프', '쥐', '쥐', '에이치', '에이치', '아이', '아이', '제이', '제이',
            '케이', '케이', '엘', '엘', '엠', '엠', '엔', '엔', '오', '오',
            '피', '피', '큐', '큐', '알', '알', '에스', '에스', '티', '티',
            '유', '유', '브이', '브이', '더블유', '더블유', '에스', '에스', '와이', '와이',
            '지', '지']

    trans = dict(zip(ENGS, KORS))
    papago_trans = get_translate(input_text) # 파파고로 번역 데이터 보내기
    is_english = re.compile('[-a-zA-Z]')
    temp = is_english.findall(papago_trans) # 파파고에서 번역이 안된 영어 문장이 있다면 temp값 존재

    result_trans = []
    if len(temp) > 0: # 영어 데이터 존재 유무
        result_trans = ''.join([trans[i] for i in temp])
        return result_trans # 한글로 번역이 안된 데이터 존재
    else:
        return papago_trans # 한글로 번역이 잘된 데이터일 경우 그대로 리턴


a = start_trans("steve jobs")
print(a)
