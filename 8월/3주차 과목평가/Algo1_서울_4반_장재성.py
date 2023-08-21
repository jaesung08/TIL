T = int(input())
for tc in range(1, T+1):  # 입력 모두 받기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]    # 기준점 상하좌우를 위한 좌표 입력
    dj = [1, 0, -1, 0]

    result = 0

    for i in range(N):  # 각 행렬을 순회할때
        for j in range(N):
            cnt = 0  # 봉우리 주변 중에 봉우리도 낮은 곳
            A = 0   # 봉우리 주변의 개수
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    A += 1      # 생성되는 봉우리 주변 땅
                    if arr[i][j] > arr[ni][nj]:
                        cnt += 1    # 생성된 땅중에 봉우리보다 낮은곳
            if A == cnt:       # 봉우리 주변 땅의 수와 낮은곳의 수가 일치한다면
                result += 1

    print(f'#{tc} {result}')


# 강사님 풀이
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T+1):  # 입력 모두 받기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            high_fd = False
            for i in range(4):
                ny, nx = y+dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[y][x] <= arr[ny][nx]:
                        high_fd = True
                        break
            if not high_fd:  # 더 높은지역을 찾지 못했다면 봉우리로 간주
                cnt += 1
    print(f'#{tc} {cnt}')

'''
각 비교가 아닌 하나라도 높은거나 같은곳이 있다면 봉우리가 아닌것으로 간주할 수 있기때문에
상하좌우 방향을 돌렸을때 높거나 같은곳이 하나도 없었다면 봉우리로 인정해준다.
나는 각 비교하여 하였음
'''
# for else 구조로 else부분은 for 루프가 중간에 break 없이 정상적으로 끝나면 실행
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
T = int(input())
for tc in range(1, T+1):  # 입력 모두 받기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):

            for i in range(4):
                ny, nx = y+dy[i], x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:  # 인접지역 지도 내부
                    if arr[y][x] <= arr[ny][nx]:
                        break
                    # for else 구조로 else부분은 for 루프가 중간에 break 없이 정상적으로 끝나면 실행
            else:  # 상하좌우 인접 지역이 현재 지역보다 낮은 경우
                cnt += 1

    print(f'#{tc} {cnt}')
