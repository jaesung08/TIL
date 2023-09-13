from django.urls import path, include
from . import views

app_name = "articles"

urlpatterns = [
    # 1번 실습 변수
    path("index/", views.index, name = 'index'),
    # 2번 실습 DTL
    path("dinner/", views.dinner, name = 'dinner'),
    # 3번 실습 form 태그
    path('search/', views.search, name = 'search'),
    # 4번 실습 throw, catch
    path('throw/', views.throw, name = 'throw'),
    path('catch/', views.catch, name = 'catch'),
    # path('articles/<int:num/>', views.detail, name ='detail'),
    # path('hello/<str:name/>', views.greeting, name = 'greeting')
]
    

    