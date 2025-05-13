from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/<int:author_id>/book/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/price/', views.book_price, name='book_price'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]