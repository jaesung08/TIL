'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

 

[입력]
 

첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )

다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )

다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )

color = 1 (빨강), color = 2 (파랑)

 

[출력]
 

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

T = int(input())
for tc in range(1, T+1):

    def color_grid(r1, c1, r2, c2, color):
       for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 0:
                    grid[r][c] = color
                elif grid[r][c] != color:
                    grid[r][c] = 3  # 겹쳐서 보라색이 됨
    
    N = int(input())
    grid = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = (map(int, input().split()))
        color_grid(r1,c1,r2,c2,color)

    cnt = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j]==3:
                cnt += 1
    
    print(f'#{tc} {cnt}')

'''
T = int(input())
for tc in range(1, T+1):

    N = int(input())

    grid = [[0 for i in range(10)] for _ in range(10)]

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 0:
                    grid[r][c] = color
                elif grid[r][c] != color:
                    grid[r][c] = 3  # 겹쳐서 보라색이 됨

    overlapping_count = sum(row.count(3) for row in grid)
    print(f"#{tc} {overlapping_count}")
    '''