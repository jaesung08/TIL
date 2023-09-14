############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def count_over_speed(speed_list):
    overspeed_list = [] # 오버된 속도값 받을 새 리스트 생성
    cnt = 0 
    for speed in speed_list: # 스피드 리스트 순회하며 스피드의 값이 100을 넘을 때 새리스트에 추가
        if speed > 100 :
            overspeed_list.append(speed)
            cnt += 1 # 새리스트에 추가될때마다 카운트 1업
            
    return(cnt)        
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(count_over_speed([119, 124, 178, 192,]))  #=> 4

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    
