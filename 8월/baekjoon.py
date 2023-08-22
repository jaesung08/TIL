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

# 14696 딱지놀이
# 별 4/ 동그라미3/ 네모2/ 세모1
N = int(input())    # N <= 1000
for _ in range(N):
    a,





