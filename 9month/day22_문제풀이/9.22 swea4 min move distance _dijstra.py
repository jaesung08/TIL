import heapq
T = int(input())
def dijkstra(start):
    # 우선순위 큐 생성
    q = []
    # 출발점 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 이미 방문한 지점 or 누적거리가 더 짧게 방문한 적 있다면 pass
        if distance[now] < dist:
            continue
        # 인접노드 확인
        for nxt, nxt_distance in graph[now]:
            # 누적거리 생성
            new_distance = dist + nxt_distance
            # 누적거리가 기존 거리보다 크다면 continue
            if distance[nxt] <= new_distance:
                continue

            distance[nxt] = new_distance
            heapq.heappush(q, (new_distance, nxt))

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(M)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append([e, c])

    # 누적거리를 저장할 변수 생성
    INF = float('inf')  # 엄청 큰 수를 저장
    distance = [INF] * (N+1)

    dijkstra(0)
    print(f'#{tc} {distance[N]}')
