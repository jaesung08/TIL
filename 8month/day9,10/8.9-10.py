# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#          print('overflow!')
#     else:
#          stack[top] = item
#
# size = 10
# stack = [0] * 10
# top = -1
#
# push(10, size)
# top += 1 	# push(20)
# stack[top] = 20

# # 수업실습1
# stack = [0] * 10
# top = -1
#
# top += 1    # push(1)
# stack[top] = 1
# top += 1    # push(2)
# stack[top] = 2
# top += 1    # push(3)
# stack[top] = 3
#
# print(stack[top])
# top -= 1
# top -= 1
# print(stack[top+1])


# # swea 4869 종이붙이기  // 재귀함수 풀이 = > 규칙성을 찾아서 함수 만들기!!
# def paper(N):
#     if N == 10:
#         return 1
#     elif N == 20:
#         return 3
#     else:
#         return paper(N-10)+ (2*paper(N-20))
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = paper(N)
#     print(f'#{tc} {cnt}')
#


# # swea 4866 괄호검사  // 스택
# def stack(text):
#     stack=[]
#     for i in text:
#         if i == "{" or i =="(":
#             stack.append(i)
#         elif stack and i == "}" and stack[-1] == "{":   # 스택이 비어있지 않고, 조건을 충족할시
#             stack.pop()
#         elif stack and i == ")" and stack[-1] == "(":
#             stack.pop()
#         elif i == "}" or i == ")":
#             stack.append(i)
#
#                 # 파이썬 내부에서 0이 False고 나머지는 True, 고로
#     if stack:   # 리스트 비어 있으면 False, 안 비어 있으면 True 반환
#         return "0"  # 스택이 비어있지 않는 경우
#     else:
#         return "1"  # 비어있는 경우 1 출력
#
# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     result = stack(text)
#     print(f'#{tc} {result}')


# 강사님 기출 왼쪽, 오른쪽 이동 // 리스트를 한정적으로 생각하지말고 더 추가해서 넣은다음에 삭제한다고 생각하기.
# arr = [3, 5, 1, 9, 7]
# for _ in range(4):
#     w = input()
#     if w == 'R':
#         a = arr.pop()
#         arr[4] = arr[3]
#         arr[3] = arr[2]
#         arr[2] = arr[1]
#         arr[1] = arr[0]
#         arr[0] = a
#     elif w == 'L':
#         b = arr[0]
#         arr[0] = arr[1]
#         arr[1] = arr[2]
#         arr[2] = arr[3]
#         arr[3] = arr[4]
#         arr[4] = b
#
# print(arr)

# ## 강사님 풀이
# arr = [3, 5, 1, 9, 7]
# T = [(input()) for _ in range(4)]
#
# def Right(lst):
#     # 리스트 뒤쪽에 있는 앞의 4개의 원소추가
#     for i in range(4):
#         lst.append(lst[i])
#     # 리스트 앞쪽의 4개의 요소제거
#     for _ in range(4):
#         lst.pop(0)
#
# def left(lst):
#     lst.append(lst[0])
#     lst.pop(0)
#
# for i in range(4):
#     if T[i] =='R':
#         Right(arr)
#     if T[i] == 'L':
#         left(arr)
# print(*arr)


# # 강사님 기출 _ 이진수로 만들기 // 재귀함수
# '''
# 자연수 N을 입력받고 재귀호 출을 사용해 N을 2진수로 만드는 코드를 작성하시오
# '''
# N = int(input())
# def bianry(N):
#     if N == 1:
#         return '1'
#     elif N == 0:
#         return '0'
#     if N >= 2:
#         a = N // 2
#         b = N % 2
#         return bianry(a) + str(b)
# result = bianry(N)
# print(result)
#
# ## 승희 풀이
# def binary(N):
#     if N == 1:
#         print('1', end = '')
#         return
#     if N == 0:
#         print('0', end = '')
#         return
#     binary(N // 2)
#     print(N % 2, end = "")
#
# N = int(input())
# binary(N)

