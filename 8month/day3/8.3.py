# # 부분집합의 합 loop를 이용한 부분집합 생성
# def print_subset(bit, arr, n):
#     for i in range (n):
#         if bit[i]:
#             print(arr[i], end=' ')
#     print(bit)
#
# # # 부분집합의 합을 구하기
# # def print_subset(bit, arr, n):
# #     total = 0 # 부분집합의 합
# #     for i in range (n):
# #         if bit[i]:
# #             print(arr[i], end=' ')
# #             total += arr[i]
# #     print(bit, total)
#
# arr = [1, 2, 3, 4]
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0]=i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print_subset(bit, arr, 4)
#

#
# arr = [1, 2, 3]
#
# n = len(arr) # n: 원소의 개수
#
# for i in range(1<<n):   # 1<<n : 부분집합의 개수
#     for j in range(n):  # 원소의 수만큼 비트를 비교함
#         if i & (1<<j):  # i의 j번 비트가 1인 경우
#             print(arr[j], end=' ')  # j번 원소 출력
#     print()
# print()
#
# # 순차 검색 알고리즘
# def sequentialSearch2(a, n, key):   # 정렬 안되있을 때
#     1 <- 0
#     while i<n and a[i]!=key:
#         i <- i+1
#     if i<n :
#         return i
#     else :
#         return -1
#
#
# def sequentialSearch2(a, n, key):  # 정렬 되있을 때
#     1 <- 0
#     while i<n and a[i]<key:
#         i <- i+1
#     if i<n and a[i] == key:
#         return i
#     else :
#         return -1
#
#
# # 이진 검색 알고리즘
# def binarySearch(a, N, key):
#     start = 0
#     end =N -1
#     while start <= end :
#         middle = (start + end)//2
#         if a[middle] == key : # 검색성공
#             return true
#         elif a[middle] > key :
#             end = middle -1
#         else :
#             start = middle +1
#     return false        # 검색실패
#
#
#
# # 선택 정렬 알고리즘
# # def SelectionSort(a[], n):
# #     for i from 0 to n-2
# #         a_list[i], ... , a_list [n-1]  # 원소 중 최솟값 a[k]찾음
# #         a[i]와 a[k] 교환
#
# def selctionSort(a, N):
#     for i in range(N-1):
#         minIdx = i
#         for j in range(i+1, N):
#             if a[minIdx] > a[j]:
#                 minIdx = j
#         a[i], a[minIdx] = a[minIdx], a[i]
#
#
# # k번째로 작은 원소를 찾는 셀렉션 알고리즘
# def select(arr, k):
#     for i in range(0, k):
#         minIndex = i
#         for j in range (i+1, len(arr)):
#             if arr[minIndex] > arr[j]:
#                 minIndex = j
#         arr[i], arr[minIndex] = arr[minIndex], arr[i]
#     return arr[k-1]


# # 2일차 swea 4837 부분집합의 합 // 실패작
# import itertools
# T = int(input())
# A = list(range(1, 13))
#
# def sum_subsets(N,K):
#     cnt = 0
#     for i in range(1, N+1):
#         subsets = itertools.combinations(A, N)
#         for subset in subsets:
#             if sum(subset) == K:
#                 cnt += 1
#     return cnt
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     result = sum_subsets(N,K)
#     print(f'#{tc} {result}')
#
#


# # list2 문제풀이
# # 실습2. swea 4836 2일차 색칠하기
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
# # for k in range(N):
# # case = [list(map(int, input().split(()))) for _ in range(N)]
#
#     grid = [[0 for i in range(10)] for _ in range(10)]
#
#     for i in range(N): # 여러개의 영역을 받기위해 작성
#         r1, c1, r2, c2, color = map(int, input().split()) # 영역을 받음
#         for r in range(r1, r2 + 1): # 영역의 각 점 행
#             for c in range(c1, c2 + 1): # 영역의 각 점 열
#                 if grid[r][c] == 0: # 영역들이 0일 경우
#                     grid[r][c] = color  # color로 주어진 색으로 변환
#                 elif grid[r][c] != color: # 색이 이미 있을 경우
#                     grid[r][c] = 3  # 겹친 영역으로 보라색3으로 칠함
#
#     overlapping_count = sum(row.count(3) for row in grid)
#     print(f"#{tc} {overlapping_count}")
#
# # 강사님 풀이
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     # 10x10 격자 생성
#     arr = [[0]* 10 for _ in range(10)]
#     result = 0
#     for k in range(N):
#         red1, blue1, red2, blue2, color = map(int, input().split())
#
#         for i in range(red1, red2+1):
#             for j in range(blue1, blue2+1):
#                 arr[i][j] += color
#                 # 격자 값이 3이면 카운팅
#                 if arr[i][j] == 3:
#                     result += 1
#
#     print(f'#{tc} {result}')

