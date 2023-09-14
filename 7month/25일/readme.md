# 7.25 
## 데이터구조2
### 비시퀸스 데이터구조
#### 세트 메서드
* set = 고유한 항목들의 정렬되지 않은 컬렉션

* .add(x)
    * 세트에 x를 추가
```py
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # {1, 2, 3, 4}

# 중복이 안되는 것을 잊지말기
```

* .clear
    * 세트의 모든 항목을 제거
```py
my_set = {1, 2, 3}
my_set.clear
print(my_set) # set( )
```

* .remove(x)
    * 세트에서 항목 x를 제거
```py
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set) # {1, 3}

my_set.remove(8)
print(my_set) # keyError
```


* .discard(x)
    * 세트 s에서 항목x를 제거. remove와 달리 없는 요소를 넣어도 에러가 없음
```py
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set) # {1, 3}

my_set.discard(8)
print(my_set) 
```

* .pop( )
    * 세트에서 임의의 요소를 제거하고 반환 // 해시테이블 상에 나타나는 순서대로 반환,
    * 순서나 규칙이 있는 것은 아니지만 해시테이블내의 순서이기에 임의는 맞으나 랜덤은 아니라고 할 수 있다.
```py
my_set = {1, 2, 3}
element = my_set.pop( )

print(element) # 1
print(my_set) # {2, 3}
```

* .update(iterable)
    * 세트에 다른 iterable 요소를 추가 
    * iterable = 반복가능한 데이터(객체)
```py
my_set = {1, 2, 3}
my_set.update([4,5,6,1])
print(my_set) #{1, 2, 3, 4, 5, 6}
```

### 세트의 집합 메서드

* set1.difference(set2) // set1 - set2 // 차집합
    * set1 에는 들어 있지만 set2에는 없는 항목으로 세트를 생성 후 반환
* set1.intersection(set2) // set1 & set2 // 교집합
    * set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환
* set1.issubset(set2) // set1 <= set2 // 부분집합으로 완전히 속할 때
    * set1의 항목이 모두 set2에 들어있으면 True를 반환
* set1.issuperset(set2) // set1 >= set2 // 부분집합으로 완전히 속할 때
    * set1가 set2의 항목을 모두 포함하면 True를 반환
* set1.union(set2) // set1 | set2 // 합집합
    * set1 또는 set2에(혹은 둘다) 들어있는 항목으로 세트를 생성 후 반환
* ![사진1](<사진1 세트 집합 메서드.png>)

#### 실습 해보기
```py
# SET = 가변형 비시퀀스(중복x) = 집합과 같은 특징

list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8, 9]
set1 = set(list1)
set2 = set(list2)

#1. set1에 4추가
set1.add(4)
print(set1)
#2. set1에 5,6,7 추가
set1.update([5,6,7])
print(set1)
#3. set1에 7제거 (2가지 방법)
set1.remove(7)
print(set1)
set1.discard(7)
print(set1)
#4. set1 차집합 set2 출력(2가지 방법)
print(set1-set2)
print(set1.difference(set2))
#5. set1 교집합 set2 출력(2가지 방법)
print(set1&set2)
print(set1.intersection(set2))
#6. set1 합집합 set2 출력(2가지 방법)
print(set1|set2)
print(set1.union(set2))

# set1.pop() => 주소값이 작은 것 부터 제거
print(id(1))
print(id(2))
print(id(3))
print(id(4))
print(set1.pop())
print(set1.pop())
print(set1.pop())
print(set1.pop())
print(set1)


```


### 딕셔너리 메서드
* dictionary = 고유한 항목들의 정렬되지 않은 컬렉션

* D.clear( )
    * 딕셔너리 D의 모든 키/ 값 쌍을 제거
```py
person = { 'name' : 'Alice', 'age' : 25}
person.clear()
print(person) # { }
```

* .get(key[ ,default])
    * 키 연결된 값을 반환하거나 키가 없으면 None혹은 기본 값을 반환

```py
person = { 'name' : 'Alice', 'age' : 25}

print(person.get('name')) # Alice
print(person.get('country')) # None
print(person.get('country', 'Unknown')) # unknown
```

* .keys()
    * 딕셔너리 키를 모은 객체를 반환
```py
person = { 'name' : 'Alice', 'age' : 25}

print(person.keys()) # dict_keys(['name', 'age'])

for k in person.keys():
    print(k)
'''
name
age
'''
```

* .values( )
    * 딕셔너리 값을 모은 객체를 반환
```py
person = { 'name' : 'Alice', 'age' : 25}
print(person.keys()) # dict_keys(['name', 'age'])

for v in person.values():
    print(v)
'''
Alice
25
'''
```

* .items()
    * 딕셔너리 키/값 쌍을 모은 객체를 반환
```py
person = { 'name' : 'Alice', 'age' : 25}

print(person.items()) # dict_items([('name','Alice') , ('age', 25 )])
for k, v in person.items():
    print(k, v)
'''
name Alice
age 25
'''
```


* .pop(key[ ,default])
    * 키를 제거하고 연결됐던 값을 반환 ( 없으면 에러나 default 반환)
```py
person = { 'name' : 'Alice', 'age' : 25}

print(person.pop('age')) # 25
print(person) # {'name': 'Alice'}
print(person.pop('country', None)) # None
print(person.pop('country')) # keyError

```

