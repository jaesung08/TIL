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

# 2477 참외밭
K = int(input())
r = []
c = []
s = []
for _ in range(6):
    a, b = map(int, input().split())
    s.append(a)
    if a == 1 or a == 2:
        c.append(b)
    else:
        r.append(b)

area = max(r) * max(c)



K = int(input())
s = []
l = []
for _ in range(6):
    a, b = map(int, input().split())
    s.append((a, b))

for i in range(6):
    for j in range(2):
        if s[i][j]: