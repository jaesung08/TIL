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


# # swea_4_im_답안지 채점
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     answer = list(map(int, input().split()))
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_score = 0
#     min_score = 10000000
#
#     for student in arr:
#         cnt = 0
#         score = 0
#         for i in range(M):
#             if student[i] == answer[i]:
#                 score += 1 + cnt
#                 cnt += 1
#             else:
#                 cnt = 0
#
#         if score >= max_score:
#             max_score = score
#         if score <= min_score:
#             min_score = score
#
#     print(f'#{tc} {max_score - min_score}')


# # # swea 1231 중위순회
# def inorder(p, N):  # N 완전이진트리의 마지막 정점
#     if p<=N:
#         inorder(p*2, N)           # 왼쪽 자식으로 이동
#         print(tree[p], end='')  # 중위 순회
#         inorder(p*2+1, N)          # 오른쪽 자식으로 이동
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0] * (N+1)
#     for _ in range(N):
#         arr = list(input().split())
#         tree[int(arr[0])] = arr[1]
#
#     print(f'#{tc}', end='')
#     inorder(1, N)
#     print()
#
#
# # 힙
# def deq():
#     global last
#     tmp = heap[1]           # 루트 백업
#     heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
#     last -= 1               # 마지막 노드 삭제
#     p = 1       # 루트에 옮긴 값을 자식과 비교
#     c = p * 2   # 왼쪽 자식 (비교할 노드 번호)
#     while c <= last:    # 자식이 하나라도 있다면
#         if c + 1 <= last and heap[c] < heap[c + 1]:     # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
#           c += 1        # 비교대상이 오른쪽 자식 노드
#         if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
#             heap[p], heap[c] = heap[c], heap[p]
#             p = c   # 자식을 새로운 부모로
#             c = p*2 # 왼쪽 자식 번호를 계산
#         else:   # 부모가 더크면
#             break # 비교 중단
#
#     return tmp
#
# heap = [0] *100
# last = 0


# # swea 5174 subtree
# def sub_tree(node):  # 서브트리의 노드의 수를 찾는 함수
#     global cnt
#     for i in range(2):  # 왼쪽 자식, 오른쪽 자식
#         if tree[i][node]:   # 해당 노드의 자식이 있다면
#             cnt += 1
#             n = tree[i][node]   # 자식 노드의 번호
#             sub_tree(n)    # 자식 노드에 대해 재귀호출
#
# T = int(input())
# for tc in range(1, T+1):
#     E, N = map(int, input().split())    # 간선개수E 노드번호N
#     temp = input().split()
#     # 노드 번호는 1번부터 E+1번까지 존재 -> 이진트리 리스트 초기화
#     tree = [[0 for _ in range(E+2)] for _ in range(2)]
#
#     for i in range(E):
#         p_node = int(temp[2*i])     # 부모노드 번호 -> 짝수 번째
#         c_node = int(temp[2*i +1])  # 자식노드 번호 -> 홀수 번째
#         if tree[0][p_node] == 0:    # 왼쪽자식이 없다면 왼쪽에 할당, 있다면 오른쪽에 할당
#             tree[0][p_node] = c_node
#         else:
#             tree[1][p_node] = c_node
#     cnt = 1
#     sub_tree(N)
#     print(f'#{tc} {cnt}')


# # swea 5176 이진탐색
# '''
# 완전 이진트리의 규칙
# 부모노드의 인덱스 : n
# 왼쪽 자식 노드의 인덱스 : 2n
# 오른쪽 자식 노드의 인덱스 : 2n +1
# '''
# def make_BST(n):
#     global node
#     if n <= N:  # n이 전체 노드 수 N보다 작거나 같을때만
#         make_BST(n * 2)     # 왼쪽 자식 노드로 이동
#         tree[n] = node
#         node += 1
#         make_BST(n*2 +1)    # 오른쪽 자식 노드로 이동
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = [0 for i in range(N+1)]
#     node = 1
#     make_BST(1)
#     print(f'#{tc} {tree[1]} {tree[N//2]}')


# # swea 5177 2진힙
# '''
# 큐 : 선입선출
# 우선순위 큐: 데이터를 우선순위를 가지고 저장, 우선순위가 높은 것 부터 꺼냄
# 힙 : 우선순위 큐를 구현하는 트리 기반의 자료구조, 최대힙, 최소힙
# import heapq => heapq 라이브러리를 사용하여 최소 힙 구현
# heapq.heappush(heap, num) :  num을 최소 힙 heap에 삽입
# heapq.heappop(heap) : 최소 힙 heap에서 가장 작은값을 꺼내 반환
# '''
# import heapq
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     tree = []
#     number = map(int, input().split())
#     for num in number:
#         heapq.heappush(tree, num) #힙에 num을 추가 => 자동으로 정렬
#     sum_v = 0
#     N = len(tree) // 2  # 부모의 노드 인덱스 계산
#     while N:
#         sum_v += tree[N-1]
#         N //= 2     # 부모노드로 올라가기 위해 N // 2
#     print(f'#{tc} {sum_v}')


# # swea 5178 노드의 합
# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int, input().split())
#     tree = [0 for _ in range(N +1)]
#     for i in range(M):
#         idx, value = map(int, input().split())
#         tree[idx] = value           # 트리에 리프노드의 값을 저장
#     for i in range(N, 0, -1):       # 노드의 개수부터 1까지 역순
#         if i //2 > 0:               # 부모 노드의 인덱스가 0보다 크다면
#             tree[i //2] += tree[i]  # 부모노드에서 자식노드의 값을 더함
#     result = tree[L]
#     print(f'#{tc} {result}')


# swea 4qks Ugly number
import heapq
N = int(input())
K = list(map(int, input().split()))
ugly = []  # 어글리 넘버 저장할 리스트
heap = [1]  # 최초 힙에 1 을 저장
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)

while len(ugly) < max(K):
    n = heapq.heappop(heap)  # 힙에서 최솟값 가져오기
    if n not in ugly:
        ugly.append(n)
        heapq.heappush(heap, n * 2)
        heapq.heappush(heap, n * 3)
        heapq.heappush(heap, n * 5)

for i in K:
    print(ugly[i - 1], end=' ')
