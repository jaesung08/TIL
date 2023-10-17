from django.urls import path
from . import views

app_name = "dataerror"

urlpatterns = [
    path("data/", views.data, name="data"),
    path("data2/<int:pk>/", views.data2, name="data2"),
    path("data3/<int:pk>/", views.data3, name="data3"),
]
