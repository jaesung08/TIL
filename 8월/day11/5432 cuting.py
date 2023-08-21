T = int(input())

for tc in range(1, T+1):
    string = input()
    stack = []
    cnt = 0 # 현상황에서 잘릴 수 있는 막대의 수
    result = 0  # 전체 짤린 막대의 수
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
            cnt += 1
        else: # 괄호가 닫힐 때, 일어날수 있는 상황에 대한 계산
            if string[i-1] == '(':
                cnt -= 1
                stack.pop()
                result += cnt
            else:
                cnt -= 1
                result += 1
    print(result)