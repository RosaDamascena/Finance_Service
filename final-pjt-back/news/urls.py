from django.urls import path
from . import views

urlpatterns = [
    path('economy_news/', views.news_info),
    path('search_news/<str:query>/', views.search_news),
    path('kospi_info/', views.kospi_info),
]
