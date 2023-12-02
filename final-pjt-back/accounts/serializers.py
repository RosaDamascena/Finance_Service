from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from .models import User
# from django.contrib.auth import get_user_model

# 회원 가입시 활용할 것
class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField( required=True, allow_blank=False, max_length=25)
    gender = serializers.CharField(required=True, max_length=3)
    birthday = serializers.CharField(required=True, max_length=8)
    address = serializers.CharField(required=False, allow_blank=True, max_length=255)
    interest = serializers.CharField(required=True, max_length=10)
    married_period = serializers.IntegerField(required=False)
    saving_target_period = serializers.IntegerField(required=False)
    main_bank = serializers.CharField(required=False, allow_blank=True, max_length=15)

    couple_nickname = serializers.CharField(required=False, allow_blank=True, max_length=25)
    couple_birthday = serializers.CharField(required=False, allow_blank=True, max_length=8)
    
    def get_cleaned_data(self):
        return {
        'email': self.validated_data.get('email',''),
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'gender': self.validated_data.get('gender', ''),
        'birthday': self.validated_data.get('birthday', ''),
        'address': self.validated_data.get('address', ''),
        'interest': self.validated_data.get('interest', ''),
        'married_period': self.validated_data.get('married_period', ''),
        'saving_target_period': self.validated_data.get('saving_target_period', ''),
        'main_bank': self.validated_data.get('main_bank', ''),
        'couple_nickname': self.validated_data.get('couple_nickname', ''),
        'couple_birthday': self.validated_data.get('couple_birthday', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # model = get_user_model()
        fields = ('id', 'email','username',  'nickname',  'gender', 'birthday', 'address','interest','married_period','saving_target_period','main_bank', 'couple_nickname', 'couple_birthday')