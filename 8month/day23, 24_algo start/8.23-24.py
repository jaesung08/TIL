# # swea 1979 어디에 단어가 들어갈 수 있을까
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]   # 빈칸은 0
#     result = 0
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if arr[i][j] == 1:
#                 cnt += 1
#             if arr[i][j] == 0 or j == N-1:
#                 if cnt == K:
#                     result += 1
#                 cnt = 0
#
#         for j in range(N):
#             if arr[j][i] == 1:
#                 cnt += 1
#             if arr[j][i] == 0 or j == N-1:
#                 if cnt ==K:
#                     result += 1
#                 cnt = 0
#
#     print(f'#{tc} {result}')


# # swea 보충 풍선퐝 보너스게임
# T = int(input())
# move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_result = 0
#     min_result = 100000000000000
#     for i in range(N):
#         for j in range(N):
#             cnt = arr[i][j]
#             for k in range(1, N):
#                 for y, x in move:
#                     ny = i + (y*k)
#                     nx = j + (x*k)
#                     if 0 <= ny < N and 0 <= nx < N:
#                         cnt += arr[ny][nx]
#             if max_result <= cnt:
#                 max_result = cnt
#             elif min_result > cnt:
#                 min_result = cnt
#
#     print(f'#{tc} {max_result - min_result}')
#
# # swea 4반 IM대비 간단한 369게임
# N = int(input())
#
# for i in range(1, N+1):
#     i = str(i)
#     clap = i.count('3') + i.count('6') + i.count('9')
#
#     if clap == 0:
#         print(i, end=' ')
#     else:
#         print("-" * clap, end=' ')


# # swea 4반 IM대비 농작물 수확하기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     def harvest_profit(field):
#         n = len(field)
#         middle = n // 2
#         total_profit = 0
#
#         for i in range(n):
#             for j in range(abs(middle - i), n - abs(middle - i)):
#                 total_profit += field[i][j]
#
#         return total_profit
#
#     result = harvest_profit(arr)
#     print(f"#{t} {result}")


# # swea 4반 im대비 magnetic
# T = 10
# for tc in range(1, T+1):
#     N =int(input())
#     mag = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     for j in range(N):
#         y, x = 0, j #
#         stack = []
#         while y < N:
#             if not stack and mag[y][x] == 1:
#                 stack.append(1)
#             elif stack and mag[y][x] == 2:
#                 cnt += stack.pop()
#             y += 1
#     print(f'#{tc} {cnt}')


# # swea 4반 im대비 영준이의 카드 카운팅
# T = int(input())
# for tc in range(1, T+1):
#     string = input()
#     # S: space D:Dia H:heart C:clover
#     # 1~13까지 존재
#     s = []
#     d = []
#     h = []
#     c = []
#     # for i in range(len(string)//
#     i = 0
#     cnt = 0
#     while i < len(string):
#         a = string[i:i+3]
#         i += 3
#         if a[:1] == 'S':
#             if a[1:3] in s:
#                 print(f'#{tc} ERROR')
#                 break
#             s.append(a[1:3])
#
#         if a[:1] == 'D':
#             if a[1:3] in d:
#                 print(f'#{tc} ERROR')
#                 break
#             d.append(a[1:3])
#
#         if a[:1] == 'H':
#             if a[1:3] in h:
#                 print(f'#{tc} ERROR')
#                 break
#             h.append(a[1:3])
#
#         if a[:1] == 'C':
#             if a[1:3] in c:
#                 print(f'#{tc} ERROR')
#                 break
#             c.append(a[1:3])
#         cnt += 1
#
#     if cnt == (len(string)//3):
#         all = 13
#         print(f'#{tc} {all -len(s)} {all -len(d)} {all -len(h)} {all -len(c)}')
#
#
# # 지윤이꺼
# T = int(input())
#
# for tc in range(1,T+1):
#     checkcard = input()
#     S = []
#     D = []
#     H = []
#     C = []
#     result = []
#     i = 0
#     for _ in range(len(checkcard) // 3):
#         check = checkcard[i: i+3]
#         if check[0] == 'S':
#             S.append(check[1:3])
#         elif check[0] == 'D':
#             D.append(check[1:3])
#         elif check[0] == 'H':
#             H.append(check[1:3])
#         elif check[0] == 'C':
#             C.append(check[1:3])
#         i = i+3
#     if len(S) != len(set(S)) or len(D) != len(set(D)) or len(H) != len(set(H)) or len(C) != len(set(C)):
#         print(f'#{tc} ERROR')
#     else:
#         result.append(13 - len(S))
#         result.append(13 - len(D))
#         result.append(13 - len(H))
#         result.append(13 - len(C))
#         print(f'#{tc}', *result)


