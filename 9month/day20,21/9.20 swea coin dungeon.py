"""
7 6 10
0 1 5
0 2 3
1 3 2
1 4 7
2 5 5
2 6 2
"""
# 던전의 개수 n, 던전을 연결하는 경로의 수 m, 코코가 보유한 골드 k
n, m, k = map(int, input().split())
# 던전번호a, b 그리고 입장하기 위한 골드 c
# 인접 그래프 생성
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

result = []

def dfs(start, costs):
    if costs > k:
        return
    result.append(start)
    for nxt, cost in graph[start]:
        dfs(nxt, costs + cost)

dfs(0, 0)
result.sort()
result.pop(0)
print(*result)





