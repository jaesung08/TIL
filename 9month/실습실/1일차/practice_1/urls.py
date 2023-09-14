from django.urls import path
from . import views

app_name = "practice1"

urlpatterns = [
    path("fruit/", views.fruit, name="fruit"),

]
