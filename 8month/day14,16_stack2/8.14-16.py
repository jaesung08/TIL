# stack = [0] * 100
# top = -1
# susik = '6528-*2/+'
# for x in susik:
#     if x not in '+-/*':
#         top += 1
#         stack[top] = int(x)
#     else:
#         if x=='+':
#             op1 = stack[top]
#             top -= 1
#             op2 = stack[top]
#             top -= 1
#             top += 1
#             stack[top] = op1 + op2
#         elif x== '-':
#
#         elif x==
#
#
# ##
# stack = [0] * 100
# top = -1
# icp = {'(':3, '*':2 , '/':2, '+':1, '-':1}
# isp = {'(':0, '*':2,  '/':2, '+':1, '-':1}
#
# fx = '(6+5*(2-8)/2)'
# susik = ''
# for x in fx:
#     if x in '(+-*/)':
#         if top == -1 or isp[stack[top]] < icp[x]:
#             top += 1    # push
#             stack[top] = x
#         elif isp[stack[top]] >= icp[x]:
#             while top > -1 and isp[stack[top]] >= icp[x]:
#                 susik += stack[top]
#                 top -= 1
#             top += 1
#             stack[top] = x
# print(susik)
#
# ## 부분집합의 합_재귀
# def f(i, N):
#     if i == N:
#         print(bit, end= ' ')
#         for j in range(N):
#             if bit[j]:
#                 print([A[j]], end=' ')
#         print()
#         return
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#         return
#
# N = 3
# A = [1,2,3]
# bit = [0]* N
# f(0, N)
#
# ## 부분집합의 합
# def f(i, N, s): # s : i-1원소까지의 부분집합의 합(포함된 원소의 합)
#     if i == N:
#         print(bit, end= ' ')
#         print(f' : {s}')
#
#         return
#     else:
#         bit[i] = 1      # 부분집합에 A[i]포함
#         f(i+1, N, s+A[i])
#         bit[i] = 0      # 부분집합에 A[i]빠짐
#         f(i+1, N, s)
#         return
#
# N = 3
# A = [1,2,3]
# bit = [0]* N
# f(0, 3, 0)
#
# # 부분집합의 합
# def f(i, N, s, t): # s : i-1원소까지의 부분집합의 합(포함된 원소의 합). t :찾으려는 합
#     global cnt
#     cnt += 1
#     if s == t:
#
#     if i == N:
#         if s == 10:
#             print(bit)
#             return
#     elif i == N:
#         return
#     else:
#         bit[i] = 1      # 부분집합에 A[i]포함
#         f(i+1, N, s+A[i], t)
#         bit[i] = 0      # 부분집합에 A[i]빠짐
#         f(i+1, N, s,t )
#         return
#
# N = 3
# A = [1,2,3]
# bit = [0]* N
# cnt = 0
# f(0, 3, 0)


# # 순열
# def f(i, N):
#     if i == N:
#         print(A)
#     else:
#         for j in range(i, N):   # 자신부터 오른쪽끝까지
#             A[i], A[j] = A[j], A[i]
#             f(i+1, N)
#             A[i], A[j] = A[j], A[i]
# A = [1,2,3]
# f(0,3)
#


# # swea 4874 Forth  // 스택문제
# T = int(input())
# for tc in range(1, T+1):
#     text = input().split()
#     stack = []
#     error = False
#
#     for i in range(len(text)-1): # 마지막 . 빼기 위해서 한개 빼고
#         if text[i].isdigit():   #해당 문자가 숫자라면
#             stack.append(text[i])   # 스택에 쌓기
#
#         else: # 해당 문자가 숫자가 아닌 연산자라면
#             try: # 에러 처리를 위한 try-except // try 문 내에서 실행하다가 실패 혹은 예외사항이 발생시 바로 except문 실행
#                 b = int(stack.pop())  # 추가된 두 숫자를 꺼내기
#                 a = int(stack.pop())  # 거꾸로 꺼내기 때문에 b,a순으로
#                 # 연산자에 맞춰 계산
#                 if text[i] ==  '+':
#                     c = a + b
#                 elif text[i] ==  '-':
#                     c = a - b
#                 elif text[i] ==  '*':
#                     c = a * b
#                 elif text[i] ==  '/':
#                 # 나머지는 버려야하니까 '//' 연산자 활용
#                     c = a // b
#                 stack.append(c)
#             except: # 숫자도 연산자도 아니라면 에러발생
#                 error = True
#     # 에러가 True거나 스택에 남은게 하나가 아니라면 error 출력
#     if error == True or len(stack) != 1:
#         print(f'#{tc} error')
#     else:
#         print(f'#{tc} {stack[0]}')
#
# # 강사님 풀이
# T= int(input())
# for tc in range(1, T+1):
#     forth = list(input().split())
#     stack = []
#     error = False
#     for i in range(len(forth)-1):
#         if forth[i].isdigit():
#             stack.append(forth[i])
#         else: # 숫자가 아닌 연산자 일 경우
#             try:
#                 b = int(stack.pop())
#                 a = int(stack.pop())
#                 if forth[i] == '+':
#                     ans = a +b
#                 elif forth[i] == '-':
#                     ans = a -b
#                 elif forth[i] == '*':
#                     ans = a * b
#                 elif forth[i] == '/':
#                     ans = a // b
#                 stack.append(ans)
#             except:
#                 error = True
#
#     if error == True or len(stack) != 1 :
#         print(f'#{tc} error')
#     else:
#         print(f'#{tc} {stack.pop()}')


