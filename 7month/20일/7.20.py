# num = int(input('숫자를 입력하세요 : '))

# # if statement
# # num이 홀수라면
# if num % 2 == 1 :
#     print(f"{num}은 홀수 입니다")
# # if num % 2 : 라고 써도 가능하다. 결과값인 1이 Ture를 뜻하기에 if문이 실행된다.
# # num이 짝수라면
# else :  # num % 2 == 0 을 쓰지 않아도됌 
#     print(f"{num}은 짝수 입니다")


# # list comprehension
# # 1. 1-10 까지 요소를 가지는 리스트 만들기
# new_list = []
# for i in range(1,11):
#     new_list.append(i) # append 리스트의 값을 순차적으로 넣는 함수
# print(new_list)

# # 2. list comprehension
# new_list2 = [i for i in range(1,11)]
# print(new_list2)

# # 1. 1-10 중 홀수 요소를 가지는 리스트 만들기
# new_list = []
# for i in range(1,11):
#      if i % 2 ==1 :
#         new_list.append(i) # append 리스트의 값을 순차적으로 넣는 함수
# print(new_list)

# # 2. list comprehension
# new_list2 = [i for i in range(1,11) if i % 2 ==1 ]
# print(new_list2)

# # # 2. 
# # new_list3 = [i if i % 2] 



# # 리스트를 만드는 3가지 방법 비교
# # 정수 1,2,3을 가지는 리스트 만들기
# numbers = [ '1', '2', '3']
# # 1. for 반복문
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers)

# # 2.map
# new_numbers2 = list(map(int, numbers))
# print(new_numbers2)

# # 3. list comprehension
# new_numbers3 = [int(number) for number in numbers]
# print(new_numbers3)

# # enumerate
# result = [ 'a', 'b', 'c']

# print(enumerate(result)) # <enumerate object at 0x000002946EBBE680>
# print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')]

# for index, elem in enumerate(result):
#     print(index, elem)
# # 0 a
# # 1 b
# # 2 c

# # 조건문 연습
# # 실습 1 정수를 입력받아 짝수면 'even', 홀수면 'odd'출력
# n= int(input())
# if n % 2==0 :
#     print ("EVEN")
# else :
#     print ("ODD")

# # 실습 2 윤년 판별하기, 윤년이면 'leap year'. 그렇지 않으면 'common year' 출력
# # 윤년의 조건1. 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다.
# # 윤년의 조건2. 연도가 400으로 나누어 떨어진다.

# year = int(input())
# if (n % 4 == 0 and n % 100 != 0) or n% 400 == 0 :
#     print("leap year")
# else :
#     print('common year')



# #  for 문 실습1) 구구단 출력

# for i in range(2,10) :
#     print()
#     print(f'<{i}단>')
#     for j in range(1, 10) :
#         result = i * j
#         print(f'{i} * {j} = {result:>2} ')

# # 실습 2 정수 n을 받아 n단의 직각 이등변 삼각형을 그리는 프로그램 작성

# n= int(input("정수를 입력하시오. : "))
# for i in range(1,n+1) :
#     print('*'*i) 

# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print( )

"""
초기식
while 조건식 :
    code ~~ 
     증감식

조건식이 참인동안 반복하는 반복문= while문
프로그램 종료 조건 만들어 주셔야 합니다.
"""
# # 실습1 continue를 이용하여 1부터 10까지 정수 중 홀수만 출력하기
# i=0
# while i < 10 :
#     i += 1
#     if i % 2 == 0 :
#         continue
#     print(i, end=' ')

# # 실습2 break을 이용하여 'Shall we close ? (y/n)' 문구에 y를 입력해야
# # 반복문을 탈출하고 'The end'를 출력하는 프로그램 작성

# while True : 
#     n = input('Shall we close ? (y/n)')
#     if n == y :
#         print("The end")
#         break

# # 실습 3 정수를 입력받아 그 정수가 몇 자릿수 숫자인지 알아내는 프로그램 작성
# n = int(input('정수를 입력하시오. : '))
# cnt = 0
# while n > 0 :
#     cnt += 1
#     n //= 10 
# print(cnt)

# 실습 : sqrt_number line을 list comprehension 으로

