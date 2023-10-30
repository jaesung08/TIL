from django.urls import path
from . import views


urlpatterns = [
    path('book_list/', views.books),
    path('book/<int:book_pk>/', views.book_one),
    path('book/<int:book_pk>/review_list/', views.reviews),
    path('review/<int:review_pk>/', views.review_one),
]
