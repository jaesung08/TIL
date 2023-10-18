# 데이터 추출 및 생성 예시

artist = {
    "id": 427,
    "name": "LE SSERAFIM",
    "type": "artist",
    "uri": "spotify:artist:4SpbR6yFEvexJuaBpgAU5p",
    "genres_ids": [
        84,
        580,
        696,
        674,
        108
    ]
}


def make_dict(data):
    new_data = {
        '이름': data.get('name'),
        '타입': data.get('type'),
        'URI-0': data.get('uri').split(':')[0]
    }
    return new_data


print(make_dict(artist))
