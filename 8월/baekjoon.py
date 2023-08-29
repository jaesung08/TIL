# # 13300 방배정
# N, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # S 성별(0-여 / 1-남) // Y 학년
# student = [[0] * 6 for _ in range(2)]
# for i in range(N):
#     S, Y = arr[i]
#     student[S][Y-1] += 1
# cnt = 0
# for i in range(2):
#     for j in range(6):
#         A = student[i][j]
#         while True:
#             if A <= 0:
#                 break
#             else:
#                 A -= K
#                 cnt += 1
# print(cnt)


# # 2309 일곱난쟁이
# arr = [int(input()) for _ in range(9)]
# A = sum(arr) - 100
#
# arr_remove = []
# def find():
#     for i in range(9):
#         for j in range(i+1, 9):
#             if arr[i] + arr[j] == A:
#                 arr_remove.append(arr[i])   # pop하고 j부터 뺐으면 진작 가능.
#                 arr_remove.append(arr[j])
#                 return
#
# find()
# for k in arr_remove:
#     arr.remove(k)
#
# arr.sort()
# for a in arr:
#     print(a)
# print()


# # 2605 줄세우기
# N = int(input())
# arr = list(map(int, input().split()))
# line = []
#
# for i in range(N):
#     line.insert((i-arr[i]), (i+1))
#
# print(*line)


# # 2669 직사각형 네개의 합집합의 면적구하기
# arr = [[0] * 101 for _ in range(101)]
# for _ in range(4):
#     y1, x1, y2, x2 = map(int, input().split())
#     for dy in range(y1, y2):
#         for dx in range(x1, x2):
#             if arr[dy][dx] == 0:
#                 arr[dy][dx] = 1
# result = 0
# for i in range(100):
#     for j in range(100):
#         result += arr[i][j]
#
# print(result)


# # 10163 색종이 // ????
# N = int(input())
# arr = [[0] * 1001 for _ in range(1001)]
# for i in range(1, N+1):
#     y, x, r, l = map(int, input().split())
#     for dy in range(y, y+r):
#         for dx in range(x, x+l):
#             if 0 <= dy < 1001 and 0 <= dx < 1001:
#                 arr[dy][dx] = i
#
# for a in range(1, N+1):
#     cnt = 0
#     for j in range(len(arr)):
#         for k in range(len(arr)):
#             if arr[j][k] == a:
#                 cnt += 1
#     print(cnt)

# # 14696 딱지놀이
# # 별 4/ 동그라미3/ 네모2/ 세모1
# N = int(input())    # N <= 1000
# for _ in range(N):
#     arr = list(map(int, input().split()))[1:]
#     brr = list(map(int, input().split()))[1:]
#
#     for i in range(4, 0, -1):   # 4부터 탐색
#         if arr.count(i) > brr.count(i):
#             print('A')
#             break
#         elif arr.count(i) < brr.count(i):
#             print('B')
#             break
#         if i == 1:          # 마지막 1까지 위의 조건을 걸쳤는데 나오지않는다면
#             print('D')
#             break

# # 2563 색종이(실버)
# grid = [[0 for _ in range(101)] for _ in range(101)]
# N = int(input())
# cnt = 0
# for _ in range(N):
#     x, y = map(int, input().split())
#     for i in range(y, y+10):
#         for j in range(x, x+10):
#             if 0 <= i <= 100 and 0 <= j <= 100:
#                 if grid[i][j] == 0:
#                     grid[i][j] = 1
#                     cnt += 1
# #
# # for k in range(100):
# #     cnt += sum(grid[k]) # 2차원배열 숫자 세는법
#
# # for k in grid:
# #     cnt += k.count(1)   #
# print(cnt)