# # 1. 부분집합의 합 swea 4837
# T = int(input())  # 테스트 케이스 개수를 입력 받음
#
# for tc in range(1, T + 1):  # 각 테스트 케이스마다 반복
#     N, K = map(int, input().split())  # 원소의 개수 N과 원소의 합 K 입력
#     arr = [i for i in range(1, 13)]  # 1부터 12까지의 숫자를 원소로 가진 리스트 arr 생성
#     result = 0  # 가능한 부분 집합의 개수를 저장할 변수 초기화
#
#     # 1 << 12는 이진수 1을 왼쪽으로 12비트 이동한 것이므로 2의 12승인 4096을 나타냄.
#     # 0부터 4095까지의 모든 수를 이진수로 표현하면 각 비트는 arr 리스트의 원소에 대응됨.
#     # 각 비트가 1인 경우 해당 인덱스의 원소를 부분 집합에 포함시킨다.
#     for i in range(1 << 12):
#         sum_sub = 0  # 부분 집합의 합을 저장할 변수 초기화
#         subset = []  # 부분 집합을 저장할 리스트 초기화
#
#         for j in range(12):
#             # i의 j번째 비트가 1인지 아닌지 알 수 있음.
#             # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 => 0100
#             if i & (1 << j):
#                 sum_sub += arr[j]  # 해당 인덱스의 원소를 부분 집합의 합에 더함
#                 subset.append(arr[j])  # 해당 인덱스의 원소를 부분 집합에 추가
#
#         # 부분 집합의 개수가 N이고, 부분 집합의 합이 K인 경우 결과 변수를 1 증가시킴
#         if len(subset) == N and sum_sub == K:
#             result += 1
#
#     print(f'#{tc} {result}')  # 결과 출력
#
#
# # #2. 이진탐색 swea 4839
#
# def bianry_search(pages, p):
#     start = 1
#     end = pages
#     mid = 0
#     cnt = 1
#     #만약 middle이 p와 같다면, 찾는 값 p를 찾은 것이므로 탐색을 종료
#     while p != mid :
#         mid = (start + end)//2
#         if mid > p :
#             end = mid
#         else:
#             start = mid
#         cnt += 1
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     P, Pa, Pb = map(int, input().split())
#     A = bianry_search(P, Pa)
#     B = bianry_search(P, Pb)
#     result = ''
#     if A == B:
#         result = 0
#     elif A < B:
#         result = 'A'
#     else:
#         result = 'B'
#     print(f'#{tc} {result}')
#
#
# #3. 특별한 정렬 swea 4843
# T = int(input())  # 테스트 케이스 개수를 입력 받음
#
# for tc in range(1, T + 1):  # 각 테스트 케이스마다 반복
#     N = int(input())  # 원소의 개수 N을 입력 받음
#     numbers = list(map(int, input().split()))  # N개의 정수를 입력 받아 리스트에 저장
#     result = []  # 결과를 저장할 리스트 생성
#
#     while len(numbers) > 0:  # numbers 리스트에 원소가 있는 동안 반복
#         max_value = max(numbers)  # numbers 리스트에서 최댓값을 구함
#         numbers.remove(max_value)  # 최댓값을 numbers 리스트에서 제거
#         result.append(max_value)  # 최댓값을 결과 리스트에 추가
#
#         min_value = min(numbers)  # numbers 리스트에서 최솟값을 구함
#         numbers.remove(min_value)  # 최솟값을 numbers 리스트에서 제거
#         result.append(min_value)  # 최솟값을 결과 리스트에 추가
#
#     # 결과 출력, result 리스트에서 처음 10개 원소만 출력
#     print(f'#{tc}', *result[:10])
#

