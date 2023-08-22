def fivedol(N, list):
    for i in range(N):
        for j in range(N):
            # 가로 방향 확인하기
            if j + 4 < N and all(list[i][j + k] == 'o' for k in range(5)):
                return 'YES'
            # 세로 방향 확인하기
            if i + 4 < N and all(list[i + k][j] == 'o' for k in range(5)):
                return 'YES'
            # 대각선 방향 (오른쪽 아래)
            if i + 4 < N and j + 4 < N and all(list[i + k][j + k] == 'o' for k in range(5)):
                return 'YES'
            # 대각선 방향 (왼쪽 아래)
            if i + 4 < N and j - 4 < N and all(list[i + k][j - k] == 'o' for k in range(5)):
                return 'YES'

    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr = [['.' for i in range(N)] for _ range(N)]
    arr = [input() for _ in range(N)]

    result = fivedol(N, arr)
    print(f'#{tc} {result}')