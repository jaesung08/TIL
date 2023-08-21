# #swea 4_im_중계기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N+1)]
#     stack = []
#     R = 1
#
#     for i in range(N+1):
#         for j in range(N+1):
#             if arr[i][j] == 2:
#                 y, x = i, j
#                 break
#             if arr[i][j] == 1:
#                 stack.append((i, j))
#     D2_max = 0
#     for ny, nx in stack:
#         D2 = abs(ny - y)**2 + abs(nx - x)**2
#         if D2_max < D2:
#             D2_max = D2
#
#     while D2_max > (R**2):
#         R += 1
#
#     print(f'#{tc} {R}')

# # swea_4_im_captcha Code
# T = int(input())
# for tc in range(1, T+1):
#     N,K = map(int, input().split()) # 샘플길이 N , 패스코드길이 K
#     sample = list(map(int, input().split()))
#     passcode = list(map(int, input().split()))
#     cnt = 0
#     result = 0
#
#     for i in range(N):
#         if sample[i] == passcode[cnt]:
#             cnt += 1
#         if cnt == K:
#             result = 1
#             break
#
#     print(f'#{tc} {result}')


# # swea_4_im_사각형그리기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     def game():
#         global cnt
#         max_area = 0
#         for y in range(N):
#             for x in range(N):
#                 cur = arr[y][x]  # 왼쪽 위 좌표의 값
#                 # 현재위치에서 오른쪽아래로 탐색
#                 for ny in range(y, N):
#                     for nx in range(x, N):
#                         # 동일한 숫자값을 만나면
#                         if arr[ny][nx] == cur:
#                             # 면적계산
#                             area = (ny - y + 1) * (nx - x + 1)
#                             # 최댓값이라면 갱신
#                             if area > max_area:
#                                 max_area = area
#                                 cnt = 1  # 새롭게 만든 큰 면적 사각형 1개
#                             elif area == max_area:
#                                 cnt += 1  # 같은 크기 면적이면 누적
#         return cnt
#     game()
#     print(f'#{tc} {cnt}')


# swea_4_im_답안지 채점
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    min_score = 10000000

    for student in arr:
        cnt = 0
        score = 0
        for i in range(M):
            if student[i] == answer[i]:
                score += 1 + cnt
                cnt += 1
            else:
                cnt = 0

        if score >= max_score:
            max_score = score
        if score <= min_score:
            min_score = score

    print(f'#{tc} {max_score - min_score}')
