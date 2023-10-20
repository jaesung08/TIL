from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
def index(request):

    return render(request, "weathers/index.html")


import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'
def problem1(request):
    df = pd.read_csv(csv_path)
    context= {
        'df' : df
    }

    return render(request, 'weathers/problem1.html', context)

# io : 입출력 연산을 위한 파이썬 표준 라이브러리
# BytesIO : 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼 : 임시저장 공간
# 파일 시스템과 유사하지만, 실제로 파일로 만들지 않고 메모리단에서 작업할 수 있다.
from io import BytesIO
# 텍스트 <-> 이진데이터를 변활할 수 있는 모듈
# plot => 이진 => 버퍼(저장) => (저장주소) => templates
import base64

# 참고: 터미널 에러
# PLT를 만드는 곳과 화면에 그리는 곳이 달라서 오류가 날 수 있다!
# 백엔드를 Agg 로 설정하여 해결
plt.switch_backend('Agg')

def problem2(request):
    # 필요한 데이터 값 추출
    df = pd.read_csv(csv_path)
    # 날짜
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date']
    # 최고, 평균, 최저의 각 온도
    hightem = df['TempHighF']
    avgtem = df['TempAvgF']
    lowtem = df['TempLowF']

    # 그래프 초기화
    plt.clf()
    # 그래프 사이즈 조정
    plt.figure(figsize=(18, 12))
    # 그래프 그리기
    plt.plot(dates, hightem, label='High Temperature')
    plt.plot(dates, avgtem, label='Average Temperature')
    plt.plot(dates, lowtem, label='Low Temperature')
    # 그래프 표 제목과 각 축 라벨달기
    plt.title("Temperature Variation", fontsize=25)
    plt.ylabel('Temperature (Fahrenheit)', fontsize=20)
    plt.xlabel('Date', fontsize=20)
    # 그래프 범례 표시
    plt.legend(loc='lower center', fontsize=18)
    # x축 갯수 정리
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=8))
    # 그리드 생성
    plt.grid(True)
    

    

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

    return render(request, "weathers/problem2.html", context)



def problem3(request):
    # 필요한 값 추출
    df = pd.read_csv(csv_path)
    # 날짜 형식 변환
    df['Date'] = pd.to_datetime(df['Date'])
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    # 각 월별 평균 최고, 평균, 최저 값 계산
    df_month_high = df.groupby("Month")["TempHighF"].mean()
    df_month_avg = df.groupby("Month")["TempAvgF"].mean()
    df_month_low = df.groupby("Month")["TempLowF"].mean()


    # 그래프 초기화
    plt.clf()
    # 그래프 사이즈 조정
    plt.figure(figsize=(18, 12))
    # 그래프그리기 (이번값은 평균값/날짜 로 계산된 값이기에 x,y축 같이 넣지 않아도 됌)
    plt.plot(df_month_high, label='High Temperature')
    plt.plot(df_month_avg, label='Average Temperature')
    plt.plot(df_month_low, label='Low Temperature')
    # 그래프 표 제목과 각 축 라벨달기
    plt.title("Temperature Variation", fontsize=25)
    plt.ylabel('Temperature (Fahrenheit)', fontsize=20)
    plt.xlabel('Date', fontsize=20)
    # 그래프 범례 표시
    plt.legend(loc='lower right', fontsize=18)
    # x축 표시 정렬
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    # 격자 생성
    plt.grid(True)
    

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

    return render(request, 'weathers/problem3.html', context)



def problem4(request):
    # 필요한 값 추출
    df = pd.read_csv(csv_path)
    df = df.replace({'Events' : ' '}, 'No Events') 
    
    # "Event" 열의 값을 분리하여 새로운 열에 저장
    df['Event_Separated'] = df['Events'].str.split(' , ')

    # 분리된 값들을 개별적으로 카운트
    event_counts = df['Event_Separated'].explode().value_counts()


    # 그래프 초기화
    plt.clf()
    # 그래프 사이즈 조정
    plt.figure(figsize=(18, 12))
    # 그래프그리기
    plt.bar(event_counts.index, event_counts.values)
    # 그래프 표 제목과 각 축 라벨달기
    plt.xlabel('Events', fontsize=25)
    plt.ylabel('Counts', fontsize=20 )
    plt.title('Event Counts', fontsize=20)
    # 격자 생성
    plt.grid(True)
    

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

    return render(request, 'weathers/problem4.html', context)