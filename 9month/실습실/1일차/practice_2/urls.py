from django.urls import path
from . import views

app_name = "practice2"

urlpatterns = [
    path("throw/", views.calculation, name="throw"),
    path("catch/", views.result, name="catch"),
]
