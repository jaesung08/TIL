# def stack(text):
#     stack=[]
#     result = []
#     if text[0] != '(':
#         return '-1'

#     for i in range(len(text)):
#         if text[i] == "(":
#             stack.append(text[i])
#             result.append('(')
#         # elif stack and text[i] != '(' and text[i-1] != '{' or text[i+1] == ')' and text[i] != '{':
#         #     if text[i-1] == '(':
#         #         result.append('+')
#         #         result.append(text[i])
#         #     elif text[i-2] == '(' and text[i] != '(' and text[i-1] != '{':
#         #         result.append('+')
#         #         result.append(text[i])

#         elif text[i] == "{":
#             stack.append(text[i])
#             result.append('(')
#         # elif stack and text[i] != '{' and text[i-1] != '(' or text[i+1] == '}' and text[i] != '(' :
#         #     if text[i - 1] == '{':
#         #         result.append('*')
#         #         result.append(text[i])
#         #     elif text[i - 2] == '{' and text[i] != '{' and text[i-1] != '(':
#         #         result.append('*')
#         #         result.append(text[i])

#         elif stack and text[i] == "}" and stack[-1] == "{":   # 스택이 비어있지 않고, 조건을 충족할시
#             stack.pop()
#             result.append(')')
#         elif stack and text[i] == ")" and stack[-1] == "(":
#             stack.pop()
#             result.append(')')
#         elif text[i] == "}" or text[i] == ")":
#             stack.append(text[i])

#                 # 파이썬 내부에서 0이 False고 나머지는 True, 고로
#     if stack:   # 리스트 비어 있으면 False, 안 비어 있으면 True 반환
#         return "-1"  # 스택이 비어있지 않는 경우
#     else:
#         return 'eval(result)'

# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     result = stack(text)
#     print(f'#{tc} {result}')


# 강사님 풀이
# 입력으로 주어진 수식의 괄호가 올바르게 짝지어졌는지 확인하는 함수
def check(form):
    stack = []  # 괄호를 저장할 스택
    for tk in form:
        if tk in ['(', '{']:
            stack.append(tk)  # 여는 괄호는 스택에 추가
        elif tk == ')':
            if stack and stack[-1] == '(':
                stack.pop()  # 짝이 맞는 여는 괄호 제거
            else:
                return 0  # 짝이 맞지 않는 경우 0 반환
        elif tk == '}':
            if stack and stack[-1] == '{':
                stack.pop()  # 짝이 맞는 여는 괄호 제거
            else:
                return 0  # 짝이 맞지 않는 경우 0 반환
    return 0 if stack else 1  # 스택이 비어있으면 모든 괄호가 짝이 맞는 경우

# 주어진 수식을 계산하는 함수
def op(form):
    stack = []  # 숫자와 연산자를 저장할 스택
    for tk in form:
        if tk == ')':
            tmp = 0
            while stack and stack[-1] != '(':
                tmp += int(stack.pop())  # 여는 괄호까지의 숫자들을 더해서 계산
            stack.pop()  # 여는 괄호 제거
            stack.append(tmp)  # 계산 결과를 스택에 추가
        elif tk == '}':
            tmp = 1
            while stack and stack[-1] != '{':
                tmp *= int(stack.pop())  # 여는 괄호까지의 숫자들을 곱해서 계산
            stack.pop()  # 여는 괄호 제거
            stack.append(tmp)  # 계산 결과를 스택에 추가
        else:
            stack.append(tk)  # 숫자나 여는 괄호는 그냥 스택에 추가
    return -1 if len(stack) != 1 else stack[0]  # 스택에 남은 숫자가 계산 결과


# 입력 처리
T = int(input())  # 테스트 케이스 개수 입력
for tc in range(1, T+1):
    form = input()  # 수식 입력
    ans = -1  # 결과 초기값 설정
    if check(form):  # 입력 수식의 괄호가 올바른 경우
        ans = op(form)  # 수식을 계산하여 결과 얻기

    print(f'#{tc} {ans}')  # 결과 출력
