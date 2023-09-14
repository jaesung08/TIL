from django.urls import path
from . import views

app_name = "practice3"

urlpatterns = [
    path("certification1/", views.certification1),
    path("certification2/", views.certification2),
    path("certification3/", views.certification3),
]
