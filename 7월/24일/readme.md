# 7.24

## 데이터 구조( data Structure )
* 여러 데이터를 효과적으로 사용 및 관리하기 위한 구조(str, list, dict 등)

### 자료구조
* 데이터 구조와 동일한 뜻으로 각 데이터의 효율적인 저장, 관리를 위해서 구조를 나눠놓은것
* ![사진1](<사진1 자료구조.png>)
* 각 데이터 구조의 **메서드** 를 호출하여 다양한 기능 활용하기

### 메서드(method)
* 객체에 속한 함수
    * => 객체의 상태를 조작하거나 동작을 수행
* 저번주에 배운 def과 똑같은 내용이나 그 함수는 global scope라면, method는 객체에 속한 함수

#### 메서드의 특징
* 메서드는 클래스(class) 내부에 정의되는 함수
* 클래스는 파이썬에서 " 타입을 표현하는 방법 " 이며 이미 은연중에 사용해 왔음.
* 예를 들어 help 함수를 통해 str을 호출해보면 class였다는 것을 알 수 있다.
* 메서드는 어딘가(클래스)에 속한 함수이며, 데이터 타입별로 다양한 기능을 가진 메서드 가 존재.
```py
print(help(list)) # 설명이 쭉 나옴

# bash에서 python 파일명.py로 실행하기
# 밑에 내용이 주르륵 나오면 q를 눌러 탈출.
```
#### 메서드 호출 방법
* 데이터 타입 객체.메서드()
* 'hello'.capitalize()
```py
# 메서드 호출 예시
# 문자열
print('hello'.capitalize()) # Hello

# 리스트
numbers = [1,2,3]
numbers.append(4) 
print(numbers) # [1, 2, 3, 4]
```

## 시퀀스 데이터 구조 (sequence data Structure)
* 시퀀스 = 순서대로 나열하여 저장하는 자료형
### 문자열 조회,탐색 및 검증 메서드

