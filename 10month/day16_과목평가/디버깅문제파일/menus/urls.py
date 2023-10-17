from django.urls import path
from . import views

app_name = 'menus'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<menu_pk>/', views.detail, name='detail'),
    path('<menu_pk>/edit/', views.edit, name='edit'),
    path('<menu_pk>/review/', views.review_create, name='review_create'),
    # 문제 08. Review Delete 동작 에러 수정
    # Todo : 리뷰를 삭제할 수 있도록 views.py를 참고하여 urls.py 수정 필요
    path('<pk1>/review/<pk2>/delete/', views.review_delete, name='review_delete'),

    # 아래는 서술형을 위한 코드로 위치 이동 및 수정하지 않습니다.
    # 문제 10 서술형
    # 해당 URL로 요청 시 정상적으로 접근이 불가능하다. 
    # 그 이유와 해결 방법을 주어진 마크다운에 작성하시오.
    path('menu_recipe/', views.menu_recipe, name='recipe'),
]
