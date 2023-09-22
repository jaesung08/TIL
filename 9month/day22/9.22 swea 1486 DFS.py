T = int(input())

def recur(level, acc_height):
    global ans

    # 가지치기
    # 현재까지 탑이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요가 없다.
    if acc_height >= B:
        ans = min(ans, acc_height)
        return

    # 기저 조건
    if level == N:
        return

    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + arr[level])
    # 안쓸 경우
    recur(level + 1, acc_height)

    # 기저 조건
    # 들어가기전(가지치기)
    # 다음 재귀함수 호출
    # 돌아왔을 때
    # 이번에는 순서를 바꿔서 가지치기 먼저

for tc in range(1, T+1):
    N, B =map(int, input().split())
    arr = list(map(int, input().split()))
    ans = float('inf') # 무한대로 큰 숫자
    recur(0, 0)
    print(f'#{tc} {ans - B}')