# # 강사님 기출 _ 콜라츠 추측
# '''
# 콜라츠 추측은 특정 자연수가 아래의 과정을 거치면 무조건 1 이 된다는 추측이다.
# 1. 어떤수가 짝수면 2로 나눈다.
# 2. 어떤수가 홀수면 3을 곱하고 1을 더한다.
# 3. 어떤수가 1이 아니라면 조건1,2를 반복한다.
#
# 주어진 자연수 N이 1디 될때까지 몇번 거쳐야 하는지 출력하는 프로그램을 작성하시오.
# '''
#
# N =int(input())
# cnt = 0
# def collatz(N, cnt):
#     if N != 1:        # 이 조건없이 해도 가능함 대신 N=1일때를 elif로
#         if N % 2 == 0:
#             a = N // 2
#             cnt += 1
#             return collatz(a, cnt)
#         else:
#             a = (N * 3) + 1
#             cnt += 1
#             return collatz(a, cnt)
#     if N == 1:
#         return cnt
#
# print(collatz(N, cnt))


# # 강사님 기출 _ 자리의 합
# N = int(input())
# result = 0
# def Num_sum(N, result):
#     a = N % 10
#     b = N // 10
#     result += a
#     if b == 0:
#         return result
#     return Num_sum(b, result)
#
# print(Num_sum(N, result))
#

# # 강사님 기출 _ 다섯 종류의 숫자카드
# # 백트래킹 : 가능한 모든 경로를 탐색하되, 특정조건을 만족하지 않는 경로는 건너뛰는 방식으로 문제해결 ex) continue
# N = list(input())
# cnt = 0
# arr = []
#
# # while True:
# for i in range(5):
#     arr.append(N[i])
#     for j in range(5):
#         arr.append(N[j])
#         for k in range(5):
#             arr.append(N[k])
#             for l in range(5):
#                 arr.append(N[l])
#
#                 for m in range(2):
#                     if (int(arr[m]) - int(arr[m + 1])) <= 3 and (int(arr[m]) - int(arr[m+1])) >= -3:
#                         cnt += 1
#                     else:
#                         continue
#
# print(cnt)
#
# # 강사님 풀이
# card = list(input())
# cnt = 0
# path = [0] * 4
#     global cnt
#     # 4장의 카드를 뽑았으면 경우의 수 증가
#     if level == 4:
#         cnt += 1
#         return # 재귀 함수 호출 종료
#
#     for i in range(5): # 다섯개의 카드 중 선택
#         path[level] = card[i] # 현재 레벨 경로에 선택한 카드 저장
#         # 연속된 카드간의 차이가 4이상이면 다음카드를 선택 => 백트래킹
#         if int(path[level]) - int(path[level -1 ]) >= 4:
#             continue
#         if int(path[level -1 ]) - int(path[level]) >= 4:
#             continue
#         # 다음 레벨로 재귀 호출
#         card_cnt(level + 1)
#
# card_cnt(0)  # 시작 level 은 0
# print(cnt)

# # 승희 풀이
# N = list(input().strip())
#
# # 뽑은 카드가 유효한지 확인
# def isvalid(result):
#     # 1115
#     for i in range(3):
#         if abs(int(result[i]) - int(result[i+1])) > 3:
#             return False
#     return True
#
# # 중복 순열 만들기
# def comb(start):
#     global cnt
#     if len(result) == 4:
#         if isvalid(result):
#             cnt += 1
#         return
#
#     for i in range(start, len(N)):
#         result.append(N[i])
#         comb(0)
#         result.pop()
#
#
# result = []
# cnt = 0
# comb(0)
# print(cnt)


# # 강사님 기출 _ 프로듀스 101배수 // 못풀겠다;;;
# N = int(input())
# numbers = list(map(int, input().split()))
# operator = ['+', '-', '*']
#
# def modify(N, numbers):
#     for i in range(N):
#         numbers[i]
#
#
#
# # 승희 풀이
# def calcul(idx, result, expression):
#
#     if idx == N-1:
#         if result == 0:
#             return
#         elif result % 101 == 0:
#             print(expression)
#             return
#         return
#
#     # * 다음 숫자
#     calcul(idx + 1, result * numbers[idx+1], expression + "*" + str(numbers[idx+1]))
#     # + 다음 숫자
#     calcul(idx + 1, result + numbers[idx + 1], expression + "+" + str(numbers[idx + 1]))
#     # - 다음 숫자
#     calcul(idx + 1, result - numbers[idx + 1], expression + "-" + str(numbers[idx + 1]))
#
#
# N = int(input())
# numbers = list(map(int, input().split()))
# calcul(0, numbers[0], str(numbers[0]))


