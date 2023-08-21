import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    pass


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    장르가 k-pop인 음악트랙 20개 가져오기
    (주의) 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(get_tracks())
    """
    ['Cupid - Twin Ver.',
    'Take Two',
    'Like Crazy',
    'MONEY',
    'OMG',
    'Like Crazy',
    'Ditto',
    'Bite Me',
    'FLOWER',
    'UNFORGIVEN (feat. Nile Rodgers)',
    'Super',
    'Hype Boy',
    'The Planet',
    'Dreamers [Music from the FIFA World Cup Qatar 2022 Official Soundtrack]',
    'Like Crazy (English Version)',
    'Cupid',
    'Run BTS',
    'Eve, Psyche & The Bluebeard’s wife',
    'Tally',
    'Spicy']
    """
