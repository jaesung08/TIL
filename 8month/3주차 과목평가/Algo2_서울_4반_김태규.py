# 소괄호 내 숫자의 합을 계산하기 위해 만든 식
def my_sum(arr):
    add = 0
    for numb in arr:
        add += numb
    return add


# 중괄호 내 숫자의 곱을 계산하기 위해 만든 식
def my_multi(arr):
    multi = 1
    for numb in arr:
        multi *= numb
    return multi


T = int(input())
for tc in range(1, T+1):
    func = input()
    stack = []      # 괄호를 담을 스택
    nums = []       # 숫자를 담을 스택
    top = -1        # 현재 스택이 가르키고 있는 인덱스
    result = 0      # 결과값을 저장할 숫자
    try:            # 예외 상황을 처리하기 위해 try 를 사용하였음
        for i in func:                  # 열린 괄호가 오는 경우, 닫힌 괄호가 오는 경우, 숫자 혹은 문자가 오는 경우로 구분
            if i == '(' or i == '{':    # 첫번째, 열린 괄호가 오는 경우
                stack.append(i)         # 괄호 스택에 열린 괄호를 추가
                nums.append([])         # 숫자 스택에는 n번째 괄호에서 연산할 숫자를 담을 리스트를 생성
                top += 1                # 스택이 가르키는 인덱스 변경
            elif i == ')' or i == '}':  # 두번째, 닫힌 괄호가 오는 경우
                if top == -1:           # 스텍이 비어있는데 닫힌 괄호가 오는 경우는 예외처리
                    raise ValueError
                elif i == ')' and stack[top] == '(':    # 소괄호의 짝이 맞을 경우
                    my_list = nums.pop()                # 숫자 스택의 가장 끝 리스트를 가져와서 값을 모두 더함
                    top -= 1                            # 스택이 가르키는 인덱스를 변경
                    add_num = my_sum(my_list)
                    if top != -1:                       # 변경한 인덱스가 -1이 아닐 경우, 다음 리스트에 추가
                        nums[top].append(add_num)
                    else:                               # 변경한 인덱스가 -1일 경우, 결과값으로 반환
                        result = add_num
                elif i == '}' and stack[top] == '{':    # 중괄호의 짝이 맞을 경우
                    my_list = nums.pop()                # 소괄호의 경우와 동일
                    top -= 1
                    multi_num = my_multi(my_list)
                    if top != -1:
                        nums[top].append(multi_num)
                    else:
                        result = multi_num
                else:
                    raise ValueError                    # 소괄호, 중괄호의 짝이 맞지 않을경우 예외처리
            elif nums:                  # 세번째, 숫자 혹은 문자가 오는 경우
                nums[top].append(int(i))    # 숫자로 치환할 수 없다면, 즉, 문자라면 ValueError 가 일어나 예외처리
            else:
                raise ValueError        # 이외에 괄호 외부에서 숫자가 오는 경우 예외처리
    except ValueError:
        result = -1                     # 예외처리시 결과값을 -1로 할당

    print(f'#{tc} {result}')
