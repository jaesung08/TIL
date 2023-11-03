from django.urls import path
from . import views

urlpatterns = [
    path('dataframe/', views.dataframe),
    path('dataframe2/', views.dataframe2),
    path('avg_data/', views.avg_data),
]

