# 어떤 숫자를 쓰셨나요?

![](https://img.shields.io/badge/TensorFlow-2.1-orange) ![](https://img.shields.io/badge/Python-3.7-blue)

TensorFlow2 + Keras와 Flask로 구현된 필기 숫자 인식 응용 프로그램입니다.

![](https://cdn.jsdelivr.net/gh/innofang/jotter/source/waht-digit-you-write/screencast.gif)

## 실행 방법?

```shell script
$ git clone --depth 1 https://github.com/InnoFang/what-digit-you-write.git
$ cd what-digit-you-write
$ conda create --name <env> --file requirements.txt
$ conda activate <env>
$ python app.py
```

복제가 너무 느리면 다음 방법을 사용할 수 있습니다.

```shell script
$ # git clone --depth 1 https://github.com.cnpmjs.org/InnoFang/what-digit-you-write.git
```

### 도커 환경

환경이 어떻게 구축되었는지는 `Dockerfile`을 참조하십시오.

````
$ git clone --depth 1 https://github.com/InnoFang/what-digit-you-write.git
$ cd what-digit-you-write
$ docker build -t ml-digit .
$ docker run -it -p 5000:5000 ml-digit
````
