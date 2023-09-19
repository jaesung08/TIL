N, M = map(int, input().split())
path = [0] * 10
def printpath(level):
    print(' '.join(map(str, path[:level]))) # 주사위 값을 문자열로 변환하여 공백을 넣어 출력

def roll1(level): # M =1 일때 N번 주사위 던져서 나올 수 있는 모든 경우
    if level == N:
        printpath(level)
        return

    for i in range(1, 7):
        path[level] = i #1. 현재 레벨의 주사위 값을 i로 설정
        roll1(level+1) #2. 다음 레벨로 재귀 호출
        path[level] = 0 #3. 백트리킹, 현재 레벨의 주사위 값을 초기화


def roll2(level):  # M=2 일때 N번 주사위 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
    if level == N:
        printpath(level)
        return

    for i in range(1, 7):
        if level > 0 and i < path[level - 1]: # 전에 나온 수보다 크거나 같은 수를 반환하여 중복을 제외
            continue
        path[level] = i  # 1. 현재 레벨의 주사위 값을 i로 설정
        roll2(level + 1)  # 2. 다음 레벨로 재귀 호출
        path[level] = 0  # 3. 백트리킹, 현재 레벨의 주사위 값을 초기화


DAT = [0] * 10
def roll3(level):  # M=2 일때 N번 주사위 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
    if level == N:
        printpath(level)
        return

    for i in range(1, 7):
        if DAT[i] == 1:
            continue
        DAT[i] = 1  # 현재 레벨에서 i 눈금 사용 체크
        path[level] = i  # 1. 현재 레벨의 주사위 값을 i로 설정
        roll3(level + 1)  # 2. 다음 레벨로 재귀 호출
        path[level] = 0  # 3. 백트리킹, 현재 레벨의 주사위 값을 초기화
        DAT[i] = 0      # 백트래킹, i눈금 사용 초기화

if M== 1:
    roll1(0)
elif M == 2:
    roll2(0)
elif M == 3:
    roll3(0)