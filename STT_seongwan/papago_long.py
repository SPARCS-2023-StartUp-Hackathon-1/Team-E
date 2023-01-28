#-*- coding: utf-8 -*-
import requests

client_id = "ZrM0JsMQut3cWxBeAc_L" # 개발자센터에서 발급받은 Client ID 값
client_secret = "9Pcod12Rht" # 개발자센터에서 발급받은 Client Secret 값
url = "https://openapi.naver.com/v1/papago/n2mt"

def translate(option, data) :   
    #data = "성 소수자인 삼촌에게 노래를 헌정했던 미국 팝스타 비욘세가 동성애를 금지한 아랍에미리트(UAE) 두바이에서 300억 원에 육박하는 출연료를 받고 호화 공연을 펼쳐 성 소수자들로부터 비판을 받고 있다. 성 소수자인 삼촌에게 노래를 헌정했던 미국 팝스타 비욘세가 동성애를 금지한 아랍에미리트(UAE) 두바이에서 300억 원에 육박하는 출연료를 받고 호화 공연을 펼쳐 성 소수자들로부터 비판을 받고 있다. "
    #요청 파라미터
    if option == "krTOen" :
        req_param = {"source":"ko", "target":"en", "text":data}
    else :
        req_param = {"source":"en", "target":"ko", "text":data}

    #요청 헤더
    req_header = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
    #print(req_param)

    res = requests.post(url,headers=req_header, data=req_param)

    #print(res.status_code, res.ok)
    if res.ok:
        trans_txt=res.json()['message']['result']['translatedText']
        return trans_txt
    else:
        print('error code', res.status_code)