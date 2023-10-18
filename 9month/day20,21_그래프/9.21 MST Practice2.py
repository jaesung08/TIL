# 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르기
# heapq도 가능, 이번엔 sort사용
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51

'''

V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f, t, w])
# w를 기준으로 정렬
edge.sort(key=lambda x: x[2])

# 사이클 발생 여부를 union find 로 해결
parents = [i for i in range(V)]


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        # print('사이클발생')
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생 하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # MST구성이 끝나면
        if cnt == V:
            break
print(f'최소비용 = {sum_weight}')