# requests 사용 예시 2 : 신간 도서 리스트

import requests
from pprint import pprint
import json


### request 방법 1

ttbkey = '부여받은 TTBKey'
query_type = 'ItemNewSpecial'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101

URL = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={ttbkey}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"

#request 보내기
response = requests.get(URL)

#받은 response를 json 타입으로 바뀌주기
response_json = response.json()

#확인
pprint(response_json)


### request 방법 2

URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

params = {
    'ttbkey': '부여받은 TTBKey',
    'QueryType': 'ItemNewAll',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

response = requests.get(URL, params=params).json()
pprint(response['item'])
