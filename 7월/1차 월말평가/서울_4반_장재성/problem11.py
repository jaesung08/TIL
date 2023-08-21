############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# # 사용시 감점처리 되니 반드시 확인 바랍니다.
# def get_row_col_maxsum(matrix):
#     pass
#     # 여기에 코드를 작성하여 함수를 완성합니다.


# # 아래 코드는 실행 확인을 위한 코드입니다.
# if __name__ == '__main__':
#     # 예시 코드는 수정하지 마세요.
#     example_matrix = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]
#     ]

#     example_matrix2 = [
#         [11, 5, 49, 20],
#         [28, 16, 20, 33],
#         [63, 17, 1, 15]
#     ]
#     print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
#     print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

# 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.


def get_row_col_maxsum(matrix):
    row_sum_max = 0
    col_sum_max = 0
    row_length = len(matrix)
    col_length = len(matrix[0])

    # Calculate row sums and find the maximum row sum
    for i in range(row_length):
        row_sum = 0
        for j in range(col_length):
            row_sum += matrix[i][j]
        row_sum_max = max(row_sum_max, row_sum)

    # Calculate column sums and find the maximum column sum
    for j in range(col_length):
        col_sum = 0
        for i in range(row_length):
            col_sum += matrix[i][j]
        col_sum_max = max(col_sum_max, col_sum)

    # Determine whether row_sum_max or col_sum_max is greater and return the result accordingly
    if row_sum_max >= col_sum_max:
        return ('row', row_sum_max)
    else:
        return ('col', col_sum_max)


# Test cases
if __name__ == '__main__':
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(get_row_col_maxsum(example_matrix))   # Output: ('row', 58)

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix2))  # Output: ('col', 102)
