# MediaPipe와 OpenCV를 이용한 동작 감지 프로그램

이 파이썬 스크립트는 MediaPipe 라이브러리와 OpenCV를 함께 활용하여 포즈 추정 모델을 사용하여 실시간 동작 감지를 수행합니다. 이 스크립트는 비디오 파일(`workout.mp4`의 경우)을 프레임 단위로 읽고 각 프레임을 처리하여 사람의 포즈를 감지하고 감지된 포즈를 프레임의 FPS(초당 프레임 수)와 함께 시각화합니다.

## 요구 사항
- 파이썬 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

## 설치
pip를 사용하여 필요한 라이브러리를 설치할 수 있습니다.
```bash
pip install opencv-python mediapipe
```

## 기능
- 포즈 추정을 이용한 실시간 동작 감지
- 각 프레임에 감지된 포즈 및 FPS 시각화
