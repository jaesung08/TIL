# converter/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .serializers import *

@api_view(['POST'])
def convert_currency(request):
    serializer = CurrencyConversionSerializer(data=request.data)
    if serializer.is_valid():
        amount = serializer.validated_data['amount']
        from_currency = serializer.validated_data['from_currency']
        to_currency = serializer.validated_data['to_currency']

        # API 키는 https://open.er-api.com/ 에서 무료로 발급받을 수 있습니다.
        api_key = 'YOUR_API_KEY'
        url = f'https://open.er-api.com/v6/latest/{from_currency}?apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        # return Response(data)
        
        if 'error' in data:
            error_message = data['error']
            return Response({'error_message': error_message}, status=400)

        exchange_rate = data['rates'][to_currency]
        converted_amount = round(amount * exchange_rate, 2)

        return Response({'amount': amount, 'from_currency': from_currency,
                         'to_currency': to_currency, 'converted_amount': converted_amount})
    else:
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def convert_currency_list(request):
    serializer = CurrencyConversionListSerializer(data=request.data)
    if serializer.is_valid():
        amount = serializer.validated_data['amount']
        from_currency = serializer.validated_data['from_currency']

        # API 키는 https://open.er-api.com/ 에서 무료로 발급받을 수 있습니다.
        api_key = 'YOUR_API_KEY'
        url = f'https://open.er-api.com/v6/latest/{from_currency}?apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        exchange_rate = {currency: f"{round(rate * amount, 2)} {currency}" for currency, rate in data['rates'].items()}
        
        return Response(exchange_rate)













# # converter/views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import requests
# from .serializers import CurrencyConversionSerializer

# @api_view(['POST'])
# def convert_currency(request):
#     serializer = CurrencyConversionSerializer(data=request.data)
    
#     if serializer.is_valid():
#         amount = serializer.validated_data['amount']
#         from_currency = serializer.validated_data['from_currency']
#         to_currency = serializer.validated_data['to_currency']

#         # API 키를 환경 변수로부터 가져오기
#         api_key = 'YOUR_API_KEY'  # 실제로는 os.environ 또는 django settings를 활용

#         url = f'https://api.koreaexim.go.kr/...?apikey={api_key}'  # 적절한 API 엔드포인트 사용
#         response = requests.get(url)

#         try:
#             response.raise_for_status()
#             data = response.json()
#         except requests.exceptions.HTTPError as errh:
#             return Response({'error_message': f"HTTP Error: {errh}"}, status=500)
#         except requests.exceptions.RequestException as err:
#             return Response({'error_message': f"Request Exception: {err}"}, status=500)

#         if 'status' in data and data['status'] != '0000':
#             error_message = data['message']
#             return Response({'error_message': error_message}, status=400)

#         exchange_rate = data['rates'][to_currency]
#         converted_amount = round(amount * exchange_rate, 2)

#         return Response({'amount': amount, 'from_currency': from_currency,
#                          'to_currency': to_currency, 'converted_amount': converted_amount})
#     else:
#         return Response(serializer.errors, status=400)