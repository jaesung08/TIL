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


# 2491 수열  // DP
n = int(input())
num = list(map(int, input().split()))

# dp: i번째까지 왔을때 수열의 최대 길이-증가할때/감소할때를 고려하여 2줄로 생성
d = [[1]*n for _ in range(2)]

for i in range(1, n):
    if num[i-1] <= num[i]:  # 증가할경우
        d[0][i] = d[0][i-1]+1
    if num[i-1] >= num[i]:  # 감소할경우
        d[1][i] = d[1][i-1]+1
print(max(map(max, d)))
