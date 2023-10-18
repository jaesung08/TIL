from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # 앞에 profile을 쓰지 않고 <username>만 쓰면 
    # 유저네임 이후에 들어오는 문자열로 받는 형식을 인식을 하지 못한다
    # 다 그냥 유저네임으로 인식
    path('profile/<str:username>',views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
