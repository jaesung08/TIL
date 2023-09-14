# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age

#     def talk(self):
#         print(f"안녕하세요, {self.name} 입니다.")


# class Professor(Person):
#     def __init__(self, name, age, department):
#         Person.__init__(self,name,age)
#         super().__init__(name, age)
#         self.department = department
# # Person 보다 super가 self를 하나라도 덜 쓴다.
# class Student(Person):
#     def __init__(self, name, age, gpa):
#         self.name = name
#         self.age = age
#         self.gpa = gpa
# # 위의 두개는 같은 의미를 축적하고있다!
# p1 = Professor("박교수", 45 , '컴퓨터공학')
# s1 = Student('김학생', 20, 3.7)

# p1.talk()
# s1.talk()

# # 다중 상속
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age

#     def greeting(self):
#         print(f"안녕하세요, {self.name} 입니다.")


# class Mom(Person):
#     gene = 'XX'

#     # def __init__(self, name):
#     #     super().__init__(name)
#     # 원래는 이렇게 __init__ 을 써서 한번 더 명시해야한다.
#     def swim(self):
#         return "엄마가 수영"
    

# class Dad(Person):
#     gene = "XY"

#     def walk(slef):
#         return "아빠가 걷기"
    
# class FirstChild(Dad, Mom):
#     Mom_gene = 'XX' # 아빠가 아닌 다른 상속자의 정보를 가져오기싶을 땐 이렇게 해야한다.
   
#     # def __init__(self, name, age):
#     #     super().__init__(name, age)

#     #     Mom.__init__(self, name, age)
#     # 슈퍼를 쓰는게 원칙적이나 Dad가 아닌 Mom을 불러오기위해선 이렇게 직접 해주기도 한다.

#     def swim(self):
#         return '첫째가 수영'
#     # def walk(self):
#     #     return '첫째가 걷기'
#     def cry(self):
#         return '첫째가 응애'
    
# baby1 = FirstChild('아가', 3)
# print(baby1.cry()) # 첫째가 응애
# print(baby1.swim()) #첫째가 수영
# print(baby1.walk()) #아빠가 걷기
# print(baby1.gene) # XY // 아빠가 우선 상속자이기 때문에 아빠의 gene을 가져옴
# print(baby1.Mom_gene) #XX //추가해서 불러줌

# print(FirstChild.mro()) # [<class '__main__.FirstChild'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class '__main__.Person'>, <class 'object'>]




# # 클래스 car 정의, 부모클래스
# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def info(self):
#         print(f"Model : {self.model}, color : {self.color}")

# # 클래스 CarDrive 정의, 자식클래스
# class CarDrive(Car):
#     def speedchange(self, speed):
#         self.speed = speed
#         print(f'speedchage : {self.speed}')

# hyundai = CarDrive('Sonata', 'White')
# #1. info 메서드 호출
# hyundai.info()
# #2. speedchanhe 메서드 호출
# hyundai.speedchange(88)





# # 클래스 상속? 자식 클래스 괄호안에 부모 클래스를 포함하면 클래스 상속
# # 자식클래스는 모든 클래스와 변수를 따로 선언하지 않아도 그대로 사용가능하다는 이점 존재
# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

# class CarDrive(Car):
#     def __init__(self, model, color, speed):
#         super().__init__(model, color)
#         self.speed = speed
#         #실습1. super() 내장함수 사용
    

#     def info(self):
#         print(f'Model : {self.model}, color : {self.color}, speed : {self.speed}')
# #실습2. info 메서드 호출
# Kia = CarDrive('sonata', 'white', '88')
# Kia.info()
# # super()함수 : 부모클래스의 메서드를 호출하기 위해 사용





# class Car:
#     def __init__(self, model):
#         self.model = model

# class Hyundai(Car):
#     color = 'white'
#     def speed(self):
#         return '80km/h'
    
# class Kia(Car):
#     color = 'black'
#     def engine(self):
#         return '1.6turbo'
    
# class CarDrive(Hyundai,Kia):
#     def speed(self):
#         return '100km/h'
#     def power(self):
#         return '1.999cc'

