# # 임의의 키워드인자 목록
# def calculate_sum(**kwargs):
#     print(kwargs) # {'name': 'Alice', 'age': 30, 'address': 'korea'}

# calculate_sum(name='Alice',age=30, address='korea')

# # 임의의 인자 목록
# def calculate_sum(*number):
#     print(number) # {'name': 'Alice', 'age': 30, 'address': 'korea'}

# calculate_sum(1, 2, 3, 4, 5)

# # scope 
# def my_func() :
#     num = 1

# print(num)
# # num 은 함수안에만 정의되있기 때문에 찾지못한다
# # 함수내의 num이 local // print()내의 num이 global

# #map 함수
# numbers = [ 1, 2, 3 ]
# result =  map(str, numbers)
# print(result) # <map object at 0x0000019A62C613D0>
# print(list(result)) # ['1', '2', '3']

# reslut=[]
# for number in numbers :
#     result.append(str(number))

# print(result)


# ####
# import sys
# sys.stdin = open('7월/19일/input.txt')

# T = int(input())
# K,N,M = map(int, input().split())

# print(K, N, M)

# #zip함수
# names = ['Alice', ' Bob', 'Charlie']
# ages = [30,  35]
# cities = ['New york', 'London', 'Paris' ]

# for name, age, city in zip(names, ages, cities):
#     print(name, age, city)

# keys = ['a', 'b', 'c']
# values = [1,2,3]
# my_dict = dict(zip(keys, values))
# print(my_dict)


# # lambda와 map 함수
# numbers = [1, 2 ,3 ,4 ,5]
# result = list(map(lambda x: x * 2, numbers))
# print(result)

# # def double_number(x):
# #     return x *2
# # 위의 lambda함수 를 풀어쓰면 이렇게된다

# #위치인자
# def greet(name, age):
#     print(f'(안녕하세요, {name}님! {age}살 이시군요.)')

# greet('Alice', 25)

# # scope

# # bulit-in scope는 내장함수
# z = 3 # global scope
# def outer():
#     x=1 # 로컬변수
#     def inner():
#         y=2 #로컬변수
#         result = x + y # x가 enclosed scope에 해당
#         print(result)
#     inner()
# outer()

# 재귀함수 -> 자기자신을 호출하는 함수

# #팩토리얼 만들어보기 
# def factorial(n) :
#     if n == 0 :
#         return 1
#     return n * factorial(n-1)

# print (factorial(8))
            
# # 어렵게 가지말고 1. 종료조건이 명확하고, 2. 반복되는 호출이 종료조건을 향하도록 작성 을 위주로하기

# lambda 매개변수 : 표현식

#1. 1회성이기때문에 함수 명이 필요없다.
#2. 표현식의 결과가 반환되기때문에 return도 필요없다

# # map()함수를 사용하여 numbers 리스트의 각 요소가 제곱된 값들로 이루어진 새로운 리스트 생성
# numbers=[1,2,3,4,5]

# result = list(map(lambda x: x*2, numbers))
# print(result)

# 패킹 : 여러 값을 하나의 시퀀스로 묶는 과정
# 예시1)
# packing_values = 1,2,3,4,5
# print(packing_values) # (1, 2, 3, 4, 5)

# numbers = [1,2,3,4,5]
# a, *b, c = numbers # *(애스터리스크): 패킹연산자로 활용
# print(a) #1
# print(b) #[2, 3, 4]
# print(c) # 5


# # print 함수에 임의의 가변인자를 작성할수 있던 이유
# print('hi', 'hello', 'goodbye', sep = "-") # hi-hello-goodbye
# print('hi',end=' ')
# print('hello') # hi hello

# # *(애스터리스크)를 언패킹 연산자로 활용
# names=['key', 'bob', 'jane']
# print(*names) # key bob jane

# ## ** : 딕셔너리 언패킹 연산자
# def my_funtion(x,y,z):
#     print(x, y, z)
# dict_values={'x':1, 'y':2, 'z':3}
# my_funtion(**dict_values) # 1 2 3


# # 파이썬 math 모듈 예시
# import math
# print(math.pi)
# print(math.sqrt(16))
# # ctrl을 누른채 math를 누르면 안에 함수를 볼 수 있다.

# from math import pi, sqrt
# print(pi)
# print(sqrt(2))

# #from 과 import 차이 2
# import random
# print(random.randint(1,46))