# # swea 4반 im대비 퍼펙트 셔플
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = input().split()
#     l = []
#     r = []
#     result = []
#     for i in range(N):
#         if i < (N+1)//2:
#             l.append(lst[i])
#         elif i >= (N+1)//2:
#             r.append(lst[i])
#
#     for j in range((N+1)//2):
#         if j > len(l)-1:
#             pass
#         else:
#             result.append(l[j])
#         if j > len(r)-1:
#             pass
#         else:
#             result.append(r[j])
#
#     print(f'#{tc}', end = ' ')
#     print(*result)


# # swea 4반 IM대비 패턴 마디의 길이
# T = int(input())
# for tc in range(1, T+1):
#     string = input()
#
#     i = 2
#     while True:
#         if string[:i] != string[i:i*2]:
#             i += 1
#         else:
#             print(f'#{tc} {i}')
#             break


# swea 4반 im대비 스도쿠 검증
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    for i in range(9):
        if len(arr[i]) == set(arr[i]):
            pass
        else:
            result = 0
        for j in range(9):
            arr[i][j]


# # swea 4반 im대비 정곤이의 단조 증가하는 수
# def check(num):
#     num = str(num)
#     for i in range(len(num) -1):
#         if num[i] > num[i +1]:
#             return False
#     return True
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     A = list(map(int, input().split()))
#     result = 0
#     for i in range(N-1):
#         for j in range(i + 1, N):
#             number = A[i] * A[j]
#             if check(number):
#                 result = max(result, number)
#         if result == 0:
#             result = -1
#     print(f'#{tc} {result}')


# BFS/DFS
# 그래프의 구조를 분석하거나 그래프 탐색 문제
# 그래프의 모든 노드를 방문하거나, 최단 경로를 찾을때

# Union- Find
# 노드간의 집합 관계를 빠르게 파악하고 관리해야하는 경우
# union = > 두 그룹을 하나로 합친다.
# Find -> 특정 노드가 어느그룹에 속해 있는지 찾는다.

# swea 4반 union -find
# find와 union 함수는 암기하여 사용.
# def find(node):
#     if node != root[node]:
#         root[node] = find(root[node])
#     return root[node]
#
# def union(x,y):
#     root_x = find(x)    # x 의 루트 부모 찾기
#     root_y = find(y)    # y 의 루트 부모 찾기
#     if rank[root_x] > rank[root_y]: # x의 부모랭크가 더크다면, y의 부모를 x의 루트부모로 결정
#         root[root_y] = root_x
#     else:
#         root[root_x] = root_y
#         if rank[root_x] == rank[root_y]:
#             rank[root_y] += 1
#
# N, Q = map(int, input().split())
# rank = [0] * (N+1)  # 각 노드의 랭크를 저장하는 리스트
# root = [i for i in range(N+1)]  # 각 노드의 루트 부모를 저장하는 리스트
# for _ in range(Q):
#     K, A, B = map(int, input().split())
#     if K == 0:
#         if find(A) == find(B):  # A 와 B가 같은 그룹에 속한다면
#             print('YES')
#         else:
#             print("NO")
#     else:
#         union(A, B) # A와 B를 같은 그룹으로 연결


# # swea 4반 인디언 합창단
# def find(node):
#     if node != root[node]:
#         root[node] = find(root[node])
#     return root[node]
#
# def union(x,y):
#     root_x = find(x)    # x 의 루트 부모 찾기
#     root_y = find(y)    # y 의 루트 부모 찾기
#     if root_x == root_y:    # 기존 유니온 함수에 추가 된 조건/ 입력받은 두 인디언이 이미 같은 팀인 경우
#         return
#     if rank[root_x] > rank[root_y]: # x의 부모랭크가 더크다면, y의 부모를 x의 루트부모로 결정
#         root[root_y] = root_x
#     else:
#         root[root_x] = root_y
#         if rank[root_x] == rank[root_y]:
#             rank[root_y] += 1
#
# N = int(input())
# rank = [0] * 26
# root = [i for i in range(26)]
# for _ in range(N):
#     a, b = input().split()
#     union(ord(a) - 65, ord(b) - 65) # 닉네임 숫자로 바꾸고 연결
# # 모든 노드의 루트 찾기
# for i in range(26):
#     find(i)
# DAT =[0]* 26
# for i in range(26):
#     DAT[root[i]] += 1   # 각 루트별 노드 개수 세기
# team = 0
# indi = 0
# for data in DAT:
#     if data > 1:    # 노드의 개수가 2개 이상이라면
#         team += 1
#     elif data == 1: # 노드의 개수가 1개라면 개인연주자
#         indi += 1
#
# print(team)
# print(indi)
