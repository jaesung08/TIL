# def under_60(scores):
#     pass
#     # 여기에 코드를 작성합니다.


# if __name__ == '__main__':
#     # 아래의 코드는 수정하지 않습니다.
#     scores = [30, 60, 90, 70]
#     print(under_60(scores)) # 1
#     # 아래 부터 추가 예제 코드 작성 가능합니다.

def under_60(scores):
    score_60 = [] #score_60 미만을 넣을 리스트 생성 
    for score in scores[:]: #제공된 scores에서 슬라이스를 통해 각 인덱스에 해당하는 점수를 반환
        if score < 60 :  # 제공된 점수가 60점 미만일 경우
            score_60.append(score)  # 생성된 리스트에 첨부

    return (len(score_60))   # 생성된 리스트내에 첨부된 갯수 확인
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    more_scores = [45, 50, 55, 65, 58, 59]
    print(under_60(more_scores))  # 5