# # swea 4875 Miro // dfs 이용한 스택 문제
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


# # swea 4880 토너먼트 카드게임 //
# def sep_group(start, end) :
#     if start == end:    # 그룹에 한명이 남았을때만 출력
#         return start
#
#     a = sep_group(start, (start + end)//2)   # 재귀함수를 통해 각 그룹에 한명이 남을때까지 돌림
#     b = sep_group((start + end)//2 +1, end)  # 이후 하나만 남아 재귀함수가 멈추고 start값이 나오면 가위바위보 진행
#     return rsp(a, b)
#
# def rsp(a, b):
#     A, B = arr[a], arr[b]
#     if A - B == 1 or A - B == -2:
#         return a
#     elif A == B :
#         return a
#     else:
#         return b
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print(f'#{tc} {sep_group(0, N-1) +1 }')  # N개이나 인덱스값 시작이 0 이기에 -1 , 출력값은 인덱스값이기에 번호는 +1


# # swea 4881 배열 최소 합 // 백트래킹 이용하기
#
#
# def array_sum():
#     stack = []
#     in_j = []
#     for i in range(N):
#         small = 10
#         for j in range(N):
#             if j not in in_j:
#                 if small > arr[i][j]:
#                     small = arr[i][j]
#                     small_j = j
#         in_j.append(small_j)
#         stack.append(small)
#     return sum(stack)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{tc} {array_sum()}')
#
# # dfs + 백트래킹 활용해서 풀기
# def DFS(idx, now_sum):
#     global min_sum
#     if now_sum >= min_sum:  # 현재 합이 최소 합보다 크면 더이상 탐색 x
#         return
#     if idx == N:    # 모든 행을 선택
#         if min_sum > now_sum:   # 모든행을 선택했으면 현재 합이 최소합보다 작으면 최소합을 현재합으로 업데이트
#             min_sum = now_sum
#             return
#     for i in range(N):
#         if not used[i]:
#             used[i] = 1
#             DFS(idx+1, now_sum + arr[idx][i])   # 다음 행으로 넘어가면서 재귀호출
#             used[i] = 0 # 복구 (백트래킹)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     used = [0] * N
#     min_sum = 21e8
#     DFS(0,0)
#
#     print(f'#{tc} {min_sum}')
#
#
#
#
#
#
# # swea 4반 다빈치 민코드 // dfs 백트래킹
# import copy
# N, M = map(int, input().split())
# lst = list(map(int, input().split()))
# path = []  # 선택된 패들의 값을 저장할 리스트
# used = [0] * N  # 패가 사용되었는지 체크
# Min = 21e8
# result = []
#
#
# def DFS(level, Sum):
#     global Min, path, result
#     if level == M:  # 패를 모두 선택하였다면
#         if Sum < Min:  # 현재 곱한값이 최소값보다 작으면 최소값 업데이트
#             Min = Sum
#             result = copy.deepcopy(path)  # 선택된 패들의 값을 최종 result에 저장
#         return
#
#     for i in range(N):
#         if used[i] == 1:  # 이미 사용된 패라면 건너 뜀뜀
#             continue
#         path.append(lst[i])  # 패를 선택하고 path 에 추가
#         used[i] = 1
#         DFS(level + 1, Sum * lst[i])  # 다음 패를 선택으로 넘어가며 재귀호출
#         used[i] = 0  # 복구 (백트래킹)
#         path.pop()
#
#
# DFS(0, 1)  # 초기레벨은 0, 초기 곱은 1
# result.sort()
# print(*result)


# swea 4반 부분집합 // 부분집합의 합
def dfs(idx, N, t, S):
    global cnt, used
    if idx == N:
        if t == S:
            cnt += 1
            return
    else:
        for j in range(N):
            if not used[j]:
                used[j] = 1
                dfs(j+1, N, t+arr[j], S)
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    used = [0] * N
    cnt = 0

    dfs(0, N, 0, S)
    print(f'#{tc} {cnt}')

# gpt랑 같이 푼 풀이


def dfs(idx, current_sum):
    global cnt
    if idx == N:
        if current_sum == S:
            cnt += 1
        return

    # 현재 원소를 선택하지 않는 경우
    dfs(idx + 1, current_sum)

    # 현재 원소를 선택하는 경우
    dfs(idx + 1, current_sum + arr[idx])


T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    dfs(0, 0)
    print(f'#{tc} {cnt}')
