# [TEAM E] TEAM E

이 Repository는 AI 회의 비서인 "Chatty Cat"을 담고있습니다.

다음과 같은 기능이 포함되어 있습니다.

- WebRTC을 통한 화상 회의 플랫폼
- 개인화 AI 비서와의 질의응답과 채팅
- 실시간 회의록와 요약
- 화상 회의 실시간 통계

## 프로젝트에서 사용한 기술

본 Repository는 `pacakge.json` 에 있는 오픈소스 패키지를 사용하였습니다.

또 다음 Code Snippet 이 포함되어 있습니다.

- [Google Cloud Speech API](https://github.com/googleapis/python-speech/blob/main/samples/microphone/transcribe_streaming_mic.py)
- [Open-EasyRTC](https://www.npmjs.com/package/open-easyrtc)
- [Google Calendar API](https://gaebalsogi.tistory.com/55)
- [ChatGPT](https://www.npmjs.com/package/chatgpt)
- [Papago API](https://developers.naver.com/docs/nmt/reference/)
- [OpenAI](https://openai.com/blog/new-and-improved-embedding-model/)

## Dev Server 실행 방법

1. 본 Repository를 로컬 환경에 Clone 받습니다.
2. `cd open-easyrtc` 폴더로 이동합니다.
3. `npm install`로 패키지 설치합니다.
4. `cd server_example`로 서버 폴더로 이동합니다.
5. `npm install`로 서버 패키지 설치합니다.
6. openAI와 ChatGPT, Papago, Google Credential 등 의 시크릿을 얻고 환경변수를 설정합니다.
7. `` 로 WebRTC 서버를 실행합니다.
8. ``로 WebRTC Client를 실행합니다.

## Production 배포 방법

본 프로젝트는 배포하지 않았습니다.

## 환경 변수 및 시크릿

필요한 환경 변수는 .env 에 명시되어 있습니다.

- SEONGWAN_organization
- SEONGWAN_YOUR_API_KEY
- PAPAGO_client_id
- PAPAGO_client_secret
- CHATGPT_API_KEY
- GOOGLECALENDAR_client_id_API_KEY
- GOOGLECALENDAR_CLIENTSECRET

## 기타

기타사항 없습니다.
