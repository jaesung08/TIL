def binary_search(target):
    start, end = 0, n -1
    check = 0

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return True
        elif a[mid] > target:
            #직전에 왼쪽 방향을 검사했다면 탐색 중단
            if check == 1:
                break
            check = 1
            end = mid -1 #끝 위치를 중간 위치보다 왼쪽으로 이동
        else:
            #직전에 오른쪽 방향을 검사했다면 탐색 중단
            if check == 2:
                break
            check = 2
            start = mid +1 #시작위치를 중간위치보다 오른쪽으로 이동
    return False

T= int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    total = 0
    for num in b:
        total += binary_search(num)
    print(f'#{tc} {total}')