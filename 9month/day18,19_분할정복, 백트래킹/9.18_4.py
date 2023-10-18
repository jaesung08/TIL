n, q = map(int, input().split())
lst = list(map(int, input().split()))
for _ in range(q):
    s, e = map(int, input().split())
    cnt = 0
    for target in lst:
        if s<= target <= e:
            cnt += 1
    print(cnt)