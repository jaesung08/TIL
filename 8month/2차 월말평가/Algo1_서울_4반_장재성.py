T = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]      # 상하좌우 방향을 위한 변수 생성
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 각 조건에 대한 입력 받기

    def big():      # 처음 조건인 가장 큰 점수 구하기
        result_max = 0
        for i in range(N):
            for j in range(N):
                score1 = arr[i][j]  # 2중 for문을 통해 2차원 배열 탐색
                A = score1          # 배열의 값을 변수로서 사용하기 위해 따로 저장
                for k, l in direction:      # 상하좌우 탐색
                    for m in range(1, A+1):     # 탐색간에 배열의 값만큼 범위 증가
                        y, x = i + (k*m), j + (l*m)     # 탐색할 좌표 값 생성
                        if 0 <= y < N and 0 <= x < N:   # 배열을 벗어나는 범위 제외
                            score1 += arr[y][x]         # 각 값을 더함

                if result_max <= score1:        # 더한 값을 기존의 최대값과 비교
                    result_max = score1         # 가장 큰 값을 저장
        return result_max


    def small():    # 두번째 조건인 가장 작은 점수 구하기
        result_min = 1000000000
        for i in range(N):
            for j in range(N):
                score2 = arr[i][j]       # 2중 for문을 통해 2차원 배열 탐색
                B = score2              # 배열의 값을 변수로서 사용하기 위해 따로 저장
                for k, l in direction:      # 상하좌우 탐색
                    for n in range(1, B + 1):        # 탐색간에 배열의 값만큼 범위 증가
                        y, x = i + (k * n), j + (l * n)     # 탐색할 좌표 값 생성
                        if 0 <= y < N and 0 <= x < N:       # 배열을 벗어나는 범위 제외
                            score2 += arr[y][x]             # 각 값을 더함
                if result_min >= score2:        # 더한 값을 기존의 최소값과 비교
                    result_min = score2         # 가장 작은 값을 저장
        return result_min
    # 입력받은 두 점수의 값의 차를 출력
    print(f'#{tc} {big()-small()}')
