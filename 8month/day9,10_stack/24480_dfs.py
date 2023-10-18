N, M, R = map(int, input().split())  # 정점N 간선M 시작정점R
node = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (M+1)
for _ in range(1, M+1):
    u, v = map(int, input().split())  # u -간선 1 -v
    node[u][v] = 1


def dfs(start, end):
    stack = []
    stack.append(start)

    while stack:
        now = stack.pop()
        print(now)
        visited[now] = True  # 1
        for next in range(1, M+1):
            if node[now][next] == 1 and visited[next] == 0:
                stack.append(next)
    if visited[end]:
        print(next)
    else:
        print('0')


dfs(R, N)

###
N, M, R = map(int, input().split())  # 정점N 간선M 시작정점R
node = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)  # 정점의 개수에 맞게 방문 여부 리스트 초기화

for _ in range(M):
    u, v = map(int, input().split())  # u - 간선 1 - v
    node[u].append(v)
    node[v].append(u)  # 양방향 간선을 나타내기 위해 반대쪽도 추가


def dfs(start):
    stack = []
    stack.append(start)
    visited[start] = True
    order = []  # 방문한 정점 순서를 저장할 리스트

    while stack:
        now = stack.pop()
        order.append(now)  # 방문한 정점을 순서에 추가

        for next_node in node[now]:
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True

    return order


order = dfs(R)
for i in range(1, N + 1):
    if visited[i]:
        print(order.index(i) + 1)
    else:
        print(0)
