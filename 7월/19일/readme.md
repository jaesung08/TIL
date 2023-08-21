# 7.19 
## Functions 함수 = **특정 작업을 수행** 하기 위한 **재사용 가능한** 코드 묶음
* 재사용성이 높고, 코드의 가독성과 유지보수성이 향상
* 디버깅 하기 용이하다.

### 내장함수(built-in function) = 파이썬이 기본적으로 제공하는 함수
* 절대값 함수 abs( ) // sum // str // type // input // int 
* 출력함수 print( ) 등이 존재한다.
* 위처럼 함수를 실행하기 위해 함수의 이름을 사용하는것을 **함수 호출 (fuction call)** 이라 한다.

### 함수구조
* ![사진1](<사진1 함수구조.png>)
* def 하여 함수의 이름과 매개변수를 지정해주고, 
* return 하여 함수의 변수 계산 값을 지정해준다.
* 주석을 통해 함수에 대한 설명서를 작성해준다.

#### 함수 정의 
* def 키워드로 시작
* 이후 함수이름 작성
* 괄호안에 매개변수를 정의
    * 매개변수는 함수에 전달되는 값
* ![사진2](<사진2 함수정의.png>)

#### 함수 body
* def ~~ : 다음에 들여쓰기된 코드블록
* 함수가 실행될 때 수행되는 코드를 정의
* 주석을 이용해 설명을 선택적으로 작성가능
#### 함수 반환값
* return 을 이용해 필요할 경우 반환할 값을 명시할 수 있음
* 함수의 실행을 종료하고 호출부분으로 반환
* result가 None이 뜬다면 return을 작성하지 않은 것
* ![사진3](<사진3 함수body와 반환.png>)

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
* ![사진4](<사진4 매개변수와 인자 예시.png>)

#### 인자의 종류
* 위치인자 (positional Arguments)
    * 함수 호출시 인자의 위치에 따라 **반드시 전달** 해야 하는 인자
    * ![사진5](<사진5 위치인자.png>)
    * 함수의 필수 요소 name과 age의 윛에 놓인 alice와 25가 위치인자!!

* 기본 인자 값(Default Argument Values)
    * 함수 정의에서 매개변수에 기본값을 할당하는 것
    * 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됌
    * ![사진6](<사진6 기본인자.png>)
    * age =30 이 기본인자값이 된다. ( 밑에처럼 40을 넣지 않았기 때문)

* 키워드 인자 (keyword arguments)
    * 함수 호출시 인자의 이름과 함께 값을 전달하는 인자
    * 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당 가능.
    * 순서와 상관없이 인자의 이름을 명시해서 전달하는 것.
    * ![사진7](<사진7 키워드인자.png>)
    * name과 age의 순서와 상관없이 이름을 명시해서 전달하였다.
    * 위치인자와 함께 사용할 수 없다!!

* 임의의 가변인자 목록 ( Arbitrary                     )
    * 정해지지 않은 개수의 인자를 처리하는 인자
    * 함수 정의시 매개변수앞에 ( * ) 을 붙여서 사용하며, 여러개의 인자를 tuple로 처리한다.
    * ![사진8](<사진8 임의의 인자.png>)
    * 소괄호를 통해 튜플임을 알 수 있다.
    * 출력이 주석과같이 (1,2,3)이 나온다.

* 임의의 가변키워드인자 목록 
     * 정해지지 않은 개수의 키워드 인자를 처리하는 인자
     * 함수 정의시 매개변수 앞에 ( ** ) 를 붙여 사용.
     * 여러개의 인자를 dict로 묶어처리
     * ![사진9](<사진9 임의의 키워드 인자.png>)

    * 함수 인자 권장 작성순서
    * 위치 -> 기본 -> 가변 -> 키워드 -> 가변키워드
    * 호출 시 인자를 전달하는 과정에서 혼란을 줄이기 위함( 절대적인 규칙 X)
    * ![사진10](<사진10 함수 인자 권장순서.png>)

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
* ![사진11](<사진11 scope 범위.png>)
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
* ![사진12](<사진12 scope 예시 .png>)
* # 답에 대해 잘 이해하고 있기!!

### ' global ' 키워드
* 변수의 스코프를 전역범위로 지정하기 위해 사용
* 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
* ![사진13](<사진13 global키워드.png>)
* 함수내에서 num에 +1 하는 것때문에 global키워드 사용
* 권장하지 않으나 문제풀이때문에 사용하긴함.

* 주의사항
    * global키워드 선언전에 접근 X
    * ![사진14](<사진14 global주의사항.png>)
    * 매개변수에 global키워드 사용불가
    * ![사진15](<사진15 global주읫항.png>)
#### globla키워드는 가급적 사용하지않고, 함수로 값을 바꾸고자 한다면 인자로 넘기고 함수의 반환값을 사용하도록 권장

## 재귀함수 = 함수 내부에서 자기 자신을 호출하는 함수
* 특정 알고리즘식 표현시 변수의 사용이 줄고 코드의 가독성이 좋아짐
* 1개이상의 base case(종료되는 상황)이 존재하고 수렴하도록 작성
* 재귀함수의 예시로 팩토리얼이 있다
    * n! = n*(n-1)! = n*(n-1)*(n-2)! = . . .
* ![사진16](<사진16 재귀함수 팩토리얼.png>)
* ![사진17](<사진17 재귀함수 팩토리얼.png>)
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
--------------------------------------------------------------------------------------------
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
![사진18](<사진18 패키지 활용.png>)
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