# # 2628 종이자르기  // 가로 세로 방향 조심하기
# x, y = map(int, input().split())
# # paper = [[1]*x for _ in range(y)]
# N = int(input())
# r = [0, x]
# c = [0, y]
# for i in range(N):
#     a, l = map(int, input().split())
#     if a == 0:
#         c.append(l)
#     elif a == 1:
#         r.append(l)
#
# r.sort()
# c.sort()
#
# r_length = []
# c_length = []
# for i in range(len(r)-1):
#     r_length.append((r[i+1] - r[i]))
# for j in range(len(c)-1):
#     c_length.append((c[j+1] - c[j]))
#
# print(max(r_length) * max(c_length))


# # 2578 빙고  // 중요하니 꼭 보고 외우기
# bingo = [list(map(int, input().split())) for _ in range(5)]
# call = [list(map(int, input().split())) for _ in range(5)]
# cnt = 0
#
# def bingo_cnt(bingo):
#     line = 0
#     for r in range(5):
#         for c in range(5):
#             if c + 4 < 5 and all(bingo[r][c + k] == 0 for k in range(5)):
#                 line += 1
#             if r + 4 < 5 and all(bingo[r + k][c] == 0 for k in range(5)):
#                 line += 1
#             if r + 4 < 5 and c + 4 < 5 and all(bingo[r + k][c + k] == 0 for k in range(5)):
#                 line += 1
#             if r + 4 < 5 and c - 4 >= 0 and all(bingo[r + k][c - k] == 0 for k in range(5)):
#                 line += 1
#
#     if line >= 3:
#         return True
#     else:
#         return False
#
# # def f(arr):
# #     ans = 0
# #     for y in range(5):
# #         if sum(arr[y]) == 0:
# #             ans += 1
# #
# #     for xx in range(5):
# #         sero = 0
# #         for yy in range(5):
# #             if arr[yy][xx] == 0:
# #                 sero += 1
# #         if sero == 5:
# #             ans += 1
# #
# #     right_dae = 0
# #     left_dae = 0
# #     for l in range(5):
# #         if arr[l][l] == 0:
# #             right_dae +=1
# #         if arr[l][4-l] == 0:
# #             left_dae +=1
# #     if right_dae == 5:
# #         ans += 1
# #     if left_dae == 5:
# #         ans += 1
# #
# #     if ans >= 3:
# #         return 3
# #     else:
# #         return 0
#
# for i in range(5):
#     for j in range(5):
#         a = call[i][j]
#         for k in range(5):
#             for l in range(5):
#                 if bingo[k][l] == a:
#                     bingo[k][l] = 0
#                     cnt += 1
#                     result = bingo_cnt(bingo)
#                     if result == 1:
#                         print(cnt)
#                         exit()


# # 1244 스위치 켜고 끄기
# N = int(input())
# switch = list(map(int, input().split()))   # 0부터 N-1까지
# s = int(input())
# for _ in range(s):
#     a, b = map(int, input().split())
#     if a == 1:  # 남학생
#         for i in range(1, N//b+1):
#             if switch[(b * i) - 1] == 1:
#                 switch[(b * i) - 1] = 0
#             elif switch[(b * i) - 1] == 0:
#                 switch[(b * i) - 1] = 1
#     elif a == 2:    # 여학생
#         for i in range(1, N//2):
#             if 0<= b-1-i <N and 0<= b-1+i <N:
#                 if switch[(b - 1) -i] == switch[(b - 1) +i]:
#                     if switch[b-1+i] == 0 and switch[(b - 1) -i]  == 0:
#                         switch[(b - 1) - i] = 1
#                         switch[(b - 1) + i] = 1
#                     else:
#                         switch[(b - 1) - i] = 0
#                         switch[(b - 1) + i] = 0
#                 else:
#                     break
#         if switch[b - 1] == 0:
#             switch[b - 1] = 1
#         else:
#             switch[b - 1] = 0
#
# # print(*switch)
# cnt = 0
# for a in switch:
#     print(a, end=' ')
#     cnt += 1
#     if cnt == 20:
#         print()
#         cnt = 0

