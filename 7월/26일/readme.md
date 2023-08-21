# 7.26
## Classes
### 객체 지향 프로그래밍(Object-Oriented Programming, OOP)
#### 절차 지향 프로그래밍
* 프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임
* C언어가 대표적인 예시
* '데이터'와 해당 데이터를 처리하는 '함수(절차)'가 분리되어 있으며, 함수 호출의 흐름이 중요
* 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
* ![사진1](<사진1 절차지향.png>)
* 실제로 시행되는 내용이 무엇이 무엇인가가 중요
* 데이터를 다시 재사용하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식
* ![사진2](<사진2 절차지향의 문제.png>)
* 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가하면서 소프트웨어에 발생한 충격

#### 객체 지향 프로그래밍 (Object Oriented Programming)
* 데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임
* 메서드를 하나의 객체로 묶어 관리하는 프로그래밍 패러다임
* ![사진3](<사진3 객체, 절차지향의 차이점.png>)
* ![사진4](<사진4 객체,절차지향의 차이점2.png>)
* 객체지향은 메서드(메서지)와 하나의 객체( 클래스 ) 
* 절차는 함수가 주체로 데이터를 다뤘다면, 객체는 데이터(객체)가 메서드를 소화시킨다.

### 객체
* ![사진5](<사진5 클래스.png>)
* 캐릭터, 전사, 마법사가 클래스. // 전사와 마법사는 캐릭터와 부모자식과 같은 클래스 사이
#### 클래스( Class )
* 파이썬에서 타입을 표현하는 방법
    * 객체를 생성하기 위한 설계도
    * 데이터와 기능을 함께 묶는 방법을 제공
#### 객체( Object )
* 클래스에서 정의한 것을 토대로 메모리에 할당된 것.
* **'속성'** 과 **'행동'** 으로 구성된 모든 것.

* ![사진6](<사진6 객체예시.png>)
* 정보는 변수, 동작은 메서드 라고 볼 수 있다.
* 이때 " 가수 " 가 클래스 라고 볼 수 있다.
* ![사진7](<사진7 클래스와 객체.png>)
* 클래스를 만든다 == 타입(list)를 만든다
```py
name = 'Alice'

print(type(name))  # <class 'str'>
```
* 변수 name의 타입은 str 클래스다.
* 변수 name은 str 클래스의 인스턴스 이다.
* 우리가 사용해왔던 데이터 타입은 모두 클래스
* 결국 문자열 타입의 변수는 str클래스로 만든 인스턴스다.
* '', 'hello', '파이썬'
    * 문자열타입(클래스)의 객체(인스턴스)

* [1, 2, 3], [1], [], ['hi']
    * 리스트타입(클래스)의 객체(인스턴스)

* "hello".upper( )
    * 문자열.대문자로( )
    * 객체.행동( )
    * 인스턴스.메서드( )

* [1, 2, 3].sort( )
    * 리스트.정렬해( )
    * 객체.행동( )
    * 인스턴스.메서드( )

* 하나의 객체(object)는 특정 타입의 인스턴스(instance)이다.
    * 123, 900, 5 ,12 는 모두 int의 인스턴스
    * 'hello', 'bye'는 모두 string의 인스턴스
    * [232, 89, 1], [] 은 모두 list의 인스턴스

