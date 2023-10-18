# find함수는 해당노드의 최상위 부모 노드를 찾는 함수
def find_set(node):
    if parent[node] == node:    # 현재 노드가 자신의 루트 노드인 경우
        return node     # 해당 노드를 반환
    # 현재 노드가 루트가 아닌경우, 재귀적으로 부모 노드 검색
    return find_set(parent[node]) # 최상위 부모노드 반환

# union
# 두 노드를 연결하는 함수
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y: #1. 이미 같은 집합인지 체크 (생략해도 됌
        return
    if x != y: #2. 다른 집합이면 같은 대표자로 수정
        parent[y] = x



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] # 인접행렬
parent = [i for i in range(N)] # 각 노드의 부모 노드

for i in range(N):
    for j in range(i+1, N):
        # 두 노드(i,j)가 연결되어 있지 않으면 컨디튜
        if arr[i][j] == 0:
            continue
        # 두 노드의 최상위 부모(루트)가 같다면
        if find_set(i) == find_set(j):
            print("WARNING")
            exit()
        # 두 노드 연결
        union(i, j)
# 각각 연결된 노드들을 집합으로 묶으면 하나의 집합으로 되면서 같은 부모 노드를 가지게된다.
# 이렇게 연결시킬수 있는 노드들을 엮어서 집합을 만들고 최상위부모 노드를 parent에 저장하고
# 다음 노드의 연결을 확인할 때 연결이 되어있어서 parent내 최상단 부모노드가 이미 같다면,
# warning을 출력한다.
print("STABLE")