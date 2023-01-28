from chatGPT_api import chatGPT
commend = "오늘 미팅 수고 하셨고, 3월 23일 오후 8시 SPARCS 최종 미팅 진행하도록 하겠습니다."
#print(type(chatGPT("캘린더에 저장해줘", commend)))

whole_transcript = [{'박성완': '박성완 테스트'}, {'신상윤': '테스트2dsfjslkfdjfdsalkfds'}, {'박성완': '준호씨의 블로그'}]

def get_speaker_word_count(transcript): # 사람별로 말한 문자열 길이 딕셔너리 반환하는 함수
    speaker_word_count = {}
    for item in transcript:
        for speaker, speech in item.items():
            if speaker in speaker_word_count:
                speaker_word_count[speaker] += len(speech)
            else:
                speaker_word_count[speaker] = len(speech)
    return speaker_word_count

def sort_transcript_by_length(transcript_dict): # 딕셔너리의 value 값 기준으로 정렬
    return dict(sorted(transcript_dict.items(), key=lambda item: item[1], reverse=True))

speaker_word_count = sort_transcript_by_length(get_speaker_word_count(whole_transcript))

print("발화 기반 회의 참여도 순위는 다음과 같습니다.")
for speaker in speaker_word_count :
    print(speaker)
    
 
