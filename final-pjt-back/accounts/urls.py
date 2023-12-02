from django.contrib import admin
from django.urls import path
from rest_framework import urls
from . import views

app_name = 'accounts'
urlpatterns = [    
    path('byebyeuser/', views.user_delete),
    path('userinfo/<str:username>/', views.user),
    path('updateinfo/<str:username>/', views.userProfile_update),
    path('checkUserID/', views.checkUserID)
]