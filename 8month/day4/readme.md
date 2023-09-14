# 8.4
## 문제풀이
* 삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5000번까지 번호가 붙어있다.
* 그리고 버스노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고, Bi이하인 모든 정류만을 다니는 버스 노선이다.
* P개의 버스 정류장에 대해 각 정류장에 몇개의 버스노선이 다니는지 구하는 프로그램을 작성하라.
+ 첫번째 줄에는 테이스 케이스의 수T가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 <= N <= 500 )이 주어진다. 다음 N개의 줄의 i번째 줄에는 두정수 A B(1<= A <= B <= 5000)가 공백 하나로 구분되어 주어진다. 다음 줄에는 하나의 정수 P( 1<= P <= 500)가 주어진다. 다음 P개의 줄 j번째 줄에는 하나의 정수 C(1<= C <= 5000)가 주어진다.
```py
T = int(input( ))
for tc in range(1, T+1):
     N = int(input( ))
     cnt = [0] * 5001	# 1-5000각 정류장을 지나는 노선수
     for _ in range(N)	# N개의 노선에 대해
           A, B = map(int, input().split( ))
           for i in range(A, B+1):
                  cnt[i] += 1	# 현재 노선의 갯수

    p = int(input( ))
    bus_stop = [int(input( ) ) for _ in range]
    print(f'#{tc},' end = ' ')
    for x in bus_stop
           print(cnt[x], end = ' ')
    print( )


```

## #2
* N x N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다. 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
* N은 5이사 15이하의 정수이다.
* K는 2이상 N 이하의 정수이다.
+ 입력은 첫 줄에 총 테스트 케이스 개수 T가 온다. 다음줄 부터 각 테스트 케이스가 주어진다. 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N과 단어의 길이 K가 주어진다. 테스트 케이스의 두번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다. 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0으로 주어진다.

```py
T = int(input())
for tc in range(1, T+1):
    N, K map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 단어가 들어갈 수 있는 자리의 수
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            if j==N-1 or arr[i][j]==0:
                if cnt == k:
                    ans += 1
                cnt = 0
    print(ans)
```

## #3 swea 16268 풍선팡2
* 종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다. 다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다. NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오. (3<=N, M<=100)
+ 입력
* 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.
+ 출력
* #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.


```py
# #3
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i,j 인접에 대해
                ni ,nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if max_v < cnt :    # i, j 인접풍선까지 더하고나면
                max_v =cnt
    print(f'#{tc} {max_v}')

# #3-2
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j] # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i,j 인접에 대해
                for p in range(1, arr[i][j]+1):
                    ni, nj = i+di[k]*p, j+dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_V}')
```

'''
N x N 의 사각형의 전투장에는 각 칸마다 몇 마리의 몬스터가 있는지 적혀있다. 광대한 영역에 마법을 시전할 수 있는 마법사 Mort는 전투장에서 최대한 많은 몬스터를 잡으려한다.
마법사 Mort는 대각선 방향으로 각 방향마다 K칸 만큼 마법을 시전할 수 있다.

마법은 마법사가 있는 지점에서 마법을 시전한 위치를 제외하고, 대각선 방향으로 방향 변화 없이 시전된다.
마법사 Mort씨가 마법을 한번 시전하여 처치할 수 있는 몬스터의 최대수를 출력하시오.
![Alt text](<마법사 사냥.jpg>)
```py
 N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

def magic(y,x):
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    result = 0
    for i in range(4):
        for j in range(1, K+1):
                ny = y + dy[i] * j
                nx = x + dx[i] * j
                if 0 <= ny < N and 0 <= nx < N:
                    result += arr[ny][nx]
    return result
result_list = []
for i in range(N):
    for j in range(N):
        result_list.append(magic(i, j))
print(max(result_list))
```
'''
![Alt text](<사각형 그리기.png>)
```py
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_area = 0
    cnt = 0
    for y in range(N):
        for x in range(N):
            cur = arr[y][x] # 왼쪽 위 좌표의 값
            # 현재위치에서 오른쪽아래로 탐색
            for ny in range(y, N):
                for nx in range(x,N):
                    # 동일한 숫자값을 만나면
                    if arr[ny][nx] == cur:
                        # 면적계산
                        area = (ny-y +1)* (nx - x +1)
                        # 최댓값이라면 갱신
                        if  area > max_area:
                            max_area = area
                            cnt = 1    # 새롭게 만든 큰 면적 사각형 1개
                        elif area ==max_area:
                            cnt += 1    # 같은 크기 면적이면 누적
    print(f'#{tc} {cnt}')
```
5
1 2 3 5 10
9 7 2 2 9
0 0 1 5 7
5 2 3 2 2
1 1 1 1 1
2

4
7 3
1 8 1 4 2 5 1
1 5 2 6 7 2 3
7 9 5 5 1 9 8
3 7 0 9 8 0 7
5 5 3 9 5 1 4
2 5 9 3 3 6 8
0 1 4 1 8 4 0
7 2
3 3 8 8 5 5 0
4 3 9 6 0 2 5
0 8 6 2 0 3 8
5 1 0 8 2 9 6
1 7 5 3 9 2 0
8 4 2 9 5 5 3
2 3 6 2 9 1 4
5 3
9 3 0 4 0
3 9 4 0 4
0 4 9 4 0
4 0 4 9 3
0 4 0 3 9
5 4
1 2 3 4 9
2 3 4 5 9
3 4 5 6 9
4 5 6 7 9
9 9 9 9 9

부분집합의 합 꼭 풀어보기 