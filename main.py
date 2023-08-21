# # hw_1_4.py
# Apple_eng = "사과는 영어로 apple"
# Banana_eng = "바나나는 영어로 banana"
# Kiwi_eng = "키위는 영어로 kiwi"

# print(Apple_eng)
# print(Banana_eng)
# print(Kiwi_eng)

# h,w = map(int, input().split())
# a=[[0 for j in range(h+1)] for i in range(w+1)]

# n = int(input())

# for i in range(n) :
#     l, d, x, y = map(int, input().split())
#     for j in range(l) :
#         if d == 0 :
#             a[x][y+j] = 1
#         else :
#             a[x+j][y] = 1

# for i in range(1, h+1):
#     for j in range(1, w+1):
#         print(a[i][j],end = ' ')
#     print()

# # 6098 코드업 문제
# array = []

# for i in range(10):
#     array.append(list(map(int, input().split())))

# x, y = 1, 1

# while True :
#     if (array[x][y] == 0) :
#         array[x][y] = 9
#     elif (array[x][y] == 2) :
#         array[x][y] = 9
#         break

#     if (array[x][y+1] == 1 and array[x+1][y] == 1) :
#         break

#     if (array[x][y+1] != 1 ):
#         y = y+1
#     elif (array[x+1][y] != 1) :
#         x = x+1

# for i in range(10) :
#     for j in range(10) :
#         print(array[i][j], end=' ')
#     print( )


# # swea 스도쿠 검증

# T = int(input())

# array = []

# for i in range(9):
#     array.append(list(map(int, input().split())))

# for i in range(9):
#     for j in range(9):

# # swea 홀수만 더하기

# def sum_o(*numbers) :
#     n = 0
#     for number in numbers :
#         if number % 2 != 0 :
#             n += number
#     return n

# T = int(input())

# for t in range (1, T+1):
#     number_s = tuple(map(int, input().split()))
#     result = sum_o(*number_s)
#     print(f'#{t} {result}')

# # swea 평균값 구하기.
# def avg(numbers) :
#     n = 0
#     for num in numbers :
#         n += num
#     n = n/10
#     return round(n)

# T = int(input())


# for t in range(1, T+1) :
#     numbers = list(map(int, input().split()))
#     result = avg(numbers)
#     print(f'#{t} {result}')

# # 큰 놈, 작은 놈, 같은 놈
# T = int(input())

# for t in range(1 ,T+1) :
#     a, b = map(int, input().split())
#     if a > b :
#         result = '>'
#     elif a == b :
#         result = '='
#     else :
#         result = '<'
#     print(f'#{t} {result}')

# # 최대수 구하기
# T = int(input())

# for t in range(1 ,T+1) :
#     numbers = list(map(int, input().split()))
#     n_max = max(numbers)
#     print(f'#{t} {n_max}')

# # 중간값 찾기

# N = int(input())

# numbers = list(map(int, input().split()))
# result = sorted(numbers)

# print(f'{result[99]}')

# # 자릿수 더하기
# N = int(input())

# answer=0
# while N > 0 :
#     answer += (N%10)
#     N = N//10

# print(answer)


# # 연월일 달력
# def is_valid_date(year, month, day):
#     # 월은 1부터 12까지의 값을 가져야 함
#     if not (1 <= month <= 12):
#         return False

#     # 각 달에 해당하는 날짜 범위 체크
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2:  # 2월은 28일까지만 고려
#         if not (1 <= day <= 28):
#             return False
#     else:
#         if not (1 <= day <= days_in_month[month - 1]):
#             return False

#     return True


# def convert_to_valid_date(date_str):
#     try:
#         year = int(date_str[:4])
#         month = int(date_str[4:6])
#         day = int(date_str[6:8])

#         if is_valid_date(year, month, day):
#             return f"{year:04d}/{month:02d}/{day:02d}"
#         else:
#             return -1
#     except ValueError:
#         return -1


# # 입력 받기
# T = int(input())  # 테스트 케이스 개수 입력

# for t in range(1, T + 1):
#     date_str = input()  # 8자리 날짜 입력

