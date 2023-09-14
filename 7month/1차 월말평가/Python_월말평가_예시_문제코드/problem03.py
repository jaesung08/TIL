def is_user_data_valid(user_data):
    # "id"와 "password" 키의 값을 가져옵니다.
    user_id = user_data.get('id')
    user_password = user_data.get('password')

    # "id" 또는 "password"가 비어있는 경우 False를 반환합니다.
    if not user_id or not user_password:
        return False

    # 둘 다 비어있지 않은 경우 True를 반환합니다.
    return True

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True
    # 아래 부터 추가 예제 코드 작성 가능합니다.

