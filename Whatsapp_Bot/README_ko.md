<!--이 부분을 삭제하지 마십시오-->
![스타 배지](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![오픈 소스 사랑](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# 왓츠앱 봇

<!--이미지는 프로젝트의 삽화이며, 여기서 팁은 유머 감각을 최대한 활용하는 것입니다 :D

다음과 같이 마크다운 사진 삽입을 복사하여 붙여넣을 수 있습니다.
<p align="center">
<img src="your-source-is-here" width=40% height=40%>
-->
![왓츠앱봇](https://user-images.githubusercontent.com/87910771/147886971-3b084c89-3370-43a6-9bf7-cf31716691be.png)


## 🛠️ 설명
<!--아래 줄을 삭제하고 원하는 내용을 추가하십시오-->
파이썬을 사용하여 WhatsApp 메시지를 보내는 간단한 봇입니다.

사용한 라이브러리는 pywhatkit이며 [여기](https://github.com/Ankit404butfound/PyWhatKit)에서 찾을 수 있습니다.

## ⚙️ 사용된 언어 또는 프레임워크
<!--아래 줄을 삭제하고 원하는 내용을 추가하십시오-->
명령 프롬프트를 열고 다음 명령을 사용하여 필요한 모듈을 설치하십시오.

```sh
pip install pywhatkit
```

## 🌟 실행 방법
<!--아래 줄을 삭제하고 원하는 내용을 추가하십시오-->
스크립트가 있는 폴더에서 터미널을 열고 다음 명령을 실행하기만 하면 됩니다.

```sh
python main.py
```

메시지를 보내는 방법에는 여러 가지가 있습니다.

```sh
# 오후 1시 30분에 연락처로 WhatsApp 메시지 보내기
pywhatkit.sendwhatmsg("+910123456789", "안녕", 13, 30)

# 위와 동일하지만 메시지를 보낸 후 2초 후에 탭 닫기
pywhatkit.sendwhatmsg("+910123456789", "안녕", 13, 30, 15, True, 2)

# 캡션으로 안녕하세요와 함께 그룹에 이미지 보내기
pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "안녕하세요")

# 캡션 없이 연락처에 이미지 보내기
pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# 오전 12시에 그룹에 WhatsApp 메시지 보내기
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "모두 안녕하세요!", 0, 0)

# 그룹에 즉시 WhatsApp 메시지 보내기
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "모두 안녕하세요!")
```


## 📺 데모

![데모](https://user-images.githubusercontent.com/87910771/147886979-a12cd79a-8f49-4603-b568-4991dde28feb.jpg)



## 🤖 저자
<!--아래 줄을 삭제하고 원하는 내용을 추가하십시오-->
[아니쉬로히야](https://github.com/AnishLohiya),
[유르네로-사이버](https://github.com/Yurnero-cyber)
