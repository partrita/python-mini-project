# N-gram 언어 모델을 이용한 텍스트 예측

<p align="center">
<img src="assets/predict.jpg" width=40% height=40%>


## ⚙️ 사용된 언어 또는 프레임워크
이 파이썬 프로젝트는 자연어 툴킷(NLTK) 라이브러리를 활용하여 N-gram 언어 모델을 구현합니다. 코드는 다음 패키지를 포함합니다.
### 패키지

1. **판다스:** 표 형식의 데이터를 처리하고 분석하는 데 사용되는 데이터 조작 라이브러리입니다.

2. **NLTK (자연어 툴킷):**
    - `bigrams`: 단어 시퀀스에서 바이그램을 추출하기 위한 모듈입니다.
    - `lm.preprocessing.pad_both_ends`: 시퀀스의 양쪽 끝을 채우기 위한 전처리 모듈입니다.
    - `tokenize.WordPunctTokenizer`: 구두점과 공백을 사용하여 텍스트를 단어로 분해하는 토크나이저입니다.

    - `lm.Vocabulary`: 주어진 텍스트 코퍼스에서 어휘를 구성하기 위한 모듈입니다.
    - `lm.Laplace`: 언어 모델링을 위한 라플라스 스무딩을 구현하는 모듈입니다.

## 🛠️ 설명

### N-gram 언어 모델 프로젝트
이 파이썬 프로젝트는 바이그램과 함께 라플라스 스무딩 모델을 사용하여 텍스트 예측 시스템을 구현합니다. 목표는 제공된 접두사를 기반으로 주어진 문장의 다음 단어를 예측하는 것입니다. 이 프로젝트는 자연어 데이터를 처리하고 모델링하기 위해 자연어 툴킷(NLTK) 라이브러리를 활용합니다.

### 작동 방식

1. **데이터 전처리:**
   - 프로젝트는 텍스트 데이터가 포함된 CSV 파일(`train.csv`)을 읽는 것으로 시작합니다.
   - `remove_html_tags`라는 함수를 사용하여 데이터 세트의 'Body' 열에서 HTML 태그를 제거합니다.
   - 텍스트는 NLTK의 `WordPunctTokenizer`를 사용하여 토큰화됩니다.

2. **N-gram 모델 구축:**
   - 그런 다음 `pad_both_ends` 함수를 사용하여 각 문장의 양쪽 끝을 특수 기호("<s>" 및 "</s>")로 채워 코퍼스를 추가로 처리합니다.
   - `bigrams` 함수를 사용하여 채워진 문장에서 바이그램을 추출합니다.
   - 어휘는 NLTK의 `Vocabulary` 클래스를 사용하여 구성됩니다.

3. **라플라스 스무딩 모델:**
   - 라플라스 스무딩 모델은 NLTK의 언어 모델링 모듈에서 `Laplace` 클래스를 사용하여 구현됩니다.
   - 모델은 바이그램 데이터에 대해 훈련됩니다.

4. **다음 단어 예측:**
   - 다음 단어 예측을 위한 접두사를 제공하기 위해 사용자 입력을 받습니다.
   - 라플라스 모델은 주어진 접두사 다음에 올 가능성을 기반으로 어휘의 각 단어에 점수를 매깁니다.
   - 각 점수와 함께 상위 3개의 예측이 표시됩니다.


## 🌟 실행 방법

1. **필수** 종속성을 설치합니다.

```bash
pip install -r requirements.txt
```

2. 코드를 **실행**합니다.

```bash
python text_prediction.py
```

## 📺 데모

![](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3BndnM1M2tnaWhlbjkxczJmcndzenh2bnlhaWFkZWR2YWhqNDg0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NIQIoC9vc7xBEPOCPY/giphy.gif)

## 🤖 저자

링크 : [louisbau](https://github.com/louisbau)
