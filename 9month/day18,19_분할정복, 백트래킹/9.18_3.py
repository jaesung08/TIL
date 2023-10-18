n = int(input())
arr = list(map(int, input().split()))
k = int(input())
lst = list(map(int, input().split()))

def binarySearch(arr, low, high, key):
    if low > high:
        return -1
    else:
        mid = (low+high) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binarySearch(arr, low, mid-1, key)
        else:
            return binarySearch(arr, mid+1, high, key)

R = []
for key in lst:
    low = 0
    high = len(arr) -1
    result = binarySearch(arr, low, high, key)
    if result == -1:
        print('X', end='')
    else:
        print('O', end='')

# # # # # # # # # # # # # # # # # # #
# 강사님 풀이
def binary_search(target):
    start, end = 0, N #시작점 끝점 초기화
    while start <= end:
        mid = (start + end) // 2
        #1. 왼쪽 부분 탐색, 중간점의 값이 찾고자 하는 값보다 큰 경우
        if A[mid] > target:
            end = mid - 1
        #2. 오른쪽 부분 탐색, 중간점의 값이 찾고자 하는 값보다 작은 경우
        elif A[mid] < target:
            start = mid + 1
        #3. 탐색 종료. 중간점의 값이 찾고자 하는 값과 같은경우
        elif A[mid] == target:
            return True
    return False #탐색이 종료 되었는데도 찾지 못한 경우
N = int(input())
A = tuple(sorted(list(map(int, input().split()))))
K = int(input())
B = tuple(map(int, input().split()))
for b in B:
    if binary_search(b):
        print('O', end = '')
    else:
        print('X', end = '')