############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):
    overspeed_list = [] # 새로운 리스트 생성
    for speed in speed_list: # 주어진 리스트내에서 기준치를 초과하면 새 리스트에 추가
        if speed > 100 :
            overspeed_list.append(speed)
    All_speed = 0
    cnt = 0
    for speed in overspeed_list: # 새 리스트에 추가된 항목들 모두 더하기
        All_speed += speed
        cnt += 1
        
    avg = All_speed / cnt
    return(avg)


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    