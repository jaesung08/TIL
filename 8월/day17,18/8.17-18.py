# def enQ(data):
#     global rear
#     rear += 1
#     Q[rear] = data
#
# def deQ():
#     global front
#     if front == rear :
#         print('Queue is Empty')
#     else:
#         front += 1
#         return Q[front]
#
# Qsize = 3
# Q = [0] * Qsize
# rear = -1
# front = -1
#
# enQ(1)
# enQ(2)
# rear += 1   # enQ(3) 과 같음
# Q[rear] = 3
#
# # enQ(4)
# print(deQ())    #1
# print(deQ())    #2
# print(deQ())    #3
# print(deQ())    #Queue is Empty // None
# ## 원형 상태 큐
# def enQ(data):
#     global rear
#     if (rear+1)%cQsize == front:
#         print('cQ is Full')
#     else:
#         rear = (rear+1)%cQsize
#         cQ[rear] = data
#
# def deq():
#     global front
#     front = (front + 1)%cQsize
#     return cQ[front]
#
#
# cQsize = 4
# cQ = [0] * cQsize
# front = 0
# rear = 0
#
# enQ(1)
# enQ(2)
# enQ(3)
# print(deq())    # 1
# print(deq())    # 2
# enQ(4)
# enQ(5)
# enQ(6)  # cQ is Full
# enQ(7)  # cQ is Full
# print(deq())    #3
# print(deq())    #4
# print(deq())    #5
# print(deq())    #2

# ## 참고용 / import 쓰면 편함
# from collections import deque
#
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())    #1
# print(q.popleft())    #2
# print(q.popleft())    #3
#
# 강사님 수
'''
##### 스택과 큐의 비교 // 강사님 수업
* 스택 : 후입 선출
+ 데이터 추가 : push, 데이터 삭제 : pop
* append, pop 사용
* DFS로 활용
- - -
+ 큐 : 선입 선출
* 데이터 추가 : enqueue, 데이터 삭제 : dequeue
+ append, pop(0) 사용
* BFS로 활용
'''
# from collections import deque
# d = deque()
# d.append(1)
# d.extend([10, 15, 20])
# print(d)    # deque([1, 10, 15, 20])
#
# for item in d:
#     print(item, end = ' ')  # 1 10 15 20
# print()
# print(d.popleft())    # 왼쪽끝에 요소 제거 후 반환
# d.pop()     # 오른쪽 끝 요소 제거 후 반환
# print(d)    # deque([10, 15])


# # swea 5097 회전
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     Queue = list(map(int, input().split()))
#     for i in range(M):
#         a = Queue.pop(0)
#         Queue.append(a)
#     result = Queue[0]
#     print(f'#{tc} {result}')

# # swea 4반 암호생성기
# T = 10
# for _ in range(1, T + 1):
#     tc = int(input())
#     queue = list(map(int, input().split()))
#
#     cycle = 1
#     while queue:
#         a = queue.pop(0) - cycle
#         if a <= 0:
#             a = 0
#             queue.append(a)
#             break
#         queue.append(a)
#         cycle += 1
#         if cycle > 5:
#             cycle = 1
#
#     print(f'#{tc}', *queue)
#
# # 강사님 풀이
# def pw(lst):
#     while True:
#         for i in range(1,6): # 1, 2, 3, 4, 5
#             num = lst.pop(0)
#             lst.append(num - i)
#
#             # 마지막 요소가 0이 되면 종료
#             if lst[-1] <= 0:
#                 lst[-1] = 0
#                 return lst
#
# T = 10
# for _ in range(1, T + 1):
#     tc = int(input())
#     numbers = list(map(int, input().split()))
#     result = pw(numbers)
#     print(f'#{tc}', *result)

# # 내 처음 풀이 // 강사님이랑 비슷한거같은데 왜안됌?
# T = 10
# for _ in range(1, T + 1):
#     tc = int(input())
#     queue = list(map(int, input().split()))
#
#     while queue:
#         for t in range(1, 6):
#             a = queue.pop(0)
#             b = a-t
#             queue.append(b)
#             if b <= 0:
#                 b = 0
#                 break
#
#     print(f'#{tc}', *queue)

