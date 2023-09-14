T = 10
for tc in range(1, T+1):
    str_N, str_num = input().split()

    N= int(str_N)
    stack = [0] * N
    top = -1

    for t in str_num:
        if top == -1 or stack[top] != t:    # 스택이 비어있거나, top원소와 다르다면
            top += 1                        # push(t)
            stack[top] = t
        else:                               # 스택이 비어있지 않고, top과 같으면
            top -= 1

    ans = ''
    for i in range(top+1):
        ans += stack[i]
    print(f'#{tc} {ans}')

    ans = ''.join(stack[:top+1])
    print(f'#{tc} {ans}')