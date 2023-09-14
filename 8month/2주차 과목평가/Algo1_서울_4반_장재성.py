# T = int(input())
# for tc in range(1, T+1): # 각 변수의 입력을 받음
#     N = int(input())
#     r1, c1, r2, c2 = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     result = 0
#     area = (r2-r1+1) * (c2-c1+1)
#     cnt = 0
#     avg_result = 0
#     for i in range(r1, r2+1):  # 제공된 범위 내에서 각 자리의 합 과 평균 구하기
#         for j in range(c1, c2+1):
#             result += arr[i][j]
#             avg_result = result // area

#     for i in range(r1, r2+1):  # 구한 평균값을 이용하여 각 자리수를 평균값으로 변환하고 횟수를 계산
#         for j in range(c1, c2+1):
#             while avg_result != arr[i][j]:
#                 if avg_result > arr[i][j]:
#                     arr[i][j] += 1
#                     cnt += 1
#                 elif avg_result < arr[i][j]:
#                     arr[i][j] -= 1
#                     cnt += 1
#                 else:
#                     break

#     print(f'#{tc} {cnt}')


# 강사님 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2 = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sumV = 0

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            sumV += arr[i][j]

    avgV = sumV // ((r2-r1+1)*(c2-c1+1))
    result = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            avgV_abs = arr[i][j] - avgV
            if avgV_abs < 0:
                avgV_abs *= -1
            result += avgV_abs

    print(f'#{tc} {result}')
