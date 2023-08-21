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
3. 4번을 적어도 3번으로 표시됍니다.
4. 3번을 적어도 4번으로 표시되고요

### unorder list

- -든 +든 *이든 상관없습니다.

+ 다시 돌아가기 키는 shift + tab

* 엔터를 여러번 눌러도 다시 돌아간다.

### check list

- [ ] 사과
- [ ] ekdrmsㄴ
- [X] didvk
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

![고양이](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FyDtgP%2FbtrJaVA4iLN%2F9QtVWLrCIrUtDz7U4Udsr0%2Fimg.jpg)

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

---

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

* 프로젝트 협업하기에 용이하기에 사용!!
* 코드의 버전을 관리하고 이전 버전과의 변경사항 비교, 개발되어온 과정 파악 용이
* 코드의 __변경이력__ 을 기록하고 __협업__ 을 원할하게 하는 도구
* => 분산 버전 관리 시스템
* git : local repository 로컬 저장소
* git hube : remote repository 원격 저장소
* working directory
  => add
* staging area
  => commit
* repository

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

* git remote -v
* git push **origin** +master	푸쉬하는데 마스터는 branch명으로
* git pull origin master	=>원격 저장소의 변경사항만 받기
* git clone https://github.com/jaesung08/First.git	=> 저장소 전체를 복제하여 다운로드
* 깃허브 주소는 원하는 원격저장소 주소를 사용
* origin에는 자신이 원격저장소에 올릴 이름으로 작성
* https://www.toptal.com/developers/gitignore/
  ignoreㅍㅏ일 만드는곳(?)

# 7.17

## 프로그램 - 명령어들의 집합

* 친구에게 우리집으로 오는길을 적어준것- 프로그램 작성
* 적어준길을 순서대로 따라가는것 - 프로그램 실행
* ~~에서 우회전, 두 블록 직진 후 좌회전 등으로 구성- 몇가지 기초연산으로 구성됌
* 컴퓨터는더 다양한 연산 집합을 가질 수 있음
  => 기존 연산을 사용해 더 많은 연산을 만들고 차곡차곡 쌓아 새로운 연산을 만들어냄

### 프로그래밍의 핵심

* 새연산을 정의하고 조합해서 유용한 작업을 수행하는것.
* **문제를 해결하기**위한 도구

### 파이썬 사용이유

* 간결하고 읽기쉬움
* 다양한 응용분야
* * 데이터 분석, 인공지능, 웹개발, 자동화 등
* 파이썬 커뮤니티의 지원
* * 세계적인 규모의 사용자로 생태계가 유지
* 컴퓨터는 기계어(0과 1)만 사용하나, 사람은 기계어 작성이 어려움.
  => 인터프리터를이용하여 명령어를 기계어로 바꿈.
* * 훨씬 사용하기 쉽고, 운영체제간 이식도 가능(확장성)
* shell을 사용하여 명령어 하나씩 사용
* 확장자가 .py인 파일에 작성된 파이썬 프로그램 실행

### 파이썬의 구성

* 표현식 = 값, 변수, 연산자 등을 조합하여 계산되고 결과를 도출하는 코드 구조
* 평가(evaluate) = 표현식이나 문장을 실행하여 그 결과를 계산하고 값을 결정하는 과정
* =>표현식이나 문장을 순차적으로 평가하여 프로그램의 동작을 결정
* 문장(statement) = 실행가능한 동작을 기술하는 코드(조건문, 반복문, 함수정의 등)
* 문장이 여러개의 표현식을 포함함
* 타입 = 값이 어떤종류의 데이터인지 어떻게 해석되고 처리 되어야하는지 정의
* => 값(피연산자)과 연산자 2가지로 분류
* 데이터 타입

  * Numeric Type = 정수(int), 실수(float)
  * set type = set
  * sequence type = list, tuple, range
  * text sequence type = str(문자열)
  * mapping type = dict
  * 기타 = none, boolean, functions
  * **리스트, 튜플, 딕션너리 의 차이점을 잘알아야함**
* 산술 연산자(우선순위 순)

  * ** 지수(제곱)
  * (-) 음수부호
  * (*) 곱셈
  * / 나눗셈
  * // 몫
  * % 나머지
  * + 덧셈
  * - 뺼셈

### 변수

* 변수(variable) = 값을 참조하는 이름
  * 할당문을 통해 변수에 값을 할당(변수명=값)
  * ![변수](%EB%B3%80%EC%88%98.png)

#### 변수명규칙

* 영문알파벳,언더스코어( _ ), 숫자로 구성
* 숫자로 시작불가
* 대소문자를 구분
* 파이썬 내부 예약어는 사용불가

  * false, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield, __ peg_parser__
* 모든 메모리에는 고유주소가 존재
* 객체(object) = 타입을 갖는 메모리 주소 내 값
* => 값이 들어있는 상자
* 변수에 참조하는 메모리 주소를 가지게 하고 고유 메모리주소에는 객체(값)을 저장

### 스타일 가이드

