# open 및 json 모듈 사용예시

import json


book = open('sample.json', encoding='utf-8')
book_detail = json.load(book)

print(book_detail)
