**제목: 웹 스크래핑 책 및 데이터프레임 생성**

## 소개
이 파이썬 스크립트는 "미스터리" 카테고리의 책이 포함된 웹사이트에서 데이터를 스크래핑하고 추가 조작 및 전처리를 위해 데이터프레임을 생성하도록 설계되었습니다. 웹 스크래핑 및 데이터 조작을 위해 `requests`, `BeautifulSoup` 및 `pandas` 라이브러리를 활용합니다.

## 요구 사항
- 파이썬 3.x
- requests 라이브러리
- BeautifulSoup 라이브러리
- pandas 라이브러리

## 설치
1. 시스템에 파이썬 3.x가 설치되어 있는지 확인합니다. 그렇지 않은 경우 공식 파이썬 웹사이트(https://www.python.org/downloads/)에서 다운로드하여 설치합니다.
2. 터미널 또는 명령 프롬프트에서 다음 명령을 실행하여 필요한 라이브러리를 설치합니다.
```
pip install requests
pip install beautifulsoup4
pip install pandas
```

## 사용 방법
1. GitHub 리포지토리에서 스크립트를 복제하거나 다운로드합니다(여기에 GitHub 리포지토리 링크 제공).
2. 즐겨 사용하는 파이썬 IDE 또는 텍스트 편집기를 사용하여 스크립트를 엽니다.
3. 스크립트의 `url` 변수를 수정하여 스크래핑하려는 "미스터리" 책 카테고리의 시작 페이지를 가리키도록 합니다.
4. 스크립트를 실행합니다. 카테고리의 여러 페이지에서 데이터를 스크래핑하여 데이터프레임에 저장합니다.
5. 결과 데이터프레임에는 책 제목, 가격 및 별점에 대한 정보가 포함됩니다.

## 사용 예
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL에서 콘텐츠를 스크래핑하는 함수
def scrape_url(url):
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  return soup

# "미스터리" 카테고리의 시작 URL
url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
print(scrape_url(url))

# 콘텐츠에서 데이터 추출
data1 = []
for i in range(1, 51):
  url = f'https://books.toscrape.com/catalogue/page-{i}.html'
  response = requests.get(url)
  response = response.content
  soup = BeautifulSoup(response, 'html.parser')
  ol = soup.find('ol')
  articles = ol.find_all('article', class_='product_pod')

  for article in articles:
    title_element = article.find('h3')
    title = title_element.get_text(strip=True)
    price_element = soup.find('p', class_='price_color')
    price = price_element.get_text(strip=True)
    star_element = article.find('p')
    star = star_element['class'][1] if star_element else None
    data1.append({"title": title, "Price": price, "Star": star})

# 쉽게 조작하고 전처리하기 위해 데이터프레임에 저장된 데이터
df = pd.DataFrame(data1)
```

## 출력
스크립트는 책 제목, 가격 및 별점을 포함하여 "미스터리" 카테고리의 책에 대한 정보가 포함된 데이터프레임을 생성합니다.


## 저자
[@Hk669].

요구 사항에 따라 이 스크립트를 자유롭게 사용하고 수정하십시오. 문제가 발생하거나 개선 제안이 있는 경우 주저하지 말고 GitHub 리포지토리에서 문제 또는 풀 리퀘스트를 생성하십시오. 즐거운 스크래핑 및 데이터 분석 되십시오!
