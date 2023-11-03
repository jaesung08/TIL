from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import numpy as np
import pandas as pd

@api_view(['GET'])
def dataframe(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949', sep=',')
    data = df.to_dict('records')
    
    return JsonResponse({'dat':data}, json_dumps_params={'ensure_ascii': False})



@api_view(['GET'])
def dataframe2(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949', sep=',')
    # NULL 값 주입
    df.fillna('NULL', inplace=True) 
    data = df.to_dict('records')

    return JsonResponse({'dat':data}, json_dumps_params={'ensure_ascii': False})


@api_view(['GET'])
def avg_data(request):
    df = pd.read_csv('data/test_data.CSV', encoding='cp949', sep=',')
    
    # 나이 열의 평균 계산
    avg_age = df['나이'].mean()
    
    # 평균 나이와의 차이를 계산한 후, 데이터프레임에 추가
    df['나이차'] = abs(df['나이'] - avg_age)
    
    # 나이와의 차이를 기준으로 데이터를 정렬
    sorted_df = df.sort_values(by='나이차')

    # 상위 10명을 출력
    avg_near10 = sorted_df.head(10)
    data =  avg_near10.to_dict('records')
    
    return JsonResponse({'dat':data}, json_dumps_params={'ensure_ascii': False})

