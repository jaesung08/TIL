from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # 프로필 페이지 : user_pk로 조회
    path('<int:user_pk>/', views.profile, name="profile"),

    
]
