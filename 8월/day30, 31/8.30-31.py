# def f(i, N):
#     if i == N:
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)


# N = 5
# A = [1, 2, 3, 4, 5]
# B = [0]*N
# f(0, N)

# # 키가 있으면 1, 없으면 0을 리턴하는 함수


# def f(i, N, key, arr):
#     if i == N:
#         return 0
#     elif arr[i] == key:
#         return 1
#     else:
#         f(i+1, N, key, arr)


# N = 5
# arr = [1, 2, 3, 4, 5]
# key = 3
# f(0, N, key, arr)


# # 재귀로 순열 생성
# def f(i, N, card):
#     if i == N:   # 순열 완성
#         return
#     else:       # card[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j]==0:
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i+1, N)
#                 used[j] = 0

# card = list(map(int, input()))  # 6장의 카드 인식
# used = [0] * 6 # 이미 사용한 카드 인지 표시
# p = [0] * 6
# f(0, 6)

# # 재귀로 순열 생성2 / 좀 더 기본형
# def f(i, N, k):
#     global cnt
#     if i == k:   # i 이전에 고른 개수, N개에서 k개를 고르는 순열
#         cnt += 1
#         print(cnt, p)
#         return
#     else:       # p[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j] == 0:
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i+1, N, k)
#                 used[j] = 0


# card = [1, 2, 3, 4, 5]  # 6장의 카드 인식
# N = 5
# K = 3
# cnt = 0
# used = [0] * N  # 이미 사용한 카드 인지 표시
# p = [0] * K
# f(0, N, K)

# # 부분집합
# a = [3, 6, 7, 1, 5, 4]
# N = 6

# for i in range(1 << N):
#     subset1 = []
#     for j in range(N):
#         if i & (i << j):       # j번 비트가 0이 아니면
#             subset1.append(a[j])
#     print(*subset1)

# # 두개의 그룹으로 부분집합
# a = [3, 6, 7, 1, 5, 4]
# N = 6

# for i in range(1 << N):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (i << j):       # j번 비트가 0이 아니면
#             subset1.append(a[j])
#         else:
#             subset2.append(a[j])
#     print(subset1, subset2)

# # 두개의 그룹으로 부분집합/ 공집합 제외
# a = [3, 6, 7, 1, 5, 4]
# N = 6

# for i in range(1, 1 << N):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (i << j):       # j번 비트가 0이 아니면
#             subset1.append(a[j])
#         else:
#             subset2.append(a[j])
#     print(subset1, subset2)

# # 두개의 그룹으로 부분집합2 /// 이건뭐노
# a = [1, 2, 3, 4]
# N = 4

# # for i in range(1, (1 << N)-1)
# for i in range(1, (1 << N)//2):  # (1, (1 << (N-1))) 과 같다.
#     subset1 = []
#     subset2 = []
#     total1 = 0
#     total2 = 0
#     for j in range(N):
#         if i & (i << j):       # j번 비트가 0이 아니면
#             subset1.append(a[j])
#             total1 += a[j]
#         else:
#             subset2.append(a[j])
#             total2 += a[j]
#     print(subset1, subset2)

#     r1 = f(subset1)
#     r2 = f(subset2)
#     if r1 and r2:
#         if min_v > abs(total1-total2):


'''
programing advanced
완전탐색 알고리즘
그래프 탐색 - > 완전 탐색: 문제해결을 위해 가능한 모든 경우의 수를 탐색하는 방법
: stack, queue, DFS, BFS, 백트리킹, 분할정복, 시뮬레이션(사과먹기, 농사)
1번 최소합 : 완전탐색 + DFS
2번 전자 카드 : 완전탐색 + 순열
'''

