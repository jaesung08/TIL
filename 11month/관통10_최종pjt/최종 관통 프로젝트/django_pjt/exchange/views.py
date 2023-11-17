# converter/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, datetime
from .serializers import *
from datetime import datetime, timedelta


@api_view(['GET'])
def convert_currency(request):
    today = datetime.now()			# 현재 날짜 추출
    yesterday = today - timedelta(days=1)
    
    api_key = 'TRLP98UbzQOqhFAAdzuA6gqLSfHOwrHF'
    date = yesterday.strftime('%Y%m%d')
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

    params = {
        'authkey': api_key,
        'searchdate': date,
        'data': 'AP01'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    serializer = CurrencyConversionListSerializer(data, many=True)
    
    return Response(serializer.data)





