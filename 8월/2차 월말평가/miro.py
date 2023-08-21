# # swea 4875 Miro // dfs 이용한 스택 문제
'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
# # 강사님 풀이
# def maze():
#     while stack:
#         y,x = stack.pop() # 현재위치를 스택에서 꺼냄
#         arr[y][x] = -1  # 지나간 길 표시
#         for dy, dx in move:
#             ny, nx = y + dy, x + dx
#             if 0 <= ny < N and 0 <= nx < N :
#                 if arr[ny][nx] == 3:
#                     return 1
#                 elif arr[ny][nx] == 0: # 갈수 있는 곳을 모두 스택에 추가
#                     stack.append((ny, nx))
#     return 0    # 도착점을 못찾으면 0 반환
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     move = [(1,0), (-1, 0), (0, 1), (0, -1)]
#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] == 2:
#                 stack = [(y,x)] # 시작점 스택에 추가
#                 break
#
#     print(f'#{tc} {maze()}')

'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# T = int(input())
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 y, x = i, j
#                 break
#     def miro(y,x):
#         q = []
#         cnt = 0
#         q.append((y, x))
#         while q:
#             y, x = q.pop(0)
#             cnt += 1
#             arr[y][x] = -1
#             for dy, dx in move:
#                 ny, nx = y + dy, x + dx
#                 if 0 <= ny < N and 0 <= nx < N :
#                     if arr[ny][nx] == 3:
#                         return cnt
#                     elif arr[ny][nx] == 0:
#                         q.append((ny, nx))
#         return 0
#
#     print(f'#{tc} {miro(y,x)}')