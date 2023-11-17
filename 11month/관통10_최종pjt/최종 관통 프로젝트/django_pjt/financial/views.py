from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests
from .serializers import *
from .models import DepositProducts, DepositOptions
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Max

api_key = settings.API_KEY

# API KEY 활용해 데이터 확인용 코드
# @api_view(['GET'])
# def deposit_products(request):
#     url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
#     params = {
#         'auth': api_key,
#         'topFinGrpNo': '020000',
#         'pageNo': 1
#     }
#     response = requests.get(url, params=params)
#     products_data = response.json()
    
#     return Response(products_data)

# @api_view(['GET'])
# def saving_products(request):
#     url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

#     params = {
#         'auth': api_key,
#         'topFinGrpNo': '020000',
#         'pageNo': 1
#     }
#     response = requests.get(url, params=params)
#     products_data = response.json()
    
#     return Response(products_data)

# 상품 DB에 저장
@api_view(['GET'])
def save_products(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(url, params=params).json()

    # return Response(response)
    for li in response.get("result").get("baseList"):
        SavingData = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
            'mtrt_int' : li.get('mtrt_int'),    
            'max_limit' : li.get('max_limit'),
        }
        serializer = DepositProductsSerializer(data=SavingData)
        if serializer.is_valid():   # raise_exception=True
            serializer.save()

    

    for li2 in response.get("result").get("optionList"):
        try:
            product_instance = DepositProducts.objects.get(fin_prdt_cd=li2.get('fin_prdt_cd'))
            product_pk = product_instance.pk
            # print(product_instance.pk)
        except DepositProducts.DoesNotExist:
            product_pk = None  # 해당 상품을 찾을 수 없는 경우
            print(li2.get('fin_prdt_cd'))

        SavingData2 = {
            # 'product' : product_pk,
            'fin_prdt_cd' : li2.get('fin_prdt_cd'),
            'intr_rate_type_nm' : li2.get('intr_rate_type_nm'),
            'intr_rate' : li2.get('intr_rate') or -1,
            'intr_rate2' : li2.get('intr_rate2'),
            'save_trm' : li2.get('save_trm'),
        }
        serializer = DepositOptionsSerializer(data=SavingData2)
        if serializer.is_valid(raise_exception=True):   # raise_exception=True
            serializer.save(product=product_instance)   # product=product_instance



    url = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    params = {
        'auth': api_key,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(url, params=params).json()
    for li in response.get("result").get("baseList"):
        SavingData = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'kor_co_nm' : li.get('kor_co_nm'),
            'fin_prdt_nm' : li.get('fin_prdt_nm'),
            'etc_note' : li.get('etc_note'),
            'join_deny' : li.get('join_deny'),
            'join_member' : li.get('join_member'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
            'mtrt_int' : li.get('mtrt_int'),    
            'max_limit' : li.get('max_limit'),
        }
        serializer = SavingProductsSerializer(data=SavingData)
        if serializer.is_valid():   # raise_exception=True
            serializer.save()

    

    for li2 in response.get("result").get("optionList"):
        try:
            product_instance = SavingProducts.objects.get(fin_prdt_cd=li2.get('fin_prdt_cd'))
            product_pk = product_instance.pk
            # print(product_instance.pk)
        except SavingProducts.DoesNotExist:
            product_pk = None  # 해당 상품을 찾을 수 없는 경우

        SavingData2 = {
            # 'product' : product_pk,
            'fin_prdt_cd' : li2.get('fin_prdt_cd'),
            'intr_rate_type_nm' : li2.get('intr_rate_type_nm'),
            'intr_rate' : li2.get('intr_rate') or -1,
            'intr_rate2' : li2.get('intr_rate2'),
            'save_trm' : li2.get('save_trm'),
        }
        serializer = SavingOptionsSerializer(data=SavingData2)
        if serializer.is_valid(raise_exception=True):   # raise_exception=True
            serializer.save(product=product_instance)   # product=product_instance
            
    return JsonResponse({'message' : 'okay'})


## DB에 저장된 상품 리스트 출력
@api_view(['GET', 'POST'])
def deposit_products(request):
    deposit_products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(deposit_products, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def saving_products(request):
    saving_products = SavingProducts.objects.all()
    serializer = SavingProductsSerializer(saving_products, many=True)
    return Response(serializer.data)


## DB에 저장된 상품의 옵션 리스트 출력
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    # 특정 상품의 옵션 리스트 반환
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(product, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_products_options(request, fin_prdt_cd):
    # 특정 상품의 옵션 리스트 반환
    product = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(product, many= True)
    return Response(serializer.data)



@api_view(['GET'])
def detail_deposit_products(request, fin_prdt_cd):
    deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer1 = DepositProductsSerializer(deposit_product)
    
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer2 = DepositOptionsSerializer(product, many= True)
    
    response_data = {
        'deposit_product' : serializer1.data,
        'deposit_product_options' : serializer2.data,
    }
    return Response(response_data)

@api_view(['GET'])
def detail_saving_products(request, fin_prdt_cd):
    saving_product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    serializer1 = SavingProductsSerializer(saving_product)
    
    product = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer2 = SavingOptionsSerializer(product, many= True)
    
    response_data = {
        'saving_product' : serializer1.data,
        'saving_product_options' : serializer2.data,
    }
    return Response(response_data)