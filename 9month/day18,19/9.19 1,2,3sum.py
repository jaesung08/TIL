arr = [1,2,3]
n = int(input())
cnt = 0
def backtracking(result):
    global cnt
    if result == n:
        cnt += 1
        return cnt
    if result > n:
        return

    for num in arr:
        backtracking(result+ num)

backtracking(0)
print(cnt)