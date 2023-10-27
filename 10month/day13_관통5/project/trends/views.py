from django.shortcuts import render, redirect
from .models import TREND, KEYWORD
from bs4 import BeautifulSoup
from selenium import webdriver
from django.utils import timezone
import matplotlib.pyplot as plt

def index(request):

    return render(request, "trends/index.html")

# Create your views here.
def keyword(request):
    if request.method == "POST":
        form = request.POST.get("name")
        if form:
            words = KEYWORD()
            words.name = form
            words.save()
        return redirect('trends:keyword')
    else:
        words = KEYWORD.objects.all()
        context = {
            'words' : words
        }
        return render(request, "trends/keyword.html", context)



def keyword_detail(request, pk):
    try:
        word = KEYWORD.objects.get(pk=pk)
        word.delete()
    except KEYWORD.DoesNotExist:
        # 항목이 존재하지 않을 경우 예외 처리
        pass
    return redirect("trends:keyword", )



def crawling(request):
    # 모든 키워드 가져오기
    keywords = KEYWORD.objects.all()
    # 기존에 있는 TREND 키워드들 삭제
    try:
        word = TREND.objects.all()
        word.delete()
    except TREND.DoesNotExist:
        # 항목이 존재하지 않을 경우 예외 처리
        pass
    # 크롬 웹 드라이버 시작
    driver = webdriver.Chrome()

    for keyword in keywords:
        # Google 검색 결과 페이지 열기
        url = f'https://www.google.com/search?q={keyword.name}'
        driver.get(url)

        # 페이지 소스 코드 및 BeautifulSoup 사용
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 검색 결과 개수 부분 추출
        result_stats = soup.select_one('div#result-stats').text

        # '약'과 '개' 사이의 검색 결과 수 추출
        from_index = result_stats.index("약")
        to_index = result_stats.index("개")
        result = result_stats[from_index + 1:to_index].replace(",", "")

        # 해당 키워드 및 검색 기간에 대한 TREND 객체 조회
        trend_with_name = TREND.objects.filter(name=keyword.name, search_period="all")

        if len(trend_with_name) == 1:
            # TREND 객체가 이미 존재하는 경우 업데이트
            for trend in trend_with_name:
                trend.result = int(result)
                trend.created_at = timezone.now()
                trend.save()
        else:
            # TREND 객체가 없는 경우 새로 생성
            trend = TREND(name=keyword.name, result=int(result), search_period="all", created_at=timezone.now())
            trend.save()

    # 모든 검색 결과 가져오기
    trends = TREND.objects.filter(search_period="all")

    context = {
        'trends': trends,
    }

    # 템플릿 렌더링
    return render(request, 'trends/crawling.html', context)



from io import BytesIO
import base64
def crawling_histogram(request):
    # TREND 모델에서 데이터 가져오기
    trends = TREND.objects.filter(search_period="all")

    # 데이터를 리스트로 추출
    keywords = [trend.name for trend in trends]
    result_counts = [trend.result for trend in trends]

    # 그래프 생성
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, result_counts)
    plt.xlabel('Keyword', fontsize= 20)
    plt.ylabel('Result', fontsize= 20)
    plt.title('Technology Trend Analysis', fontsize = 22)
    plt.legend(['Trend'], loc='upper right', fontsize=12)
    # 이미지를 파일로 저장
    plt.savefig('bar_chart.png')
    
    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')

    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹 페이지에 사용할 수 있도록 
    # URI 형식(주소형식)으로 만들어진 문자열을 생성
    context = {
        # chart_image : 저장된 이미지의 경로
        'chart_image' : f'data:image/png;base64,{image_base64}'
    }

    return render(request, "trends/crawling_histogram.html", context)



def crawling_advanced(request):
    # 모든 키워드 가져오기
    keywords = KEYWORD.objects.all()
    # 기존에 있는 TREND 키워드들 삭제
    # try:
    #     word = TREND.objects.all()
    #     word.delete()
    # except TREND.DoesNotExist:
    #     # 항목이 존재하지 않을 경우 예외 처리
    #     pass
    # 크롬 웹 드라이버 시작
    driver = webdriver.Chrome()

    for keyword in keywords:
        # Google 검색 결과 페이지 열기
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        driver.get(url)

        # 페이지 소스 코드 및 BeautifulSoup 사용
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 검색 결과 개수 부분 추출
        result_stats = soup.select_one('div#result-stats').text

        # '약'과 '개' 사이의 검색 결과 수 추출
        from_index = result_stats.index("약")
        to_index = result_stats.index("개")
        result = result_stats[from_index + 2:to_index].replace(",", "")

        # 해당 키워드 및 검색 기간에 대한 TREND 객체 조회
        trend_with_name = TREND.objects.filter(name=keyword.name, search_period="year")

        if len(trend_with_name) == 1:
            # TREND 객체가 이미 존재하는 경우 업데이트
            for trend in trend_with_name:
                trend.result = int(result)
                trend.created_at = timezone.now()
                trend.save()
        else:
            # TREND 객체가 없는 경우 새로 생성
            trend = TREND(name=keyword.name, result=int(result), search_period="year", created_at=timezone.now())
            trend.save()

    # 모든 검색 결과 가져오기
    trends = TREND.objects.filter(search_period="year")

    # 데이터를 리스트로 추출
    keywords = [trend.name for trend in trends]
    result_counts = [trend.result for trend in trends]

    # 그래프 생성
    plt.clf()
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, result_counts)
    plt.xlabel('Keyword', fontsize= 20)
    plt.ylabel('Result', fontsize= 20)
    plt.title('Technology Trend Analysis', fontsize = 22)
    plt.legend(['Trend'], loc='upper right', fontsize = 12)
    # 이미지를 파일로 저장
    plt.savefig('bar_chart.png')
    
    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')

    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹 페이지에 사용할 수 있도록 
    # URI 형식(주소형식)으로 만들어진 문자열을 생성
    context = {
        # chart_image : 저장된 이미지의 경로
        'chart_image' : f'data:image/png;base64,{image_base64}'
    }

    # 템플릿 렌더링
    return render(request, "trends/crawling_advanced.html", context)