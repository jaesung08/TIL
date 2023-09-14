# ############## 주의 ##############
# # 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# # 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# # 사용시 감점처리 되니 반드시 확인 바랍니다.
# def sum_digits(number):
#     pass
#     # 여기에 코드를 작성하여 함수를 완성합니다.

# # 아래 코드는 실행 확인을 위한 코드입니다.
# if __name__ == '__main__':
#     # 예시 코드는 수정하지 마세요.
#     print(sum_digits(123))  # => 6
#     # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.

def sum_digits(n):
    # 기저 조건: n이 한 자리 수인 경우
    if n < 10:
        return n

    # n의 마지막 자리 숫자와 나머지 숫자를 구합니다.
    last_digit = n % 10
    remaining_digits = n // 10

    # 나머지 숫자들의 합을 재귀적으로 계산하고, 마지막 자리 숫자를 더하여 반환합니다.
    return last_digit + sum_digits(remaining_digits)


# Test cases
if __name__ == '__main__':
    print(sum_digits(123))  # Output: 6
    print(sum_digits(9))    # Output: 9
    print(sum_digits(456))  # Output: 15
    print(sum_digits(9876543210))  # Output: 45
