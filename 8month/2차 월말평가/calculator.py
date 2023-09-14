# 강사님 기출 _ 자동 수학 계산기
'''
+와 -가 들어가있는 수식을 입력받고 자동으로 계산해주는 프로그램을 작성하라.

100+100-50+30
'''
# input = 100+100-50+30
# print(eval(input())) # 메서드 쓰면 한방에 끝

# eval 메서드 안쓰고 푸는법
ex = input()
if ex[0] == '-':
    ex = '0' + ex
word = ex.split('+') # 덧셈기호 기준으로 분리
ans = 0
for w in word:
    w = w.split('-') # 뺄셈으로 분리  => 100(+)100(-)50(+)30
    inner_ans = int(w[0]) # 첫번째 요소는 더해줄 값

    for i in range(1, len(w)): #나머지 요소들은 빼줄값
        inner_ans -= int(w[i])
    ans += inner_ans
print(ans)



'''
다음과같이배열에0이상인정수Ai, 소괄호( ), 중괄호{ }가들어있다.
괄호안의숫자는다음규칙에따라연산을한다.
-가장안쪽의괄호를먼저연산한다.
-소괄호( ) 안의숫자는모두더한다.
-중괄호{ } 안의숫자는모두곱한다.
-괄호의짝이맞지않는경우-1을출력한다

(2{(58)7}43)
'''

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
