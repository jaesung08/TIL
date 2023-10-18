# # 클래스 정의
# class Person:
#     pass
# # 인스턴스 생성 = 변수 생성
# iu = Person()

# # 메서드 호출
# iu.메서드()

# # 속성(변수) 접근
# iu.attribute



# # 클래스 정의
# class Person:
#     # 속성(변수)
#     blood_color = 'red'

#     # 메서드 # 중에서도 생성자 메서드(인스턴스를 만들면 호출 됌)
#     def __init__(self, name) :# 개발자가 직접호출 XX 안해도됌
#         self.name = name # 직접쓰지 않아도됌

#     def singing(self): # self는 인스턴스 자신을 칭함.
#         return f'{self.name}가 노래합니다'
    
# # 인스턴스 생성
# singer1 = Person('iu') # singer1이라는 인자가 필요함
# singer2 = Person('BTS')

# # 메서드 호출
# print(singer1.singing())
# print(singer2.singing())

# # 속성(변수) 사용
# print(singer1.blood_color)
# print(singer2.blood_color)



# # Person 정의
# class Person:
#     name = 'unknown'

#     def talk(self):
#         print(self.name)

# p1 = Person()
# p1.talk()  # unknown // self. name이 없어 클래스로 찾아감.
# # 자신의 이름공간이 없어서 클래스의 이름공간을 찾아감

# # p2 인스턴스 변수 설정 전/후
# p2 = Person()
# p2.talk() # unknown

# p2.name = 'kim'
# p2.talk() # Kim

# print(Person.name) #unknown
# print(p1.name) #unknown
# print(p2.name) # kim



# #인스턴스.메서드() // 이 형태가 아래의 축약형
# 'abc'.upper() 

# #클래스.메서드(인스턴스 자기자신) // 두개는 같은 형식
# str.upper('abc') 



######객체. 메서드()
'abc'.upper()
# 인스턴스는 객체와 같은말
# 객체만 지칭할 때는 겍체, 클래스와 연관지어 부를때는 인스턴스
# 인스턴스.메서드()


# class Person:
#     name = 'kai' # 클래스 변수 == 멤버변수

# #실습1. 클래스 변수에 접근하여 kai를 출력해보세요.
# kai = Person() #1. 인스턴스 생성.
# print(kai.name) #2. 클래스 변수 호출. (인스턴스.클래스변수)


# class Person:
#     def say(self): #인스턴스 메서드
#         print("welcome.")

# #실습2. say()메서드를 호출해 보세요.
# kai = Person() # 인스턴스 생성
# kai.say() # 인스턴스 메서드 호출


# class Person:
#     def __init__(self, name): # 생성자 함수
#         self.name = name #인스턴스 변수

#     def say(self): #인스턴스 메서드
#         print(f'Welcome. {self.name}')

# #실습3. say()메서드를 호출해 보세요.
# kai = Person("kai")
# kai.say()


# 클래스 -> car
# 객체 -> Hyundai, Kia, Ssangyong

# class Car:
#     model =  "sonata" #클래스 변수= 멤버변수
#     color = "white"

#     def speedchange(self, v):  # 인스턴스 메서드
#         print(f"speed : {v}")
#         self.speed = v

# # Sonata 출력, white 출력, speed : 80 출력
# A = Car() 
# print(A.model) # sonata
# print(A.color) # white
# A.speedchange(80) # speed : 80


# # ----> 생성자 메소드 구조로 바꾸기 // 생성자 함수를 쓰면서 구조가 바뀜
# # # Sonata 출력, white 출력, speed : 80 출력
# class Car: 
#     def __init__(self, name, model, color, speed) : #생성자 함수
#         self.name = name #인스턴스 변수
#         self.model = model
#         self.color = color
#         self.speed = speed

#     def info(self):
#         print(f'Hi {self.name} model : {self.model}, color : {self.color}, speed : {self.speed}')


# hyundai = Car('A', 'sonata', 'white', 80) # 인스턴스 = 클래스명()
# hyundai.info() # 인스턴스.메서드



# # 생성자 구조로 객체예시 짜보기
# class Singer :
#     def __init__(self, name, job, birth, country):  #생성자 함수
#         self.name = name  # 인스턴스 함수
#         self.job = job
#         self.birth = birth
#         self.country = country

#     def rap(self):  #인스턴스 메서드
#         print(f'안녕하세요 저는 {self.name} 입니다. 제 직업은 {self.job}이며, 국적은 {self.country}입니다.')  

#     def dance(self):
#         print(f'(춤 추는 중)') 
    
#     def sing(self):
#         print(f'소몰이')

# A = Singer('진호', '가수', '1995.04.05', '한국')
# A.rap()
# A.dance()
# A.sing



# class Singer :
#     def __init__(self):
#         self.occ = "가수"
#         self.birth = "1985년 5월 15일"
#         self.nat = "대한민국"

#     def rap(self):
#         print("랩하는중")

#     def dance(self):
#         print("댄스")

#     def sing(self):
#         print("소몰이 창법")

# # 인스턴스 생성, 인스턴스 속성 출력, 인스턴스 메서드 호출
# Asinger = Singer()
# print(f"직업 : {Asinger.occ}")
# print(f"생년월일 : {Asinger.birth}")
# print(f"국적 : {Asinger.nat}")
# Asinger.rap()
# Asinger.dance()
# Asinger.sing()