# # sewa 4반 그래프 BFS
# arr = [
#     [0,0,0,0,1,0],
#     [1,0,1,0,0,1],
#     [1,0,0,1,0,0],
#     [1,1,0,0,0,0],
#     [0,1,0,1,0,1],
#     [0,0,1,1,0,0]
# ]
# s = int(input())
# used = [0] * 6
# def bfs(now):
#     q = []
#     q.append(now)
#     while q:
#         now = q.pop(0)
#         print(now)
#         for i in range(6):
#             if used[i] == 1: continue #이미 방문한 노드는 건너뛰기
#             if arr[now][i] == 1:
#                 used[i] = 1 # i번째 노드를 방문했다고 체크
#                 q.append(i)
# used[s] = 1 #시작 노드 방문
# bfs(s)
#
# # 강사님 풀이 /  그래프 BFS
# from collections import deque
# arr = [
#          [0, 0, 0, 0, 1, 0],
#          [1, 0, 1, 0, 0, 1],
#          [1, 0, 0, 1, 0, 0],
#          [1, 1, 0, 0, 0, 0],
#          [0, 1, 0, 1, 0, 1],
#          [0, 0, 1, 1, 0, 0]
# ]
# s = int(input())
# used = [0] * 6
# def bfs(now):
#     q = deque()
#     q.append(now)
#     while q:
#         now = q.popleft()
#         print(now)
#         for i in range(6):
#             if used[i] == 1: continue
#             if arr[now][i] ==1:
#                 used[i] = 1
#                 q.append(i)
# used[s] = 1
# bfs(s)
#
# # swea 4반 트리인접행렬
# # 강사님 풀이 / 트리 인접행렬
# from collections import deque
# arr = [
#     [0,1,0,0,1,0],
#     [0,0,1,0,0,1],
#     [0,0,0,1,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]
# ]
# k = int(input())
# def bfs(now):
#     q = deque()
#     q.append(now) #시작 노드를 큐에 추가
#     while q:
#         now = q.popleft()# 큐에서 하나의 노드를 꺼낸후 출력
#         print(now, end=' ')
#         for i in range(6): # 현재 노드와 연결된 모든 노드를 확인
#             if arr[now][i] == 1: # 현재 노드와 1번째 노드가 연결되어 있다면
#                 q.append(i) # i번째 노드를 큐에 추가
# bfs(k) #bfs(너비우선탐색) k 부터 시작


# # swea 5105 미로의 거리 // BFS 문제 !!
# T = int(input())
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 y, x = i, j
#                 break
#     def miro(y,x):
#         q = []
#         cnt = 0
#         q.append((y, x))
#         while q:
#             y, x = q.pop(0)
#             cnt += 1
#             arr[y][x] = -1
#             for dy, dx in move:
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N :
#                     if arr[ny][nx] == 3:
#                         return cnt
#                     elif arr[ny][nx] == 0:
#                         q.append((ny, nx))
#         return 0
#
#     print(f'#{tc} {miro(y,x)}')
#
# # 강사님 풀이
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
# def start():
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 return i, j
#
# def bfs(y,x):
#     queue = []
#     queue.append((y,x))     # 시작위치 큐에 추가
#     visited[y][x] = 1       # 시작 위치 방문 표시
#     while queue:
#         cy, cx = queue.pop(0)
#         if arr[cy][cx] == 3:      # 도착 위치면 거리 반환
#             return visited[cy][cx] -2   # 시작과 끝을 제외
#         for dy, dx in move:
#             ny = cy + dy
#             nx = cx + dx
#             if 0 <= ny < N and 0 <= nx < N: # 미로 범위 이내
#                 if arr[ny][nx] != 1 and visited[ny][nx] == 0:  # 벽이아니고 방문을 안한 경우
#                     visited[ny][nx] = visited[cy][cx] + 1   # 거리갱신
#                     queue.append((ny, nx))   # 큐에 추가
#     return 0    # 경로없으면 0 반환
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     si, sj = start()
#     print(f'#{tc} {bfs(si, sj)}')


# # swea 4반 원형시계 돌리기 / 오른쪽으로 돌려야해서 append말고 insert
# K = int(input())
# arr = [12, 3, 6, 9]
# angle = (K % 360) // 90
# for i in range(angle):
#     A = arr.pop()
#     arr.insert(0, A)
#
# print(arr[0], arr[3], arr[1], arr[2])
# #
# # K = int(input())
# # arr = [12, 3, 6, 9]
# # angle = (K % 360) // 90
# # for i in range(angle):
# #     A = arr.pop(0)
# #     arr.append(A)
# #
# # print(arr[2], arr[1], arr[3], arr[0])

