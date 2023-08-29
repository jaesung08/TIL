# # 슬라이싱 윈도우(sliding window)
# #1. 주로 리스트와 같은 시퀀스타입에서 일정 크기의 '윈도우'를 정한다.
# #2. 그 윈도우를 데이터의 처음부터 끝까지 움직이면서 해결한다.
#
# '''
# n개의 정수를 입력받고, 연속된 m개의 정수들의 합을 구할 때까지 최대값 구하기
# 합이 가장 큰 구간의 값은 무엇일까요? (2 <= m,n <= 100,000)
#
# input
# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3
# output
# 21
#
# '''
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# sum = 0
# for i in range(m):  # 처음 m개의 구간의 합 구하기
#     sum += arr[i]
#     max_v = sum
# for i in range(n - m):  # 가장 앞 수를 빼고 뒷 수를 더하면서 움직인다.
#     sum += arr[i + m]
#     sum -= arr[i]
#     if sum > max_v:
#         max_v = sum
# print(max_v)
#
#
# # 투 포인터(Two pointer)
# # 주로 리스트와 같은 시퀀스 타입에서 두개의 포인터를 사용하여 문제를 풀이하는 방법
# '''
# 1부터 10000사이의 n개의 자연수 중에서 연속된 숫자를 더했을때 합이 m이 되는 경우는 몇가지 인가요?
# (투 포인터 -> 구간의 크기가 정해지지 않았을때)
#
# input
# 10 5
# 1 2 3 4 2 5 3 1 1 2
#
# output
# 3
# '''
#
# n, target = map(int, input().split())
# arr = list(map(int, input().split()))
#
# cnt, sum = 0, 0
# # 투 포인터 high, low
# high, low = 0, 0
# while True:
#     if sum >= target or high == n:  # 합이 타겟보다 크거나 같다면 ( 범위 좁히기 )
#         sum -= arr[low]
#         low += 1
#     elif sum < target:      # 합이 타겟보다 작다면 ( 범위 넓히기 )
#         sum += arr[high]
#         high += 1
#     if sum == target:
#         cnt += 1
#     if low == n:
#         break
# print(cnt)


# # swea 4반 슬라이싱 윈도우
# T = int(input())
# for tc in range(1, T+1):
#     n, w = map(int, input().split())
#     arr = list(map(int, input().split()))
#     sum = 0
#     for i in range(w):
#         sum += arr[i]
#     max_value = sum
#     for j in range(n - w):
#         sum += arr[j+w]
#         sum -= arr[j]
#         if max_value <= sum :
#             max_value = sum
#             s_idx = j+1
#             e_idx = j+w
#     print(f'#{tc} {s_idx} {e_idx} {max_value}')

# # swea 4반 슬라이싱 윈도우 - 오염수 정화
# N = int(input())
# arr = list(map(int, input().split()))
# result = 21e8
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         A = arr[i] + arr[j]
#         if abs(A) == 0 or abs(A) < result:
#             result = abs(A)
#             idx1 = arr[i]
#             idx2 = arr[j]
# print(f'{idx1} {idx2}')

# # 강사님 풀이
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# # 투포인터 초기화
# left = 0
# right = n-1
# # 변수초기화
# minimum = 2e9 + 1
# ansleft = 0
# ansright = 0
# while left < right:
#     sum = arr[left] + arr[right]
#     # 합이 0 이면 두수를 출력하고 프로그램 종료
#     if sum == 0:
#         print(arr[left], arr[right])
#         exit()
#     # 절대값을 이용해서 최소차이를 찾기
#     if minimum > abs(sum):
#         minimum = abs(sum)
#         ansleft = left
#         ansright = right
#     #합이 0보다 크면 right를 줄이고, 합이 0보다 작으면 left를 늘린다.
#     if sum > 0 :
#         right -= 1
#     else:
#         left += 1
# print(arr[ansleft], arr[ansright])


# # swea 4반 슬라이싱 윈도우 - 예식장 서빙
# T = int(input())
# for tc in range(1, T+1):
#     n, r = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = 1
#     for i in range(n):
#         lst = []
#         for j in range(1, r+1):
#             a = i - j
#             b = i + j
#             if a < 0:
#                 a = n + a
#             elif b >= n:
#                 b = b - n
#             lst.append(arr[i])
#             lst.append(arr[a])
#             lst.append(arr[b])
#         if abs(len(lst) - len(set(lst))) > 2: # 조건에 맞춰 출력하는 것을 구현하지못했음
#             result = 0
#     if result:
#         print(f'#{tc} YES')
#     else:
#         print(f'#{tc} NO')

# 강사님 풀이
T = int(input())
for tc in range(1, T+1):
    n, r = map(int, input().split())
    foods = list(map(int, input().split()))
    arr = foods * 2  # 원형테이블 고려
    DAT = [0] * 201  # 각 음식의 개수를 저장할 dat
    # 시작, 끝 인덱스 초기화
    start = 0
    end = 2 * r
    flag = 0    # 서빙에 성공했는지 판단하는 변수
    # 초기 구간에서 음식의 개수를 세고 , 3개 이상 중복되는지 확인
    for k in range(start, end):
        DAT[arr[k]] += 1
        if DAT[arr[k]] > 2:
            flag = 1
            break
    # 슬랑이딩 윈도우 기법
    while end < 2 * n and flag == 0:    # end가 리스트의 끝에 도달하거나, flag가 1이 되면 종료
        DAT[arr[end]] += 1
        if DAT[arr[end]] > 2:
            flag = 1
            break
        # start 포인터가 가리키는 요소의 빈도수 1 감소
        DAT[arr[start]] -= 1
        start += 1  # start, end 1씩 증가 시켜 다음 요소로 이동
        end += 1

    if not flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')
