from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from .models import DepositProducts, DepositOptions
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Max


@api_view(['GET'])
def save_deposit_products(request):
    # requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금
    # 상품 목록과 옵션 목록을 DB에 저장 
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
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

    return JsonResponse({'message' : 'okay'})



@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        # GET: 전체 정기예금 상품 목록 반환
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # POST: 상품 데이터 저장
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    # 특정 상품의 옵션 리스트 반환
    product = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(product, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    # 가입 기간에 상관없이 금리가 가장 높은 상품 찾기
    top_product = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    options = DepositOptions.objects.get(intr_rate2 = top_product['intr_rate2'])
    print(options)
    # 해당 오션의 상품 찾기
    product = DepositProducts.objects.get(id=options.product_id)
    print(product)

    # 상품 및 옵션 데이터를 직렬화
    product_serializer = DepositProductsSerializer(product)
    options_serializer = DepositOptionsSerializer(options)
    
    # 응답 데이터 구성
    response_data = {
        'top_product': product_serializer.data,
        'options': options_serializer.data
    }
    
    return Response(response_data)
