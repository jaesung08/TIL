# requests 사용 예시 2

import requests
from pprint import pprint
from spotify_config import getHeaders


def get_music():
    # search API 문서: https://developer.spotify.com/documentation/web-api/reference/search
    URL = 'https://api.spotify.com/v1'

    headers = getHeaders()
    params = {
        'q': 'artist:BTS track:Take Two',  # 필수 파라미터
        'type': 'track',                  # 필수 파라미터
        'market': 'KR',
        'limit': 1
    }

    # 요청 보내 받아온 결과는 requests 타입의 데이터이고, 파이썬에서 바로 쓸 수 없으며
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해 json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # response 구조는 위의 공식 문서에서 확인할 수 있다.
    result = response.get('tracks').get('items')

    return result


if __name__ == '__main__':
    """
    아티스트 BTS의 Take Two 이름의 트랙 정보를 조회하는 기능
    """
    pprint(get_music())
    """
    [{'album': {'album_type': 'single',
                'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX'},
                            'href': 'https://api.spotify.com/v1/artists/3Nrfpe0tUJi4K4DXYWgMUX',
                            'id': '3Nrfpe0tUJi4K4DXYWgMUX',
                            'name': 'BTS',
                            'type': 'artist',
                            'uri': 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'}],
                'external_urls': {'spotify': 'https://open.spotify.com/album/3jeQDa9OFZ6GndLindHx3k'},
                'href': 'https://api.spotify.com/v1/albums/3jeQDa9OFZ6GndLindHx3k',
                'id': '3jeQDa9OFZ6GndLindHx3k',
                'images': [{'height': 640,
                            'url': 'https://i.scdn.co/image/ab67616d0000b2738a701e76e8845928f6cd81c8',
                            'width': 640},
                        {'height': 300,
                            'url': 'https://i.scdn.co/image/ab67616d00001e028a701e76e8845928f6cd81c8',
                            'width': 300},
                        {'height': 64,
                            'url': 'https://i.scdn.co/image/ab67616d000048518a701e76e8845928f6cd81c8',
                            'width': 64}],
                'is_playable': True,
                'name': 'Take Two',
                'release_date': '2023-06-09',
                'release_date_precision': 'day',
                'total_tracks': 1,
                'type': 'album',
                'uri': 'spotify:album:3jeQDa9OFZ6GndLindHx3k'},
    'id': '5IAESfJjmOYu7cHyX557kz',
    'is_local': False,
    'is_playable': True,
    'name': 'Take Two',
    'popularity': 96,
    'preview_url': 'https://p.scdn.co/mp3-preview/ef43da30a06fcad16898e9fff1cadd0ccf953fc9?cid=6dd824599d1a411ba1e4de1a723a2db8',
    'track_number': 1,
    'type': 'track',
    'uri': 'spotify:track:5IAESfJjmOYu7cHyX557kz'}]
    """
