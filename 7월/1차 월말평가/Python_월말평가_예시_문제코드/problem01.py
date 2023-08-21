# 파이썬 내장함수 min 사용 금지
# def min_score(scores):
#     pass
#     # 여기에 코드를 작성합니다.
# if __name__ == '__main__':
#     # 아래의 코드는 수정하지 않습니다.
#     scores = [30, 60, 90, 70]
#     print(min_score(scores)) # 30
#     # 아래 부터 추가 예제 코드 작성 가능합니다.

def min_score(scores):
    # 리스트의 첫 번째 값을 최저점으로 초기화합니다.
    min_score = scores[0]
    
    # 리스트의 나머지 값을 순회하며 최저점을 찾습니다.
    for score in scores[1:]:
        if score < min_score:
            min_score = score
    
    return min_score # 최종 찾은 최저점을 반환 

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    python_scores = [80, 90, 70, 60]
    html_scores = [50, 40, 70, 80]
    javascript_scores = [90, 80, 60, 50]
    project_scores = [70, 80, 90, 60]

    total_scores = [python_scores[0], html_scores[1], javascript_scores[2], project_scores[3]]
    print(min_score(total_scores))