# import math
# numbers = [1, 4, 9, 16, 25]

# sqrt_numbers =[]
# for number in numbers:
#     sqrt_numbers.append(math.sqrt(number))

# print (sqrt_numbers)

# # 위 3줄을 한줄로 표현할수 있다.
# sqrt_numbers = [math.sqrt(number) for number in numbers]
# print (sqrt_numbers)
# # 실습2 : if 추가 짝수만 추가해보세요.
# sqrt_numbers = [math.sqrt(number) for number in numbers if number%2==0]
# print (sqrt_numbers)

# #실습 4-1
# import requests

# # 무작위 유저 정보 요청 경로
# API_URL = 'https://jsonplaceholder.typicode.com/users/1'
# # API 요청
# response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# # 특정 데이터 출력
# print(parsed_data['name'])
# print(parsed_data['username'])
# print(parsed_data['company']['name'])

# # 실습 4-2
# # ws_4_2.py
# import requests

# # 무작위 유저 정보 요청 경로

# # API 요청
# user_names = []  # Empty list to store user names
# for i in range(1, 11):
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}' 
#     response = requests.get(API_URL).json()
#     user_names.append(response['name'])

# print(user_names)


# # 실습 4-3
# # ws_4_3.py
# import requests

# dummy_data = []  # Empty list to store user data
# for i in range(1, 11):
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}' 
#     response = requests.get(API_URL).json()
    
#     user_data = {
#         'name': response['name'],
#         'lat': response['address']['geo']['lat'],
#         'lng': response['address']['geo']['lng'],
#         'company name': response['company']['name']
#     }
#     dummy_data.append(user_data)

# print(dummy_data)

# # 실습 4-3 줄바꿈 추가

# import requests

# dummy_data = []  # Empty list to store user data
# for i in range(1, 11):
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}' 
#     response = requests.get(API_URL).json()
    
#     user_data = {
#         'name': response['name'],
#         'lat': response['address']['geo']['lat'],
#         'lng': response['address']['geo']['lng'],
#         'company name': response['company']['name']
#     }
#     dummy_data.append(user_data)

# # Print each dictionary on a new line
# for user in dummy_data:
#     print(user)

# # 실습 4-4
# import requests

# def censorship(company_name, user_name):
#     if company_name in black_list:
#         print(f"{company_name} 소속의 {user_name}은 등록할 수 없습니다.")
#         return False
#     else:
#         print("이상없습니다")
#         return True

# def create_user():
#     censored_user_list = {}
#     for i in range(1, 11):
#         API_URL = f'https://jsonplaceholder.typicode.com/users/{i}' 
#         response = requests.get(API_URL).json()
#         company_name = response['company']['name']
#         user_name = response['name']
        
#         if censorship(company_name, user_name):
#             if company_name in censored_user_list:
#                 censored_user_list[company_name].append(user_name)
#             else:
#                 censored_user_list[company_name] = [user_name]
    
#     return censored_user_list

# black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

# censored_user_list = create_user()
# print(censored_user_list)

# # 실습 4-5