# # swea 5099 피자굽기 / 뒤지게 어려움
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())    # 화덕 크기 및 피자 양
#     pizza_chz = list(map(int, input().split()))   # 피자의 치즈양
#     cheeze = []  #치즈
#
#
#     def pizza(N, M):
#         global cheeze
#         for i in range(M):
#             cheeze.append([i + 1, pizza_chz[i]])
#         #print(cheeze)   #[[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]]
#         oven = cheeze[:N]
#         #print(oven)    # [[1, 7], [2, 2], [3, 6]]
#         remain_pizza = cheeze[N:]
#
#         while len(oven) > 1:  # 하나 남으면 중단
#             check = oven.pop(0)  # 맨 앞의 피자를 꺼냄  [1,7]
#             check[1] //= 2  # check[0]은 인덱스 7//2
#             # check[1](남은 치즈양)이 0이면,
#             if check[1] == 0:
#                 if remain_pizza:  # 남은 피자가 있다면 넣는다
#                     oven.append(remain_pizza.pop(0))
#             else:  # 치즈가 다 안녹았으면 다시 맨뒤로 넣는다.
#                 oven.append(check)
#                 # 화덕에 마지막 남은 피자 출력
#         return oven[0][0]
#     print(f'#{tc} {pizza(N, M)}')


# #  강사님풀이
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     cheeses = list(map(int, input().split()))   # 각 피자의 초기 치즈 양
#     # 피자 인덱스(피자번호), 치즈의 양을 저장할 리스트
#     pizzas = [[i+1, p] for i, p in enumerate(cheeses)]
#     oven = pizzas[:N]
#     remain = pizzas[:N]
#
#     while len(oven) > 1:    # 화덕에 피자가 한개 남을때까지 반복
#         now = oven.pop(0)   #화덕에서 피자 꺼내기
#         # now[0] : 피자의 인덱스 번호 , now[1] : 피자의 치즈양
#         now[1] //= 2    # 치즈양을 절반으로 줄이기
#         if now[1] == 0 :    # 줄인 치즈양이 0이 될때
#             if remain:      # 남은 피자를 화덕에 넣기
#                 oven.append(remain.pop(0))
#         else: # 치즈가 다 안녹았다면, 다시 화덕에 넣기
#             oven.append(now)
#     print(f'{tc} {oven[0][0]}')


# # swea 5102 노드의 거리
# # 1 차 풀이 // 행렬이 제대로 이루어지지않아 2번 케이스가 나오지않음.
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(E)]
#     S, G = map(int, input().split())
#
#
#     def BFS(now):
#         q = []
#         visited = [0] * (V + 1)
#         q.append(now)
#         visited[now] = 0
#         while q:
#             new = q.pop(0)
#             for x, y in arr:
#                 if x == new:
#                     q.append(y)
#                     visited[y] = visited[new] + 1
#             if new == G:
#                 return visited[new]
#         return 0
#
#
#     result = BFS(S)
#     print(f'#{tc} {result}')
# ## 2차 완
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#
#     G = [[] for _ in range(V + 1)]  # 주어진 값을 2차원 행렬로 재생성
#     for _ in range(E):
#         y, x = map(int, input().split())
#         G[y].append(x)
#         G[x].append(y)
#
#     start, end = map(int, input().split())
#
#
#     def BFS(start, end):
#         q = []
#         visited = [0] * (V + 1)
#         level = [0] * (V + 1)
#         q.append(start)
#         visited[start] = 1  # 방문했는지 표시
#         while q:
#             new = q.pop(0)
#             for i in G[new]:
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     q.append(i)
#                     level[i] = level[new] + 1
#             if new == end:
#                 return level[new]
#         return 0
#
#
#     result = BFS(start, end)
#     print(f'#{tc} {result}')
#
#
# # 강사님 표시
# def bfs(start, end):
#     q = []
#     q.append((start, 0))  # 큐에 시작노드와 초기거리 넣기
#     while q:
#         n, cnt = q.pop(0)  # 현재 노드와 거리 dequeue
#
#         if not visited[n]:  # 노드를 방문하지 않았다면
#             visited[n] = 1  # 노드 방문 표시하기
#
#         for j in arr[n]:  # 현재 노드에 연결된 노드 탐색
#             if not visited[j] and j == end:  # 목표 노드에 도착
#                 return cnt + 1  # 현재 거리 +1 으로 반환
#             elif not visited[j]:  # 아직 방문하지 않은 노드라면
#                 q.append((j, cnt + 1))  # enq하기
#     return 0  # 경로가 없으면 0 반환
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     arr = [[] for _ in range(V + 1)]
#     visited = [0] * (V + 1)
#     for i in range(E):
#         n1, n2 = map(int, input().split())
#         arr[n1].append(n2)
#         arr[n2].append(n1)
#
#     S, G = map(int, input().split())
#
#     print(f'#{tc}', bfs(S, G))