# # 백준 도키도키 간식드리미
# N = int(input())
# arr1 = list(map(int, input().split()))
# arr2 = []
# S = 1
# while S <= N:
#     if arr1[0] != S:
#         a = arr1.pop(0)
#         arr2.append(a)
#     elif (arr1[0] == S) or (arr2[-1] == S):
#         S += 1
#     elif arr2[-1] != S:
#         b = arr2.pop()
#         arr1.append(b)
#     elif S == N:
#         print("Nice")
#     else:
#         print("Sad")

# N = int(input())
# arr1 = list(map(int, input().split()))
# arr2 = []
# S = 1
# while S <= N:
#     if arr1 and arr1[0] == S:
#         S += 1
#         arr1.pop(0)
#     elif arr2 and arr2[-1] == S:
#         S += 1
#         arr2.pop()
#     elif arr1 and arr1[0] != S:
#         arr2.append(arr1.pop(0))
#     else:
#         print("Sad")
#         break
#
# if S > N:
#     print("Nice")

### 8.10 ###

# # 피보나치 수 DP 비교
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# cnt = 0
# print(fibo(30), cnt)


# ###
# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return memo[n]
#     else:
#         if memo[n] == 0:
#             memo[n] = fibo(n-1) + fibo(n-2)
#         return memo[n]
#
#
# n = 30
# cnt = 0
# memo = [0] * (n+1)
# memo[0]=0
# memo[1]=1
# print(fibo(n), cnt)

# ### DP
# def fibo(n):
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
#
# dp = [0] * (100+1)
# dp[0] = 0
# dp[1] = 1
# for i in range(2, 101):
#     dp[i] = dp[i - 1] + dp[i - 2]
# print(fibo(100))


# # DFS / 이해가안되는데?ㅋㅋ
# '''
# V E
# v1 w1 v2 w2
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
#
# def dfs(n, V, adj_m):
#     stack = []  # stack 생성
#     visited = [0] * (V+1)   # visited 생성
#     visited[n] = 1  # 시작점 방문 표시
#     print(n)    # do[n] : 각 시작점의 정점에서 할거
#     while True:
#         for w in range(1, V+1):
#             if adj_m[n][w] == 1 and visited[w] == 0:
#                 stack.append(n)   # push(v), v = w
#                 n = w
#                 print(n)    # do(w)
#                 visited[n] = 1    # w 방문 표시
#                 break   # for w, n에 인접인 w 찾은경우
#         else: # 방문할 곳이 더이상 없다면 뒷걸음지
#             if stack:   # 스택에 지나온 정점이 남아있으면
#                 n = stack.pop() # pop()해서 다시 다른 w 찾기
#             else:   # 스택이 비어있으면
#                 break   # while True 탐색 끝
#     return
#
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
# adj_m = [[0]*(V+1) for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1
#
# dfs(1, V, adj_m)


# # swea 4871 그래프경로 // DFS
# def dfs(s,g):
#     stack = []
#     stack.append(s) # 시작 노드를 스택에 추가하고 시작 False = 0 , True = 1
#
#     while stack:    # 스택이 비어있지 않을 경우 계속 반복
#         v = stack.pop()     # 스택에서 노드 꺼냄
#
#         if visited[v] == 0: # 노드에 방문하지 않았다면 False = 0 , True = 1
#             visited[v] = 1  # 노드를 방문 한걸로 바꿈 False = 0 , True = 1
#
#             for w in range(1, V+1):
#                 if graph[v][w] == 1 and visited[w] == 0: # 연결되어있음 & 방문되지 않은 노드라면
#                     if w == g:      # 노드 번호가 도착 노드라면
#                         return 1    # 경로가 존재하기 때문에 1 반환
#                     stack.append(w) # 스택에 방문한 노드 추가
#     return 0        # 모든 탐색을 마쳤는데도 도착 노드로의 경로를 찾지 못했다면 0 반환
#
#
# T = int(input())                # 테스트 케이스 개수
# for tc in range(1, T+1):
#     V, E = map(int, input().split())    # V개 이내의 노드를 E개의 간선으로 연결
#     visited = [0 for _ in range(V+1)]   # 노드 번호가 1번부터이기때문에 V+1 사용 // False = 0 , True = 1
#     graph = [[0 for _ in range(V+1)] for _ in range(V+1)]  # 노드간의 간선을 저장하기 위해 작성
#     for _ in range(E):
#         i, j = map(int, input().split())    # E개만큼 움직이는 간선 경로 제공
#         graph[i][j] = 1  # 노드 i에서 j로의 간선이 존재함을 표시한다. False = 0 , True = 1s
#
#     s, g = map(int, input().split())        # 출발점과 끝점 제공
#     result = dfs(s,g)
#     print(f'#{tc} {result}')


