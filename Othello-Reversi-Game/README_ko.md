<h1 align="center">⚫ 오델로/리버시 ⚪ </h1>

`pygame` 라이브러리를 사용하여 **Python3**로 만든 2인용 GUI 장착 [오델로/리버시](https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english) 게임입니다.

## 📜 설명
오델로는 한쪽은 검은색, 다른 쪽은 흰색인 64개의 디스크가 있는 8x8 보드에서 하는 보드 게임입니다. 각 플레이어는 32개의 디스크를 받으며, 그 중 각 플레이어의 2개는 다음과 같이 보드에 놓입니다.

![이미지](https://github.com/TERNION-1121/Othello-Reversi-Game/assets/97667653/ea03fdd8-9abc-4b14-bdc9-7d983fb38041)

<br>

움직임은 상대방의 디스크를 "측면 공격"한 다음 "측면 공격"된 디스크를 자신의 색으로 뒤집는 것으로 구성됩니다.
측면 공격이란, 디스크가 X 칸에 있고 Y 칸에 다른 디스크가 있는 경우 다음과 같습니다.
- X와 Y가 같은 행에 있거나,
- X와 Y가 같은 열에 있거나,
- X와 Y가 같은 대각선에 있는 경우,

플레이하는 동안 위의 경우 중 하나(또는 그 이상)가 발생하면 X와 Y 사이의 상대방 디스크가 자신의 색으로 뒤집힙니다.

<br>

예:

> 여기 흰색 디스크 A는 이미 보드에 있었고, 흰색 디스크 B를 놓은 후 흰색 디스크 A와 B 사이의 검은색 디스크 행이 측면 공격을 당했습니다.

![06a8330dc692b7631a2e50660e4a7346](https://github.com/TERNION-1121/Othello-Reversi-Game/assets/97667653/84feed70-ee16-4f4f-baad-39a3ecc148ed)

> 따라서 측면 공격을 받은 검은색 디스크가 흰색으로 뒤집혔습니다.

![cd51ed676fb49538035a8bf006ffbe96](https://github.com/TERNION-1121/Othello-Reversi-Game/assets/97667653/bafe9059-7a32-4d93-aaa2-bfc97a311fce)

게임 규칙에 대한 자세한 설명은 이 [링크](https://www.worldothello.org/about/about-othello/othello-rules/official-rules/english)를 확인하십시오.


### 게임 방법 🎮
1. 소스 코드 다운로드
2. 컴퓨터에 `pip`와 함께 Python3를 설치했는지 확인하십시오.
3. `numpy` 및 `pygame` 라이브러리를 설치합니다. 이렇게 하려면 터미널을 열고 `pip install numpy` 및 `pip install pygame`을 입력합니다.
4. `main.py` 파일을 실행하고 게임을 플레이하십시오!

## 저자
이 프로젝트는 [비크란트 싱 바두리야](https://www.github.com/TERNION-1121)가 기여했습니다.

친절한 관심에 감사드립니다!
