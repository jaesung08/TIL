############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    for i in word: # 주어진 문자열을 하나씩 숫자로 변환 
        a = ord(i)  
        b= a+num
        if b > 122  :  # 변환된 숫자를 조건에서 벗어나지 않도록 조건문 설정
            b = 97+(b-123)
            
        elif 97>b> 90:
            b = 65+(b-91)
            x = chr(b)
        x = chr(b)   
        print(x, end='')
        
        

        
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    