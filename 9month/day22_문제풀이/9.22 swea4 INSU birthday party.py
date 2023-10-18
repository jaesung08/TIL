from heapq import *
## 풀다 말았음
T = int(input())
for tc in range(1, T+1):
    # N개의 집, M개의 경로, 목표 집 X
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, d = map(int, input().split())
        graph[s].append([e, d])
    print(graph)
    # 누적거리를 저장할 변수 생성

    result = []
    def bfs(start):
        q = [[start, 0]]
        visited = [0] * (N+1)
        visited[start] = 1

        while q:
            now, dist = q.pop(0)
            if now == X:
                distance.append(dist)
                return

            for nxt, nxt_dist in graph[now]:
                if visited[nxt]:
                    continue
                q.append([nxt, dist+nxt_dist])

    for i in range(1, N+1):
        distance = []
        bfs(i)
        result.append(max(distance))

    print(f'#{tc} {max(result)}')

