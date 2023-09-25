T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 사격횟수
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited_r = [0]* N
    visited_c = [0]* N
    result = 0
    def dfs(y, x, total):
        global result
        if y == N-1:
            result = max(result, total)
            return

        visited_c[y] = 1
        visited_r[x] = 1
        for j in range(N):
            if visited_r[j] == 0:
                dfs(y+1, j, total+arr[y+1][j])
                visited_c[y+1] = 0
                visited_r[j] = 0

    for j in range(N):
        dfs(0, j, arr[0][j])
        visited_c[0] = 0
        visited_r[j] = 0

    print(f'#{tc} {result}')

# 강사님풀이
# 2번문제 사격게임

# i: 현재행, N: 전체 행의 수, s: 현재까지의 점수 합
def func(i, N, s):
    global max_v
    if i == N: # 모든 행을 다 본 경우
        if max_v < s:
            max_v = s
    else:
        for j in range(i, N):  # 현재 행부터 마지막 행까지 순회
            p[i], p[j] = p[j], p[i]
            # 재귀호출로 다음 행으로 넘어가며 점수를 더해준다
            func(i + 1, N, s + arr[i][p[i]])
            # 백트래킹 (원래 순서로 다시 바꿔줌)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]  # 초기 순서 저장하는 리스트 p
    max_v = 0
    func(0, N, 0)
    print(f'#{tc} {max_v}')