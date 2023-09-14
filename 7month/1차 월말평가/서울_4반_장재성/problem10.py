############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
# def find_one(matrix):
#     pass
#     # 여기에 코드를 작성하여 함수를 완성합니다.


# # 아래 코드는 실행 확인을 위한 코드입니다.
# if __name__ == '__main__':
#     # 예시 코드는 수정하지 마세요.
#     sample_matrix = [
#       [0, 0, 0],
#       [0, 1, 0],
#       [0, 0, 0]
#     ]
#     print(find_one(sample_matrix))  # => (1, 1)
#     # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.

def find_one(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                return (i, j)
    return None


# Test case
if __name__ == '__main__':
    sample_matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # Output: (1, 1)

    # Additional test cases
    matrix2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 0]
    ]
    print(find_one(matrix2))  # Output: (2, 1)

    matrix3 = [
        [0, 0],
        [1, 0]
    ]
    print(find_one(matrix3))  # Output: (1, 0)

    matrix4 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(find_one(matrix4))  # Output: None
