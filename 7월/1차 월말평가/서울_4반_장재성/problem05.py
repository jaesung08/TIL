############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def change_pwd(word, secret_code):
    num_list = []
    for i in word: # 주어진 문자에 해당하는 숫자를 뽑아서 리스트 작성
        num = secret_code.get(i)
        num_list.append(num)
        
    for j in num_list: # 작성된 리스트를 차레대로 출력 
        print(j, end='')
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    secret_code = {
        'a': 3,    'b': 8,    'c': 0,    'd': 1,
        'e': 7,    'f': 6,    'g': 7,    'h': 1,
        'i': 2,    'j': 5,    'k': 3,    'l': 6,
        'm': 5,    'n': 0,    'o': 7,    'p': 9,
        'q': 8,    'r': 2,    's': 4,    't': 9,
        'u': 6,    'v': 3,    'w': 2,    'x': 4,
        'y': 8,    'z': 1,    ' ': 0,
    }
    print(change_pwd('ssafy', secret_code)) # => 44368
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    