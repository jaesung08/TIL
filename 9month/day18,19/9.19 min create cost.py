def func(cur, total):
    global min_v
    #가지치기 : 현재까지의 비용이 이미 알려진 최소비용보다 크면 더 볼 필요가 없다
    if total > min_v:
        return
    #최소비용 업데이트
    if cur == n:
        min_v = min(min_v, total)
        return
    # 현재 제품을 각 공장에 할당하는 경우 모두 고려
    for i in range(n):
        if visited[i] == 1: #해당 공장이 이미 할당된 경우는 생략
            continue
        visited[i] = 1 #현재 공장을 할당했다고표시
        func(cur + 1, total + arr[cur][i]) # 다음제품으로 넘어가기
        visited[i] = 0 # 백트래킹

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0 for _ in range(n)]
    min_v = float('inf')
    func(0, 0)
    print(f'#{tc} {min_v}')