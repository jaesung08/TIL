'''
Spotify에 요청을 보내기 위한 Header파일
'''

import requests

# 📌 여기에 발급받은 API_CLIENT_ID와 API_CLIENT_SECRET을 넣으세요.
API_URL = 'https://api.spotify.com/v1'
API_CLIENT_ID = ''
API_CLIENT_SECRET = ''

# 아래 코드는 수정하지 않습니다.
data = {
    'grant_type': 'client_credentials',
    'client_id': API_CLIENT_ID,
    'client_secret': API_CLIENT_SECRET
}


def getHeaders():
    # Access Token 발급받기(유효 시간은 한 시간, 이 후 새로 요청 필요)
    secure_key = requests.post('https://accounts.spotify.com/api/token', headers={
                               'Content-Type': 'application/x-www-form-urlencoded'}, data=data).json()
    # print('access token: ', secure_key.get('access_token'))

    access_token = secure_key.get('access_token')
    ACCESS_TOKEN = access_token

    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    return headers
