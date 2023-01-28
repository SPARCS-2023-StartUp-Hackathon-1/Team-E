from chatGPT_api import chatGPT
commend = "오늘 미팅 수고 하셨고, 3월 23일 오후 8시 SPARCS 최종 미팅 진행하도록 하겠습니다."
print(type(chatGPT("캘린더에 저장해줘", commend)))

whole_transcript = [{'박성완': '박성완 테스트'}, {'신상윤': '테스트2'}, {'박성완': '준호씨의 블로그'}]

name = "박성완"
text = ""

for transcript in whole_transcript :
    for key,value in transcript.items() :
        if(key == name) :
            text += value

print(text)

"""
names = set()
for name in whole_transcript :
    for key in name.keys() :
        names.add(key)
print(names)
"""