"""
URL configuration for mypjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    # 1. 날씨 API 테스트
    path('', views.index, name='index'),
    # 2. 서울의 5일치 예보 데이터 확인
    # 3. 예보 데이터 중 원하는 데이터만 DB에 저장
    path('save-data', views.save_date),
    # 4. 저장된 데이터 전체 조회
    path('list-data/', views.list_data),
    # 5. 특정 조건 데이터 확인 : 섭씨 30도가 넘는 시간대 조회
    path('hot_weathers/', views.hot_weathers),
]