# # 2477 참외밭
# K = int(input())
# s = []
# c = []
# r = []
# for _ in range(6):
#     a, b = map(int, input().split())
#     s.append((a, b))
#     if a == 1 or a == 2:
#         c.append(b)
#     else:
#         r.append(b)
#
# area = max(r) * max(c)
#
# for i in range(6):
#     for j in range(2):
#         if s[i][1] == max(c):
#             i1 = i
#         if s[i][1] == max(r):
#             i2 = i
# a = i1 - 1
# b = i1 + 1
#
# c = i2 - 1
# d = i2 + 1
# if i1 == 0:
#     a = 5
# elif i1 == 5:
#     b = 0
# if i2 == 0:
#     c = 5
# elif i2 == 5:
#     d = 0
#
# r_length = abs(s[a][1] - s[b][1])
# l_length = abs(s[c][1] - s[d][1])
#
# total_area = area -(r_length * l_length)
# print(total_area * K)


# # 10157 자리배정
# # 가로 C, 세로 R의 좌석 0 없이 1,1 부터 C,R까지
# # 대기순서 K
# c, r = map(int, input().split())
# k = int(input())
# c2, r2 = c, r
# c0, r0 = 2, 1
#
# c1, r1 = 1, 1
# k -= 1
# # if c * r < k:
# #     print(0)
# #     exit()
#
# while k > 0:
#     while k > 0:
#         if r1 == r2:
#             r2 -= 1
#             break
#         r1 += 1
#         k -= 1
#     while k > 0:
#         if c1 == c2:
#             c2 -= 1
#             break
#         c1 += 1
#         k -= 1
#     while k > 0:
#         if r1 == r0:
#             r0 += 1
#             break
#         r1 -= 1
#         k -= 1
#     while k > 0:
#         if c1 == c0:
#             c0 += 1
#             break
#         c1 -= 1
#         k -= 1
#
# if r1 < 0 or c1 < 0:
#     print(0)
# elif r0 > r or c0 > c or c2 < 0 or r2 < 0:
#     print(0)
# else:
#     print(c1, r1)


# # 10158 개미
# # 가로 w 세로 h  (0,0) ,(w,h)
# # 개미의 좌표 (p,q)
# # t 시간 후의 x,y 의 좌표
# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
# a = (p + t) // w    # 반복된 횟수를 구해 홀수면 -1 중, 짝수면 +1 중
# b = (q + t) // h    # w,h 값 만큼 도달하지 못했을땐 나눠도 0 인것을 생각하면 이해됌.
#
# if a % 2 == 0:  # 짝수이면 + 중이기에 남은 값 그대로 반환
#     x = (p + t) % w
# else:           # 홀수이면 - 중이기에 남은 값을 최댓값에서 빼기
#     x = w - (p + t) % w
#
# if b % 2 == 0:
#     y = (q + t) % h
# else:
#     y = h - (q + t) % h
#
# print(x, y)


# # 2559 수열
# N, K = map(int, input().split())    # N: 날짜의수, K: 연속적인 날짜의 수
# arr = list(map(int, input().split()))   # 측정한 온도 / N일 만큼
# result = []
# result.append(sum(arr[:K]))
#
# for i in range(N - K):
#     result.append(result[i] - arr[i] + arr[i + K])
#
# print(max(result))


# # 2491 수열  // DP
# n = int(input())
# num = list(map(int,input().split()))
#
# #dp: i번째까지 왔을때 수열의 최대 길이-증가할때/감소할때를 고려하여 2줄로 생성
# d = [[1]*n for _ in range(2)]
#
# for i in range(1,n):
#     if num[i-1]<=num[i]: #증가할경우
#         d[0][i] = d[0][i-1]+1
#     if num[i-1]>=num[i]: #감소할경우
#         d[1][i] = d[1][i-1]+1
# print(max(map(max, d)))