* s.find(x) = x의 첫번째 위치를 반환. 없으면 -1을 반환 // 이 중 자주 씀
```py
print('banana'.find('a')) # 1
print('banana'.find('z')) # -1
```
* s.index(x) = x의 첫번째 위치를 반환. 없으면 오류발생 // find 다음 자주씀
```py
print('banana'.find('a')) # 1
print('banana'.find('z')) # ValueError: 
```
* s.isalpha() = 알파벳 문자 여부(유니코드 상 문자)
```py
string1 = 'Hello'
string2 = '123'
print(string1.isalpha()) #True
print(string2.isalpha()) #False
string3= 'abc1234acv'
print(string3.isalpha()) #False
```
* s.isupper() = 모두 대문자 여부
* s.islower() = 모두 소문자 여부
```py
string1 = 'Hello'
string2 = 'hello'
print(string1.isupper()) # True
print(string2.isupper()) # False
print(string1.islower()) # False
print(string2.islower()) # False
```
* s.istitle() = 타이틀 형식 여부
문자열이 제목 케이스 문자열이고 하나 이상의 문자가 있는 경우 True를 돌려줍니다. 예를 들어 대문자 앞에는 케이스 없는 문자만 올 수 있고 소문자는 케이스 문자 뒤에만 올 수 있습니다. 그렇지 않은 경우는 False를 돌려줍니다.
```py
'Hello world'.title()
'Hello World'
print('Hello World'.istitle()) # True
```
#### Python Documentation를 구글에 검색해서 라이브러리 확인
[파이썬 도큐멘터리](https://docs.python.org/ko/3/library/index.html)

### 문자열 조작 메서드

* .replace(old, new[ ,count])   // 대괄호는 파이썬 문법이 아니라 코딩에서 ebnf표기법을 사용해서 나타냄(헷갈리지 않게 알고있기를), 여기서는 선택인자로 사용되었음!! 공식문서(파이썬 도큐멘터리)에서 확인 후 필요하면 사용
    * 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
```py
text = 'Hello, world!'
new_text = text.replace('world', 'Python')
print(new_text) # Hello, Python!
```

* .strip([chars])
    * 문자열 양 끝의 공백 혹은 지정문자를 제거
```py
text ='        Hello, world!        '
new_text = text.strip()
print(new_text) # 'Hello, world!'
```

* .split( sep=None, maxsplit =1 ) // 중요함
    * 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
```py
text = 'Hello, world!'
words = text.split(',')
print(words) # ['Hello', 'world!']
```

* 'separator '.join([iterable]) // 중요함
    * iterabel 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결

```py
words = ['Hello', 'Python!']
text = '-'.join(words)
print(text) # 'Hello-world!'
```


### 실습해보기
```py
a= "practice makes perfect"

#1. 문자열 a에서 'e의 갯수세기
print(a.count('e'))
#2. 문자열 a에서 'i'의 위치찾기 (2가지)
print(a.index('i')) # 'i'가 존재하지 않으면 에러
print(a.find('i')) # 'i가 존재하지 않으면 -1 리턴 // 보통 문제에서 이거 많이씀!!
#3. 문자열a 의 문자사에이 .(점) 삽입
print('.'.join(a))
#4  문자열 a를 공백 기준으로 분리하여 출력 -> 리시트로 출력
print(a.split())
#5  문자열 a에서 ' makes'를 'made'로 바꿔서 출력
print(a.replace('makes','made'))
#6 문자열 a를 대문자와 소문자로 변환하여 출력
print(a.upper())
print(a.lower())
#7 문자열 a에서 양쪽 공백 삭게하기
print(a.strip())

# 더 궁금하면 ctrl누르고 메서드 클릭하기   

# 대문자 A의 아스키코드 56
# 소문자 a의 아스키코드 64
```

* 이외 추가적인 메서드
* ![사진2](<사진2 문자열 메서드 추가.png>)
* 메서드는 이어서 사용가능하다!
* ![사진3](<사진3 메서드는 연속사용가능.png>)

- - -
- - -
- - -
### 리스트 값 추가 및 삭세 메서드

* .append(x)  // 중요함
     * 리스트 마지막에 항목 x를 추가
'''py
my_list = [1,2,3]
my_list.append(4)
print(my_list) # [1,2,3,4]
'''

* .extend(ilterable) // 중요함
    * 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
```py
numbers = [1,2,3]
numbers2 = [4,5,6]
# print(numbers.append(numbers2))
# print(numbers.extend(numbers2))
# 두가지는 원본은 변경하기때문에 None이 출력된다.

numbers.append(numbers2)
print(numbers) #[1,2,3,[4,5,6]]
#or 
numbers.extend(numbers2)
print(numbers) #[1,2,3,4,5,6]
```

* .insert(i, x)
    * 리스트의 지정한 인덱스 i위치에 항목 x를 삽입
```py
my_list = [1,2,3]
my_list.insert(1,5)
print(my_list) #[1, 5, 2, 3]
```

* .remove(x)
    * 리스트에서 첫 번째로 일치하는 항목을 삭제
```py
my_list = [1,2,3]
my_list.remove(2)
print(my_list) # [1,3]
```

* .pop(i) // 중요함
    * 리스트에서 지정한 인덱스의 항목을 제거하고 **반환** , 작성하지 않을 경우 마지막 항목을 제거
```py 
my_list = [1,2,3,4,5]

item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2,3,4]
```

* .clear()
     * 리스트의 모든 항목 삭제
```py 
my_list = [1,2,3,4,5]
my_list.clear()

print(my_list)  # []
```

### 리스트 탐색 및 정렬 메서드

* .index(x)
    * 리스트에서 첫 번째로 일치하는 항목의 **인덱스**를 반환
```py 
my_list = [1,2,3,4,5]
index = my_list.index(2)

print(index)  # 1 // 인덱스번호가 출력된것임.
```

* .count(x)
    * 리스트에서 항목 x가 등장하는 횟수를 반환
```py 
my_list = [1,2,2,3,3,3]
count = my_list.count(3)

print(count)  # 3
```

* .sort() // 좀 중요
    * 원본리스트를 오름차순으로 정렬
```py 
my_list = [3, 2, 1]
my_list.sort()
print(my_list) # [1,2,3]

# 내림차순
my_list.sort(reverse=True)
print(my_list) # [3,2,1]
```
```py
numbers =[1,3,5,4,2,6]
# sort 메서드 // 정렬 하는 것은 같음.
print(numbers.sort()) # None
# sorted 함수 // 반환이 있다. 원본이 바뀌지 않았기때문에 출력 가능
print(sorted(numbers)) #[1,2,3,4,5,6]
print(numbers) #[1,3,5,4,2,6]
```

* .reverse( ) // 좀 중요
    * 리스트의 순서를 역순으로 변경(정렬 XXX)
```py
my_list = [1, 3, 1, 8, 2, 9]
my_list.reverse( )
print(my_list) # [9, 2, 8, 1, 3, 1]
```


## 실습해보기
```py
# 리스트 메서드 실습
a = ['b','a','n','a','n']
# 반환하지 않는 메서드 = 원본은 변경
#1. 리스트 a의 마지막에 'a'추가하기
a.append('a')
print(a)
#2. 리스트 a를 오름차순으로 정렬. a출력(원본변경)
a.sort()
print(a)
#2-1. 오름차순 정렬 (원본변경x)
print(sorted(a))
#3. 리스트 a를 내림차순으로 정렬. a출력
a.sort(reverse=True)
print(a)
#4. 리스트 a를 역순으로 뒤집기. a출력
a.reverse()
print(a)
#5. 리스트 a에서 문자 'a' 삭제하기. a출력
a.remove('a')
print(a)

# 반환하는 메서드 = 대부분 원본 변경 XX
#6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 삭제한 요소 출력
print(a.pop())
#7. 리스트 a에서 문자 'n'의 개수를 출력
count = a.count('n')
print(count)
```



### 추가 참고 메서드
* .isdecimal( )
    * 문자열이 모두 숫자문자로(0~9)로만 이루어져 있어야 True
* .isdigit( )
    * isdeciaml()과 비슷하지만, 유니코드 숫자도 인식('①'도 숫자로 인식)
* .isnumeric( )
    *  isdigit( ) 과 유사하지만, 몇가지 추가적인 유니코드 문자들을 인식( 분수, 지수, 루트기호도 숫자로 인식)
* ![사진4](<사진4 참고용 메서드.png>)

* 원본과 복사본 차이 주의
```py
numbers =[1,3,5]
# 1. 할당
list1 = numbers

# 2. 슬라이싱
list2 = numbers[ : ]
numbers[0] = 100

print(list1) #[100,3,5] // numbers의 주소를 참조하기 때문에 똑같아 짐
print(list2) #[1,3,5] //슬라이싱 했기때문에 numbers와는 다른 새로운 주소(복사본)가 생성됌.
```

### 반환하는 메서드인지 아닌지가 중요함!








