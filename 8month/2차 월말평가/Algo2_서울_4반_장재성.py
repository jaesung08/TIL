T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Acard = input().split()     # 조건에 대한 입력받기
    Bcard = []          # 카드를 받기 위한 덱 생성
    Ccard = []
    stack = []          # 숫자가 아닌 연산자를 처리할 스택 생성
    bonus = 0           # 연산자의 값을 처리할 보너스 값 변수 선언

    for i in Acard:     # 입력받은 카드를 순회
        if i.isdigit():     # 카드의 값이 숫자라면
            i = int(i)      # 숫자값을 정수선언
            if stack or bonus != 0:     # 스택에 + 가 쌓였거나 보너스가 0이 아니라면
                for _ in range(len(stack)):     # 스택에 쌓인 수 만큼 보너스 숫자 업
                    bonus += 1
                    stack.pop()
                i += bonus              # 보너스 만큼 값 추가

            if i % 2 == 1:          # 계산된 값이 홀수라면 B카드덱으로
                Bcard.append(i)

            elif i % 2 == 0:        # 값이 짝수라면 C카드덱으로
                Ccard.append(i)
        else:
            stack.append(i)         # 숫자가 아니라면 연산자를 위한 스택에 넣기

    result = 0                  # 결과값 변수 선언
    for j in range(1, M+1):     # 김싸피 차례만큼 순회
        Q = Bcard.pop(0)
        if j == M:              # 만약 김싸피 차례가 온다면 카드 값을 결과값에 더함
            result += Q
        elif not Bcard:         # 김싸피 차례가 되기 전 카드덱이 비어버린다면
            Q = 0               # 값을 0으로 처리
            break

    for j in range(1, M+1):     # 김싸피 차례만큼 순회
        W = Ccard.pop()
        if j == M:              # 만약 김싸피 차례가 온다면 카드 값을 결과값에 더함
            result += W
        elif not Ccard:         # 김싸피 차례가 되기 전 카드덱이 비어버린다면
            W = 0               # 값을 0으로 처리
            break

    print(f'#{tc} {result}')
# 처음부터 홀수 혹은 짝수만 나오는 등 B와C 카드덱이 비어서 들어오는 경우를 고려하지 못하였음.

# 강사님 풀이
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(input().split())
    B = []
    C = []
    bonus = 0
    for i in range(N):
        if A[i] == '+':
            bonus += 1
        else:
            num = int(A[i]) + bonus
            if num % 2 == 1:
                B.append(num)
            else:
                C.append(num)

    for i in range(K):
        card1 = B.pop(0) if B else 0        # 이게 내가 하고싶었던 것.
        card2 = C.pop() if C else 0

    print(f'#{tc} {card1 + card2}')


# 2
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Acard = input().split()     # 조건에 대한 입력받기
    Bcard = []          # 카드를 받기 위한 덱 생성
    Ccard = []
    stack = []          # 숫자가 아닌 연산자를 처리할 스택 생성
    bonus = 0           # 연산자의 값을 처리할 보너스 값 변수 선언

    for i in Acard:     # 입력받은 카드를 순회
        if i.isdigit():     # 카드의 값이 숫자라면
            i = int(i)      # 숫자값을 정수선언
            if stack or bonus != 0:     # 스택에 + 가 쌓였거나 보너스가 0이 아니라면
                for _ in range(len(stack)):     # 스택에 쌓인 수 만큼 보너스 숫자 업
                    bonus += 1
                    stack.pop()
                i += bonus              # 보너스 만큼 값 추가

            if i % 2 == 1:          # 계산된 값이 홀수라면 B카드덱으로
                Bcard.append(i)

            elif i % 2 == 0:        # 값이 짝수라면 C카드덱으로
                Ccard.append(i)
        else:
            stack.append(i)         # 숫자가 아니라면 연산자를 위한 스택에 넣기

    result = 0                  # 결과값 변수 선언
    for j in range(1, M+1):     # 김싸피 차례만큼 순회
        if Bcard:
            Q = Bcard.pop(0)
            if j == M:              # 만약 김싸피 차례가 온다면 카드 값을 결과값에 더함
                result += Q
        elif not Bcard:         # 김싸피 차례가 되기 전 카드덱이 비어버린다면
            Q = 0               # 값을 0으로 처리
            break

    for j in range(1, M+1):     # 김싸피 차례만큼 순회
        if Ccard:
            W = Ccard.pop()
            if j == M:              # 만약 김싸피 차례가 온다면 카드 값을 결과값에 더함
                result += W
        elif not Ccard:         # 김싸피 차례가 되기 전 카드덱이 비어버린다면
            W = 0               # 값을 0으로 처리
            break

    print(f'#{tc} {result}')
