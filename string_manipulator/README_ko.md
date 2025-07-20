<!--이 부분을 삭제하지 마십시오-->

# 문자열 조작기

## 🛠️ 설명
StringManipulator는 다양한 문자열 조작을 수행하기 위한 편리한 인터페이스를 제공하도록 설계된 파이썬 클래스입니다. 연결, 길이 계산, 슬라이싱, 반복, 대소문자 변환, 스트리핑, 분할, 서식 지정 및 보간과 같은 일반적인 문자열 작업을 캡슐화합니다.

## ⚙️ 사용된 언어 또는 프레임워크
이 프로그램은 Python3로 만들어졌습니다.

## 🌟 사용법
다음과 같이 문자열로 `StringManipulator` 클래스를 인스턴스화합니다.

```python
my_string = "Hello, World!"
manipulator = StringManipulator(my_string)
```
## 📺 사용 예
```my_string = "Hello, World!"
manipulator = StringManipulator(my_string)

print("연결된 문자열:", manipulator.concatenate(" Goodbye"))
print("문자열 길이:", manipulator.length())
print("슬라이스된 문자열:", manipulator.slice(7, None))
print("반복된 문자열:", manipulator.repeat(3))
print("대문자:", manipulator.uppercase())
print("소문자:", manipulator.lowercase())
print("스트립된 문자열:", manipulator.strip())
print("분할된 문자열:", manipulator.split(","))
print("서식이 지정된 문자열:", manipulator.format("Alice", 30))
print("보간된 문자열:", manipulator.interpolate(name="Bob", age=25))
```
## 🤖 저자
Larry Hussey, Binary Poet ( [caneslarry.com](https://caneslarry.com) )
