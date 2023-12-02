from rest_framework import serializers
from .models import *
from accounts.models import *
from accounts.serializers import *

# ------------- DB 저장 serializers -------------
class DepositProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositProducts
    fields = '__all__'
    read_only_fields=('like_user', 'join_user',)
    
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProductOptions
        fields = '__all__'
        read_only_fields=('product',)
        
class SavingsProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = SavingsProducts
    fields = '__all__'
    read_only_fields=('like_user', 'join_user',)
    
class SavingsOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsProductsOptions
        fields = '__all__'
        read_only_fields=('product',)

# -------------- 댓글 serializers ------------

class DP_CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    class Meta:
        model = DP_Comment
        fields = '__all__'
        read_only_fields=('user', 'article')
        
class SP_CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SP_Comment
        fields = '__all__'
        read_only_fields=('user', 'article')
        
