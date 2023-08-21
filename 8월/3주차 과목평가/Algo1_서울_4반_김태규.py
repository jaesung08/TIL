T = int(input())
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]                  # 상하좌우 네칸을 확인하기 위한 방향배열
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0                                         # 결과값을 저장할 숫자 자료
    for y in range(N):
        for x in range(N):                          # 2차원 배열 탐색
            is_top = True                           # 각 칸에 대하여 봉우리인지 판단할 Flag
            for dy, dx in direction:                # 상하좌우 네칸을 확인
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:     # 상하좌우가 2차원 배열의 인덱스를 벗어나는지 확인
                    if arr[ny][nx] >= arr[y][x]:    # 만약 상하좌우 값 중 크거나 같은 값이 있다면 봉우리가 아님
                        is_top = False
            if is_top:
                cnt += 1                            # 봉우리임이 확인되면, 결과값에 1을 더하고 다음 지점을 탐색
    print(f'#{tc} {cnt}')
