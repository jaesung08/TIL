from bs4 import BeautifulSoup
from selenium import webdriver


def get_google_data(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 검색 결과 가져오기
    # div 태그 안의 id 가 result-stats 라는 요소
    result_stats = soup.select_one("div#result-stats")
    print(result_stats.text)


get_google_data('파이썬')