* 코드의 일관성과 가독성을 향상하기위한 규칙과 권장사항들의 모음
  * 변수명은 무엇을 위한 변수인지 직관적인 이름을 가져야한다.
  * 공백4칸을 사용하여 코드블록 들여쓰기(tab사용은 에디터가 변환해줬기때문에 사용가능)
  * 한줄의 길이는 79자로 제한, 길어지면 줄바꿈 사용
  * 문자와 밑줄(_)을 사용하여 함수,변수,속성의 이름 작성( 밑줄 쓴것을 snake_case 라 칭함)
  * 함수 정의나 클래스 정의 등의 블록사이에는 빈 줄 추가( 2줄을 권장)
  * pep8 사이트에서 파이썬 가이드 참고
  * 파이썬튜터 참고
    * [파이썬 설문](https://www.jetbrains.com/ko-kr/lp/devecosystem-2022/)
    * [pep8](https://peps.python.org/pep-0008/)
    * [파이썬 튜터](https://pythontutor.com/)

### 주석

* 프로그램 코드내에 작성되는 설명이나 메모
* 인터프리터에 의해 실행되지않음
* (#) 을 사용하여 작성
* """	""" 여러줄 주석용으로 사용 => 보통 설명문 넣을떄 사용
* 코드의 특정부분을 설명할 때
* 임시로 코드를 비활성화할 때
* 코드를 이해하거나 문서화할 때
* 다른 개발자나 자신에게 코드의 의도나 동작을 설명할 때

# 7.18

## Data Types

* 값의 종류와 그 값에 적용 가능한 **연산과 동작을 결정** 하는 속성

  * Numeric Type = 정수(int), 실수(float), complex(복소수)
  * set type = set, dict
  * sequence type = list, tuple, range
  * text sequence type = str(문자열)
  * mapping type = dict
  * 기타 = none, boolean, functions
  * **리스트, 튜플, 딕션너리 의 차이점을 잘알아야함**
* 데이터 타입이 필요한 이유

  * 값들을 구분하고 어떻게 다뤄야 하는지 알 수 있음.
  * 각 데이터 값에 적합한 도구를 가짐
  * 타입을 명시적으로 지정하여, 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해하고, 잘못된 데이터 타입의 오류를 미리 예방

## Numeric Type

### int = 정수 자료형

    * 2진수(binary) = 0b    [print(0b10) #2]
    * 8진수(octal) = 0o     [print(0x30) #24]
    * 16진수(hexadeciaml) = 0x     [print(0x10) #16]

    * print(bin(12))	= 0b1100
    * print(oct(12))	= 0o14
    * print(hex(12))	= 0xc

### float = 실수 자료형(실수에 대한 근삿값)

    * 유한 정밀도
         * 0.66666666666666666 = 2/3에 대한 근삿값
         * 1.66666666666666667 = 5/3에 대한 근삿값
         * 컴퓨터는 2진수를 쓰기 때문에 0.1을 2진수로 표현하면 무한대로 반복
         * => 무한대숫자를 표현 할수 없어 10진법의 근사값을 표시
         * 이런 증상을 floating point rounding error 라고 함

* 실수 연산 시 해결책
  * 1. 임의의 작은 수 활용
  * 2. math 모듈 활용
* ![실수 연산시 해결책](사진1 실수 연산의 해결책.png)
  * 지수 표현 방식
    * 314 * 0.01 = 314e - 2 = 314**(-2)
    * e = 10^

## Sequence Type = 여러개의 값들을 **순서대로 나열** 하여 저장하는 자료형

    * ( str, list, tuple, range )
    * 순서(sequence) = 값들이 순서대로 저장 (정렬XXX)
    * 인덱싱(indexing) = 각 값에 고유인덱스(번호)를 가지고 있어, 인덱스를 사용하여 특정 위치 값을 선택하거나 수정할 수 있음
    * 슬라이싱(slicing) = 인덱스 범위를 조절해 부분적인 값을 추출 가능
    * 길이(legnth) =  len()함수를 사용하여 저장된 값의 갯수(길이)를 구할 수 있음
    * 반복(lteration) = 반복문을 사용하여 저장된 값들을 반복적으로 처리 가능
    * 5가지 모두 사용가능하고 가변,불변에 따라 나눌수 있음

### str = 문자열( **불변** 시퀸스자료형 )

* 문자열은 여러 문자의 조합
* 작은 따옴표(') 또는 큰따옴표(") 으로 감싸서 표현

  * 중첩따옴표 => 작은 따옴표 안에 큰따옴표로 표현, 큰따옴표 안에 작은 따옴포로 표현
  * " 가나다라마바사'아자차카'타파하"
* 역슬래시를 사용하여 특수한 기능 사용

  * \\n = 줄바꿈
  * \\t = 문자 사이 탭 삽입
  * \\\ = 백슬래시
  * \\' = 작은 따옴표
  * \\" = 큰따옴표
    * print( '철수야 \\' 안녕 \\' ' ) = 철수야 '안녕'
* string Interpolation = 문자열 내 변수나 표현식을 삽입하는 방법

  * f-string = f 또는 F 접두어를 붙이고 표현식을 {expression}으로 작성하여 문자열에 파이썬 표현식의 값을 삽입함.
  * print(f'Debugging {bugs} {counts} {area}')  => {} 자리에 각 변수에 입력된 값이 출력
  * (이전에는 .format 이라는 함수를 사용 하였으나 최근에는 f-string 사용)
  * (더 이전에는 %s, %d, %f 등을 사용했음 )
  * 인덱싱 = 그 자리의 요소 찾아오기 //  슬라이싱 = 그 사이의 자리 요소 찾아오기 // 길이 = 요소의 갯수
  * ![문자열 시퀸스 특징](사진2 문자열 시퀀스 특징.png)
* 인덱스 = 시퀀스 내의 값들에 대한 고유 번호, 각 값의 위치를 식별

  * ![사진3](사진3 인덱스.png)
* 슬라이싱 = 시퀸스의 일부범위를 추출하여 새로운 시퀸스를 생성

  * ![사진4](사진4 슬라이싱.png)
  * 슬라이싱 범위의 마지막은 예외
  * [ :3] 이라면 처음부터 3까지 // 처음이라는 값은 작성X
  * [3: ] 이라면 3부터 마지막 까지 // 마지막 또한 마찬가지
  * 마지막에 -1 은 시작지점이 0이라는 인덱스의 특성을 고려한것이다 !
  * ![사진5](사진5 슬라이싱.png)
  * [0:5:2] 0부터5까지 (step)2칸씩 추출
  * [ : : -1] step을 음수로 추출할 시 거꾸로 읽혀 hello가 olleh로 추출 => **문자열 뒤집기**

```
    * greeting[start:end:step]
    * step>0 이면 start가 0이므로 end-1
    * step<0 이면 start가 -1이므로 end+1
```

#### => 문자열은 불변입니다. 잊지마세요. 필요하면 새로운 문자열을 만들기.

### list = **가변** 시퀸스 자료형

* 리스트는 0개 이상의 객체 포함하여 데이터 목록 저장 // 빈 리스트가 가능
* 대괄호( [ ] )로 표시
* 어떠한 자료형도 저장할 수 있음

  * [ 1, 2, 3 'pyhthon' , ['hello', 'world' , '!!!']] => 5개의 자료
* 중첩된 리스트의 접근

  * ![사진6](사진6 중첩리스트 접근.png)
  * [4][-1] 4번째 인덱스의 -1 즉 문자열의 마지막 값 '!!!' 출력
  * [-1][1][0] 3단계를 걸쳐 w 출력
* 가변형 !! 인덱스를 호출하여 다른 값을 입력가능

  * ![사진7](사진7 리스트 가변.png)

### Tuple = 불변 시퀸스 자료형

* 0개 이상의 객체 포함 // 빈 튜플 가능
* 소괄호로( () )로 표시
* 어떤 자료형도 저장 가능
* 하나의 자료형만 있어도 (1, ) 으로 " , " 를 사용해야함
* 리스트와 유사하나 불변 데이터 자료형

  * => 개발자가 쓰기보다는 **파이썬의 내부 동작**에서 사용됌
* 여러개의 값을 할당하여 그룹화 할때 사용

  * x, y =(10, 20)  이럴 때 사용
  * => 개발자가 쓰일이 없기 때문에 크게 의식하지 않아도 됌

### range = 연속된 정수 시퀀스를 생성하는 불변 자료형

* range(n)

  * 0부터 n-1까지의 숫자 시퀀스
* range(n,m)

  * n 부터 m-1까지의 숫자 시퀀스
* 마지막에 -1 은 시작지점이 0이라는 인덱스의 특성을 고려한것이다 !
* range(n,m,s)

  * n 부터 m-1까지 s마다 건너뛴 숫자 시퀸스
  * range[start🔚step]
  * start < end = start부터 end-1까지 step만큼 증가
  * start > end = start부터 end+1까지 step만큼 감소
* ![사진8](사진8 range 사용법.png)

  * 리스트를 활용하여 값을 활용함

## Non-Sequence Types

### dict = 딕셔너리 (순서와 중복이 없는 가변 자료형)

* Key : value 의 세트 형태
  * key는 불변형 자료형만 사용가능(str, int, float, tuple, range ...)
  * value는 모든 자료형 사용가능
* 중괄호 ( {} )로 표기
* ![사진9](사진9 딕셔너리.png)
  * Key를 활용하여 value에 접근 // 대괄호 ( [] )를 활용하여 값을 추출
  * 가변형이기에 키를 활용해 value값 변경 가능

```python
# dict안에 dict 또있는경우
my_dict = {
    'a1' : {'b1':1, 'b2':2, 'b3':3},
    'a2' : {'b1':4, 'b2':5, 'b3':6},
    'a3' : {'b1':7, 'b2':8, 'b3':9}
}
# value 5를 출력
print(my_dict['a2']['b2'])
# 다른방법 .get( ) 을 사용한다
print(my_dict.get('a2').get('b2'))

```

### set = 세트 ( 순서와 중복이 없는 가변 자료형)

* 수학에서의 집합이라 보면 됌
* 중괄호 ( {} )로 표기
* 빈 자료형은 꼭 "set( )" 로 표기 해야함 ( 딕셔너리와 겹치기 때문 )
* ![사진10](사진10 세트 연산.png)
  * 수학의 집합과 똑같은 연산
  * | 합집합 // - 차집합 // & 교집합 //
  * 튜플과 같이 조금 독특하다

```python
# set 실습
set_1 = { 1,2,3,4,5,6,7,8,8,9,10}
set_2 = {2,3,5,6,8,9,11}
# 합집합
print(set_1 | set_2)
# 차집합
print(set_1 - set_2)
# 교집합
print(set_1 & set_2)
```

```python
# 세트의 사용예시 - 로또번호 추첨
import random

lotto_set=set()

while len(lotto_set) < 6 :
    number = random.randint(1,45)
    lotto_set.add(number) #set에 추가하는 .add

lotto_list = list(lotto_set)
lotto_list.sort  # sort는 오름차순 정렬
print(lotto_list)
```

## Other Types

### None = 값이 없을 표현하는 자료형

* 0이랑은 다르게 정말 값이 없다 라는 것을 표현

### boolean = 참과 거짓을 표현하는 자료형

* True 와 False
* 비교 / 논리 연산의 평과 결과로 사용
* 주로 조건/ 반복문과 함께 사용
* ![사진11](사진11 불린.png)

### collection = 여러개의 항목을 담는 자료구조

* str, list, tuple, set, dict
* ![사진12](사진12 collection.png)
  * 불변/가변과 순서 여부에 따라 나눠진다
  * range는 무의미하다용
* 불변과 가변의 차이
  * 불변은 하나의 메모리 주소에 할당해서 바꿀수없다
  * 가변은 각각의 메모리 주소에 하나의 값을 할당하기 때문에 바꿀 수 있다.
  * 하여 **리스트를 객체의 참조를 모아놓은 컬렉션** 이라 칭함

```
List_1 = [1, 2, 3,]
List_2 = List_1

List_1[0] = 100
print(List_1) # [100, 2, 3]
print(List_2) # [100, 2, 3]
```

* 리스트는 같은 곳을 복사하여 변환시키지 않아도 똑같아짐 // 프레임은 다르나 객체를 공유하게 되기 때문이다.

---

### 문자열 : ' ' 불변 시퀸스 자료형 -> 알고리즘 IM형 문자형 파싱(인덱싱, 슬라이싱 등)

### 리스트 : [ ] 가변 시퀸스 자료형 -> 알고리즘 IM형 방향배열 등 ,,, A형 DFS,BFS

### 튜플 : ( ) 불변 시퀸스 자료형 -> 알고리즘 방향배열

### 레인지 : 생성형 불변 시퀀스 자료형

### 딕셔너리 : 가변 비시퀸스 자료형-> ket : value -> DB의 Json 형식과 비슷

### 세트 : 가변 비시퀸스 자료형 -> 중복을 허용하지 않음 -> 집합

```
행- 가로 한줄을 뜻함
열- 세로 한줄을 뜻함

1행     1열 2열 3열 4열
2행
3행
4행
```

## Type Conversion = 형변환

### lmplicit Type Conversion = 암시적 형 변환

* 파이썬이 자동으로 형변환 하는 것
* Boolean과 Numeric Type에서만 가능
  정수 -> False = 0
  실수 -> False = 0.0
  문자열 -> False = "" (공백아니고 아예 없어야함)
* ![사진13](사진13 암시적 형변환.png)
* 때문에 더했을때 값이 나올 수 있게됌
* 정수 + 실수= 실수

### Explicit Type Conversion = 명시적 형변환

* 개발자가 직접 형변환 시키는 것
* str(문자열) -> integer : 형식에 맞는 숫자만 가능
* integer -> str : 모두 가능

```python
print(int('1')) #1
print(str(1)+'등' #1등
print(float( '3.5' )) # 3.5
print(int( 3.5 ) ) #3 // 형변환할때는 버림이 된다.
prunt(int( '3.5' ) ) # 에러발생
=> print( int( float('3.5') ) )  # 3
```

* ![사진14](사진14 형변환.PNG)

## 연산자

### 산술 연산자

* ![사진15](사진15 산술연산자.PNG)

### 복합연산자

* ![사진16](사진16 복합연산잔.PNG)

### 비교 연산자

* ![사진17](사진17 비교연산자.PNG)
* 항상 부등호가 먼저 사용되어야함
* ==, !=은 동등성을 띄고 값을 확인하나 is와 is not은 식별성을 띄고 레퍼런스(주소)를 비교한다.
* is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용!

```python
print(2.0 == 2) # True
print(2,0 is 2) #False

a=3
b=3
print(a==b) #True
print(a is b) #False
```

### 논리연산자

* and(논리곱) = 모두 다 참이여야 True
* or(논리합) = 하나 만 참이여도 True
* not(논리부정) = True-> False // False->True
* 비교 연산자와 함께 사용가능하다

단축평가예시

* ![사진18](사진18 단축평가.PNG)
* and
  * 첫번째 피연산자가 False라면 전체표현식은 False이며 두번째 피연산자는 무시
  * 첫번째 피연산자가 True라면 두번째 피연산자에 의해 결정되며, 두번째 피연산자가 결과로 반환
* or
  * 첫번째 피연산자가 True라면 전체표현식은 True이며 두번째 피연산자는 무시
  * 첫번째 피연산자가 False라면 두번째 피연산자에 의해 결정되며, 두번째 피연산자가 결과로 반환
* a와b가 공백이 아니기때문에 true이며 두번째 연산자인 b가 포함되지않기에 false
* a와b가 공백이 아니기때문에 true이며 두번째 연산자인 a가 포함되기때문에 True

#### 단축평가는 코드실행을 최적화하여, 불필요한 연산을 줄이기 위해 시행.

### 멤버쉽 연산자

* in = 왼쪽 피연산자가 오른쪽 피연산자의 시퀸스에 속하는지를 확인!
* not in = 왼쪽 피연산자가 오른쪽 피연산자의 시퀸스에 속하지않는지를 확인!
* ![사진19](사진19 멤버쉽연산자.PNG)

### 시퀸스형 연산자

* 시퀸스 간 연산에서 사용될 때 다른 역할을 가짐
* + 결합 연산자
* * 반복 연산자
* ![사진20](사진20 시퀸스형연산자.PNG)

### 연산자 우선순위

* ![사진21](사진21 연산자 우선순위.PNG)

# 7.19

## Functions 함수 = **특정 작업을 수행** 하기 위한 **재사용 가능한** 코드 묶음

* 재사용성이 높고, 코드의 가독성과 유지보수성이 향상
* 디버깅 하기 용이하다.

### 내장함수(built-in function) = 파이썬이 기본적으로 제공하는 함수

* 절대값 함수 abs( ) // sum // str // type // input // int
* 출력함수 print( ) 등이 존재한다.
* 위처럼 함수를 실행하기 위해 함수의 이름을 사용하는것을 **함수 호출 (fuction call)** 이라 한다.

### 함수구조

* ![사진1](사진1 함수구조.png)
* def 하여 함수의 이름과 매개변수를 지정해주고,
* return 하여 함수의 변수 계산 값을 지정해준다.
* 주석을 통해 함수에 대한 설명서를 작성해준다.

#### 함수 정의

* def 키워드로 시작
* 이후 함수이름 작성
* 괄호안에 매개변수를 정의
  * 매개변수는 함수에 전달되는 값
* ![사진2](사진2 함수정의.png)

#### 함수 body

* def ~~ : 다음에 들여쓰기된 코드블록
* 함수가 실행될 때 수행되는 코드를 정의
* 주석을 이용해 설명을 선택적으로 작성가능

#### 함수 반환값

* return 을 이용해 필요할 경우 반환할 값을 명시할 수 있음
* 함수의 실행을 종료하고 호출부분으로 반환
* result가 None이 뜬다면 return을 작성하지 않은 것
* ![사진3](사진3 함수body와 반환.png)

#### 함수 정의 및 호출

```py
def 함수명(매개변수)
    코드 (함수바디)
return ~~~ (함수반환값)
인풋은 파라미터, 아웃풋은 리턴 벨류

# 함수호출
함수명(함수인자)

매개변수는 있을수도 있고 없을 수도 있습니다.
반환값은 있을 수도 있고 없을 수도 있습니다. 

-> 총 4가지 유형의 함수 존재!!
```

```python
def get_sim(num1, num2):
    return (num1 + num2)

num1 = 5
num2 = 3
result = get_sum(num1,num2)
print(result)

# 매개변수가 없는 함수로 변형(출력결과는 같게)
def get_sum():
    num1, num2 = 5, 3
    return num1 + num2

result= get_sum()
print(result)
# return 반환값이 없는 함수로 변환(출력결과는 같게)
def get_sim(num1, num2):
    result = num1 + num2
    print(result)

num1 = 5
num2 = 3
get_sum(num1, num2)

```

### 매개변수와 인자

* 매개변수 (parameter)
  * 함수를 정의할 때, 함수가 받을 값을 나타낸 변수
* 인자 (argument)
  * 함수를 호출할 때 실제로 전달하는 값
* ![사진4](사진4 매개변수와 인자 예시.png)

#### 인자의 종류

* 위치인자 (positional Arguments)

  * 함수 호출시 인자의 위치에 따라 **반드시 전달** 해야 하는 인자
  * ![사진5](사진5 위치인자.png)
  * 함수의 필수 요소 name과 age의 윛에 놓인 alice와 25가 위치인자!!
* 기본 인자 값(Default Argument Values)

  * 함수 정의에서 매개변수에 기본값을 할당하는 것
  * 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됌
  * ![사진6](사진6 기본인자.png)
  * age =30 이 기본인자값이 된다. ( 밑에처럼 40을 넣지 않았기 때문)
* 키워드 인자 (keyword arguments)

  * 함수 호출시 인자의 이름과 함께 값을 전달하는 인자
  * 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당 가능.
  * 순서와 상관없이 인자의 이름을 명시해서 전달하는 것.
  * ![사진7](사진7 키워드인자.png)
  * name과 age의 순서와 상관없이 이름을 명시해서 전달하였다.
  * 위치인자와 함께 사용할 수 없다!!
* 임의의 가변인자 목록 ( Arbitrary                     )

  * 정해지지 않은 개수의 인자를 처리하는 인자
  * 함수 정의시 매개변수앞에 ( * ) 을 붙여서 사용하며, 여러개의 인자를 tuple로 처리한다.
  * ![사진8](사진8 임의의 인자.png)
  * 소괄호를 통해 튜플임을 알 수 있다.
  * 출력이 주석과같이 (1,2,3)이 나온다.
* 임의의 가변키워드인자 목록

  * 정해지지 않은 개수의 키워드 인자를 처리하는 인자
  * 함수 정의시 매개변수 앞에 ( ** ) 를 붙여 사용.
  * 여러개의 인자를 dict로 묶어처리
  * ![사진9](사진9 임의의 키워드 인자.png)
  * 함수 인자 권장 작성순서
  * 위치 -> 기본 -> 가변 -> 키워드 -> 가변키워드
  * 호출 시 인자를 전달하는 과정에서 혼란을 줄이기 위함( 절대적인 규칙 X)
  * ![사진10](사진10 함수 인자 권장순서.png)

## 함수와 scope

### python의 범위(Scope)

* 함수는 코드 내부에 local scope 를 생성하며, 그 외의 공간인 global scope로 구분
* scope

  * global scope : 코드 어디에서든 참조할 수 있는 공간
  * local scope : 함수가 만든 scope ( 함수 내부에서만 참조 가능)
* variable

  * global variable : global scope에 정의된 변수
  * local variable : local scope에 정의된 변수

```python
# scope 
def my_func() :
    num = 1

print(num)
# num 은 함수안에만 정의되있기 때문에 찾지못한다
# 함수내의 num이 local // print()내의 num이 global
```

* num은 local에 존재하기때문에 global에서 사용할 수 없다.
* 이는 변수의 **수명주기** 와 연관이 있다.

#### 변수의 수명주기

* built-in scope
  * 파이썬 실행 후 영원히 유지
* global scope
  * 모듈이 호출된 시점 이후 or 인터프리터가 끝날 때까지 유지
* local scope
  * 함수가 호출될 때 생성되어, 종료될 때까지만 유지

#### 이름 검색 규칙

* 파이썬에서 사용되는 이름들은 특정한 이름공간에 저장되있음
* 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름
  * local scope : 지역범위(현재 작업중인 범위)
  * Enclosed scope : 지역범위 한단계 위 범위
  * Global scope : 최상단에 위치한 범위
  * Built-in scope : 모든 것을 담고 있는 범위(정의하지않아도 사용할 수 있는 모든 것)
* 함수 내에서 바깥 Scope 변수에 접근은 가능하나 수정은 불가함.
* ![사진11](사진11 scope 범위.png)

```py
# bulit-in scope는 내장함수
z = 3 # global scope
def outer():
    x=1 # 로컬변수
    def inner():
        y=2 #로컬변수
        result = x + y # x가 enclosed scope에 해당
        print(result)
    inner()
outer()
```

* LEGB Rule에 의해 하위scope에서 내장함수를 사용시 내장함수를 하위scope에서 사용 불가하기때문에 사용하지 않는다.
* LEGB Rule때문에 내장함수와 같은 이름이 사용불가
* ![사진12](사진12 scope 예시 .png)
* # 답에 대해 잘 이해하고 있기!!

### ' global ' 키워드

* 변수의 스코프를 전역범위로 지정하기 위해 사용
* 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
* ![사진13](사진13 global키워드.png)
* 함수내에서 num에 +1 하는 것때문에 global키워드 사용
* 권장하지 않으나 문제풀이때문에 사용하긴함.
* 주의사항

  * global키워드 선언전에 접근 X
  * ![사진14](사진14 global주의사항.png)
  * 매개변수에 global키워드 사용불가
  * ![사진15](사진15 global주읫항.png)

#### globla키워드는 가급적 사용하지않고, 함수로 값을 바꾸고자 한다면 인자로 넘기고 함수의 반환값을 사용하도록 권장

## 재귀함수 = 함수 내부에서 자기 자신을 호출하는 함수

* 특정 알고리즘식 표현시 변수의 사용이 줄고 코드의 가독성이 좋아짐
* 1개이상의 base case(종료되는 상황)이 존재하고 수렴하도록 작성
* 재귀함수의 예시로 팩토리얼이 있다
  * n! = n*(n-1)! = n*(n-1)*(n-2)! = . . .
* ![사진16](사진16 재귀함수 팩토리얼.png)
* ![사진17](사진17 재귀함수 팩토리얼.png)
* 팩토리얼이 자기자신을 재귀적으로 호출하여 숫자n의 팩토리얼 계산
* 재귀함수는 n이 0이 될때까지 반복, 종료조건을 설정하여 멈출수 있도록 함
* 재재귀 호출의 결과를 이용해 문제를 작은 단위의 문제로 분할하고, 다시 분할 된 문제들의 결과를 종합하여 최종결과 도출.
* => 종료조건이 명확하고, 반복되는 호출이 종료조건을 향하도록 작성! STACK이라 칭하기도함.
* ### 어렵게 가지말고 1. 종료조건이 명확하고, 2. 반복되는 호출이 종료조건을 향하도록 작성 을 위주로하기

## 유용한 함수

### 유용한 내장함수

* map(function, iterable)
  * 순회 가능한 데이터구조(iterable)의 모든요소에 함수를 적용하고, 그결과를 map object로 반환

```python
#map 함수
numbers = [ 1, 2, 3 ]
result =  map(str, numbers)
print(result) #<map object at 0x0000019A62C613D0>
print(list(result)) #['1', '2', '3']

a = list(map(int, input().split()))

```

* zip(*iterables)
  * 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
names = ['Alice', ' Bob', 'Charlie']
ages = [30,  35]
cities = ['New york', 'London', 'Paris' ]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)


keys = ['a', 'b', 'c']
values = [1,2,3]
my_dict = dict(zip(keys, values))
print(my_dict)

```

* 리스트의 갯수가 맞지않으면 맞는 갯수 만큼만 작성됌!!!

### lambda함수 = 이름없이 정의되고 사용되는 익명함수

* lambda 매개변수 : 표현식
* lamda키워드를 사용
* 매개변수 : 함수에 전달되는 매개변수들 // 쉼표를 사용해 구분
* 함수의 실행코드블록으로 결과값을 반환하는 표현식

```python
# lambda와 map 함수
numbers = [1, 2 ,3 ,4 ,5]
result = list(map(lambda x: x * 2, numbers))
print(result)

# def double_number(x):
#     return x *2
# 위의 lambda함수 를 풀어쓰면 이렇게된다

# lambda 매개변수 : 표현식

#1. 1회성이기때문에 함수 명이 필요없다.
#2. 표현식의 결과가 반환되기때문에 return도 필요없다

```

---

## packing 패킹

* 여러개의 value를 하나의 시퀀스로 묶는 과정 ( 하나의 변수에 묶음)
* 튜플형태로 묶인다.

```py
# 패킹 : 여러 값을 하나의 시퀀스로 묶는 과정
# 예시1)
packing_values = 1,2,3,4,5
print(packing_values) # (1, 2, 3, 4, 5) 튜플형태
```

```py
numbers = [1,2,3,4,5]

a, *b, c = numbers # *(애스터리스크): 패킹연산자로 활용
print(a) #1
print(b) #[2, 3, 4] *b는 남은 요소들을 리스트로 패킹하여 할당 
print(c) # 5
```

* print 함수에 임의의 가변인자를 작성할수 있던 이유
* print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
* objects를 텍스트 스트림 file로 인쇄하는데, sep으로 구분되고 end를 뒤에 붙입니다. 있다면 sep, end, file 및 flush는 반드시 키워드 인자로 제공해야 합니다.
* 모든 비 키워드 인자는 str()하듯이 문자열로 변환된 후 쓰이듯 sep과 end도 문자열이여야 합니다.
* objects가 주어지지 않는다면 print()는 end만 사용합니다

```py
# print 함수에 임의의 가변인자를 작성할수 있던 이유

print('hi', 'hello', 'goodbye', sep = "-") # hi-hello-goodbye
print('hi',end=' ')
print('hello') # hi hello
```

## 언패킹 Unpacking

* 패킹된 변수를 개별적인 변수로 분리하여 할당하는것
* ( * )는 리스트 언패킹, ( ** )는 딕셔너리 키-값을 언패킹

```py
# *(애스터리스크)를 언패킹 연산자로 활용
names=['key', 'bob', 'jane']
print(*names) # key bob jane

## ** : 딕셔너리 언패킹 연산자
def my_funtion(x,y,z):
    print(x, y, z)
dict_values={'x':1, 'y':2, 'z':3}
my_funtion(**dict_values) # 1 2 3
```

## 모듈 import

* 모듈과 라이브러리는 같은 말인가? xx
* 라이브러리는 모듈과 패키지의 집합이다.
* 한 파일로 묶인 변수와 함수 모음
* 특정한 기능을 하는 코드가 작성된 파이썬 파일
* import 혹은 from을 사용해 모듈을 호출해 사용한다.

```py
# 파이썬 math 모듈 예시
import math
print(math.pi) # 3.141592653589793
print(math.sqrt(16)) # 4.0
# ctrl을 누른채 math를 누르면 안에 함수를 볼 수 있다.
# help(math) 입력도 가능

from math import pi, sqrt
print(pi)
print(sqrt(2))

#from 과 import 차이 2
import random
print(random.randint(1,46))

from random import *
print(randint(1,46))
```

### 사용자 정의 모듈

* 모듈 my_math.py 작성 ( 이름은 각자 알아서 작성)
* 다른 .py파일에서 import 혹은 from 하여 호출

```py
# my_math.py
def add(x,y):
    return x + y

# 사용자 설정 모듈 
import my_math
print(my_math.add(1,2))

from my_math import *
print(add(1,2))
```

## 파이썬 표준 라이브러리

* 모듈과 패키지의 집합

### 패키지

* 관련된 모듈들을 하나의 디렉토리에 모아놓은것
* 

![사진18](사진18 패키지 활용.png)

* 왼쪽 사진과 같이 디렉토리내에 활용하여 경로 활성화

```py
# 라이브러지- 패키지 디렉토리 
from my_package.math import my_math
from my_package.statistics import tools
print(my_math.add(1,2))
print(tools.mod(1,2))

```

#### PLS내부 패키지

* 설치없이 바로 import하여 사용

#### 외부 패키지( pip install )

* python installer package = 외부패키지 설치를 도와주는 패키지 관리 시스템
* pip install Somepackage (== 1.0.0) or (>= 1.0.5) 등 버전을 명시하여 설치가능
* git bash에서 pip install requests 입력
* [ramdom-data](https://random-data-api.com/api/v2/users)
* [Json viewer](https://jsonviewer.stack.hu/)

```py
# 패키징 설치 Json
import requests

url = 'https://random-data-api.com/api/v2/users'

response = requests.get(url).json()
print(response)
# https://jsonviewer.stack.hu/에서 출력을 텍스트에 입력하면 정리된 모습 확인 할 수 있음

# 실습) united states를 출력해보세요. - key로 접근

print(response['address']['country'])
print(response.get('address').get('country'))

```

#### 패키지 사용목적

* 모듈들의 이름공간을 구분하여 충돌을 방지하고
* 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

# 7.20

## 제어문(Control Statement)

* 조건문
* 반복문
* 코드의 실행 흐름을 제어하거나 조건에 따라 코드 블록을 반복적으로 실행

## 조건문(Conditional Statement)

* 주어진 조건식을 평가하여 참(True)인 경우에만 코드블록을 실행하거나 건너뜀
* if, elif, else
* 조건식에는 비교연산, 논리연산, 멤버연산등 ,,,

### ' if ' statement

```py
# if statement의 기본 구조
if 표현식 :
    코드블록
elif 표현식 : 
    코드블록
else :
    코드블록

num = int(input('숫자를 입력하세요 : '))

# if statement
# num이 홀수라면
if num % 2 == 1 :
    print(f"{num}은 홀수 입니다")
# if num % 2 : 라고 써도 가능하다. 결과값인 1이 Ture를 뜻하기에 if문이 실행된다.
# num이 짝수라면
else :  # num % 2 == 0 을 쓰지 않아도됌 
    print(f"{num}은 짝수 입니다")

```

* 복수 조건문 ( if // elif // elif // else )
  * 조건식을 동시에 검사하는게 아니라 순차적으로 비교
* 중첩 조건문

```py
dust = 480

if dust >150:
    print('매우나쁨')
    if dust > 300:
	print(' 위험해요! 나가지마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else :
    print('좋음')
```

* 위와 같이 if 문 내에 if문이 존재하는 중첩 조건문도 가능하다.

## 반복문(Loop Statement)

* 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
  * 특정 작업을 반복적으로 수행
  * 주어진 조건이 참인 동안만 반복해서 실행
* for // while

### ' for ' statement

* 임의의 시퀸스 항목들을 그 시퀸스에 들어있는 순서대로 반복
  * 시퀀스는 인덱스가 있고 순서가 있고 길이(갯수)가 있는 항목

```py
# for statement 의 기본구조
for 변수 in 반 가능한 객체 :
     코드블록
```

#### 반복 가능한 객체(iterable) =리스트, 튜플, 문자열, range등

* 반복문에서 순회할 수 있는 객체
  * 시퀸스 객체 뿐만아니라 dict, set 등도 포함
  * [ 1, 2, 3] 이라면 1(리스트 내 첫 항목)부터 변수에 할당되고 코드블록을 실행 후 2(2번째 항목)가 또 할당됌.
  * 이렇게 마지막 객체까지 변수에 할당되면 for 문은 끝나게 된다.

```py
# 문자열 순회
country = 'korea'
for char in country :
    print(char)
"""
k
o
r
e
a
"""
# range 순회
for i in range(5) 
    print(i)
"""
0
1
2
3
4
"""
# 인덱스로 접근해서 변경하기
numbers = [4, 6, 10, -8 ,5 ]

for i in range(len(numbers)) : 
    numbers[i] = numbers[i] * 2

print(numbers) # [8, 12, 20, -16, 10 ]
```

```py
# 중첩된 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers :
    for inner in inners :
	print(outer, inner)

"""
A c
A d # 안쪽 반복문이 끝나야 밖으로 나가게 됌
B c
B d
"""

# 중첩 LIST 순회
# 바깥 리스트를 순회하면서 중첩반복을 사용해 안쪽 반복 순회
elements = [['A', 'B'], ['c', 'd']]

for elem in elements :
    print (elem)
"""
['A', 'B']
['c', 'd']
"""
for elem in elements :
    for item in elem :
        print (item)
"""
A
B
c
d
"""
```

### ' while ' statement

* 주어진 조건식이 참인 동안 계속 반복해서 실행( 조건식이 거짓이 될때까지만 반복)

```py
# while statement 의 기본구조
while 조건식 :
     코드블록
# while 문 예시 
a = 0

while a <3:
    print(a)
    a += 1

print('끝')
"""
0
1
2
끝
"""
# while문을 사용해 입력값에대한 종료조건 활용 (if문)
number = int(input("양의 정수를 입력해주세요. : ")
while number <= 0 :
    if number < 0 :
        print( ' 음수를 입력했습니다.')
    else : 
        print(' 0은 양의 정수가 아닙니다. ')
    number = int(input("양의 정수를 입력해주세요. : ")

print('잘했습니다!')
```

### while문은 반드시 **종료 조건** 이 필요

## 적절한 반복문 판단하기

* for문 ( iterable의 요소를 하나씩 순회하며 반복)

  * 반복 횟수가 명확하게 정해져 있는 경우
  * 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할때
* while (주어진 조건식이 참인 동안 반복)

  * 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 경우
  * 예를 들어 사용자의 입력을 받아 특정 조건이 충족될 때 까지 반복하는 경우

## 반복제어

* for문과 while이 때로는 일부만 실행하고 중간에 멈추어야할때
* break 반복을 즉시 중지
* continue 다음 반복으로 건너뜀

### break

* if 와 break을 사용함
* break을 만날시 for 혹은 while문이 바로 종료됌.
* ![사진1](사진1 break 예시1.png)![사진2](사진2 break예시2.png)

### continue

* if와 continue를 사용
* continue를 만나면 하위 남은 조건문 내 코드를 모두 건너뛰고 다음반복이 됌.
* ![사진3](사진3 continue 예시.png)

#### 반복제어문의 주의 사항

* break과 continue를 남용하는 것은 코드의 가독성 저하
* 특정 종료조건을 만들어 break을 대신하거나 if문을 사용해 continue 대신 코드를 건너뛸 수 있음
* ![사진4](사진4 주의사항.png)
* expression은 새 리스트에 들어갈 항목들의 형태

## LIST Comprehension

* 간결하고 효율적인 **리스트** 생성 방법
* 1. [ ]
* 2. map+list( )

```py
# LIST Comprehension 구조
[expression for 변수 in iterable ]
list(expression for 변수 in iterable)

예시
# list comprehension
# 1. 1-10 까지 요소를 가지는 리스트 만들기
new_list = []
for i in range(1,11):
    new_list.append(i) # append 리스트의 값을 순차적으로 넣는 함수
print(new_list)

# 2. list comprehension
new_list2 = [i for i in range(1,11)]
print(new_list2)


# LIST Comprehension 구조
[expression for 변수 in iterable if 조건식]
list(expression for 변수 in iterable if 조건식)


# 1. 1-10 중 홀수 요소를 가지는 리스트 만들기
new_list = []
for i in range(1,11):
     if i % 2 ==1 :
        new_list.append(i) # append 리스트의 값을 순차적으로 넣는 함수
print(new_list)

# 2. list comprehension
new_list2 = [i for i in range(1,11) if i % 2 ==1 ]
print(new_list2)
```

#### 간결해지나 가독성이 떨어지기때문에 comprehension을 남용하지 말자

```py
# 리스트를 만드는 3가지 방법 비교
# 정수 1,2,3을 가지는 리스트 만들기
numbers = [ '1', '2', '3']
# 1. for 반복문
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# 2.map
new_numbers2 = list(map(int, numbers))
print(new_numbers2)

# 3. list comprehension
new_numbers3 = [int(number) for number in numbers]
print(new_numbers3)

```

### pass

* 아무 동작도 하지않고 넘어가는 역할
* 문법적으로는 문장이 필요하지만, 프로그램 실행에는 영향을 주지않아야 할 때 사용
* 1. 코드 작성중 미완성부분
* ![사진5](사진5 패스1.png)
* 2. 조건문에서 아무런 동작을 수행하지 않아야할때
* ![사진6](사진6 패스2.png)
* 3. 무한루프에서 조건이 충족되지 않을 때 pass하여 루프를 계속 진행하는 방법
* ![사진7](사진7 패스3.png)

### enumerate(iterable, start=0)

* iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
* ![사진8](사진8 enumerate.png)

```py
# enumerate
result = [ 'a', 'b', 'c']

print(enumerate(result)) # <enumerate object at 0x000002946EBBE680>
print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]

for index, elem in enumerate(result):
    print(index, elem)
# 0 a
# 1 b
# 2 c
```
