# N= 2 # 행크기
# M = 4 # 열의 크기
# arr = [[0,1,2,3],
#        [4,5,6,7]]
#
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])


# N= 2 # 행크기
# M = 4 # 열의 크기
# arr = [[0,1,2,3],
#       [4,5,6,7]]
# for i in range(N):
#     for j in range(M):
# 	    print(arr[i][j+ (M-1-2*j)*(i%2)])

# N= 2 # 행크기
# M = 4 # 열의 크기
# arr = [[0,1,2,3], [4,5,6,7]]
# for i in range(N):
#     for j in range(M):
#         if i%2:
#
#         else:
#     print(arr[i][j])


# # 행열만들기 하면안되는 것
# N= 2 # 행크기
# M = 4 # 열의 크기
# arr = [[0]*M for _ in range(N)]
# arr2 = [[0]*M]*N # 한줄만 만들고 밑에줄에 그 갯수만큼 복사한거기 때문에 이렇게쓰면 안됌
#
# arr[0][0] = 1
# arr2[0][0] = 1
# print(arr)
# print(arr2)


# # 뿜
# N= 2 # 행크기
# M = 4 # 열의 크기
# arr = [[0,1,2,3],[4,5,6,7]]
#
# max_v
# for i in range(N):
#     row_total=0
#     for j in range(M):
#         row_total += arr[i][j]
#         if max_v < row_total:
#             max_v = row_total


# #
# '''
# 3
# 123
# 456
# 789
# '''
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# print(arr)

#
# #
# '''
# 3
# 123
# 456
# 789
# '''
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# max_v = 0 # 모든원소가 0이상이라면 0으로
# for i in range(N):
#     for j in range(N):
#         # arr [i][j] 중심으로
#         s = arr[i][j]
#         for k in range(4):
#             ni, nj = i+di[k], j+dj[k]
#             if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않도록
#                 s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s :
#             max_v = s
#
#
# ##
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total =0
# total =0
# for i in range(N):
#     total1 += arr[i][i]


# ###################################
# # 2차원 리스트 IM대비
# # 실습1. swea 16504 Gravity
# T = int(input())
# for tc in range(1, T+1):
#     # 방의 가로길이 입력
#     N = int(input())
#     grid = [[0 for i in range(N)] for _ in range(100)]
#
#     # 방의 가로길이만큼 반복
#     for i in range(N):
#         box = list(map(int, input().split()))
#         for j in range(N):
#             grid[j][box[j]] = 1
#
#
# # 강사님 풀이
# T = int(input())
# for tc in range(1, T+1):
#     # 방의 가로길이 입력
#     N = int(input())
#     arr = list(map(int, input().split())) # 각 상자들의 높이를 리스트로 생성
#     max = 0 # 최댓값을 받을 변수 0으로 생성
#     #방의 가로길이 만큼 반복
#     for i in range(N):
#         cnt = 0
#         # 현재 위치의 오른쪽에 있는 모든 상자를 확인
#         for j in range (i+1 ,N): # 첫 가로칸 바로옆부터 시작
#             # 현재위치의 상자가 오른쪽의 상자보다 높이가 크면
#             if arr[i] > arr[j]:  # 앞 가로칸 상자의 높이가 다음칸 상자의 높이보다 크다면
#                 cnt += 1    # 움직일수 있으므로 +1
#         # 최댓값
#         if max <= cnt :
#             max = cnt
#     print(f'{tc} {max}')
#
#
#
#
#
#
#
#
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