# # swea 5188 최소합
# T = int(input())
# move = [(0, 1), (1, 0)]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visit = [[0]*N for _ in range(N)]
#
#     def DFS(y,x):
#         if y == N-1 and x == N-1:  # 도착지에 도달한 경우
#             return arr[y][x] # 현재 위치의 값 반환
#
#         if visit[y][x] != 0:    # 이미 계산한 위치인 경우 저장된 값 반환
#             return visit[y][x]
#
#         min_sum = 1e8   # 현재 위치에서 아래 또는 오른쪽으로 이동할 때의 최소 합을 찾기 위한 변수 초기화
#         for dy, dx in move: # 아래(0) 또는 오른쪽(1)으로 이동하는 경우를 반복
#             ny, nx = y + dy, x + dx  # 다음 위치 계산
#             if 0 <= ny < N and 0 <= nx < N:  # 그리드 범위 내에 있는지 확인
#                 min_sum = min(min_sum, DFS(ny, nx))  # 다음 위치로 이동하여 최소 합 계산
#
#         visit[y][x] = arr[y][x] + min_sum  # 현재 위치의 값과 아래/오른쪽 중 최소 합을 저장하여 방문 배열 업데이트
#         return visit[y][x]  # 최소 합 반환
#
#     result = DFS(0, 0)  # 시작점에서 DFS 호출하여 최소 합 계산
#     print(f'#{tc} {result}')  # 테스트 케이스 번호와 결과 출력
#
# # 강사님 풀이
# dir = [(0,1), (1,0)]
# def dfs(x, y, sum_v):
#     global result
#     # 가지치기 : 불필요한 경로 차단 -> 조건에 맞지않으면 탐색X
#     if sum_v >= result:
#         return
#     # 목표지점에 도착한 경우
#     if x == N-1 and y == N-1:
#         if sum_v < result:
#             result = sum_v
#         return
#
#     for dx, dy in dir:
#         nx, ny = x+ dx, y+ dy
#         if -1 < nx < N and -1 < ny < N:
#             dfs(nx, ny, sum_v + arr[nx][ny])
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     result = float('inf')   # 무한대표현, 음의 무한대는 -float('inf')
#     # 탐색시작
#     dfs(0, 0, arr[0][0])
#     print(f'#{tc} {result}')


# # swea 5189 전자카트 / 강사님풀이
# def cart(cur, start, total):
#     global result
#     if cur == n - 1:    # 모든 구역을 다 돌았을 경우
#         result = min(result, arr[start][0] + total)   # 총 배터리 사용량의 최소값 업데이트
#         return
#     for i in range(1, n):   # 모든 구역 탐색 => 순열
#         if visited[i] == 0 and start != i:  # 아직 방문하지 않은 구역이고, 시작구역과 다른경우
#             visited[i] = 1      #1 방문표시
#             cart(cur+1, i, total + arr[start][i])   #2 다음 구역으로 이동
#             visited[i] = 0     #3 방문표시 지우기
#
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     # arr[y][x] y 가 출발 / x 가 도착
#     visited = [0 for _ in range(n)]
#     result = float('inf')
#     cart(0, 0, 0)
#     print(f'#{tc} {result}')


# # swea 4반 정사각형반 // 같은 카운트 중에 가장 작은 값을 찾으려할때 오류 발생 // 해결
# def move(N, y, x, arr):
#     global cnt
#     cnt += 1
#     # if arr[y][x] == N**2:
#     #     return
#     for dy, dx in dir:
#         ny = y + dy
#         nx = x + dx
#         if 0 <= ny < N and 0 <= nx < N:
#             if arr[ny][nx] == arr[y][x] + 1:
#                 move(N, ny, nx, arr)
#
# T = int(input())
# dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_R = 0
#     ans = []
#     A = 1e8
#     for i in range(N):
#         for j in range(N):
#             cnt = 0
#             move(N, i, j, arr)
#             A = arr[i][j]
#             if cnt > max_R:
#                 ans = []
#                 max_R = cnt
#
#             if cnt == max_R:
#                 ans.append(A)
#     ans.sort()
#     print(f'#{tc} {ans[0]} {max_R}')
#
#
# # 강사님풀이
# dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     v = [0] * (N * N + 1)
#     for i in range(N):
#         for j in range(N):
#             for r, c in dir:
#                 # 격자내에 있어야하고, 현재 칸의 숫자 + 1이 다음 칸의 숫자인 경우
#                 if 0 <= i+r < N and 0 <= j+c < N and arr[i][j] + 1 ==arr[i+r][j+c]:
#                     v[arr[i][j]] = 1    # 연속된 숫자임을 표시
#
#     start, cnt, temp = 0, 1, 1
#     for i in range(len(v) - 1, -1, -1):
#         if v[i] == 1:   # 연속된 숫자의 경우
#             temp += 1   # 연속 카운트 증가
#         else:
#             if cnt <= temp: # 최댓값 갱싱
#                 cnt = temp
#                 start = i + 1   # 시작점 갱신
#             temp = 1    # 연속카운트 초기화
#     print(f'#{tc} {start} {cnt}')

# 그리디 알고리즘 : 각 단계에서 '지금 당장 가장 좋은 선택'을 하는 방법을 사용하는 알고리즘
# 가장 쉬운 예제 : 거스름돈 -> 가장 적은 개수의 동전으로 거슬러 준다

