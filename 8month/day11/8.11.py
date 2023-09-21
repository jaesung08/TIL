# # 강사님 기출 _ DFS 시작하기
# n = int(input()) # 노드의 개수
# Aij = [list(map(int, input().split())) for _ in range(n)] # 인접행렬 입력
# visited = [0 for _ in range(n)]
#
# def dfs(v):
#
#     visited[v] = 1
#     print(v, end=' ')
#     for j in range(n):
#         if Aij[v][j] == 1 and visited[j] == 0:
#             dfs(j)
#
# dfs(0)
#
# # 강사님 풀이
# n = int(input()) # 노드의 개수
# arr = [list(map(int, input().split())) for _ in range(n)] # 인접행렬 입력
#
# def dfs(now):
#     print(now, end=' ')     # 현재 방문한 노드 출력
#     for i in range(n):
#         if arr[now][i] == 1:   # 현재 노드와 i 번째 노드가 연결되어 있다면
#             dfs(i)
#
#
# dfs(0)
#
# '''---------------------------------------------------------------'''

# # 강사님 기출 _ 2층에서 경로출력
# n = int(input())
# Aij = [list(map(int, input().split())) for _ in range(n)] # 인접행렬 입력
# visited = [0] * 3 # 현재경로에서 방문한 노드를 저장할 리스트
#
# def dfs(now, level):
#     global visited
#     visited[level] = str(now)   # 현재 방문한 노드를 저장
#     if level == 2:      # 모든 노드를 방문했으면, 노드를 출력
#         print(' '.join(visited))
#     for i in range(n):
#         if Aij[now][i] == 1:     #연결되어있따면
#             dfs(i, level+1)
#
#
# dfs(0, 0)

# # stack으로 풀기
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# def DFS(n, V, adj_m):
#     stack = []  #stack 생성
#     visited = [0] * (V+1) #방문점 생성
#     visited[n] = 1 #시작점 방문 표시
#
#     while True:
#         for w in range(1, V): # 현재 정점 n에 인접하고 미방문 w 찾기
#             if adj_m[n][w] == 1 and visited[w] == 0:
#                 stack.append(n)
#
#                 n = w  #새로 옮겨갈 위치 w
#                 stack.append(n)
#                 if len(stack) == 3:
#                     for i in stack:
#                         print(i, end = ' ')
#                     print()
#                 stack.pop()
#
#                 visited[n] = 1 # w 방문 표시
#                 break # for w,n에 인접인 c찾은경우
#         else:
#             if stack: #스택에 지나온 정점이 남아있으면
#                 n = stack.pop() #pop해서 다른 w찾을 준비
#             else: #스택이 비어있으면
#                 break #탐색끝
#     return
#
# DFS(0, n, arr)

# # 강사님 기출_ 탐정
# n = int(input())
#
# evid = [-1, 0, 0, 1, 2, 4 ,4]
# time = [8, 3, 5, 6, 8, 9, 10]
# stack = []
#
# def dfs(now):
#     global stack
#     next = evid[now]
#     stack.append(now)
#     if now == 0:
#         for i in range(len(stack)):
#             a = stack.pop()
#             b = time[a]
#             if a == 0:
#                 print(f'{a}번index(출발)')
#             else:
#                 print(f'{a}번index({b}시)')
#         return
#     dfs(next)
#
# dfs(n)
#
# # # 강사님 풀이
# n=int(input())
# evid = [-1, 0, 0, 1, 2, 4 ,4]
# times = [8, 3, 5, 6, 8, 9, 10]
#
# def dfs(idx, time):
#     if evid[idx] == -1:
#         print(f'{idx}번index(출발)')
#         return
#
#     dfs(evid[idx], times[idx])
#     print(f'{idx}번index({times[idx]}시)')
#
# dfs(n, times[n])




# 강사님 기출 _ 그래프 순회
n, k = map(int, input().split())
s = int(input())
arr = [[[0] * n] for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a].append(b)

def dfs(a):
    print(a, end=' ')
    b = arr[a]
    dfs(b)
dfs(a)




# # 강사님 기출 _ 바이러스
# N = int(input())
# M = int(input())
#
# arr = [[0]*N for _ in range(N)]
# visited = [0] * N
#
# for _ in range(N):
#     c1, c2 = map(int, input().split())
#     arr[c1-1][c2-1] = arr[c2-1][c1-1] = 1
#
# def dfs(v):
#     visited[v] = 1
#     for i in range(N):
#         if arr[v][i] == 1 and visited == 0:
#             dfs(i)
#
# dfs(0)
# print(sum(visited)-1)
#
# ## 2번 풀이
# N = int(input())
# M = int(input())
#
# arr = [[0]*N for _ in range(N)]
# visited = [0] * N
# cnt = 0
#
# for _ in range(N):
#     c1, c2 = map(int, input().split())
#     arr[c1].append(c2)
#     arr[c2].append(c1)
# visited[1]=1
# def dfs(c1):
#     global cnt
#     for i in arr[c1]:
#         if not visited[i]:
#             visited[i] = 1
#             cnt += 1
#             dfs(i)
# dfs(1)
# print(cnt)
























