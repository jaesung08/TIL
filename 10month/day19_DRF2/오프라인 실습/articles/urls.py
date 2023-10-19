from django.urls import path
from . import views


urlpatterns = [
    # 게시글 전체 조회, 게시글 생성( 대상: 게시글 전체 )
    path('articles/', views.article_list),
    # 게시글 상세 조회, 삭제, 수정( 대상: 게시글 하나 )
    path('articles/<int:article_pk>/', views.article_detail),
]
