'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''

T = int(input())
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# 특정위치를 기점으로 상하좌우 문자를 붙여아하므로
# 파라미터로 좌표값도 받아야한다.
def dfs(y, x, number):
    if len(number) == 7:
        result.add(number)
        return

    for dy, dx in move:
        ny = y+ dy
        nx = x+ dx

        ## 갈 수 없는 위치면 continue
        if ny <0 or ny >= 4 or nx <0 or nx >= 4:
            continue

        # 갈수 있따면 다음ㅊ위치로 이동
        dfs(ny, nx, number + maps[ny][nx])


for tc in range(1, T+1):
    # 서로 다른 수를 합친다 => 문자열이 더 좋다
    maps = [input().split() for _ in range(4)]

    # 7자리 수를 중복 제거하여 저장
    result = set()
    # 시작지점 돌리기
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')