# user_data = [
#     {
#         'blood_group': 'AB',
#         'company': 'Stone Inc',
#         'mail': 'ian17@yahoo.com',
#         'name': 'Kathryn Jenkins',
#         'website': [
#             'https://www.boyd-herrera.com/',
#             'https://watson.com/',
#             'http://www.mitchell.com/',
#             'http://irwin-cline.biz/',
#         ],
#     },
#     {
#         'blood_group': 'AB+',
#         'company': 'Fleming Ltd',
#         'mail': 'patricianelson@yahoo.com',
#         'name': 'Angel Williamson',
#         'website': [
#             'https://wilson-johnson.com/',
#             'https://santiago-hammond.com/',
#             'https://morales.com/',
#             'https://fry-fleming.com/',
#         ],
#     },
#     {
#         'blood_group': 'A+',
#         'company': 'Scott PLC',
#         'mail': 'lisajones@gmail.com',
#         'name': 'Stephanie Herman MD',
#         'website': ['https://www.boyer-stevens.org/', 'http://www.johnson.com/'],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'Warren-Stewart',
#         'mail': 'allisonjennifer@gmail.com',
#         'name': 'Jon Martinez',
#         'website': ['https://www.berg.com/'],
#     },
#     {
#         'blood_group': 'AB+',
#         'company': 'Fisher Inc',
#         'mail': 'mross@yahoo.com',
#         'name': 'Justin Brown',
#         'website': [
#             'https://www.gray.com/',
#             'https://jones.com/',
#             'http://williams.biz/',
#             'https://hammond.net/',
#         ],
#     },
#     {
#         'blood_group': 'B-',
#         'company': 'Pearson Group',
#         'mail': 'gravesbarbara@hotmail.com',
#         'name': 'Bobby Patterson',
#         'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'White, Andrade and Howard',
#         'mail': 'mcole@gmail.com',
#         'name': 'Michelle Strickland',
#         'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'Brown-Young',
#         'mail': 'tmorales@hotmail.com',
#         'name': 'Stephanie Moore',
#         'website': ['https://schmidt.com/'],
#     },
#     {
#         'blood_group': 'AB+',
#         'company': 'Brooks PLC',
#         'mail': 'wellsmatthew@hotmail.com',
#         'name': 'Dr. David Johnson',
#         'website': [
#             'http://ford-dean.com/',
#             'http://www.petersen.com/',
#             'https://thompson-cooley.info/',
#             'http://ryan-gay.com/',
#         ],
#     },
#     {
#         'blood_group': 'A-',
#         'company': 'Stewart Group',
#         'mail': 'sean37@hotmail.com',
#         'name': 'Veronica Webb',
#         'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
#     },
#     {
#         'blood_group': 'AB+',
#         'company': 'Cabrera, Perry and Harris',
#         'mail': 'bgonzales@yahoo.com',
#         'name': 'Lisa Wilcox',
#         'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
#     },
#     {
#         'blood_group': 'B+',
#         'company': 'Thomas, Lozano and Lopez',
#         'mail': 'bperry@yahoo.com',
#         'name': 'Brian Simmons',
#         'website': [
#             'http://reid.com/',
#             'http://www.roman-neal.biz/',
#             'https://www.hoover.org/',
#             'https://www.lynn.com/',
#         ],
#     },
#     {
#         'blood_group': 'O+',
#         'company': 'Baker-Leach',
#         'mail': 'johnlucas@yahoo.com',
#         'name': 'Carlos Robinson',
#         'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'Higgins, Higgins and Garcia',
#         'mail': 'chris66@gmail.com',
#         'name': 'Gabriel Collins',
#         'website': ['https://www.cole-pugh.com/'],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'Tanner, Wheeler and Weaver',
#         'mail': 'leonardtammy@gmail.com',
#         'name': 'Christopher Cook',
#         'website': [
#             'https://www.myers-reynolds.com/',
#             'https://dunlap-rogers.com/',
#             'https://luna.net/',
#             'http://smith-miller.com/',
#         ],
#     },
#     {
#         'blood_group': 'A-',
#         'company': 'Schaefer-Hunter',
#         'mail': 'nsummers@gmail.com',
#         'name': 'Daniel Monroe',
#         'website': [
#             'https://cook.net/',
#             'http://carpenter.com/',
#             'http://morris-terrell.com/',
#         ],
#     },
#     {
#         'blood_group': 'B+',
#         'company': 'Stephens Group',
#         'mail': 'rolson@gmail.com',
#         'name': 'Molly Parks',
#         'website': [
#             'https://wright-vincent.biz/',
#             'http://www.cruz.com/',
#             'http://olson.org/',
#             'http://gomez.com/',
#         ],
#     },
#     {
#         'blood_group': 'O-',
#         'company': 'Fitzgerald, Costa and Hobbs',
#         'mail': 'jennifervang@hotmail.com',
#         'name': 'Jill Patterson',
#         'website': [
#             'https://www.brewer.com/',
#             'https://malone-murray.info/',
#             'http://evans.com/',
#             'https://ortiz.com/',
#         ],
#     },
#     {
#         'blood_group': 'A-',
#         'company': 'Frazier Ltd',
#         'mail': 'vsolis@hotmail.com',
#         'name': 'Marie May',
#         'website': [
#             'http://pratt.info/',
#             'http://www.ortega.com/',
#             'http://www.smith.net/',
#             'https://nichols.biz/',
#         ],
#     },
#     {
#         'blood_group': 'O+',
#         'company': 'Rodriguez and Sons',
#         'mail': 'michael09@yahoo.com',
#         'name': 'Julia Gonzalez',
#         'website': [
#             'https://www.cantrell.com/',
#             'https://www.smith.net/',
#             'http://delgado.com/',
#             'http://stevens.com/',
#         ],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'Brown-Arnold',
#         'mail': 'christopher79@hotmail.com',
#         'name': 'David Garza',
#         'website': ['https://price.net/'],
#     },
#     {
#         'blood_group': 'A+',
#         'company': 'Butler-Hernandez',
#         'mail': 'angiechoi@yahoo.com',
#         'name': 'Leslie Kemp',
#         'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
#     },
#     {
#         'blood_group': 'A-',
#         'company': 'Schneider-Hensley',
#         'mail': 'cesarsantos@hotmail.com',
#         'name': 'Brandon Peterson',
#         'website': [
#             'https://www.owens-gay.com/',
#             'https://www.santiago.org/',
#             'https://www.singleton.com/',
#         ],
#     },
#     {
#         'blood_group': 'O-',
#         'company': 'Hunter, Alvarado and Stewart',
#         'mail': 'thomas16@gmail.com',
#         'name': 'Matthew Stanley',
#         'website': ['https://nelson.com/'],
#     },
#     {
#         'blood_group': 'A+',
#         'company': 'Elliott, Mullins and Michael',
#         'mail': 'smithedward@hotmail.com',
#         'name': 'Robert Brown',
#         'website': ['http://montgomery-rogers.biz/', 'http://www.williams-nixon.com/'],
#     },
#     {
#         'blood_group': 'AB+',
#         'company': 'Velasquez-Garcia',
#         'mail': 'samanthawilson@yahoo.com',
#         'name': 'Stephanie Cohen',
#         'website': ['http://jackson-harris.com/'],
#     },
#     {
#         'blood_group': 'A+',
#         'company': 'Mccoy-Hopkins',
#         'mail': 'lli@yahoo.com',
#         'name': 'Michael Clark',
#         'website': [
#             'https://www.harding.info/',
#             'https://www.jones.biz/',
#             'http://knight-adkins.org/',
#             'http://www.alvarado-mendoza.org/',
#         ],
#     },
#     {
#         'blood_group': 'O+',
#         'company': 'Kerr Ltd',
#         'mail': 'georgebrittany@yahoo.com',
#         'name': 'Brandon White',
#         'website': ['https://flowers-parker.info/', 'http://oliver-rice.info/'],
#     },
#     {
#         'blood_group': 'AB-',
#         'company': 'Villarreal, Wood and Smith',
#         'mail': 'denise73@yahoo.com',
#         'name': 'Kevin Blevins',
#         'website': [
#             'http://www.ramirez.info/',
#             'https://mckay.net/',
#             'http://duran.com/',
#         ],
#     },
#     {
#         'blood_group': 'O+',
#         'company': 'Jenkins-Garcia',
#         'mail': 'kwoodward@hotmail.com',
#         'name': 'Michelle Dixon',
#         'website': [
#             'http://www.taylor.com/',
#             'https://bates-trujillo.org/',
#             'https://www.thomas-boyer.org/',
#         ],
#     },
# ]

# blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
# black_list = ['Jenkins-Garcia', 'Stephens Group', 'White, Andrade and Howard', 'Warren-Stewart']

# def create_user():
#     for i in user_data :
#     blood_group = i[blood_group]
#     company = i[company]
# def is_validation():
#     pass

# 실전 4-2
# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

# rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

# for i in list_of_book :
#     if i not in rental_book :
#         print(f"{i} 은/는 보유하고 있지 않습니다.")
#         break

# if list_of_book == rental_book :   
#     print("모든 도서가 대여 가능한 상태 입니다.")


# # 실전 4-4
# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

# rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

# missing_book = []

# missing_book = [book for book in list_of_book if book not in rental_book]

# for book in missing_book :
#     print(f"{book} 을/를 보충하여야합니다.")