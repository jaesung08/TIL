############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def make_answer(security_str, security_code):
    answer_list = []
    for i in security_code:  # 주어진 코드에 해당하는 인덱스의 문자를 가져와 리스트 생성.
        x = security_str[i]
        answer_list.append(x)

    for j in answer_list:  # 생성된 리스트 출력
        print(j, end='')


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4, 11, 17, 21, 24])
    print(answer)   # => SSAFY
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.


def make_answer(security_str, security_code):
    answer = ''
    for index in security_code:
        answer += security_str[index]
    return answer
