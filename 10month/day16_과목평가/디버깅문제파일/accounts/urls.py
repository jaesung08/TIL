from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit, name='edit'),
    path('signup/', views.signup, name='signup'),
    path('resign/', views.resign, name='resign'),
]
