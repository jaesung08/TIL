# # swea 1979 어디에 단어가 들어갈 수 있을까
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]   # 빈칸은 0
#     result = 0
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 cnt += 1
#             if arr[i][j] == 0 or j == N-1:
#                 if cnt == K:
#                     result += 1
#                 cnt = 0
#
#         for j in range(N):
#             if arr[j][i] == 1:
#                 cnt += 1
#             if arr[j][i] == 0 or j == N-1:
#                 if cnt ==K:
#                     result += 1
#                 cnt = 0
#
#     print(f'#{tc} {result}')


# # swea 보충 풍선퐝 보너스게임
# T = int(input())
# move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_result = 0
#     min_result = 100000000000000
#     for i in range(N):
#         for j in range(N):
#             cnt = arr[i][j]
#             for k in range(1, N):
#                 for y, x in move:
#                     ny = i + (y*k)
#                     nx = j + (x*k)
#                     if 0 <= ny < N and 0 <= nx < N:
#                         cnt += arr[ny][nx]
#             if max_result <= cnt:
#                 max_result = cnt
#             elif min_result > cnt:
#                 min_result = cnt
#
#     print(f'#{tc} {max_result - min_result}')

# BFS/DFS
# 그래프의 구조를 분석하거나 그래프 탐색 문제
# 그래프의 모든 노드를 방문하거나, 최단 경로를 찾을때

# Union- Find
# 노드간의 집합 관계를 빠르게 파악하고 관리해야하는 경우
# union = > 두 그룹을 하나로 합친다.
# Find -> 특정 노드가 어느그룹에 속해 있는지 찾는다.

def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]


def union(x, y):
    root_x = find(x)    # x 의 루트 부모 찾기
    root_y = find(y)    # y 의 루트 부모 찾기
    if rank[root_x] > rank[root_y]:  # x의 부모랭크가 더크다면, y의 부모를 x의 루트부모로 결정
        root[root_y] = root_x
    else:
        root[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


N, Q = map(int, input().split())
rank = [0] * (N+1)  # 각 노드의 랭크를 저장하는 리스트
root = [i for i in range(N+1)]  # 각 노드의 루트 부모를 저장하는 리스트
for _ in range(Q):
    K, A, B = map(int, input().split())
    if K == 0:
        if find(A) == find(B):  # A 와 B가 같은 그룹에 속한다면
            print('YES')
        else:
            print("NO")
    else:
        union(A, B)  # A와 B를 같은 그룹으로 연결
