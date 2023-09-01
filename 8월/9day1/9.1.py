# 4366 정식이의 은행업무
# 2817 부분 수열의 합
# 1861 정사각형 방


# # swea 4반 최대상금 / 완전탐색
# T = int(input())
# for tc in range(1, T+1):
#     num, m = map(int, input().split())
#     lst = []
#     num = str(num)
#     for i in range(len(num)):
#         lst.append([num[i], i])
#
#     lst.sort()
#     print(lst)
#     for j in range(m):
#         A = lst.pop(0)
#         B = lst.pop()
#         A[1], B[1] = B[1], A[1]
#         lst.append(A)
#         lst.append(B)
#         lst.sort()
#     lst.sort(key=lambda x: x[1])
#     result = ''
#     for i in range(len(num)):
#         result += lst[i][0]
#     print(result)

# 강사님 풀이
from collections import deque
T = int(input())
for tc in range(1, T+1):
    num, c = input().split()    # 숫자판 정보, 교환횟수
    c = int(c)
    now = set([num])    # 현재 가능한 숫자판 조합을 담는 집합
    next = set()    # 다음턴
    for _ in range(c):  # 교환 횟수만큼 숫자판 자리 교환
        while now:  # 현재 가능한 모든 숫자판 조합 확인
            s = now.pop()   # 하나의 숫자판 조합을 가져오고, 리스트로 변환
            s = list(s)
            # 숫자판의 모든 자리를 서로 교환
            for i in range(len(num)-1):
                for j in range(i + 1, len(num)):
                    # 두자리를 서로 교환
                    s[i], s[j] = s[j], s[i]
                    # 교환한 결과를 next 집합에 추가
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]     # 다시 원래 자리로 돌려 놓기
        now, next = next, now
    result = max(map(int, now))
    print(f'#{tc} {result}')


# swea 4반 탈주범 검거 / BFS
'''
룩업테이블 : 미리 계산된 값을 저장해놓은 테이블(리스트)
=> 계산시간을 줄이고, 코드를 간결하게 하기위해서
'''
# 파이프 모양별로 4방향 연결 가능 여부 나타내는 리스트 -> [상, 하, 좌, 우]
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [
    1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
# 상, 하, 좌, 우 이동을 위한 dir
di, dj = [-1, 1, 0, 0], [0, 0, 1, 1]
# 상하, 좌우 매칭하기 위한 리스트(상-하, 좌-우)
opp = [1, 0, 3, 2]


dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 격자의 크기
    check = [[-1 for _ in range(M)] for _ in range(N)]  # 최단 거리를 저장할 리스트
    q = deque()  # bfs 를 위한 큐 생성
    for i in range(N):
        t = input()  # 격자를 입력 받으면서
        for j in range(M):
            if t[j] == 'W':  # W를 발견하면
                q.append((i, j))  # 큐에 추가하고
                check[i][j] = 0  # 거리를 0으로 설정
    result = 0
    while q:
        x, y = q.popleft()  # 큐에서 하나를 꺼내고, 상하 좌우로 이동
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            # 이동이 가능하고, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                q.append((nx, ny))  # 1. 큐에 추가
                check[nx][ny] = check[x][y] + 1  # 2. 거리 갱신
                result += check[nx][ny]  # 3. result 갱신
    print(f'#{tc} {result}')


# # swea 4반 물놀이를 가자 /BFS+ Queue
# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     visited = [[-1] * m for _ in range(n)]
#     q = []
#     for i in range(n):
#         tmp = input()
#         for j in range(m):
#             if tmp[j]=='W':
#                 q.append((i, j))
#                 visited[i][j] = 0
#
#     dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#     def bfs():
#         while q:
#             x, y = q.pop(0)
#             for dx, dy in dir:
#                 nx = x + dx
#                 ny = y + dy
#                 if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
#                 if visited[nx][ny] != -1: continue
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited[x][y] + 1
#
#     bfs()
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             result += visited[i][j]
#     print(f'#{tc} {result}')

dir = [(0, 1), (-1, 0), (1, 0), (0, -1)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    check = [[-1 for _ in range(M)] for _ in range(N)]
    q = deque()
    for i in range(N):
        t = input()
        for j in range(M):
            if t[j] == 'W':
                q.append((i, j))
                check[i][j] = 0
    result = 0
    while q:
        x, y, = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1
    for i in range(N):
        for j in range(M):
            result += check[i][j]

    print(f'#{tc} {result}')
