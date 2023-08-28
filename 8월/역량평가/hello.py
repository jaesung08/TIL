# # IM 문제 - 학생들의 점수 구해서 비교하기
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     correct = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     result = []
#
#     for i in range(N):
#         score = 0
#         cnt = 0
#         for j in range(M):
#             if correct[j] == arr[i][j]:
#                 cnt += 1
#                 score += cnt
#             else:
#                 cnt = 0
#         result.append(score)
#
#     print(f'#{tc} {max(result) - min(result)}')

# # A 형 마을별 인원나눠 최소값구하기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())    # 마을의 갯수
#     arr = [list(map(int, input().split())) for _ in range(N)]   # 마을간 연결
#     people = list(map(int, input().split()))       # 마을 사람들의 수
#     lst1 = []
#     lst2 = []
#     visit = [[0]*N for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if i == j:
#                 continue
#             lst1.append(i)
#             cnt += 1
#
#             if arr[i][j] == 1 and visit[i][j] == 0:
#                 lst1.append(j)
#                 cnt += 1
#                 visit[i][j] = 1
#
#             elif arr[i][j] == 1 and visit[i][j] == 0 and (lst1.count(i) or lst1.count(j)):
#                 lst2.append(j)
#                 cnt += 1
#                 visit[i][j] = 1







# A형 기지국 건설
T = int(input())
direction1 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1)]    # w는 홀수 일때 갈수 있는 방향
direction2 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1)]  # w는 짝수 일때 갈수 있는 방향
for tc in range(1, T+1):
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    stack = []
    result = []

    def DFS(cnt, arr):
        global score, result
        y, x = stack.pop()
        visit[y][x] = -1        # (h,w) 좌표 / h = 세로 w = 가로
        score += arr[y][x]
        cnt += 1
        if cnt == 4:
            c = score**2
            result.append(c)
            score = 0
            return c

        if y//2 != 0 or y == 1:
            for i, j in direction1:
                dy = y + i
                dx = x + j
                if 0 <= dy < h and 0 <= dx < w and visit[dy][dx] == 0 :
                    stack.append((dy, dx))
                    DFS(cnt, arr)
                    visit[dy][dx] = 0

        elif y//2 == 0:
            for i, j in direction2:
                dy = y + i
                dx = x + j
                if 0 <= dy < h and 0 <= dx < w and visit[dy][dx] == 0:
                    stack.append((dy, dx))
                    DFS(cnt, arr)
                    visit[dy][dx] = 0

    def DFS2(arr):
        global score, result
        y, x = stack.pop()
        visit[y][x] = -1        # (h,w) 좌표 / h = 세로 w = 가로
        score += arr[y][x]
        stack2 = []
        if y // 2 != 0 or y == 1:
            for i, j in direction1:
                dy = y + i
                dx = x + j
                if 0 <= dy < h and 0 <= dx < w and visit[dy][dx] == 0:
                    A = arr[dy][dx]
                    stack2.append(A)
                    visit[dy][dx] = -1
            stack2.sort()
            for _ in range(3):
                score += stack2.pop()
            c = score**2
            result.append(c)
            score = 0
            return 0

        elif y // 2 == 0:
            for i, j in direction2:
                dy = y + i
                dx = x + j
                if 0 <= dy < h and 0 <= dx < w and visit[dy][dx] == 0:
                    A = arr[dy][dx]
                    stack2.append(A)
                    visit[dy][dx] = -1
            stack2.sort()
            for _ in range(3):
                score += stack2.pop()
            c = score**2
            result.append(c)
            score = 0
            return 0



    for a in range(h):
        for b in range(w):
            score = 0
            stack.append((a, b))
            DFS(0, arr)
    for a in range(h):
        for b in range(w):
            score = 0
            stack.append((a, b))
            DFS2(arr)

    print(f'#{tc} {max(result)}')
# #









# # dfs없이 노가다
# T = int(input())
# direction1 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1)]    # w는 홀수 일때 갈수 있는 방향
# direction2 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1)]  # w는 짝수 일때 갈수 있는 방향
# for tc in range(1, T+1):
#     w, h = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(h)]
#
#     result = []
#     cnt = 0
#
#     for y in range(h):
#         for x in range(w):          # 1번 움직임
#             score = 0
#             visit = [[0] * w for _ in range(h)]
#             # score += arr[y][x]
#             visit[y][x] = -1
#             if y//2 != 0 or y == 1:
#                 for i, j in direction1:
#                     dy = y + i
#                     dx = x + j
#                     if 0 <= dy < h and 0 <= dx < w and visit[dy][dx] == 0:
#                         # score += arr[dy][dx]        # 2번움직이기
#                         visit[dy][dx] = -1
#                         if dy // 2 != 0 or dy == 1:
#                             for i, j in direction1:
#                                 ny = dy + i
#                                 nx = dx + j
#                                 if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0:
#                                     # score += arr[ny][nx]        # 3번움직이기
#                                     visit[ny][nx] = -1
#                                     if ny // 2 != 0 or ny == 1:
#                                         for i, j in direction1:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx] # 4번움직이기
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#                                     if dy // 2 == 0:
#                                         for i, j in direction2:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#                         if dy // 2 == 0:
#                             for i, j in direction2:
#                                 ny = dy + i
#                                 nx = dx + j
#                                 if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0:
#                                     # score += arr[ny][nx]        # 3번움직이기
#                                     visit[ny][nx] = -1
#                                     if ny // 2 != 0 or ny == 1:
#                                         for i, j in direction1:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#                                     if dy // 2 == 0:
#                                         for i, j in direction2:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#             if y//2 == 0:
#                 for i, j in direction2:
#                     dy = y + i
#                     dx = x + j
#                     if 0 <= dy < h and 0 <= dx < w and visit[dy][dx] == 0:
#                         # score += arr[dy][dx]        # 두번돌림
#                         visit[dy][dx] = -1
#                         if dy // 2 != 0 or dy == 1:
#                             for i, j in direction1:
#                                 ny = dy + i
#                                 nx = dx + j
#                                 if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0:
#                                     # score += arr[ny][nx]  # 3번움직이기
#                                     visit[ny][nx] = -1
#                                     if ny // 2 != 0 or ny == 1:
#                                         for i, j in direction1:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#                                     if dy // 2 == 0:
#                                         for i, j in direction2:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#                         if dy // 2 == 0:
#                             for i, j in direction2:
#                                 ny = dy + i
#                                 nx = dx + j
#                                 if 0 <= ny < h and 0 <= nx < w and visit[ny][nx] == 0:
#                                     # score += arr[ny][nx]  # 3번움직이기
#                                     visit[ny][nx] = -1
#                                     if ny // 2 != 0 or ny == 1:
#                                         for i, j in direction1:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#                                     if dy // 2 == 0:
#                                         for i, j in direction2:
#                                             zy = dy + i
#                                             zx = dx + j
#                                             if 0 <= zy < h and 0 <= zx < w and visit[zy][zx] == 0:
#                                                 score = arr[y][x] + arr[dy][dx] + arr[ny][nx] + arr[zy][zx]
#                                                 visit[zy][zx] = -1
#                                                 result.append(score)
#
#     A = (max(result))**2
#     print(f'#{tc} {A}')