# # swea 4반 동전 교환
# n = int(input())
# cnt = 0
# result = 0
# while n != 0:
#     if n // 500 != 0:
#         A = (n // 500)
#         n = n % 500
#         cnt = cnt + A
#     elif n // 100 != 0:
#         B = (n // 100)
#         n = n % 100
#         cnt = cnt + B
#     elif n // 50 != 0:
#         C = (n // 50)
#         n = n % 50
#         cnt = cnt + C
#     elif n // 10 != 0:
#         D = n // 10
#         n = n % 10
#         cnt += D
# print(cnt)


# # swea 4반 배관공 콰리오
# n, L = map(int, input().split())
# leaks = list(map(int, input().split()))
# # 구멍의 위치 정렬
# leaks.sort()
# cur = leaks[0]  # 첫번째 구멍의 위치저장
# cnt = 1     # 첫번째 구멍을 막기 위해 1로 초기화
# for i in range(1, n):   # 두번째 구멍으로 부터 확인
#     if leaks[i] - cur < L:   # 현재 테이프로 다음 구멍을 막을 수 있으면 pass
#         continue
#     else:
#         # 현재 구멍의 위치를 갱신하고, 테이프 개수 1 증가
#         cur = leaks[i]
#         cnt += 1
# print(cnt)


# # swea 4반 종강파티
# n, m = map(int, input().split())
# six_min = float('inf')
# one_min = float('inf')
# for _ in range(m):
#     six_cost, one_cost = map(int, input().split())
#     # 현재까지 가장 저렴한 6병 세트와 낱개 가격 업데이트
#     six_min = min(six_min, six_cost)
#     one_min = min(one_min, one_cost)
# if one_min * 6 < six_min: # 낱개가 세트로 사는것보다 싸다면 모두 낱개로 구매
#     print(one_min * n )
# else:
#     buy = n // 6
#     n %= 6  # 6으로 나눈 나머지가 남은 병수
#     if n * one_min > six_min:   # 낱개가 세트로 사는것보다 비싸다면
#         buy += 1
#         print(buy * six_min)
#     else:
#         print(buy * six_min + one_min * n)


# # 31일 수업
# def ncr(n, r):
#     if r == 0:
#         print(tr)
#     elif n < r:     # 남은원소보다 많은 원소를 선택해야하는 경우
#         return      # 불가
#     else:
#         tr[r-1] = a[n-1]    # a[n-1]조합에 포함시키는 경우
#         ncr(n-1, r-1)
#         ncr(n-1, r)         # a[n-1]을 포함시키지 않는 경우


# N = 5
# R = 3
# a = [1, 2, 3, 4, 5]
# tr = [0]*R
# ncr(N, R)
# '''
# [3, 4, 5]
# [2, 4, 5]
# [1, 4, 5]
# [2, 3, 5]
# [1, 3, 5]
# [1, 2, 5]
# [2, 3, 4]
# [1, 3, 4]
# [1, 2, 4]
# [1, 2, 3]
# '''


# def nCr(n, r, s):
#     if r == 0:
#         print(comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             nCr(n, r-1, i+1)


# A = [1, 2, 3, 4, 5]
# N = len(A)
# R = 3
# comb = [0] * R
# nCr(N, R, 0)
# '''
# [3, 2, 1]
# [4, 2, 1]
# [5, 2, 1]
# [4, 3, 1]
# [5, 3, 1]
# [5, 4, 1]
# [4, 3, 2]
# [5, 3, 2]
# [5, 4, 2]
# [5, 4, 3]
# '''
# '''
# 배열 arr의 부분집합(subset) 중에서 원소들의 합이 0인 부분집합을 모두 찾아서
# 출력하는 재귀적인 방법을 구현한 것입니다.
# 코드의 구조는 재귀 함수를 사용하여 모든 가능한 부분집합을 생성하고,
# 해당 부분집합의 합이 0인지 검사하는 방식으로 동작합니다.
# '''


# def subset(i, N):
#     if i == N:
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += arr[j]
#         if s == 0:
#             for j in range(N):
#                 if bit[j]:
#                     print(arr[j], end=' ')
#             print()
#     else:
#         bit[i] = 1
#         subset(i+1, N)
#         bit[i] = 0
#         subset(i+1, N)
#     return


# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# N = len(arr)
# bit = [0] * N
# subset(0, N)

# 회의실 배정하기
N = 10
a = [1, 4, 1, 6, 6, 10, 5, 7, 3, 8, 5, 9, 3, 5, 8, 11, 2, 13, 12, 14]

