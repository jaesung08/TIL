# T = int(input())                        # 각 변수의 입력을 받음
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = 0

#     # 1부터 N까지 크기가 점점 증가할 때 arr[0]부터 arr[N-1]까지 규칙에 따라 합을 구함
#     for i in range(1, N+1):
#         result += sum(arr[0:N:i])
#     if result <= 0:  # 구한 합이 음수일 경우 0으로 처리
#         result = 0

#     print(f'#{tc} {result}')


# 강사님 풀이
T = int(input())                        # 각 변수의 입력을 받음
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0

    for i in range(N):
        for j in range(0, N, i+1):
            result += numbers[j]
    result = result if result >= 0 else 0

    print(f'{tc} {result}')
