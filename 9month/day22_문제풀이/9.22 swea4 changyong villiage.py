# # find함수는 해당노드의 최상위 부모 노드를 찾는 함수
# def find_set(node):
#     if parent[node] == node:    # 현재 노드가 자신의 루트 노드인 경우
#         return node     # 해당 노드를 반환
#     # 현재 노드가 루트가 아닌경우, 재귀적으로 부모 노드 검색
#     return find_set(parent[node]) # 최상위 부모노드 반환
#
# # union
# # 두 노드를 연결하는 함수
# def union(x, y):
#     dx = find_set(x)
#     dy = find_set(y)
#     if dx < dy:
#         parent[y] = dx
#     else:
#         parent[x] = dy
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())  # N은 사람수, M은 연결된 관계의 수
#     parent = [i for i in range(N+1)]  # 각 노드의 부모 노드
#     graph =[[] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#     for i in range(1, N+1):
#         for j in graph[i]:
#             union(i, j)
#     result = set(parent)
#     print(f'#{tc} {len(result)-1}')

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)

    group = set()
    for i in range(1, N+1):
        # 해당 사람이 그룹에 속해있지않다면, 해당 사람의 최종 그룹을 찾아 set에 추가
        if parents[i] not in group:
            x = find(i)
            if x not in group:
                group.add(x)
    print(f'#{tc} {len(group)}')