# mycar = CarDrive('sonata')
# #speed 메서드 호출 -> 출력
# print(mycar.speed())
# #engine 메서드 호출 -> 출력
# print(mycar.engine())
# #power 메서드 호출 -> 출력
# print(mycar.power()) 
# #color 클래스 변수 접근 -> 출력 -> 속성의 경우 상속 순서에 의해 결정
# print(mycar.color) # white




# # 오버라이딩 : 부모클래스의 메서드를 자식클래스에서 재정의 하는 것.
# class Car:
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color

#     def info(self):
#         print (f'Model : {self.model}, color : {self.color}')
              
# class CarDrive(Car):
#     #실습1. info 메서드를 오버라이딩
#     def info(self):
#         print(f'The model of the car is {self.model}')
#         print(f'The color is {self.color}')
# #실습2. info메서드 호출
# Kia = CarDrive('sonata', 'black')
# Kia.info()

# # 상속 관련 함수 mro() - > 메소드 결정 순서 -> 어떤 부모클래스를 가지는지
# print(CarDrive.mro()) # [<class '__main__.CarDrive'>, <class '__main__.Car'>, <class 'object'>]


# # NameError, TypeError, IndexError
# def calculate_sum(a, b):
#     return a + b

# numbers = [1, 2, 3, 4, 5]
# total_sum = 0   # 없을때 NameError 1번 # []가 되있으면 TypeError 2번

# for i in range(len(numbers)):
#     total_sum = calculate_sum(total_sum, numbers[i])

# print(f"종합 : {total_sum}")





# # #실습8-1
# class Animal:
#     num_of_animal = 0

#     def __init__(self):
#         Animal.num_of_animal += 1



# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

# class Cat(Animal):
#     def __init__(self):
#         super().__init__()

# class Pet(Dog, Cat):
#     def access_num_of_animal(self):
#         return (f'동물의 수는 {self.num_of_animal}마리 입니다.')

# dog = Dog()
# print(Pet.access_num_of_animal(Animal))
# cat = Cat()
# print(Pet.access_num_of_animal(Animal))


# #실습8-2
# class Dog:
#    pass

# dog1 = Dog()
# dog1.bark()
# ################
# class Dog:
#    def __init__(self):
#       pass
#    def bark(self) :
#       print('멍멍!')

# dog1 = Dog()
# dog1.bark()

# # 실습8-3
# class Cat:
#    def __init__(self):
#       pass
#    def meow(self) :
#        print('야옹!')
# cat1 = Cat()
# cat1.meow()


# # 실습 8-4
# class Pet:
#     pass

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()
##########
# class Pet:
#     def __init__(self,sound):
#         self.sound = sound
    
#     def make_sound(self):
#         print(f'{self.sound}')

#     def bark(self):
#         print('멍멍!')

#     def meow(self):    
#         print('야옹!')

#     def play(self):    
#         print('애완동물과 놀기')

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()


# 실습8-5
# class Sound:
#     def __init__(self, sound):
#         self.sound = sound

# class Dog():
#     sound = '멍멍'
#     def __str__():
#         return f'{Dog.sound} 소리를 냅니다.'
    

# class Cat():
#     sound = '야옹'
#     def __str__(self):
#         return f'{Cat.sound} 소리를 냅니다.'


# class Pet(Dog, Cat):

#     def __str__(self):
#          return f'애완동물은 {Pet.sound} 소리를 냅니다.'

# Animal = Pet()

# print(Animal)

############
# 과제 8-2
# def check_number():
#     try:
#         N = int(input("숫자를 입력하세요 : "))
#         if N > 0 :
#             print('양수입니다.')
#         elif N < 0  :
#             print("음수입니다.")
#     except ValueError:
#         print("잘못된 입력입니다.")

# check_number()

# 과제 8-4
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        N = input("이름을 입력하세요: ")
        A = input("나이를 입력하세요: ")

        if not A.isdigit():
            print("나이는 숫자로 입력해야 합니다.")
        elif not N.isalpha():
            print("이름을 제대로 입력해 주세요.")
        else:
            self.user_data = {N: int(A)}

    def display_user_info(self):
        if not self.user_data:
            print("사용자 정보가 입력되지 않았습니다.")
        else:
            for name, age in self.user_data.items():
                print(f"사용자 정보\n이름: {name}\n나이: {age}")

user = UserInfo()
user.get_user_info()
user.display_user_info()
