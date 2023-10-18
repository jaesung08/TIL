import json


def dec_artists(artists):
    # 여기에 코드를 작성합니다.
    pass


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