meet = []
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
meet.sort(key=lambda x: x[1])
meet = [[0, 0]]+meet
S = []
j = 0
for i in range(1, N+1):
    if meet[i][0] > meet[j][1]:  # si >= fj
        S.append(i)
        j = i
print(S)    # [1, 4, 8, 10]


# swea 탐욕 알고리즘 컨테이너 운반
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))  # N개의 컨테이너
    t = list(map(int, input().split()))  # M개의 트럭
    w.sort(reverse=True)
    t.sort(reverse=True)
    box = [0] * N
    used = [0] * M
    result = 0

    for i in range(N):
        for j in range(M):
            if w[i] <= t[j] and box[i] == 0 and used[j] == 0:
                result += w[i]
                box[i] = 1
                used[j] = 1
                break

    print(f'#{tc} {result}')

# ---------------------------------------------------------------------------------------
# swea 탐욕 알고리즘 화물 도크
# 람다 안쓰고 풀던거
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # [[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]]
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 람다함수를 이용해서 뒷자리에 맞춰서 정렬 # [[4, 14], [8, 18], [17, 20], [20, 23], [23, 24]]
    arr.sort()
    time = 0
    cnt = 0
# [[2, 7], [2, 14], [5, 21], [7, 15], [9, 24], [11, 15], [13, 16], [13, 19],
# [13, 22], [16, 22], [17, 21], [18, 19], [20, 23], [20, 24], [23, 24]]

    for i in range(N):
        if arr[i][0] >= time:
            a = 0
            for k in range(i, N):
                if arr[i][1] <= arr[k][0]:
                    a = k
                    break
            if all(arr[i][1] <= arr[j][1] for j in range(i+1, a)):
                cnt += 1
                time = arr[i][1]
    print(f'#{tc} {cnt}')

# swea 탐욕 알고리즘 화물 도크
#  key=lambda x: x[1] 를 이용하여 뒷자리로 정렬
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])  # 람다함수를 이용해서 뒷자리에 맞춰서 정렬
    time = 0
    cnt = 0

    for i in range(N):
        if arr[i][0] >= time:
            cnt += 1
            time = arr[i][1]
    print(f'#{tc} {cnt}')


# swea 탐욕 알고리즘 베이비진 게임
def check_run(cards):
    for i in range(len(cards)):
        if (cards[i] + 1) in cards:
            if (cards[i] + 2) in cards:
                return True
    return False


def check_triplet(cards):
    for c in cards:
        if cards.count(c) >= 3:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = []
    p2 = []
    result = 0
    while lst:
        p1.append(lst.pop(0))
        p2.append(lst.pop(0))
        if result == 1 or result == 2:
            break
        if len(p1) >= 3 and len(p2) >= 3:
            if check_run(p1) or check_triplet(p1):
                result = 1
                break
            if check_run(p2) or check_triplet(p2):
                result = 2
                break

    print(f'#{tc} {result}')

# swea 4반 회의실 배정
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
time = 0
cnt = 0
for i in range(N):
    if arr[i][0] >= time:
        cnt += 1
        time = arr[i][1]

print(cnt)


# swea 4반 액체괴물 놀이
N = int(input())
arr = list(map(int, input().split()))
result = []
while arr:
    arr.sort()
    a = arr.pop(0)
    b = arr.pop(0)
    c = a+b
    arr.append(c)
    result.append(c)
    if len(arr) == 1:
        break
print(sum(result))


# swea 4반 수학 놀이
# 10을 나누면 되는데 글자를 직접빼느라 헛 수고함
a, b = map(int, input().split())
cnt = 0
c = str(b)
while a <= int(c):
    if int(c[-1]) // 2 == 0 and int(c[-1]) != 1:
        c = int(c)//2
        c = str(c)
        cnt += 1
    elif int(c[-1]) == 1 and len(c) == 2:
        c = c[:-1]
        cnt += 1
    elif int(c[-1]) // 2 >= 0 and int(c[-1]) != 1:
        c = int(c)//2
        c = str(c)
    elif int(c) < a:
        print(-1)
        break

print(cnt)

# 강사님 풀이
a, b = map(int, input().split())
cnt = 0
while b >= a:
    if b == a:
        print(cnt)
        exit()
    if b % 10 == 1:  # 1의 자리가 1인 경우 1을 제거
        b //= 10
    elif b % 2 == 0:  # 짝수 인 경우 2로 나눈다.
        b //= 2
    else:  # 이 두조건에 해당하지 않으면 만들수 없다
        print(-1)
        exit()
    cnt += 1
print(-1)