'''
3 3 5 3 1
2 2 4 2 6
4 9 2 3 4
1 1 1 1 1
3 3 5 9 2

map 배열을 하드코딩해주세요
그리고 map에서 대각선 방향의 합이 가장 큰 값이 나오는 좌표(x,y)를 출력하세요
단 대각선 방향의 합을 구하는 sum(x,y)를 만들어서 사용해주세요
sum(x,y)는 특정 좌표 (x,y)에서 대각선 방향의 합을 반환하는 함수입니다.
int sum(int x, int y)
 // (x,y)로 부터 대각선 방향의 합을 반환
'''
# 내 풀이 인데 실패함 ㅠㅠ
# def Sum(x,y):
#     max_num = 0
#     a = arr[x + 1][y + 1] + arr[x - 1][y - 1] if 0 <= y - 1 < len(arr) and 0 <= x - 1 < len(arr[0]) else 0  # 인덱스 범위 확인
#     b = arr[x - 1][y + 1] + arr[x + 1][y - 1] if 0 <= y + 1 < len(arr) and 0 <= x + 1 < len(arr[0]) else 0  # 인덱스 범위 확인
#     if a > b:
#         max_num = a
#     elif a < b:
#         max_num = b
#
#     return max_num
#
# arr = [[3, 3, 5, 3, 1],
#        [2, 2, 4, 2, 6],
#        [4, 9, 2, 3, 4],
#        [1, 1, 1, 1, 1],
#        [3, 3, 5, 9, 2]]
# total_max = 0
# coord = ()
# for i in range(5):
#     for j in range(5):
#         max_num = Sum(i,j)
#         if total_max < max_num:
#             total_max = max_num
#             coord = (i, j)
# print(coord)

# # 강사님 풀이
# arr = [[3, 3, 5, 3, 1],
#        [2, 2, 4, 2, 6],
#        [4, 9, 2, 3, 4],
#        [1, 1, 1, 1, 1],
#        [3, 3, 5, 9, 2]]
# max_result = 0
# max_x = 0
# max_y = 0
# def sum(y,x):
#     # 대각선의 방향
#     direct = [(1,1), (1,-1), (-1,1), (1,-1)]
#     result = 0
#     for i,j in direct:
#         dir_y = y + i
#         dir_x = x + j
#         if 0<= dir_y < len(arr) and 0 <= dir_x < len(arr[0]):
#             result += arr[dir_y][dir_x]
#     return result
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if sum(i, j) > max_result:
#             max_result = sum(i,j)
#             max_x, max_y = i, j
# print(max_y, max_x)

'''
4x5 사이즈의 맵(문자배열)을 준비합니다. 모든 칸의 값은 "_"(언더바)로 채워집니다.
그리고 폭탄을 투하할 좌표(y,x) 두곳을 입력받아주세요.    
그리고 두 폭탄이 터진 후의 맵을 출력해주세요
폭탄이 터지면 상하좌우 그리고 대각선 방향이 #으로 표시됩니다.
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
_ _ _ _ _
'''

# MAP = [['_'for i in range(4)]for _ in range(5)]
# N = int(input())
#
# def bomb(x,y):
#     direct = [(1,1), (1,-1), (-1,1), (1,-1), (0,1), (0,-1), (1,0), (-1,0)]
#     for i, j in direct:
#         dir_x = x + j
#         dir_y = y + i
#         if 0 <= dir_x < len(MAP) and 0 <= dir_y < len(MAP[0]):
#             MAP[dir_x][dir_y] = '#'
#
#
# for _ in range(N):
#     x, y = map(int, input().split())
#     bomb(x, y)
#
# print(MAP)

# # 2일차 swea 4837 부분집합의 합 // 미완성
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

# # swea 11315 오목판정 D3 나중에 다시 풀어보기
# def fivedol(N, list):
#     for i in range(N):
#         for j in range(N):
#             # 가로 방향 확인하기
#             if j + 4 < N and all(list[i][j + k] == 'o' for k in range(5)):
#                 return 'YES'
#             # 세로 방향 확인하기
#             if i + 4 < N and all(list[i + k][j] == 'o' for k in range(5)):
#                 return 'YES'
#             # 대각선 방향 (오른쪽 아래)
#             if i + 4 < N and j + 4 < N and all(list[i + k][j + k] == 'o' for k in range(5)):
#                 return 'YES'
#             # 대각선 방향 (왼쪽 아래)
#             if si + 4 < N and j - 4 < N and all(list[i + k][j - k] == 'o' for k in range(5)):
#                 return 'YES'
#
#     return 'No'
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     # arr = [['.' for i in range(N)] for _ range(N)]
#     arr = [input() for _ in range(N)]
#
#     result = fivedol(N, arr)
#     print(f'#{tc} {result}')
