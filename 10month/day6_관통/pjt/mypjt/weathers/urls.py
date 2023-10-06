"""
URL configuration for firstpjt project.

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

app_name = 'weathers'

urlpatterns = [
    path("", views.index, name="index"),
    path('problem1/', views.problem1, name = 'problem1'),
    path('problem2/', views.problem2, name = 'problem2'),
    path('problem3/', views.problem3, name = 'problem3'),
    path('problem4/', views.problem4, name = 'problem4'),

    
]
