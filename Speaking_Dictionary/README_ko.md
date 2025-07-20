# 말하는 사전
말하는 사전은 사용자가 프로그램(장치)에 직접 영어 단어를 말하여 그 의미를 찾을 수 있도록 하는 파이썬 프로그램입니다. 그러면 프로그램(장치)이 직접 그 단어의 정의를 소리 내어 설명합니다.

### 전제 조건
pyttsx3: pip install pyttsx3
PyDictionary: pip install PyDictionary
speech recognition: pip install SpeechRecognition
gTTS: pip install gtts

+pip install pyaudio

### 스크립트 실행 방법
SpeakingDictionary.py
1. 말하는 사전을 시작하려면 먼저 'hello'라고 말하십시오.
2. SpeakingEngine이 "어떤 단어를 찾고 싶으세요?"라고 말하면 천천히 그리고 정확하게 단어를 말하십시오.
3. 인식기가 단어를 인식하면 올바른 단어를 인식했는지 묻습니다.
4. "yes"라고 말하면 SpeakingEngine이 그 단어의 정의를 소리 내어 말합니다.
5. 인식기가 단어를 인식하지 못했거나 4단계에서 "no"라고 말하면 말하는 사전은 정의를 말하지 않습니다.

### 스크립트의 샘플 사용을 보여주는 스크린샷/GIF
[말하는 사전](https://user-images.githubusercontent.com/69775935/140873415-dc79bdd7-d36e-4ca5-ae6f-4da88837f5f0.png)

### 저자 이름
이예진 : 19lyaejin, https://github.com.19lyaejin
