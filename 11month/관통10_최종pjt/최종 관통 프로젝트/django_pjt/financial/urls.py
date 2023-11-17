from django.urls import path
from . import views

urlpatterns = [
    # 예적금 상품 리스트
    path('deposit_products/', views.deposit_products ),
    path('saving_products/', views.saving_products ),
    # 상품 전체 저장
    path('save_products/', views.save_products),
    # 옵션목록 
    path('deposit_products_options/<str:fin_prdt_cd>/', views.deposit_products_options ),
    path('saving_products_options/<str:fin_prdt_cd>/', views.saving_products_options ),
    # 상품 detail
    path('deposit_products/<str:fin_prdt_cd>/', views.detail_deposit_products ),
    path('saving_products/<str:fin_prdt_cd>/', views.detail_saving_products ),

]
