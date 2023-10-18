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
* ![사진1](<사진1 break 예시1.png>)![사진2](<사진2 break예시2.png>)

### continue
* if와 continue를 사용
* continue를 만나면 하위 남은 조건문 내 코드를 모두 건너뛰고 다음반복이 됌.
* ![사진3](<사진3 continue 예시.png>)

#### 반복제어문의 주의 사항
* break과 continue를 남용하는 것은 코드의 가독성 저하
* 특정 종료조건을 만들어 break을 대신하거나 if문을 사용해 continue 대신 코드를 건너뛸 수 있음
* ![사진4](<사진4 주의사항.png>)
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
* ![사진5](<사진5 패스1.png>)
* 2. 조건문에서 아무런 동작을 수행하지 않아야할때
* ![사진6](<사진6 패스2.png>)
* 3. 무한루프에서 조건이 충족되지 않을 때 pass하여 루프를 계속 진행하는 방법
* ![사진7](<사진7 패스3.png>)

###  enumerate(iterable, start=0) 
* iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
* ![사진8](<사진8 enumerate.png>)
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

