T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B + 1):
            bus_stop[j] += 1
    P = int(input())
    C = [int(input()) for _ in range(P)]

    print(f'#{tc}', end= ' ')
    for k in C:
        print(bus_stop[k], end=' ')
    print()