# # 클래스 변수의 활용
# class Person():
#      count = 0 #클래스 변수

#      def __init__(self, name):
#           self.name = name
#           Person.count +=1
          
# # 인스턴스를 생설할 떄 마다 count가 1씩 증가
# person1 = Person('에스파')
# person2 = Person("BTS")

# print(Person.count)


# # 클래스 메서드로 변환
# class Singer :
#     occ = "가수"
#     birth = "1985년 5월 15일"
#     nat = "대한민국"

#     @classmethod
#     def rap(cls):
#         print("랩하는중")

#     @classmethod
#     def dance(cls):
#         print("댄스")

#     @classmethod
#     def sing(cls):
#         print("소몰이 창법")

# # 인스턴스 생성, 인스턴스 속성 출력, 인스턴스 메서드 호출
# Asinger = Singer()
# print(f"직업 : {Asinger.occ}")
# print(f"생년월일 : {Asinger.birth}")
# print(f"국적 : {Asinger.nat}")
# Asinger.rap()
# Asinger.dance()
# Asinger.sing()


# # 스태틱 메소드로 변환
# class Singer :
#     occ = "가수"
#     birth = "1985년 5월 15일"
#     nat = "대한민국"

#     @staticmethod
#     def rap():
#         print("랩하는중")

#     @staticmethod
#     def dance():
#         print("댄스")

#     @staticmethod
#     def sing():
#         print("소몰이 창법")
# # 인스턴스 생성, 인스턴스 속성 출력, 인스턴스 메서드 호출
# Asinger = Singer()
# print(f"직업 : {Asinger.occ}")
# print(f"생년월일 : {Asinger.birth}")
# print(f"국적 : {Asinger.nat}")
# Asinger.rap()
# Asinger.dance()
# Asinger.sing()

# # 매직 메서드 실습
# class Circle :

#     def __init__(self, r):
#         self.r = r
    
#     def area(self):
#         return 3.14* self.r * self.r
    
#     def __str__(self):
#         return f'[원] radius {self.r}'
    
# c1 = Circle(10)
# c2 = Circle(5)

# print(c1)
# print(c2)


# # 데코레이터 실습
# def my_decorator(func):
#     def wrapper():
#         print('함수 실행 전')
#         # 원본 함수 호출
#         result = func()

#         print("함수 실행 후")
#         return result
#     return wrapper

# # 데코레이터 적용

# @my_decorator
# def my_function():
#     print("원본함수 실행")
# my_function()

# #실습 7-1
# class Shape:
#    def __init__(self, width, height):
#         self.width = width
#         self.height = height

# shape1 = Shape(5, 3)
# print(shape1.width, shape1.height)

# #실습7-2
# class Shape:
#    pass

# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)
################################
# class Shape:
#    def __init__(self, width, height):
#         self.width = width
#         self.height = height
   
#    def calculate_area(self):
#        return (self.width * self.height)
# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)

# #실습7-3
# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_perimeter(self):
#         perimeter = self.width*2 + self.height*2
#         return perimeter

# shape1 = Shape(5, 3)
# perimeter1 = shape1.calculate_perimeter()
# print(perimeter1)

# # 실습7-4
# class Shape:
#    def __init__(self, width, height):
#          self.width = width
#          self.height = height
#          self.Area = width * height
#          self.Perimter = (width + height)*2
#    def print_info(self):
#       print(f'Width : {self.width}')
#       print(f'Height : {self.height}')
#       print(f'Area : {self.Area}')
#       print(f'Perimeter : {self.Perimter}')

# shape1 = Shape(5, 3)
# shape1.print_info()

# # 실습7-5
# class Shape:
#    def __init__(self, width, height):
#          self.width = width
#          self.height = height
         
#    def __str__(self):
#         return f'Shape: width={self.width}, height={self.height}'

# shape1 = Shape(5, 3)
# print(shape1)

# 과제 7-2
# class StringRepeater:
#     pass

# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")
# ###############
# class StringRepeater:
#     def repeat_string(self, n ,word):
#         self.n = n
#         self.word = word
#         for _ in range(n):
#             print(word)

# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")

# 과제 7-4
# class Person:
#    pass

# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)
# # #####################
# class Person:
#     number_of_people = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.number_of_people +=1

#     def introduce(self):
#         print(f'제 이름은 {self.name}이고 , 저는{self.age}입니다.')
        
# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)

# ws_4_3.py
import requests

dummy_data = []  
for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}' 
    response = requests.get(API_URL).json()
    user_data = {
        'company name': response['company']['name'],
        'lat': float(response['address']['geo']['lat']),  # Convert to float
        'lng': float(response['address']['geo']['lng']),  # Convert to float
        'name': response['name']
    }
    dummy_data.append(user_data)

for user in dummy_data:
    lat = user['lat']
    lng = user['lng']
    if lat > 80 or lat < -80 or lng > 80 or lng < -80:
        print(user)
#  if (lat_list[user] < 80 or lat_list[user] > -80) and (lng_list[user] < 80 or lng_list[user] > -80):