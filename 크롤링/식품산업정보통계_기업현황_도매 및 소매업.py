from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime
import time

# Chrome 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 백그라운드 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# 웹페이지 열기
url = "https://www.atfis.or.kr/home/company.do"
driver.get(url)

# 페이지 로딩 대기
wait = WebDriverWait(driver, 10)

# ✅ 0. "도매 및 소매업" 탭 선택
try:
    # '도매 및 소매업' 탭 클릭 (a 태그 기반)
    tab_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'businessType=distribution')]")))
    driver.execute_script("arguments[0].click();", tab_element)
    time.sleep(6)  # 페이지가 변하는 동안 기다림
    print("✅ '도매 및 소매업' 탭 선택 완료")
except:
    print("❌ '도매 및 소매업' 탭 선택 실패")


# ✅ 1. "전국" 체크박스 선택
try:
    check_nationwide = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), '전국')]")))
    driver.execute_script("arguments[0].click();", check_nationwide)
    time.sleep(1)
    print("✅ '전국' 체크박스 선택 완료")
except:
    print("❌ '전국' 체크박스 선택 실패")

# ✅ 2. "도매업" 체크박스 선택
try:
    check_wholesale = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), '도매업')]")))
    driver.execute_script("arguments[0].click();", check_wholesale)
    time.sleep(1)
    print("✅ '도매업' 체크박스 선택 완료")
except:
    print("❌ '도매업' 체크박스 선택 실패")

# ✅ 3. "소매업" 체크박스 선택
try:
    check_retail = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), '소매업')]")))
    driver.execute_script("arguments[0].click();", check_retail)
    time.sleep(1)
    print("✅ '소매업' 체크박스 선택 완료")
except:
    print("❌ '소매업' 체크박스 선택 실패")

# ✅ 4. "시작년도 2023" 선택
try:
    start_year = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), '2023년')]")))
    start_year.click()
    time.sleep(1)
    print("✅ '시작년도 2023' 선택 완료")
except:
    print("❌ '시작년도' 체크 실패")

# ✅ 5. "종료년도 2023" 선택
try:
    end_year = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), '2023년')]")))
    end_year.click()
    time.sleep(1)
    print("✅ '종료년도 2023' 선택 완료")
except:
    print("❌ '종료년도' 체크 실패")

# ✅ 6. "검색" 버튼 클릭
try:
    search_button = driver.find_element(By.ID, "btnSearch")
    driver.execute_script("arguments[0].click();", search_button)
    time.sleep(3)
    print("✅ '검색' 버튼 클릭 완료")
except:
    print("❌ 검색 버튼 클릭 실패")

# ✅ 7. "목록수 100개" 선택
try:
    # 드롭다운 요소 찾기
    select_element = wait.until(EC.presence_of_element_located((By.ID, "changePageUnit")))
    # JavaScript로 값 변경
    driver.execute_script("arguments[0].value = '100';", select_element)
    # 변경 사항 반영을 위해 이벤트 트리거 (change 이벤트 발생)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", select_element)
    time.sleep(3)  # 페이지 업데이트 대기
    print("✅ '목록수 100개' 선택 완료")
except:
    print("❌ '목록수 100개' 선택 실패")



# ✅ 8. 데이터 크롤링 (페이지 넘기면서 진행)
data = []
page = 1
current_page = 1  # 현재 페이지

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 현재 시간 포맷팅
    print(f"📄 {current_page} 페이지 크롤링 중...", [{now}])
    
     # ✅ "테이블 데이터"가 정상적으로 로드될 때까지 기다리기
    try:
        table_rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr")))
    except:
        print("❌ 테이블 데이터를 찾을 수 없음! 다음 페이지로 이동할 수 없음.")
        break  # 테이블이 없으면 종료

    for row in table_rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) > 0:
            data.append([
                cols[1].text.strip(),  # 순위
                cols[2].text.strip(),  # 기업명
                cols[3].text.strip(),  # KSIC (업종)
                cols[4].text.strip(),  # 매출액
                cols[5].text.strip(),  # 영업이익
                cols[6].text.strip()   # 순이익
            ])

    # try:
    #     next_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'다음')]")  # "다음" 버튼 찾기
    #     if page == 3:
    #         print("----------5페이지 도달--------------")
    #         break
    #     if next_buttons:
    #         next_buttons[-1].click()  # 마지막 "다음" 버튼 클릭
    #         time.sleep(3)  # 페이지 로딩 대기
    #         page += 1
    #     else:
    #         print("✅ 마지막 페이지 도달!")
    #         break
    # except:
    #     print("❌ 다음 페이지 버튼 클릭 실패!")
    #     break  # 다음 페이지 버튼이 없으면 종료

    # ✅ 다음 페이지 버튼 찾기 (1순위: "{page+1}페이지로 이동")
    next_page_xpath = f"//li[@title='{current_page + 1}페이지로 이동']/a"
    next_page_button = driver.find_elements(By.XPATH, next_page_xpath)

    # ✅ "다음 {page+1}페이지로 이동" 버튼 찾기 (2순위)
    next_group_xpath = f"//li[@title='다음 {current_page + 1}페이지로 이동']/a"
    next_group_button = driver.find_elements(By.XPATH, next_group_xpath)

    # ✅ 버튼이 있을 경우 JavaScript로 강제 클릭
    if next_page_button:
        driver.execute_script("arguments[0].scrollIntoView();", next_page_button[0])  # 스크롤 이동
        time.sleep(1)
        driver.execute_script("arguments[0].click();", next_page_button[0])  # 강제 클릭
        time.sleep(3)  # 페이지 로딩 대기
        current_page += 1
        continue  # 다시 루프 시작

    elif next_group_button:
        driver.execute_script("arguments[0].scrollIntoView();", next_group_button[0])  # 스크롤 이동
        time.sleep(1)
        driver.execute_script("arguments[0].click();", next_group_button[0])  # 강제 클릭
        time.sleep(3)
        current_page += 1
        continue  # 다시 루프 시작

    print("✅ 마지막 페이지 도달!")
    break  # 모든 페이지 크롤링 완료

# ✅ 8. 데이터프레임 변환 및 엑셀 저장
columns = ["순위", "기업명", "KSIC", "매출액", "영업이익", "순이익"]
df = pd.DataFrame(data, columns=columns)
df.to_excel("식품산업정보통계_기업현황_도매 및 소매업.xlsx", index=False)

# # ✅ 9. 브라우저 종료
# driver.quit()

print("✅ 모든 데이터를 수집하여 '식품산업정보통계_기업현황_도매 및 소매업.xlsx' 파일로 저장 완료!")
