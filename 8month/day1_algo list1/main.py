# This is a sample Python script.
# # 버블정렬 : # 인접한 두 요소를 비교하여 큰값을 오른쪽으로 이동시키는 과정을 반복.
#
# numbers = [63, 31, 27, 11 ,25]
# def bubble(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)- i -1 ):
#             if arr[j] > arr[j+1]:
#                 arr[j, arr[i+1]] = arr[j+1],arr[j]
#
# bubble(numbers)
# print(numbers)


# # 카운팅 정렬 : 정수를 정렬하는 알고리즘, 각 숫자의 개수를 세어서 정렬
# def counting(arr):
#     max_value = max(arr)
#     # 카운트 저장할 리스트
#     count_arr = [0] * (max_value + 1 )
#
#     for num in arr:
#         count_arr[num] += 1
#
#     sorted_arr = []
#     for i, count in enumerate(count_arr):# 인덱스와 값을 쌍으로 반환
#         sorted_arr.extend([i]*count) # iterable 반복가능한 객체 추가
#
#     return sorted_arr
#
# list1 = [1, 4, 1, 2, 7, 5, 2]
# print(counting(list1))
# sorted_list = counting(list1)
# print(sorted_list)

# #순열 : 주어진 항목들로 만들 수 있는 모든 가능한 순서(튜플)
# #itertools 모듈 사용 // 교재 속 코드는 너무 복잡해지기때문에 이 방식을 사용!!
# import itertools
#
# arr = [1,2,3]
# result = list(itertools.permutations(arr))
# print(result)


# # 탐욕 알고리즘 : 각 단계에서 가장 최선의 선택을 하는 방법
# # 거스름돈을 줄 때 가장 적은 수의 동전을 사용하여 거스름돈을 주는 문제
# # 최선의 선택 : 가장 큰 단위의 동전부터 사용하는것
# # 실습 : 동전 종류가 100원, 50원, 10원 거스름돈이 380원이라면 어떻게해야 가장 적은 수의 동전으로 거스름돈을 받을까요?
#
def greedy(money, coins):
    coins.sort(reverse = True )
    # 거스름 돈의 개수를 저장할 딕셔너리
    change = {coin : 0 for coin in coins}
    for coin in coins:
        while money >= coin:
            money -= coin
            # 해당 coin(동전)의 개수를 1씩 증가
            change[coin] += 1
    return change


result = greedy(380, [100, 50, 10])
print((result))

# # swea Programing Intermediate list1 4828 min/max
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     min_num = arr[0]
#     max_num = arr[0]
#
#     for i in range(N):
#         if min_num > arr[i]:
#             min_num = arr[i]
#         if max_num <= arr[i]:
#             max_num = arr[i]
#     print(f'#{tc} {(max_num - min_num)}')
#
# # swea Programing Intermediate list1 4831 전기버스
# T = int(input())
# for tc in range(1, T+1):
#         K, N, M = map(int, input().split()) # K 정류장수, N 종점, M 층전기가 설치된 정류장 수
#         arr = list(map(int, input().split()))
#
#         ch = [0]* (N+1)
#
#         for i in arr :
#                 ch[i] += 1
#                 current = 0 # 현재위치
#                 count = 0 # 충전 횟수
#         while current < N :
#                 #갈수 있는 최대 거리 계산
#                 if  ch[current + K]:
#                         current += K
#                         count += 1
#                 #충전소 찾기
#                 else :
#                         for j in range(1, k):
#                                 # 충전소를 찾으면 충전, count 증가
#                                 if ch[current + k - j]:
#                                         current += K -j
#                                         count += 1
#                                         break
#                                 else :
#                                         count = 0
#                                         break
#         # 최대거리가 도착점보다 멀가나 같으면, 반복종료
#         if current + k >= N:
#                 current = N
#         print( f'#{tc} {count}')
#
# # 전기버스 다른풀이
#
# T = int(input())
# for tc in range(1, T+1):
#         K, N, M = map(int, input().split()) # K 정류장수, N 종점, M 층전기가 설치된 정류장 수
#         arr = list(map(int, input().split()))
#         # curr : 현재위치 ,cnt : 충전횟수
#         curr, cnt = 0, 0
#         # 종점 도착할 때 까지 반복
#         while curr != N:
#                 # curr+ k : 한번 충전으로 갈 수 있는 거리, N : 종점까지 거리
#                 if N <= curr + k:
#                         curr = N
#                         break
#                 # 충전소 뒤에서 부터 순회
#                 for i in range(len(arr)-1, -1, -1):
#                         # 리스트 arr 의 값이 curr+k(한번 충전으로 갈 수 있는 거리) 이내에 있다면
#                         if arr[i] <= curr + k:
#                                 cnt += 1 # 충전횟수 증가
#                                 curr = arr[i] # 현재 위치를 충전소 위치로 변경
#                                 arr = arr[i+1:] # 해당 충전소 이후의 정류장만 남기기
#                                 break
#                         # 충전소를 찾지 못한다면
#                         if i == 0 :
#                                 cnt = 0
#                                 curr = N # 현재위치를 종점으로
#
#         print(f'#{tc} {cnt}')
#
#
#


# swea Programing Intermediate list1 4834 숫자 카드
# T = int(input())
#
# for i in range(1, T +1):
#         N = int(input())
#         cards = input()
#         # 숫자의 등장 횟수를 저장할 딕셔너리 생성
#         counts = {str(n) : 0 for n in range(10)}
#         # 각 숫자의 등장 횟수를 세기
#         for card in cards:
#             counts[card] += 1
#         max_count = max(counts.values())
#         # max_count와 같은 횟수를 가진 숫자들 중 가장 큰 숫자를 찾는다.
#         max_number = max([int(num) for num, count in counts.items() if count == max_count])
#         print(f'#{i} {max_number} {max_count}')

# # swea Programing Intermediate list1 4835 구간 합
#
# T = int(input())
#
# for i in range(1, T + 1 ):
#         N, M = map(int, input().split())
#         arr = list(map(int, input().split()))
#         new_arr = []
#
#         for j in range(N - M + 1) :
#                 result = 0
#             #j부터 j+M까지의 합
#                 for k in range(j ,j+M):
#                         result += arr[k]
#                 new_arr.append(result)
#         max_arr = max(new_arr)
#         min_arr = min(new_arr)
#         print(f'#{i} {max_arr - min_arr}')
#



#
# money = 380
# def money_calculate(money) :
#         if money < 10 :
#            return money
#
#         if money > 100 :
#             h = money // 100
#             remain_money = money % 100
#
#         if 100 > money > 10 :
#             h = money // 10
#             remain_money = money % 10
#
#         return (h) + money_calculate(remain_money)
#
# print(money_calculate(money))




# swea Programing Intermediate list1 4828 min/max
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     min_num = arr[0]
#     max_num = arr[0]
#
#     for i in range(N):
#         if min_num > arr[i]:
#             min_num = arr[i]
#         if max_num <= arr[i]:
#             max_num = arr[i]
#     print(f'#{tc} {(max_num - min_num)}')


# swea Programing Intermediate list1 4831 전기버스
# T = int(input())
# for tc in range(1, T+1):
#     K,N,M = map(int, input())
