<!--이 부분을 삭제하지 마십시오-->
![스타 배지](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![오픈 소스 사랑](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# Flask 애플리케이션을 위한 Firebase 인증

## 🛠️ 설명
이 프로젝트는 Firebase 인증을 사용하여 개발자가 Flask 애플리케이션에 안전한 사용자 인증 기능을 쉽게 구현할 수 있도록 합니다. Firebase 인증은 이메일/비밀번호, 소셜 미디어 로그인(예: Google, Facebook, Twitter) 등 다양한 인증 방법을 제공합니다. 사용자 등록, 로그인, 비밀번호 재설정을 포함한 전체 인증 프로세스를 처리하며 비밀번호 해싱 및 토큰 기반 인증과 같은 보안 모범 사례를 처리합니다.

## ⚙️ 사용된 언어 또는 프레임워크
 - Flask, Firebase
 - HTML, CSS, Bootstrap


## 🌟 실행 방법
 - ### 모든 요구 사항 설치
    `pip install -r requirements.txt`를 실행하여 모든 요구 사항을 설치합니다.
 - ### 프로젝트를 위한 Firebase 설정

   - [firebase](https://firebase.google.com/) 프로젝트를 만들고 웹 프로젝트를 설정한 다음 `프로젝트 설정`에서 모든 `프로젝트 구성`을 가져옵니다.

   - Firebase 프로젝트의 **인증** 섹션으로 이동하여 `이메일 및 비밀번호`
 인증을 활성화합니다.

   - `프로젝트 구성`은 다음과 같습니다.
```bash
  "apiKey": YOUR_API_KEY ,
  "authDomain": YOUR_AUTH_DOMAIN,
  "databaseURL": YOUR_DATABASEURL,
  "projectId": YOUR_PROJECT_ID,
  "storageBucket": YOUR_STORAGE_BUCKET,
  "messagingSenderId": YOUR_MESSAGING_SENDER_ID,
  "appId": YOUR_APP_ID,
  "measurementId": YOUR_MEASUREMENT_ID
```
- ### 프로젝트 환경 설정
   - 이제 프로젝트 디렉토리에 `.env` 파일을 만들고 다음 매개변수를 그대로 포함합니다.
```bash
export FIREBASE_APIKEY=YOUR_API_KEY
export FIREBASE_AUTHDOMAIN=YOUR_AUTH_DOMAIN
export FIREBASE_DATABASEURL=YOUR_DATABASEURL
export FIREBASE_PROJECT_ID=YOUR_PROJECT_ID
export FIREBASE_STORAGE_BUCKET=YOUR_STORAGE_BUCKET
export FIREBASE_MESSAGING_SENDER_ID=YOUR_MESSAGING_SENDER_ID
export FIREBASE_APP_ID=YOUR_APP_ID
export FIREBASE_MEASUREMENT_ID=YOUR_MEASUREMENT_ID
```

- ### 이제 프로젝트를 실행하기만 하면 됩니다.
  - 프로젝트를 실행하려면 VSCode 또는 다른 코드 편집기의 `bash` 터미널로 이동하여 `./start_server.sh`를 실행합니다.
  - 그러면 `.env`를 직접 설정할 필요가 없습니다.


## 📺 데모
![이미지](https://github.com/MBSA-INFINITY/MBSA-Forms/assets/85332648/2200ef81-57de-4619-ba33-4bed2cf31780)
![이미지](https://github.com/MBSA-INFINITY/MBSA-Forms/assets/85332648/ad83c91d-e140-4f4b-9b30-81b4903f1011)

## 🤖 저자

Github - [MBSA-INFINITY](https://github.com/MBSA-INFINITY)
LinkedIn - [MBSAIADITYA](https://www.linkedin.com/in/mbsaiaditya/)
포트폴리오 - [MBSA](https://mbsaiaditya.in/)