# from random import *
# print(randint(1,46))

# # 사용자 설정 모듈 
# import my_math
# print(my_math.add(1,2))

# from my_math import *
# print(add(1,2))

# # 라이브러지- 패키지 디렉토리 
# from my_package.math import my_math
# from my_package.statistics import tools
# print(my_math.add(1,2))
# print(tools.mod(1,2))

# # 패키징 설치 Json
# import requests

# url = 'https://random-data-api.com/api/v2/users'

# response = requests.get(url).json()
# print(response)
# # https://jsonviewer.stack.hu/에서 출력을 텍스트에 입력하면 정리된 모습 확인 할 수 있음

# # 실습) united states를 출력해보세요. - key로 접근

# print(response['address']['country'])
# print(response.get('address').get('country'))





# #실습 1번
# number_of_people = 0


# def increase_user():
#     global number_of_people
#     number_of_people += 1

# increase_user()
# print(number_of_people)

#실습 2번
# number_of_people = 0
# print (f"현재 가입된 유저의 수 : {number_of_people}")
# def increase_user():
#     global number_of_people
#     number_of_people += 1

# def create_user(name, age, address):
#     increase_user()
#     print(f'{name}님 환영합니다!')
#     user_info = {'name':name,'age':age,'address':address}
#     print(user_info)
#     print(f"현재 가입된 유저의 수 : {number_of_people}")

# create_user('홍길동', 30, '서울')

# # 실습 3번

# # book.py
# number_of_book = 100
# def decrease_book(books):
#     global number_of_book
#     number_of_book -= books
#     print(f'남은 책의 수 : {number_of_book}')
# # ws_3_3.py
# from book import decrease_book
# def rental_book(name, books):
#     decrease_book(books)
#     print(f'{name}님이 {books}의 책을 대여하였습니다. ')

# rental_book('홍길동', 3)

# # 실습4
# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# def create_user(name, age, address):
#     print(map(f'{name}님 환영합니다!',name))
#     user_info = {'name':name,'age':age,'address':address}
   
#     all_user = []
#     all_user += user_info
#     print(all_user)
#     # print(f"현재 가입된 유저의 수 : {number_of_people}")

# print(create_user())

# # user_info =dict(name,age,address) 
# # print(user_info)

# # 실전 3-2
# def add_numbers(a,b):
#     print(f'{a}와 {b}를 인자로 넘긴 경우')
#     print(a+b)

# #수정한 add_numbers() 함수를 호출하시오.
# add_numbers(3,5)


# # 실전 3-3

# from book import decrease_book
# number_of_people = 0

# def increase_user():
#     '''
#     이용자 수가 늘 때마다 count +1 하는 함수입니다.
#     '''
#     global number_of_people
#     number_of_people += 1

# def create_user(name, age, address):
#     '''
#     이용자의 이름, 연령, 주소를 받아 dictionary에 저장하고
#     환영 인사를 출력하는 함수입니다.
#     '''
#     user_info = {}
#     user_info['name'] = name
#     user_info['age'] = age
#     user_info['address'] = address
#     increase_user()
#     print(f'{name}님 환영합니다!')
#     return user_info

#  # 실전 3-4 

# # number_of_people = 0
# # user_list = []

# # def increase_user():
# #     global number_of_people
# #     number_of_people += 1

# def create_user(name, age, address):
#     # increase_user()
#     user_info = {
#         "name": name,
#         "age": age,
#         "address": address
#     }
#     print(f"{name}님 환영합니다!")
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# user_list = list(map(create_user, name, age, address))
            
# for user in user_list:
#     print(user, end='')


# # 실습 3-4 
# # 실습 번호.py
# number_of_people = 0
# user_list = []

# def increase_user():
#     global number_of_people
#     number_of_people += 1

# def create_user(name, age, address):
#     increase_user()
#     user_info = {
#         "name": name,
#         "age": age,
#         "address": address
#     }
#     print(f"{name}님 환영합니다!")
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# many_user = list(map(lambda n, a, ad: create_user(n, a, ad), name, age, address))
# # =list(map(create_user,name,age,address))
# print(many_user)


from book import decrease_book

def rental_book(info):
    num_of_books=info['age']//10
    decrease_book(num_of_books)
    print(f'{info["name"]}님이 {num_of_books}의 책을 대여하였습니다. ')
    
for i in range(len(many_user)) :
    rental_book(many_user[i])

