# 1번

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 16진수 자리수 N
    P = list(input()) # 암호화된 16진수 P 리스트
    key = int(input()) # 한 자리 16진수 key 입력받아 정수로 변환
    
    H = [0] * N
    for i in range(N):
        # XOR연산(^) : 두 비트 값이 다를때는 1반환, 같을 때는 0 반환
        H[i] = int(P[i], 16) ^ key # P의 i번쨰 자리를 16진수를 정수로 변환 후 key와 XOR연산
    print(f"#{tc}", end = " ") 
    
    for x in H:
        print(f"{x:X}", end = "")
    print()

# 2번

#i : 현재행, N : 전체 행의 수, s : 현재까지의 점수 합
def func(i, N, s):
    global max_v
    if i == N: # 모든 행을 다 본 경우
        if max_v < s:
            max_v = s
    else:
        for j in range(i, N): # 현재 행부터 마지막 행까지 순회
            p[i], p[j] = p[j], p[i]
            # 재귀호출로 다음 행으로 넘어가며 점수를 더해준다
            func(i +1, N, s + arr[i][p[i]])
            # 백트래킹 (원래 순서로 다시 바꿔줌)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [ list(map(int,input().split())) for _ in range(N) ]
    p = [ i for i in range(N) ] #초기 순서 저장하는 리스트 P
    max_v = 0
    func(0, N, 0)
    print(f"#{tc} {max_v}")
    
    
# 3번
# n^2가 짝수면 n이 짝수다
# 
# 대우명제 => n이 홀수이면 n^2이 홀수이다.
# n = 2k + 1표현해서 증명
# 대우명제가 참이므로, 본 명제 또한 참이다.