# # 진법 변경
# print(bin(12))  # 0b1100
# print(oct(12))  # 0o14
# print(hex(12))  # 0xc

# print(2/3)  #0.6666666666666666
# print(3/5)  #0.6

# # 지수(제곱하는 횟수) 표현 10^
# print(314e-2)   #3.14
# print(314e2)    #31400.0
# print(314**-(2))#3.14

# # f-string
# print(f'Debugging roaches 13 room')
# bugs = 'roaches'
# counts = 13
# area = 'living room'
# print(f'Debugging {bugs} {counts} {area}')
# # print( "Debugging {} {} {}".format(bugs, counts, area))
# # print( "Debugging %s %d %s" % (bugs, counts, area ))

# # f-string 응용
# greeting = 'hi'
# print(f'{greeting:>10}')    # 왼쪽에 10자리 확보 후 실행( : > 사이에 들어가는 것이 공백을 채워줌)
# print(f'{greeting:^10}')    # 가운데 정렬
# print(f'{3.141592:.4f}')    # 실수 자리수 표현


# # 불변과 가변
# my_str = 'hello'
# # my_str[0] = 'z'

# my_list = [1, 2, 3]
# my_list[0] = 100
# print(my_list)


# List_1 = [1, 2, 3,]
# List_2 = List_1

# List_1[0] = 100
# print(List_1) # [100, 2, 3]
# print(List_2) # 리스트 1과 같은 값을 가짐!

# decimal= 10
# #1. 2진수 출력
# binary = bin(decimal)[2:] 
# print(binary)  # 0b 0o 0x 를 없애고싶다면 위처럼 인덱스 슬라이스 하기
# #2. 8진수 출력
# print(oct(decimal))
# #3. 16진수 출력
# print(hex(decimal))

# a = 3.2 - 3.1
# b = 1.2 - 1.1

# # 부동 소수점 값을 출력할 때 f-string을 활용하여 부동소수점의 정확를 제어 할 수 있음
# print(f'{a}')
# print(f'{b}')
# print(f'{a:.1f}')
# print(f'{b:.1f}')

# print(314e-2)
# print(314*10**-2)

# # IM형으로 문자열 파싱 문제가 나옴 !!
# # IM형으로 문자열 파싱 문제가 나옴 !!
# # IM형으로 문자열 파싱 문제가 나옴 !!

# greeting = "hello world"

# #1 인덱싱  W 출력하기
# print(greeting[6]) 
# #2-1 슬라이싱 hello 출력하기
# print(greeting[:5])
# #2-2 슬라이싱 world 출력하기
# print(greeting[-5:])
# print(greeting[6:])
# #2-3 슬라이싱 거꾸로 출력하기
# print(greeting[: : -1])
# #3 내장함수 사용하여 문자열의 길이 출력
# print(len(greeting))
# #4 for문을 활용하여 hello world를 출력해보세요 ( 2가지 방법 )
# for i in greeting:
#     print(i, end=" ") # end안쓰면 한글자씩 나타남
# print() # 밑에꺼랑 줄바꿈요

# for i in range(len(greeting)):
#     print(greeting[i], end=" ")

# greeting[start:end:step]
# step>0 이면 start가 0이므로 end-1
# step<0 이면 start가 -1이므로 end+1


# # 2차원리스트 = 행렬
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]

# #1 인덱싱하여 3을 출력해보세요
# print(array[0][2])
# #2 인덱싱하여 7을 출력해보세요.
# print(array[2][0])

# # 2차원리스트를 입력받는 방법
# rows = int(input("행의 개수를 입력하세요."))
# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# matrix = [list(map(int, input().split()))for _ in range(rows)] # 위의 3줄이 이거 한줄과 똑같다.

# for row in matrix :
#     print(row)    

# # 튜플을 사용하는 예시 : 방향 배열

# def move_around(position):
#     x, y =position
#     direction = [ (0,1),(0,-1),(1,0),(-1,0)] # 상 하 좌 우를 뜻하는 튜플사용
#     direction2 = [(-1,1)] # 오른쪽 위에 방향\

# # range -> 주로 반복문과 함께 쓰임
# range(5)
# # range(end) : 0부터 end-1까지 1만큼증가
# range(1,5)
# # range(start,end) : start부터 end-1까지 1만큼증가
# range(1, 8 ,2)
# # range(start, end, step) : start 부터 end-1까지 step만큼 증가
# # start> end : step 만큼 감소함

# # dict안에 dict 또있는경우
# my_dict = {
#     'a1' : {'b1':1, 'b2':2, 'b3':3},
#     'a2' : {'b1':4, 'b2':5, 'b3':6},
#     'a3' : {'b1':7, 'b2':8, 'b3':9}
# }
# # value 5를 출력
# print(my_dict['a2']['b2'])
# # 다른방법 .get( ) 을 사용한다
# print(my_dict.get('a2').get('b2'))

# # set 실습
# set_1 = { 1,2,3,4,5,6,7,8,8,9,10}
# set_2 = {2,3,5,6,8,9,11}
# # 합집합
# print(set_1 | set_2)
# # 차집합
# print(set_1 - set_2)
# # 교집합
# print(set_1 & set_2)

# # 세트의 사용예시 - 로또번호 추첨
# import random

# lotto_set=set()

# while len(lotto_set) < 6 :
#     number = random.randint(1,45)
#     lotto_set.add(number) #set에 추가하는 .add 

# lotto_list = list(lotto_set)
# lotto_list.sort()  # sort는 오름차순 정렬
# print(lotto_list)



# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# '''
# - 작가와 작품 목록 참고
# - 허균 : 홍길동전, 장생전, 도문대작
# - 임제 : 수성지, 백호집, 원생몽유록
# - 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
# '''
# information[authors[0]] = books[1]
# information[authors[1]] = books[3]
# information[authors[2]] = books[4]
# information[authors[3]] = books[0]
# information[authors[4]] = books[2]

# for key, value in information.items():
#      print(key," : " ,value)
#      # 딕셔너리를 .items  를 사용하여 키와 밸류 값을 추출하여 모두 출력



# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'], 
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'], 
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'], 
#     ['성공의 열쇠', '내면의 변화', '목표의 달성']
# ]

# backup_catalog = None

# ''' 
# 도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
# '성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
# '''

# print('catalog와 backup_catalog를 비교한 결과')
# # 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오. 
# print(catalog == backup_catalog)

# backup_catalog = catalog

# print('backup_catalog : ')
# print(backup_catalog)
# print()
# catalog[3] = ['성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀']
# print('catalog : ')
# print(catalog)



# book = 1
# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# print(guide)
# print(book * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3
# print(changes)
# print(total - rental)


# authors = ['작자 미상', '이항복', '임제', '임제', 
#            '조성기', '조성기', '조성기', '임제', 
#            '허균', '허균', '허균', '임제', '임제', 
#            '임제', '임제', '임제', '임제', '임제', 
#            '임제', '임제', '임제', '박지원', '이항복', 
#            '남영로', '남영로', '남영로', '이항복', '임제', '임제']

# print(list(set(authors)))

# # 리스트의 목록을 하나씩 뺴고싶을때

# numbers= [1, 2, 3, 4, 5]
# total = 0
# for num in numbers :
#     total += num
# # => sum(numbers) = total

# print(total)








