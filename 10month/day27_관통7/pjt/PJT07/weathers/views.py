from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests
from .serializers import WeatherSerializer
from .models import Weather

# Create your views here.
@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city ='Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(url).json()

    return Response(response)


@api_view(['GET'])
def save_date(requsest):
    api_key = settings.API_KEY
    city ='Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

    response = requests.get(url).json()

    for li in response.get("list"):
        SavingData = {
            'dt_txt': li.get('dt_txt'),
            'temp' : li.get('main').get('temp'),
            'feels_like' : li.get('main').get('feels_life'),
        }
        # 저장하기 위해 데이터를 포장
        serializer = WeatherSerializer(data=SavingData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 저장 완료 메세지
    return JsonResponse({'message': 'okay'})





@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()
    # 응답할 수 있는 형태(JSON)로 포장
    serializer = WeatherSerializer(weathers, many =True)
    return Response(serializer.data)



@api_view(['GET'])
def hot_weathers(request):
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers:
        # 섭씨 = 켈빈 - 273.15
        temp = round(weather.tmp - 273.15, 2)
        if temp > 20:

            hot_weathers.append(weather)
    serializer = WeatherSerializer(hot_weathers, many = True)
    return Response(serializer.data)