* .setdefault(key[ ,default]) // get과 비슷하나 다름
    * 키와 연결된 값을 반환, 키가 없다면 default와 연결환 키를 딕셔너리에 추가하고 default를 반환
    * 조건문반환 시 유용?
```py
person = { 'name' : 'Alice', 'age' : 25}

print(person.setdefault('country','KOREA')) # KOREA
print(person.setdefault('age', 50)) # 이렇게 하여도 25가 출력. 키가 없을시에만 가능
print(person) #  { 'name' : 'Alice', 'age' : 25, 'country' : 'KOREA' }
```

* .update([other])
    * other가 제공하는 키/값 쌍으로 딕셔너리를 갱신, 기존 키는 덮어씀
```py
person = { 'name' : 'Alice', 'age' : 25}
ohter_person = { 'name' : 'Jane', 'gender' : 'Female'}

person.update(ohter_person)
print(person) #  { 'name' : 'Jane', 'age' : 25, 'gender' : 'Female'}

person.update(age = 50)
print(person) #  { 'name' : 'Jane', 'age' : 50, 'gender' : 'Female'}

person.update(country = 'KOREA')
print(person) #  { 'name' : 'Jane', 'age' : 50, 'gender' : 'Female', 'country' : 'KOREA'}
# 많은 양의 정보도 추가할 수 있다.
```

## 비슷한 메서드 활용
```py
blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']

# []
new_dict = {}
for blood_type in blood_types : # blood_type을 순회
    if blood_type in new_dict : # 기존에 키가 존재한다면
        new_dict[blood_type] +=1 # 기존에 키의 값을 1 증가
    else :                      #
        new_dict[blood_type] = 1 # 키가 존재하지않는다면
print(new_dict)


# .get()
new_dict = {}
for blood_type in blood_types : # blood_type을 순회
    new_dict[blood_type] = new_dict.get(blood_type, 0) +1
print(new_dict)

# .setdefault()
new_dict = {}
for blood_type in blood_types : # blood_type을 순회
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
print(new_dict)


#Counter 매서드를 활용하여 실습
from collections import Counter
result = Counter(blood_types)
print(result) # Counter({'A': 3, 'B': 3, 'O': 3, 'AB': 3})
```


#### 딕셔너리 실습해보기
```py
# 딕셔너리 영한 사전 실습
my_dict = {
    'plus':['더하기','장점'],
    'minus':['빼기','적자'],
    'multiply':['곱하기','다양하게'],
    'division':['나누기','분열']
}
#1. 영어단어를 입력하면 단어의 뜻을 보여주는 프로그램 (2가지 방법)
print(my_dict.get(input()))
print(my_dict.setdefault(input()))
print(my_dict[input()])
#2. 영한사전에서 단어들의 목록을 출력
print(my_dict.keys())
for k in my_dict.keys():
    print(k)
# 3. 다음 단어와 뜻을 추가하고, 사전에 있는 모든 단어와 뜻을 출력(3가지 방법)
# square, 제곱,사각형
new_dict = {'square' : '제곱'}
my_dict.update(new_dict)
# or
my_dict.update(square = '제곱')

my_dict['square'] = ['제곱','사각형']

my_dict.setdefault('suqare',['제곱','사각형'])

print(my_dict)
print(my_dict.items())

#4. 입력받은 단어와 뜻을 삭제하는 프로그램 작성(2가지 방법)
my_dict.pop(input())
print(my_dict)

del my_dict[input()]
print(my_dict)
```


## 데이터 타입과 복사
* 변경 가능한 데이터 타입 과 변경 불가능한 데이터 타입에 따라 복사가 달라짐.

* 가변 데이터 타입
* ![사진2](<사진2 가변데이터타입복사.png>)

* 불변 데이터 타입
* ![사진3](<사진3 불변데이터타입복사.png>)

### 복사유형
* 할당
* 앝은복사
* 깊은복사

#### 할당
* ![사진4](<사진4 할당예시.png>)
* ![사진5](<사진5 할당 원리.png>)
* 객체에 대한 객체 참조를 복사하기 때문이다!

#### 앝은 복사
* 슬라이싱 혹은 copy를 통해 객체는 원본 객체와 독립적으로 존재한다.
```py
# 얕은복사
a=[1,2,3]
# 슬라이싱
b = a[:]
b[0] = 100
print(a,b) # [1,2,3] [100,2,3]

# copy
c = a.copy()
c[0] = 100
print(a,c) # [1,2,3] [100,2,3]
```

* 얕은 복사의 한계
* 객체 안에 가변객체가 있을 경우, a,b 혹은 a,c와 주소는 다르지만 내부 객체의 주소가 같아 함께 변경된다.
```py
# 얕은복사의 한계
# 슬라이싱
a= [1,2,[1,2]]

b= a[:]
b[2][0] = 999
print(a,b) # [1, 2, [999, 2]] [1, 2, [999, 2]]

# copy
c = a.copy()
c[2][0] = 999
print(a,c) # [1, 2, [999, 2]] [1, 2, [999, 2]]
```

#### 깊은복사
* 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 한다.
```py
# 깊은복사
import copy

original_list = [1,2,[1,2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999
print(original_list, deep_copied_list) #[1, 2, [1, 2]] [1, 2, [999, 2]]
```