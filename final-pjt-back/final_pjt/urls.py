"""
URL configuration for final_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from news import views as mpviews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('dj-rest-auth/signup/', include('dj_rest_auth.registration.urls')),
    path('api/v1/', include('bank_products.urls')),

    # 환율계산기 url
    path('api/v1/exchange_rate/', include('exchangerate.urls')),

    # 프로필 업데이트
    path('accounts/profile/', include('accounts.urls')),

    # news
    # path('api/v1/news/', mpviews.news_info),
    path('api/v1/news/', include('news.urls')),

    # 코스피 지수
    path('api/v1/kospi/', mpviews.kospi_info),

]