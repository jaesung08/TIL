# #1
# T = int(input( ))
# for tc in range(1, T+1):
#      N = int(input( ))
#      cnt = [0] * 5001	# 1-5000각 정류장을 지나는 노선수
#      for _ in range(N)	# N개의 노선에 대해
#            A, B = map(int, input().split( ))
#            for i in range(A, B+1):
#                   cnt[i] += 1	# 현재 노선의 갯수
#
#     p = int(input( ))
#     bus_stop = [int(input( ) ) for _ in range(P)
#     print(f'#{tc}, end = '')
#     for x in bus_stop
#            print(cnt[x], end = ' ')
#     print( )
#


# #2
# T = int(input())
# for tc in range(1, T+1):
#     N, K map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0 # 단어가 들어갈 수 있는 자리의 수
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[i][j]:
#                 cnt += 1
#             if j==N-1 or arr[i][j]==0:
#                 if cnt == k:
#                     ans += 1
#                 cnt = 0
#     print(ans)


# #3
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
#             for k in range(4):  # i,j 인접에 대해
#                 ni ,nj = i + di[k], j + dj[k]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     cnt += arr[ni][nj]
#             if max_v < cnt :    # i, j 인접풍선까지 더하고나면
#                 max_v =cnt
#     print(f'#{tc} {max_v}')
#
# # #3-2
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
#             for k in range(4):  # i,j 인접에 대해
#                 for p in range(1, arr[i][j]+1):
#                     ni, nj = i+di[k]*p, j+dj[k]*p
#                     if 0 <= ni < N and 0 <= nj < M:
#                         cnt += arr[ni][nj]
#             if max_v < cnt:
#                 max_v = cnt
#     print(f'#{tc} {max_V}')


# # 마법사 문제
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())
#
# max_monster = 0
# di = [1, 1, -1, -1]
# dj = [-1, 1, 1, -1]
# for i in range(N):
#     for j in range(N):
#         monster = 0
#         for k in range(4):
#             for p in range(1, K+1):
#                 ni, nj = i + di[k] * p, j + dj[k] * p
#                 monster += arr[ni][nj]
#             if max_monster < monster:
#                 max_monster = monster
# print(max_monster)
#
# 강사님풀이
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())
#
# def magic(y,x):
#     dy = [1, 1, -1, -1]
#     dx = [-1, 1, 1, -1]
#     result = 0
#     for i in range(4):
#         for j in range(1, K+1):
#                 ny = y + dy[i] * j
#                 nx = x + dx[i] * j
#                 if 0 <= ny < N and 0 <= nx < N:
#                     result += arr[ny][nx]
#     return result
# result_list = []
# for i in range(N):
#     for j in range(N):
#         result_list.append(magic(i, j))
# print(max(result_list))

# # 바이러스 문제
# T = int(input())
# for tc in range(1, T+1):
#     N, P = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     def virus(y,x):
#         dy = [0, 1, 0, -1]
#         dx = [1, 0, -1, 0]
#         result = arr[y][x]
#         for i in range(4):
#             for j in range(1, P+1):
#                     ny = y + dy[i] * j
#                     nx = x + dx[i] * j
#                     if 0 <= ny < N and 0 <= nx < N:
#                         result += arr[ny][nx]
#         return result
#
#     result_list = []
#     for i in range(N):
#         for j in range(N):
#             result_list.append(virus(i, j))
#     print(f'#{tc} {max(result_list)}')


# 사각형 그리기 게임
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def game(y, x):
        max_area = 0
        cnt = 0
        cur = arr[y][x]
        for ny in range(y, N):
            for nx in range(x, N):
                if arr[ny][nx] == cur:
                    area = (ny - y + 1) * (nx - x + 1)
                    if area > max_area:
                        max_area = area
                        cnt = 1
                    elif area == max_area:
                        cnt += 1
        return cnt
    result_list = []
    for i in range(N):
        for j in range(N):
            result_list.append(game(i, j))

    print(f'#{tc} {max(result_list)}')

    # max_area = 0
    # cnt = 0
    # for y in range(N):
    #     for x in range(N):
    #         cur = arr[y][x] # 왼쪽 위 좌표의 값
    #         # 현재위치에서 오른쪽아래로 탐색
    #         for ny in range(y, N):
    #             for nx in range(x,N):
    #                 # 동일한 숫자값을 만나면
    #                 if arr[ny][nx] == cur:
    #                     # 면적계산
    #                     area = (ny-y +1)* (nx - x +1)
    #                     # 최댓값이라면 갱신
    #                     if  area > max_area:
    #                         max_area = area
    #                         cnt = 1    # 새롭게 만든 큰 면적 사각형 1개
    #                     elif area ==max_area:
    #                         cnt += 1    # 같은 크기 면적이면 누적
    # print(f'#{tc} {cnt}')
