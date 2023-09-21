from collections import deque
def bfs(start, c):
    # n은 기존값, c는 카운트 횟수
    q = deque([(start, c)])
    visited = set()
    visited.add(start)
    while q:
        n, c = q.popleft()

        if n == b:
            return c

        for nxt in (n+1, n-1, n*2, n-10):
            if nxt <= 1000000 and nxt not in visited:
                visited.add(nxt)
                q.append((nxt, c+1))


T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    result = bfs(a, 0)
    print(f'#{tc} {result}')