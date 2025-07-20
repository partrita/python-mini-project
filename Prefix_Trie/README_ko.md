<!--이 부분을 삭제하지 마십시오-->

![스타 배지](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![오픈 소스 사랑](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

## 🛠️ 설명

파이썬에서 간단한 접두사 트라이 구현. 삽입, 검색을 허용하고 트라이의 문자열이 접두사로 시작하는지 확인합니다.

## ⚙️ 사용된 언어 또는 프레임워크

이 프로그램은 Python3로 만들어졌습니다.

## 🌟 실행 방법

이 트라이를 사용하려면 파이썬 파일 상단에 다음을 추가하여 트라이 클래스를 가져옵니다.
`from trie import Trie`

그런 다음 생성자 `trie = Trie()`를 사용하여 트라이를 만들 수 있습니다.

**메소드:**\
 _insert(word)_ - 트라이에 단어를 삽입합니다.\
 _search(word)_ - 단어가 트라이에 있으면 반환합니다.\
 _starts_with(prefix)_ - 트라이의 단어가 접두사로 시작하면 반환합니다.\

삽입하려면 `trie.insert("word")`를 실행합니다.\
검색하려면 `trie.search("word")`를 실행합니다.\
트라이에 접두사가 포함되어 있는지 확인하려면 `trie.starts_with("w")`를 실행합니다.

## 🤖 저자

[팀 부옹](https://github.com/Tim-Vuong)

LeetCode 문제에 대한 크레딧:
https://leetcode.com/problems/implement-trie-prefix-tree/description/
