############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    avg = 0
    for i in range(number): # 소수 및 17에 해당하지 않는 조건 배제 후 이외의 숫자 합 구하기
        if i==2 or i==3 or i==5 or i==7:
            avg +=i
        elif i==1 or i%2==0 or i%3==0 or i%5==0 or i%7==0 :
            pass
        elif i%17==0:
            pass
        else :
            avg +=i      
            
    return(avg) # 숫자 합 반환
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    