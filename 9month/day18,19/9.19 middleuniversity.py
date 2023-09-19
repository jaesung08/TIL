import heapq

max_heap = []
min_heap = []
mid = 500

def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v) # maxheap을 구현을 위해 -1 곱하기
    else:
        heapq.heappush(min_heap, v)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    push(a)
    push(b)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, mid)
        mid = -heapq.heappop(max_heap)  #maxheap 에서 값을 꺼낼때 -1 곱해주기
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)  # maxheap에 값을 넣을때 -1 곱하기
        mid = heapq.heappop(min_heap)
    print(mid)
