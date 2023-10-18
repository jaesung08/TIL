# {1,2,3} 집합에서 3개의 숫자를 선택하는 기본적인 예제

arr = [i for i in range(1,4)]
path = [0]*3

def backtracking(cnt):
    #재귀를 끝내는 기저 조건
    #숫자 3개를 골랐을 때 종료
    if cnt == 3:
        print(*path)
        return
    # 1차 가지치기 (여기선 없음)

    # 반복문
    for num in arr:
        # 가지치기 - 중복된 숫자 제거
        if num in path:
            continue
        # 들어가기 전 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt+1)
        # 돌아와서 할 로직(초기화) { 여기가 제일 중요 }
        path[cnt] = 0


cnt = 0
backtracking(cnt)


#############################################################
