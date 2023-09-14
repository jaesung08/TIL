# # swea 4408 자기방으로 돌아가기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#

# swea 1860 진기의 최고급 붕어빵

# swea 4615 재밌는 오셀로 게임

# swea 1220 magnetic


# # swea 4반 문제풀이 파리퇴치3
# direction1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# direction2 = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     result = []
#     for i in range(N):
#         for j in range(N):
#             cnt = arr[i][j]
#             for y1, x1 in direction1:
#                 for k in range(1, M):
#                     y = i + (y1 * k)
#                     x = j + (x1 * k)
#                     if 0 <= y < N and 0 <= x < N:
#                         cnt += arr[y][x]
#             result.append(cnt)
#             cnt = arr[i][j]
#             for y2, x2 in direction2:
#                 for k in range(1, M):
#                     y = i + (y2 * k)
#                     x = j + (x2 * k)
#                     if 0 <= y < N and 0 <= x < N:
#                         cnt += arr[y][x]
#             result.append(cnt)
#
#     result = max(result)
#     print(f'#{tc} {result}')

# # swea 4반 문제풀이 의석이의 세로로 말해요
# # from pprint import pprint
# # new_arr = [list(i)for i in zip(*arr)]
# #     pprint(new_arr)
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(input()) for _ in range(5)]
#     lst =[]
#     while arr:
#         try:
#             for i in range(5):
#                 lst.append(arr[i].pop(0))
#         except:
#             pass
#
#     print("".join(lst))
#     # i = 0
#     # l = len(arr[i])
#     # for j in range(l):
#     #     for k in range(5):
#     #         lst.append(arr[k][j])
#     #     i += 1
#     # print("".join(lst))
#
# # 지피티로 풀기
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(input()) for _ in range(5)]
#     lst = []
#
#     max_length = max(len(word) for word in arr)  # 가장 긴 단어의 길이
#     for i in range(max_length):
#         for j in range(5):
#             if i < len(arr[j]):
#                 lst.append(arr[j][i])
#
#     print(f"#{tc} {''.join(lst)}")

# # 강사님 풀이
# T = int(input())
# for tc in range(1, T+1):
#     arr = [list(input()) for _ in range(5)]
#     s = [[0]*15 for _ in range(15)]
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             s[i][j] = arr[i][j]
#     word = ''
#     for i in range(15):
#         for j in range(15):
#             if s[j][i] != 0:
#                 word += s[j][i]
#     print(f'#{tc} {word}')


# # swea 4반 im대비 홈 방범 서비스
# T = int(input())
# for i in range(1, T+1):
#     N, M = map(int, input().split())    # N 길이 / M 집 한채당 방범비
#     arr =[list(map(int, input().split())) for _ in range(N)]    # ㅈ집이 1 빈곳 0
#     # 운영비용 = k*k + (k-1)*(k-1)
#     '''
#     방범 구역 가운데에 집이 존재
#     그럼 방범 범위를 넓혀가면서 방범비가 - 가 되지않는지 확인
#     방범비가 - 가 아닐때 포함된 집의 갯수 저장
#     ㅇㅋ 가보자고
#     '''
#     k =1
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:


# swea 4반 im대비 당근 포장하기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()
    can = []    # 당근의 포장 조건을 만족하는 개수차이
    for i in range(1, N - 1):       # 첫번째 상자와 두번째 상자의 차이
        for j in range(i + 1, N):    # 두번째 상자와 세번째 상자의 차이
            A = Ci[:i]  # 첫번째 상자
            B = Ci[i:j]  # 두번째 상자
            C = Ci[j:]
            if A[-1] == B[0] or B[-1] == C[0]:  # 같은 크기의 당근이 인접한 상자에 있다면
                continue
            if len(A) * len(B) * len(C) == 0:   # 빈 상자가 있다면
                continue
            if len(A) > N//2 or len(B) > N//2 or len(C) > N//2:     # 한 상자에 N//2개를 초과하는 당근이 있다면
                continue
            # 상자간의 당근 갯수 차이
            can.append(
                max(abs(len(A)-len(B)), abs(len(B)-len(C)), abs(len(C)-len(A))))
    try:
        print(f'#{tc} {min(can)}')
    except:
        print(f'#{tc} {-1}')

# swea 4반 im대비 홈방법 서비스
T = int(input())


def solve():
    ans = 0  # 최대 서비스 제공 집의 수
    K = N + 1   # 최대 가능한 서비스 영역의 크기
    for k in range(K, 0, -1):
        cost = k * k + (k-1) * (k-1)
        for y in range(N):
            for x in range(N):
                cnt = 0     # 현재 위치에서 서비스 가능한 집의수
                for hy, hx in houses:
                    dist = abs(hy - y) + abs(hx - x)
                    if dist < k:   # 거리가 k보다 작으면 서비스 가능 -> 카운트 증가
                        cnt += 1
                if cnt * M - cost >= 0:  # 수익이 운영비용보다 크거나 같은경우 / 손해보지 않기위해서
                    ans = max(ans, cnt)  # 둘 중 더 큰값 저장
        if ans != 0:
            return ans
    return ans


for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 길이 / M 집 한채당 방범비
    arr = [list(map(int, input().split())) for _ in range(N)]    # 집이 1 빈곳 0
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                houses.append((i, j))
    result = solve()
    print(f'#{tc} {result}')


# 당근 다시 풀기
T = int(input)
for tc in range(1, T+1):
    N = int(input)
    Ci = list(map(int, input().split()))