# # 2527 직사각형  //  ㅋㅋ ㅋㅋ ㅋ못풀어
# # 직사각형 a, 선분b, 점c
# for _ in range(4):
#     x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
#
#     # case (d)
#     if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:    # 범위가 겹치지 않을때
#         print('d')
#         continue
#
#     elif x1 == p2 or x2 == p1:      # 한쪽 끝의 길이가 같을때
#         # case (c)
#         if q1 == y2 or q2 == y1:       # 점에서 만나는 경우
#             print('c')
#             continue
#         # case (b)
#         else:               # 아닌경우/점에서 만나는거 제외 전부 선으로 만남
#             print('b')
#             continue
#     elif q1 == y2 or q2 == y1:      # 반대로 y축 끝의 길이가 같을때
#         print('b')
#         continue
#
#     # case (a)
#     else:               # 벗어나는것도 선만 겹치는것도 아닐때
#         print('a')
#         continue


# 2564 경비원
r, c = map(int, input().split())
arr = [[0] * r for _ in range(c)]
n = int(input())
# (a,l) a = 북1, 남2, 서3, 동4
# 북이면 y=c 남이면 y=0 서면 x=0 동이면 x=r
lst = [list(map(int, input().split())) for _ in range(n)]
dx, dy = map(int, input().split())
length = []
for i in range(n):
    if lst[i][0] == 1:
        y, x = c, lst[i][1]
    elif lst[i][0] == 2:
        y, x = 0, lst[i][1]
    elif lst[i][9] == 3:
        y, x = lst[i][1], 0
    else:
        y, x = lst[i][1], r
    arr[y][x] = 1
    length.append((y.x))

if dx == 1:
    y, x = c, dy
elif dx == 2:
    y, x = 0, dy
elif dx == 3:
    y, x = dy, 0
else:
    y, x = dy, r
arr[y][x] = 2


# 2116 주사위 쌓기
'''
두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 한다.
1번 주사위 윗면의 숫자는 2번 주사위 아랫면의 숫자와 같고, 2번 주사위 윗면의 숫자는 3번 주사위 아랫면의 숫자와 같아야 한다


이렇게 쌓아 놓으면 긴 사각 기둥이 된다. 이 사각 기둥에는 4개의 긴 옆면이 있다.
이 4개의 옆면 중에서 어느 한 면의 숫자의 합이 최대가 되도록 주사위를 쌓고자 한다.
이렇게 하기 위하여 각 주사위를 위 아래를 고정한 채 옆으로 90도, 180도, 또는 270도 돌릴 수 있다.
한 옆면의 숫자의 합의 최댓값을 구하는 프로그램을 작성하시오.
'''

T = int(input())
square = [list(map(int, input().split())) for _ in range(T)]
# 0-5 1-3 2-4 마주보는 인덱스\
result = []
for j in range(6):
    sum_s = 0
    start = square[0][j]
    for i in range(T):
        tb_list = []  # 각 바닥의 숫자를 담을 리스트 생성
        index = square[i].index(start)  # 바닥의 수의 인덱스를 구함
        tb_list.append(start)   # 바닥의 수 리스트에 담기
        if index == 0 or index == 5:    # 마주보는 면(윗면)의 인덱스 선택 후
            start = square[i][5 - index]    # 새로운 바닥의 수 선언
            tb_list.append(start)           # 윗면이자 새로운 바닥의 수 리스트에 담기
        elif index == 1 or index == 3:
            start = square[i][4 - index]
            tb_list.append(start)
        elif index == 2 or index == 4:
            start = square[i][6 - index]
            tb_list.append(start)
        side = list(set(square[i]) - set(tb_list))  # 6개의 수 중에서 위아래면 제거
        sum_s += max(side)  # 남은 옆면 중 가장 큰 값 더하기

    result.append(sum_s)  # 주사위 높이만큼 반복이 끝나면 결과값 리스트에 더해두기
result.sort(reverse=True)   # 내림차순으로 정렬

print(result[0])