# # 승희 풀이
# def dfs(now, visited):
#     visited[now] = True
#
#     for next in graph[now]:
#         if not visited[next]:
#             dfs(next, visited)
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     graph = [[0] for _ in range(V+1)]
#     visited = [False] * (V+1)
#     for _ in range(E):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#     S, E = map(int, input().split())
#     dfs(S, visited)
#     print(f'#{tc} 1' if visited[E] else f'#{tc} 0')

# # 강사님 풀이
# def dfs(start, end):
#     stack = [] # 탐색할 노드를 저장할 스택 초기화
#     visited = [False] * (v + 1)
#     stack. append(start) # 시작점을 스택에 넣음
#
#     while stack: # 스택이 비어있으면 반복문 종료
#         now = stack.pop()   # 스택의 마지막 노드를 꺼냄
#         visited[now] = True # 현재 노드를 방문
#         for next in range(1, v +1):
#             if node[now][next] and not visited[next]:  # 방문하지 않았고, 연결되어 있다면
#                 stack.append(next)  # 스택에 추가
#     if visited[end]: # 끝점에 방문했다면
#         return 1
#     else:
#         return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     v, e = map(int, input().split())  # 노드와 간선의 개수
#     node = [[0 for _ in range(v+1)] for _ in range(v+1)] # 인접행렬 초기화
#     for _ in range(e):
#         start, end = map(int, input().split())
#         node[start][end] = 1 # 해당 인접행렬에 1 할당 // 노드와 노드의 간선 연결
#     s, g =map(int, input().split())
#
#     print(f'#{tc} {dfs(s,g)}')


# # 강사님 기출 _ 문자열 노드 DFS'
# '''
# RKFCBICM
# 0 1 1 1 0 0 0 0
# 0 0 0 0 1 1 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 1
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
#
# # RKBIFCCM
# '''
# # 그래프의 기본 구성 요소 : 노드, 간선
# # 인접행렬 해석
# '''
# 0 1 1 1 0 0 0 0
# 0 0 0 0 1 1 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 1
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# '''
# # 첫번쨰 노드(0)은 두번쨰 노드(1), 세번쨰 노드(2), 네번째노드(3)과 연결되어있다.
# # 두번째 노드(1)은 다섯번째 노드(4), 여섯번째 노드(5)와 연결되어있다.
# # 네번쨰 노드(3)은 일곱번쨰 노드(6), 여덟번째 노드(7)과 연결되어있다.
# lst = list(input()) # 노드 입력
# N = len(lst) # 노드의 개수
# adj = [list(map(int, input().split())) for _ in range(N)]  # 인접행렬 입력
# visited = [0 for _ in range(N)]
#
# def dfs(v):
#     print(lst[v], end='')
#     visited[v] = True
#
#     for i in range(N):
#         if adj[v][i] and not visited[i]: # 연결되어 있고, 아직 방문하지 않았다면
#             dfs(i)
#
# dfs(0)


# # swea 4873 반복문자 지우기 // stack
# def earase(word):
#     for char in word:
#         # 만약 반복 문자 라면 (stack에 문자가 이고, 현재 문자가 스택의 마지막 문자와 같다면)
#         if stack and char == stack[-1]:
#             stack.pop() # 반복문자 제거
#         else:
#             stack.append(char)
#     return len(stack)
#
# T = int(input())
# for tc in range(1, T+1):
#     str1 = list(input())
#     stack = []
#     result = earase(str1)
#     print(f'#{tc} {result}')
