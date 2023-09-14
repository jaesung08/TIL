T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def fly_catch(y, x):
        max_fly = 0
        result = 0
        for i in range(M):
            for j in range(M):  # 파리채의 크기
                ny = y + i
                nx = x + j
                if 0 <= ny < N and 0 <= nx < N:
                    result += arr[ny][nx]
                    if max_fly <= result:
                        max_fly = result
        return max_fly

    max_result = 0
    for i in range(N):
        for j in range(N):
            Result = fly_catch(i, j)
            if max_result < + Result:
                max_result = Result
    print(f'#{tc} {max_result}')