# # 1149 rgb 거리 // 미완성
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# result = 0
# '''
# 1번집은 2번집과 색이 달라야함
# n번집은 n-1번집과 색이 달라야함
# i번집은 i-1, i+1번집과 색이 달라야함
#
# 빨강 초록 파랑 각각의 비용
# 1    2    3
#
# 각 비용의 최솟값 출력
# '''
# k = -1
# for i in range(n):
#     small = 21e8
#     for j in range(3):
#         if j == k:
#             continue
#         if arr[i][j] <= small:
#             small = arr[i][j]
#             k = j
#
#     result += small
#
# print(result)


# 1463 1로 만들기  // dp 문제
# # 내풀이
# n = int(input())
# cnt = 0
# while n != 1:
#     cnt += 1
#     if (n - 1) % 3 == 0:
#         n -= 1
#     elif n % 3 == 0:
#         n //= 3
#     elif n % 2 == 0:
#         n //= 2
#     else:
#         n -= 1
# print(cnt)

# # dp - bottom up 풀이 / for문
# n = int(input())
# d = [0] * (n + 1)	## d에 계산된 값을 저장해둔다. n + 1이라고 한 이유는, 1번째 수는 사실 d[1]이 아니고 d[2]이기 때문에, 계산하기 편하게 d[1]을 1번째 인 것 처럼 만들어준다.
#
# for i in range(2, n + 1):
# ## 여기서 왜 if 1빼는 방법, 2 나누기, 3 나누기 동등하게 하지 않고 처음에 1을 빼고 시작하는지 의아해 할 수 있다.
# ## 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문이다.
# ## 즉 셋 다 시도하는 방법이 맞다.
#
# ## 여기서 if elif else를 사용하면 안된다. if만 이용해야 세 연산을 다 거칠 수 있다, 가끔 if continue, else continue를 쓰는 분도 계신데, 난 이게 편한듯.
#     d[i] = d[i - 1] + 1
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)	## 1을 더하는 것은 d는 결과가 아닌 계산한 횟수를 저장하는 것 이기 때문이다. d[i]에는 더하지 않는 이유는 이미 1을 뺄 때 1을 더해준 이력이 있기 때문이다.
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
# print(d[n])
#
# # dp - top down 풀이 / 재귀 사용
# x=int(input())
# dp={1:0}
# def rec(n):
#     if n in dp.keys():
#         return dp[n]
#     if (n%3==0) and (n%2==0):
#         dp[n]=min(rec(n//3)+1, rec(n//2)+1)
#     elif n%3==0:
#         dp[n]=min(rec(n//3)+1, rec(n-1)+1)
#     elif n%2==0:
#         dp[n]=min(rec(n//2)+1, rec(n-1)+1)
#     else:
#         dp[n]=rec(n-1)+1
#     return dp[n]
# print(rec(x))
#
# # bfs풀이
# x=int(input())
# Q=[x]
# visited=[0]*(x+1)
# while Q:
#     c=Q.pop(0)
#     if c==1:
#         break
#     if c%3==0 and visited[c//3]==0:
#         Q.append(c//3)
#         visited[c//3]=visited[c]+1
#     if c%2==0 and visited[c//2]==0:
#         Q.append(c//2)
#         visited[c//2]=visited[c]+1
#     if visited[c-1]==0:
#         Q.append(c-1)
#         visited[c-1]=visited[c]+1
# print(visited[1])


# 1620 포켓몬 마스터 이다솜
# 시간 초과 때문에 딕셔너리 사용해야함
# N, M = map(int, input().split())
# arr = (input() for _ in range(N))
# answer = [input() for _ in range(M)]
#
# for ans in answer:
#     if ans.isdigit():
#         ans = int(ans)
#         A = arr[ans-1]
#         print(A)
#     else:
#         for i in range(N):
#             if arr[i] == ans:
#                 print(i+1)

N, M = map(int, input().split())
dict = {}
for i in range(1, N + 1):
    a = input()
    dict[i] = a
    dict[a] = i

for j in range(M):
    answer = input()
    if answer.isdigit():
        print(dict[int(answer)])
    else:
        print(dict[answer])
