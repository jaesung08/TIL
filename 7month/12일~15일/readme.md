# SSAFY Today I Learned

## 7/12
### git   	
1) git hub (클라우드 같은거)
2) bash ( 윈도우에서 리눅스 명령어를 사용할 수 있게 해주는 도구/ 간편리하며 git hub를 위해 사용 )

+ Gui : 윈도우gui, 리눅스
<->
Tui :
->
Cli : cmd, powershell, bash

+ 인터페이스= 기계와 소통하기 위한 도구 **위에는 전부 인터페이스**

* ChatGPT
  * Generative/Pre-trained/Transformer
  * 생성모델  / 사전훈련  / 트랜스포머ai모델( 딥러닝 모델, 자연어처리가 가능한)

  * HTML=> 틀
  * CSS => 꾸며주는거
  * 자바스크립트 => 로직

* 클라이언트 만들기 ( 프론트엔드)
  * 클라이언트와 서버가 상호작용
  * API는 클라이언트가 서버에 요청하는 규칙
  * api로 요청하면 응답을 Json으로 보냄

* Json은 키와 밸류로 구성됌
  * key : value
  * 딸기 : 5개
  * 수박 : 3개
  * 생수 : 8팩

### vs-code단축키
* ctrl + s : 저장
* ctrl + j : 터미널창
* ctrl + w : 닫기
* ctrl + / : 주석

## 7/13

### 마크다운- 언어? 가독성이 좋음 편의성도 좋음
- 개발자로 성장하기
- 대체어디서부터 시작해서 어디까지 해야할까?
- python과 java를 배우면 개발자가 되는걸까?
  제일 중요한건 **꾸준한 학습**을 할 수 있는 사람인지를 보여줘야 한다.


## 개발자로 성장하기 

### ordered 리스트 작성하기
1. 탭을 눌러보세요
2. 엔터를 두 세번 눌러보세요 
   1. 탭을 누르면 2-1번
4. 4번을 적어도 3번으로 표시됍니다.
3. 3번을 적어도 4번으로 표시되고요


### unorder list
-  -든 +든 *이든 상관없습니다.
 + 다시 돌아가기 키는 shift + tab
  * 엔터를 여러번 눌러도 다시 돌아간다.

### check list 
- [ ] 사과
- [ ] ekdrmsㄴ
- [x] didvk
- [X] 라면
- [ ] tnrwn
- [ ] 


### code block
```python
a = input()
a = str()
print(a)


```

```C
# include <stadio.h>
int main()
(
    print ("hello world\n")
    return 0;
)



```

### 링크 url 걸기
[싸피] (https://edu.ssafy.com/edu/main/index.do)

### 이미지 걸기는 앞에 느낌표를 붙여야함
![고양이](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FyDtgP%2FbtrJaVA4iLN%2F9QtVWLrCIrUtDz7U4Udsr0%2Fimg.jpg )

### 글씨 굵게 표현하기
굵게 할 때는 언더바나 별표 두개

__굵은글씨__

**굵은글씨**

글 중간에 __이렇게 강조__ 합니다

### 글꼴 기울기

기울기는 언더바나 별표 한개

_안녕안녕_

*이렇게 기울이지*

글 중간에 _이렇게_ 기울이지

엥 별로 하랬는데 언더바도 되네요

### 굵게 기울이기

___굵게 기울이기___

### 취소선 

~~ 취소선 ~~

### 수평선 만들기
이렇게하는거지용
 _ _ _
스페이스바 언더바 언더바 언더바


## CLI를 사용하는 이유
* GUI가 사용하기는 쉽지만, 단계가 많고 성능을 상대적으로 많이 소모하기에 
수많은 서버/개발 시스템이 CUI 를 활용해 조작환경을 제공한다.
* => 개발자의 기본소양이기때문에 CLI사용

### 깃 허브 터미널 명령어 모음 ctrl J

* cd ./이동할 파일이름
* cd .. 경로 하나 나가기
* ls 	//그 폴더에서 리스트들 보여주기
* rm -r 삭제할파일이름
* rm *전체삭제할 파일명
* clear	 //전체 지우기
* touch a.txt 	//폴더에 a.txt파일 만들기
* mkdir new_folder // new_folder라는 폴더 만들기
* tab키 // 자동완성 //자주 이용하기

### git을 사용하는 이유
*   프로젝트 협업하기에 용이하기에 사용!!
* 코드의 버전을 관리하고 이전 버전과의 변경사항 비교, 개발되어온 과정 파악 용이

* 코드의 __변경이력__ 을 기록하고 __협업__ 을 원할하게 하는 도구
* => 분산 버전 관리 시스템

* git : local repository 로컬 저장소
* git hube : remote repository 원격 저장소


*  working directory
=> add

*  staging area
=> commit

*  repository

### git 명령어
* git config --global user.name 장재성
* git config --global user.email lancer98@naver.com
* git config --global -l  	(영어 L임)
* git init  깃 넣기
* rm -rf git 깃 삭제
* git init
* rm -rf .git

* echo > a.txt > b.txt > c.txt 이파일들 만 깃
* echo c.txt>> .gitignore 이 파일만 깃 삭제

* rm .gitignore 깃 삭제 취소
* git add . 애드
* git status 상태보기
* git reset 애드 취소
* git add . 
* git commit -m 'first commit'   ' '이름으로 커밋하기
* git log 로그 보기
* rm -rf .git


## 7/14

* 깃허브 가입하기
* branch명 master로 설정 후 Repositories만들기

* 터미널에서 커밋후 로그 확인이 되면
git remote add origin https://github.com/jaesung08/First.git	
* 깃허브주소창에 애드

### 깃허브 커밋하는 명령어
*  git remote -v 

*  git push **origin** +master	푸쉬하는데 마스터는 branch명으로

*  git pull origin master	=>원격 저장소의 변경사항만 받기
*  git clone https://github.com/jaesung08/First.git	=> 저장소 전체를 복제하여 다운로드
*  깃허브 주소는 원하는 원격저장소 주소를 사용
* origin에는 자신이 원격저장소에 올릴 이름으로 작성


*  https://www.toptal.com/developers/gitignore/
ignoreㅍㅏ일 만드는곳(?)
