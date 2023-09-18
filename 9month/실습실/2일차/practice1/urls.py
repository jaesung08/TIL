from django.urls import path
from . import views

app_name = "practice1"

urlpatterns = [
    path("price/<str:thing>/<int:cnt>/", views.price, name="price"),
]