# # swea 4반 결혼 정보 회사
# N = int(input())  # 가입된 사람의 수
# T = int(input())  # 연관된 관계의 수
# arr = [[] for _ in range(N + 1)]
# for i in range(T):
#     n1, n2 = map(int, input().split())  # n1 : A, n2: B 연관관계
#     arr[n1].append(n2)
#     arr[n2].append(n1)
# s = int(input())  # 주인공의 번호
# g = int(input())  # 주인공과 소개가 가능한지 알아볼 번호
# visited = [0] * (N + 1)
#
#
# def bfs(start, end):
#     q = []
#     q.append(start)
#     visited[start] = 1
#     while q:
#         s = q.pop(0)
#
#         if not visited[s]:  # 노드를 방문하지 않았다면
#             visited[s] = 1  # 노드 방문 표시하기
#
#         for j in arr[s]:
#             if j == end and not visited[j]:
#                 return 'YES'
#             elif not visited[j]:
#                 q.append(j)
#     return 'No'

# print(bfs(s, g))


# # 강사님풀이
# def bfs(start, target):
#     q = []
#     q.append(start)     # 시작위치 큐에 추가
#     visited[start] = 1
#     while q:
#         now = q.pop(0)
#         for i in range(1, N+1):
#             if arr[now][i] == 0:    # 연관이 없는 회원은 무시
#                 continue
#             if visited[i] == 1:     # 이미 방문한 회원 무시
#                 continue
#             if i == target:     # 타겟 회원을 찾을 수 있으면 YES출력
#                 print('YES')
#                 return
#             q.append(i)
#             visited[i] = 1
#     print('NO')
#
# N = int(input())
# T = int(input())
# arr = [[0] * (N+1) for _ in range(N+1)]
# visited = [0] * (N+1)
# for _ in range(T):
#     n1, n2 = map(int, input().split())  # n1 : A, n2: B 연관관계
#     arr[n1][n2] = 1
#     arr[n2][n1] = 1
# s = int(input())  # 주인공의 번호
# g = int(input())  # 주인공과 소개가 가능한지 알아볼 번호
# bfs(s, g)


# # swea 4반 출근하기 편한 지역 // 실패
# N, M = map(int, input().split())  # N: 지역의 수/ M: 버스로 이동가능한 관계의 수(배열의 수)
# arr = [[] for _ in range(N+1)]
# for i in range(M):
#     n1, n2 = map(int, input().split())
#     arr[n1].append(n2)
#     arr[n2].append(n1)
#
# R, K = map(int, input().split())  # 직장이 있는 지역 R, 출근하기 편한 버스 탑승횟수
# visited = [0] * (N + 1)
# level = [0] * (N + 1)
#
#
# def bfs(start, end):
#     q = [start]
#     visited[start] = 1
#
#     while q:
#         s = q.pop(0)
#
#         for j in arr[s]:
#
#             if not visited[s] and j == end:
#                 visited[s] = 1
#                 pass
#
#             elif not visited[j]:
#                 q.append(j)
#                 visited[s] = 1
#                 level[j] = level[s] + 1
#     return 0
#
# cnt = 0
# bfs(R, N)
#
# for l in range(1, N + 1):
#     if level[l] <= K:
#         cnt += 1
# print(cnt)

# # 강사님 풀이
# N, M = map(int, input().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
# for _ in range(M):
#     A, B = map(int, input().split())
#     arr[A][B] = 1
#     arr[B][A] = 1  # 양방향 그래프
# cnt = 0
# R, K = map(int, input().split())  # 직장이 있는 지역 R, 출근하기 편한 버스 탑승횟수
# visited = [0] * (N + 1)
#
# def bfs(node):
#     global cnt
#     q = []
#     q.append(node)
#     visited[node] = 1
#     while q:
#         now = q.pop(0)
#         if visited[now] -1 <= K:    # 탐색 깊이가 K 이하면 카운트 증가
#             cnt += 1
#         if visited[now] -1 > K:
#             break
#         for i in range(1, N+1):
#             if arr[now][i] == 0:    # 연결되지 않은 노드 건너뜀
#                 continue
#             if visited[i] > 0:      # 이미 방문한 노드 건너뜀
#                 continue
#             visited[i] = visited[now] + 1
#             q.append(i)
#     return
#
# bfs(R)
# print(cnt)


# swea 4반 최소환승
N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    arr[n1][n2] = 1
    arr[n2][n1] = 1
T = int(input())
cnt = 0
visited = [0] * (N+1)


def bfs(N, T):
    global cnt, visited
    q = []
    q.append(1)
    visited[1] = 1
    # min_visited = 0
    while q:
        now = q.pop(0)
        # if visited[now] == N:
        #     if visited[now] <= min_visited:
        #         min_visited = visited[now]

        for i in range(1, N+1):
            if i != T:
                if arr[now][i] == 0:
                    continue
                if visited[i] != 0:
                    continue

                visited[i] = visited[now] + 1
                q.append(i)
    if visited:
        return visited[N] - 1
    else:
        return -1


a = bfs(N, T)
print(a)

# swea 4반 더블 리모콘
S = int(input())
D = int(input())
