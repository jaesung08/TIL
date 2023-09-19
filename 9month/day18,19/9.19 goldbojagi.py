n = int(input())
lst = list(map(int, input().split()))
path = []
lst.sort()
# 짱돌의 무게를 path에 저장해서 그 안에 있다면 멈춤
def getgold(cnt):
    if not lst:
        print(cnt)
        return
    a1 = lst.pop(0)
    a2 = lst.pop(0)
    if a1 in path or a2 in path:
        print(cnt)
        return
    lst.append((a2*2))
    path.append((a2*2))
    lst.sort()
    getgold(cnt+2)
getgold(0)

# 내 풀이는 답은 나오나 옳지 않은 방법인거 같음.

##### 강사님 풀이
import heapq
N = int(input())
arr = list(map(int, input().split()))
que = [] # 황금과 짱돌을 저장할 최소 힙
cnt = 0 #황금의 개수
for i in range(N):  #입력받은 황금의 무게들을 최소 힙에 추가
    heapq.heappush(que, [arr[i], -1])  # 각 황금의 무게와 -1(황금을 뜻함)을 저장
while que:  # 힙의 요소가 있을 때 까지 잔복
    x, tp = heapq.heappop(que)  # 힙에서 가장 가까운 돌을 꺼낸다.
    if tp == 0: # 꺼낸돌이 짱돌이면
        break
    cnt += 1

    y, tp = heapq.heappop(que) # 다음 가장 가벼운 돌을 꺼낸다
    if tp == 0:
        break
    else:
        heapq.heappush(que, [y*2, 0])  # 황금의 2배의 무게의 짱돌을 힙에 추가
    cnt += 1
print(cnt)