#     # 날짜 변환
#     result_date = convert_to_valid_date(date_str)

#     # 출력
#     print(f"#{t} {result_date}")

# # 알파벳을 숫자로 변환
# Word = input()
# for i in range(len(Word)) :
#     N = ord(Word[i])
#     T = N-64
#     print(f'{T}', end=' ')


# # swea 2047 신문 헤드라인
# Sentence = input()
# print(Sentence.upper())

# # swea 2046 스탬프 찍기
# n =int(input())
# print('#' * n)

# # for i in range(n):
# #     print('#', end='')

# # swea 2043 서랍의 비밀번호
# password, startnumber = map(int, input().split())
# print(password -startnumber +1 )

# # swea 2029 몫과 나머지 출력하기
# T = int(input())
# for tc in range(1, T+1):
#     a, b= map(int, input().split())
#     print(f'#{tc} {a//b} {a%b}')

# # swea 2027 대각선 출력하기
# for i in range(5):
#     for j in range(5):
#         if i == j :
#             print('#',end='')
#         else :
#             print('+',end='')
#     print()

# # swea 2025 N줄 덧셈
# n = int(input())
# plusnum = 0
# for i in range(1,n+1):
#     plusnum += i
# print(plusnum)
# # or
# n = int(input())
# print(n*(n+1)//2)

# # swea 1938 아주 간단한 계산기
# a, b= map(int, input().split())
# print(f'{a+b} \n {a-b} \n {a*b} \n {a//b}')

# # swea 1933 간단한 N의 약수
# N = int(input())
# numbers=[]
# for i in range(1, N+1):
#     if N % i == 0:
#         numbers.append(i)
# for j in (numbers):
#     print(j, end=' ')
# # or
# k = int(input())
# for i in range(1, k+1):
#     if k % i == 0:
#         print(i, end=' ')

# # swea 1936 1대1 가위바위보
# a, b = map(int, input().split())

# if a > b :
#     if a == 3 and b ==1 :
#         print('B')
#     else:
#         print('A')
# elif b > a :
#     if a == 1 and b ==3 :
#         print('A')
#     else:
#         print('B')

# swea  2019


# # swea user problem 11092
# T = int(input())
# for tc in range (1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))

#     min_idx = 0 # 최솟값의 인덱스
#     max_idx = 0
#     for i in range(1,N):
#         if arr[min_idx] > arr[i]:
#             min_idx = i
#         if arr[max_idx] <= arr[i]:
#             max_idx = i
#     print (f'#{tc} {abs(max_idx - min_idx)}')

# # swea user 9386 연속한 1의 개수
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = input().split('0')


# T = int(input())  # 테스트 케이스의 수 입력
# for tc in range(1, T+1):
#     N = int(input())  # 정수 N 입력
#     x = input().split('0')  # 입력된 정수를 0을 기준으로 분리하여 리스트로 저장

#     max_x = 0  # 가장 긴 연속된 1의 개수를 저장할 변수 초기화

#     for i in x:  # 0을 기준으로 분리된 리스트를 순회
#         if max_x < len(i):  # 분리된 부분 리스트의 길이가 현재까지 가장 긴 연속된 1의 개수보다 큰 경우
#             max_x = len(i)  # 가장 긴 연속된 1의 개수를 해당 부분 리스트의 길이로 업데이트

#     print(f'#{tc} {max_x}')  # 결과 출력


# # swea 2019 더블더블
# N = int(input())
# result = 1
# print(result, end=' ')

# for _ in range(N):
#     result = result*2
#     print(result, end=' ')

# # 다른풀이
# a = int(input())
# for i in range(0, a+1):
#     print(2**i, end=' ')

# # swea 1545 거꾸로 출력해보아요
# N = int(input())
# for i in range(N+1):
#     print(8-i, end=' ')

# # swea 1926 간단한 369게임
# N = int(input())

# for i in range(1, N+1):
#     i = str(i)
#     clap = i.count('3') + i.count('6') + i.count('9')

#     if clap == 0:
#         print(i, end=' ')
#     else:
#         print("-" * clap, end=' ')