'''
NxM의 격자형 공간에 K화력의 폭탄들이 설치 되어있습니다.  N은 세로 크기이며, M은 가로 크기 입니다.
여러개의 폭탄들이 동시에 터진다고 했을 때, 터지고 난 후의 모양을 알아내는 프로그램을 제작하려 합니다.
폭탄은 모두 동시에 터지며, 폭탄 이 있는곳과 상,하,좌,우 각각 k칸 만큼 퍼집니다. 벽이 있는곳은 폭발이 차단됩니다.
# : 벽 / @ : 폭탄 / _ : 빈칸 / % : 폭발
입력 예시
3 5
2
-#-#@
-#-#@
@___#
출력예시
%#_#%
%#_#%
%%%_#
입력예시
3 5
2
_#_#_
_#_#_
@_@__
출력예시
%#%#_
%#%#_
%%%%%
'''
# 내풀이 인데 x,y 바껴서 틀림
# def bomb(N, M, K, arr):
#     direct = [(0, 1), (0,-1), (-1, 0), (1, 0)]
#     for i in range(M):
#         for j in range(N):
#             if arr[i][j] == '@':
#                 arr[i][j] = '%'
#                 for dx, dy in direct:
#                     for k in range(1, K + 1):
#                         dir_x = i + k*dx
#                         dir_y = j + dy*k
#                         if 0 <= dir_x < M and 0 <= dir_y < N:
#                             if arr[dir_x][dir_y] != '#':
#                                 arr[dir_x][dir_y] = '%'
#                             else:
#                                 break
#
# N, M = map(int, input().split())
# K = int(input())
# arr = [list(input())for _ in range(N)]
# bomb(N, M, K, arr)
# for row in arr:
#     print(*row, sep='')


#
# # 강사님 풀이
# N, M = map(int, input().split())
# K = int(input())
# arr = [list(input())for _ in range(N)]
# directions = [(0,1), (0,-1), (-1,0), (1,0)]
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]=='@':
#             for dy, dx in directions:
#                 for k in range(1, K +1):
#                     ny, nx = i+ (k* dy), j+ (k* dx)
#                     if 0 <= ny < N and 0 <= nx < M :
#                         if arr[ny][nx] == '_':
#                             arr[ny][nx] = '%'
#                         if arr[ny][nx] == '#':
#                             break
#             arr[i][j]= '%'
#
# for row in arr:
#     print(*row, sep='')

'''
빙고게임은 다음과 같은 방식으로 이루어진다.
먼저 아래와 같이 5x5의 방고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다.
다음은 사회자가 부르는 수를 차례로 지워나간다
예를 들어 23, 3, 21이 불렸다면 이 세수를 지운뒤 빙고판의 모습은 다음과 같다.
'입력 예시'
첫번째 줄 부터 다서번째 줄까지 빙고판의 각 행에 적힌 숫자가 공백으로 구분되어 주어진다.
여섯번째 부터 열번째 줄까지 사회자가 부르는 숫자가 순서대로 각 줄에 5개씩 공백으로 구분되어 주어진다.
빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 숫자가 중복없이 사용된다.
'출력 예시'
첫번째 줄에 사회자가 어떤 숫자를 불렀을때 빙고가 완성되는 지 출력한다.
'''

# bingo = [list(input().split())for _ in range(5)]
# result = [list(input().split())for _ in range(5)]
#
# for i in range(5):
#     for j in range(5):
#         for k in result:
#             if bingo[i][j]== k:
#                 bingo[i][j]= '#'
#             if

# 강사님 풀이
# 빙고판입력받기
board = [int(num) for _ in range(5) for num in input().split()]
# 사회자가 번호 부르기
call = [int(num) for _ in range(5) for num in input().split()]
cnt = 0
x_lst = [0]*10
y_lst = [0]*10
di_lst1 = [0]*10
di_lst2 = [0]*10

for n in call:
    # 부른숫자의 인덱스 찾기
    a = board.index(n)
    # 인덱스를 이용해 해당 숫자의 위치 x,y 계산
    x, y = a//5, a % 5
    # 가로 세로 대각선 빙고 개수 카운트증가
    x_lst[x] += 1
    y_lst[y] += 1
    di_lst1[x + y] += 1
    di_lst2[y - x + 4] += 1
    # 빙고 개수를 확인하여 count 증가
    if x_lst[x] == 5:
        cnt += 1
    if y_lst[y] == 5:
        cnt += 1
    if di_lst1[x+y] == 5 or di_lst2[y-x+4] == 5:
        cnt += 1
    # 카운트가 3이 되면 빙고완성 후 반복문 종료
    if cnt == 3:
        print(n)
        break