#### 객체(object)의 특징
* 타입(Type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
* 속성(attribute) : 어떤 상태(데이터)를 가지는가?
* 조작법(method) : 어떤 행위(함수)를 할 수 있는가?ㄴ

* Python의 객체와 클래스
##### 객체(object) = 속성(attribute) + 기능(Method)

### 클래스
* 클래스의 구조
```py
# 클래스 정의
class Person:
    pass
# 인스턴스 생성 = 변수 생성
iu = Person()

# 메서드 호출
iu.메서드()

# 속성(변수) 접근
iu.attribute
```

* 클래스의 활용
```py
# 클래스 정의
class Person:
    # 속성(변수), 멤버 변수
    blood_color = 'red'

    # 메서드 # 중에서도 생성자 메서드(인스턴스를 만들면 호출 됌)
    def __init__(self, name) :# 개발자가 직접호출 XX 안해도됌
        self.name = name # 직접쓰지 않아도됌

    def singing(self): # self는 인스턴스 자신을 칭함.
        return f'{self.name}가 노래합니다'
    
# 인스턴스 생성
singer1 = Person('iu') # singer1이라는 인자가 필요함
singer2 = Person('BTS')

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)
print(singer2.blood_color)
```
* ![사진8](<사진8 클래스활용1.png>)![사진9](<사진9 클래스활용2.png>)![사진10](<사진10 클래스활용3.png>)
#### 인스턴스와 클래스 간의 이름공간(namespace)
* 클래스를 정의하면, 클래스와 해당하는 이름공간 생성
* 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름공간 생성
* 인스턴스에서 특성 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색.
* ![사진12](%EC%82%AC%EC%A7%8412.png)

```py
# Person 정의
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()  # unknown // self. name이 없어 클래스로 찾아감.
# 자신의 이름공간이 없어서 클래스의 이름공간을 찾아감

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk() # unknown

p2.name = 'kim'
p2.talk() # Kim

print(Person.name) #unknown
print(p1.name) #unknown
print(p2.name) # kim
```
* p1은 인스턴스 변수가 정의되지 않아 클래스 변수(unknown)이 출력됨
* p2는 인스턴스 변수가 정의되어 인스턴스 변수(Kim)이 출력됨
* Person 클래스의 값이 Kim으로 변경된 것이 아닌 p2 인스턴스의 이름공간에 name이 Kim으로 저장됨.

* 독립적인 이름공간을 가지는 이점.
    * 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근 불가능.
    * 객체 지향 프로그램의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화하고 각각의 객체가 독립적으로 동작하도록 보장.
    * 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음.
    * 코드의 가독성, 유지보수성, 재사용성을 높이는 데 도움을 줌.

### 클래스 변수 활용
* 인스턴스가 생성될 때 마다 클래스 변수가 늘어나도록 설정할 수 있음.
* ![사진13](<사진13 클래스변수 활용.png>)

* 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경.
* ![사진14](<사진14 클래스변수활용2.png>)
```py
# 클래스 변수의 활용
class Person():
     count = 0 #클래스 변수

     def __init__(self, name):
          self.name = name
          Person.count +=1
          
# 인스턴스를 생설할 떄 마다 count가 1씩 증가
person1 = Person('에스파')
person2 = Person("BTS")

print(Person.count)
```
### 메서드
* 인스턴스 메서드 = 우리가 배운 함수(메서드) // 인스턴스.메서드
* 클래스 메서드 // 클래스.메서드
* 정적 메서드

#### 인스턴스 메서드(instance method)
* 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
    * 인스턴스의 상태를 조작하거나 동작을 수행 
    * [1,2,3].append => list클래스의 인스턴스 메서드 .append

##### 인스턴스 메서드 구조
* 클래스 내부에 정의되는 메서드의 기본
* 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달 받음 
    * 그저 하나의 함수이며, 인스턴스 메서드의 가장 기본적인 설정으로 쓸 수 있지만 쓰지 않는다. 
    * 만약 인스턴스 메서드를 만든다면, self를 첫번째에 두어야 한다.
```py
class MyClass:

    def instance_method(self, arg1, ... ):
         pass
```
##### self동작원리
* upper메서드를 사용해 문자열을 대문자로 변경하기
```py
#인스턴스.메서드() // 이 형태가 아래의 축약형
'abc'.upper() 

#클래스.메서드(인스턴스 자기자신) // 두개는 같은 형식
str.upper('abc') 
```
* 실제 내부에선 하위 형식 처럼 동작이 이루어진다.
* str클래스가 upper를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것이다.
* **인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유**

* 위의 .upper()는 str.upper의 객체지향방식으로 단축한 호출표현이다.
* 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자가 아닌, 객체 스스로 메서를 호출하여 코드를 동작하는 객체 지향적 표현.

##### 생성자 메서드(Constructor method)
* 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
    * 인스턴스 변수들의 초기값을 설정.
* 생성자 메서드의 구조
* ![사진15](<사진15 생성자 메서드.png>)
* 실습해보기
```py
######객체. 메서드()
'abc'.upper()
# 인스턴스는 객체와 같은말
# 객체만 지칭할 때는 겍체, 클래스와 연관지어 부를때는 인스턴스
# 인스턴스.메서드()


class Person:
    name = 'kai' # 클래스 변수 == 멤버변수

#실습1. 클래스 변수에 접근하여 kai를 출력해보세요.
kai = Person() #1. 인스턴스 생성.
print(kai.name) #2. 클래스 변수 호출. (인스턴스.클래스변수)


class Person:
    def say(self): #인스턴스 메서드
        print("welcome.")

#실습2. say()메서드를 호출해 보세요.
kai = Person() # 인스턴스 생성
kai.say() # 인스턴스 메서드 호출


class Person:
    def __init__(self, name): # 생성자 함수
        self.name = name #인스턴스 변수

    def say(self): #인스턴스 메서드
        print(f'Welcome. {self.name}')

#실습3. say()메서드를 호출해 보세요.
kai = Person("kai")
kai.say()


클래스 -> car
객체 -> Hyundai, Kia, Ssangyong

class Car:
    model =  "sonata" #클래스 변수= 멤버변수
    color = "white"

    def speedchange(self, v):  # 인스턴스 메서드
        print(f"speed : {v}")
        self.speed = v

# Sonata 출력, white 출력, speed : 80 출력
A = Car() 
print(A.model) # sonata
print(A.color) # white
A.speedchange(80) # speed : 80


# ----> 생성자 메소드 구조로 바꾸기 // 생성자 함수를 쓰면서 구조가 바뀜
# # Sonata 출력, white 출력, speed : 80 출력
class Car: 
    def __init__(self, name, model, color, speed) : #생성자 함수
        self.name = name #인스턴스 변수
        self.model = model
        self.color = color
        self.speed = speed

    def info(self):
        print(f'Hi {self.name} model : {self.model}, color : {self.color}, speed : {self.speed}')


hyundai = Car('A', 'sonata', 'white', 80) # 인스턴스 = 클래스명()
hyundai.info() # 인스턴스.메서드



# 생성자 구조로 객체예시 짜보기
class Singer :
    def __init__(self, name, job, birth, country):  #생성자 함수
        self.name = name  # 인스턴스 함수
        self.job = job
        self.birth = birth
        self.country = country

    def rap(self):  #인스턴스 메서드
        print(f'안녕하세요 저는 {self.name} 입니다. 제 직업은 {self.job}이며, 국적은 {self.country}입니다.')  

    def dance(self):
        print(f'(춤 추는 중)') 
    
    def sing(self):
        print(f'소몰이')

A = Singer('진호', '가수', '1995.04.05', '한국')
A.rap()
A.dance()
A.sing



class Singer :
    def __init__(self):
        self.occ = "가수"
        self.birth = "1985년 5월 15일"
        self.nat = "대한민국"

    def rap(self):
        print("랩하는중")

    def dance(self):
        print("댄스")

    def sing(self):
        print("소몰이 창법")

# 인스턴스 생성, 인스턴스 속성 출력, 인스턴스 메서드 호출
Asinger = Singer()
print(f"직업 : {Asinger.occ}")
print(f"생년월일 : {Asinger.birth}")
print(f"국적 : {Asinger.nat}")
Asinger.rap()
Asinger.dance()
Asinger.sing()
```
#### 클래스 메서드( class method )
* 클래스가 호출하는 메서드
    * 클래스의 변수를 조작하거나, 클래스 레벨의 동작 수행.

##### 클래스 메서드 구조
* @classmethod 데코레이터를 사용하여 정의
* 호출시, 첫번째 인자로 호출하는 클래스(cls)가 전달됨.
```py
class MyClass :

    @classmethod # 데코레이터로 클래스 메서드로 기능한다는 뜻으로 붙임
    def class_method(cls, arg1, ...)" # 호출하는 cls가 첫번째 인자로 사용
         pass
```
* ![사진16](%EC%82%AC%EC%A7%8416.png)

```py
# 클래스 메서드로 변환
class Singer :
    occ = "가수"
    birth = "1985년 5월 15일"
    nat = "대한민국"

    @classmethod
    def rap(cls):
        print("랩하는중")

    @classmethod
    def dance(cls):
        print("댄스")

    @classmethod
    def sing(cls):
        print("소몰이 창법")

# 인스턴스 생성, 인스턴스 속성 출력, 인스턴스 메서드 호출
Asinger = Singer()
print(f"직업 : {Asinger.occ}")
print(f"생년월일 : {Asinger.birth}")
print(f"국적 : {Asinger.nat}")
Asinger.rap()
Asinger.dance()
Asinger.sing()
```

#### 스태틱 메서드( static method)

* 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
    * 주로 클래스와 관련이 있지만, 인스턴스와 상호작용이 필요하지 않은 경우에 사용
##### 스태틱 메서드 구조
* @staticmethod 데코레이터를 사용하여 정의
* 호출시, 필수적으로 작성해야할 매개변수가 없음.
* 즉, 객체상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용
```py
class MyClass :

    @staticmethod # 데코레이터로 스태틱 메서드로 기능한다는 뜻으로 붙임
    def static_method(arg1, ...)" # 호출하는 필수 매개변수가 없음.
         pass
```
```py
# 스태틱 메소드로 변환
class Singer :
    occ = "가수"
    birth = "1985년 5월 15일"
    nat = "대한민국"

    @staticmethod
    def rap():
        print("랩하는중")

    @staticmethod
    def dance():
        print("댄스")

    @staticmethod
    def sing():
        print("소몰이 창법")
# 인스턴스 생성, 인스턴스 속성 출력, 인스턴스 메서드 호출
Asinger = Singer()
print(f"직업 : {Asinger.occ}")
print(f"생년월일 : {Asinger.birth}")
print(f"국적 : {Asinger.nat}")
Asinger.rap()
Asinger.dance()
Asinger.sing()
```

### 메서드 정리
* 인스턴스 메서드
    * 인스턴스 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행// self 

* 클래스 메서드
    * 인스턴스의 상태에 의존하지 않는 기능을 정의// cls
    * 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

* 스태틱 메서드
    * 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행


##### 각자의 역할
* 클래스가 사용해야 할 것
    * 클래스 메서드
    * 스태틱 메서드

* 인스턴스가 사용해야 할 것
    * 인스턴스 메서드 // 구조상 나머지 두 메서드를 호출을 가능하긴하나 하면 안됌.

```py
class MyClass:

    def instance_method(self):
        return 'instance method', self #self 사용

    @classmethod
    def class_method(self):
        return 'class method', cls #cls사용

    @staticmethod
    def static_method():
        return 'static method' #아무것도 사용x
```

* 클래스는 모든 메서드를 호출할 수 있다.
     * 그러나 클래스는 클래스와 스태틱 메서드만 사용하도록한다.
* 인스턴스는 모든 메서드를 호출할 수 있다.
    * 그러나 인스턴스는 인스턴스 메서드만 사용하도록 한다.

* => 기능상 가능하나 유지보수와 여러가지를 따졌을 때 올바른 메서드만 사용하는 것이 옳다.
     * 가능하다고 써도된다는 것은 아님.

## 참고
### 매직 메서드
* 특별한 인스턴스 메서드
* 특정상황에서 자동으로 호출되는 메서드
*Double underscore( _ _ ) 가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
     * 스페셜 메서드 혹은 매직 메서드라 칭함
* ![사진17](<사진17 매직메서드.png>)
* __init__ =  인스턴스를 호출할 때 자동으로 반드시 처음에 호출되는 특수한 함수
* __str__ = 문장열 반환기능!!
```py
# 매직 메서드 실습
class Circle :

    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14* self.r * self.r
    
    def __str__(self):
        return f'[원] radius {self.r}'
    
c1 = Circle(10)
c2 = Circle(5)

print(c1)
print(c2)
```
### 데코레이터(Decorator)
* 다른 함수의 코드를 유지한채로 수정하거나 확장하기 위해 사용되는 함수
* ![데코레이터](<사진18 데코레이터.png>)
* 따로 직접쓸일 없으니 알고만 있자.
```py
# 데코레이터 실습
def my_decorator(func):
    def wrapper():
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()

        print("함수 실행 후")
        return result
    return wrapper

# 데코레이터 적용

@my_decorator
def my_function():
    print("원본함수 실행")
my_function()
```
### 객체지향은 절차지향의 대조되는 것이 아니라 절차지향을 기반으로 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성등의 이점을 가지는 패러다임.