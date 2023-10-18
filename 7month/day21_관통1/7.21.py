import requests

url = "https://fakestoreapi.com/carts"
response = requests.get(url).json()

print(response)

# JSON 실습
import json

json_data = '''
{
    "name" : "김싸피",
    "age" : 28,
    "hobbies" : [
        "공부하기",
        "복습하기"
    ]
}
'''
data = json.loads(json_data)
print(data)

#Json에서 원하는 데이터만 가져오기
name = data.get('name')
print(name)



API_KEY = '51e69c8492a36944eb6454e81949fdfa'
lat = 37.56
lon =126.97
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

import requests
# api 요청보내기
response = requests.get(url).json()
response

temp= response['main']['temp']
temp -= 273.15
temp

 # 본인의 API KEY 로 수정합니다.
api_key = "d8ac7b184792adf08a6f6bb6bd619d37"
url = f'https://fss.or.kr/finlife/finlifeapi/depositProductsSearch.xml?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
result = requests.get(url).json()
    
print(result)