from django.urls import path
from articles import views

app_name = 'articles'


urlpatterns = [
    # 전체 게시글 조화
    path('index/', views.index, name='index'),
    # 단일 게시글 조회
    path('<int:pk>/', views.detail, name = 'detail'),
    # create
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    # delete
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    # update
    # path('<int:pk>/edit/', views.edit, name= 'edit'),
    path('<int:pk>/update/', views.update, name= 'update'),
]


