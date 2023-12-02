from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import User, UserSerializer, CustomRegisterSerializer
# permission Decorators // 권한에 대한 것
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import check_password
from rest_framework import status

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def user(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@ api_view(['PUT',])
@permission_classes([IsAuthenticated])
def userProfile_update(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['POST'])
def user_delete(request):
    user = request.user
    password = request.data.get('password1')

    if user.is_authenticated:
        print(password)
        if password and check_password(password, user.password):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def checkUserID(request):
    username = request.data['username']
    if User.objects.filter(username=username).exists():
        isExist = True
    else:
        isExist = False

    result = {'isExist': isExist}
    return JsonResponse(result, status=status.HTTP_200_OK) 

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def userDetail_list(request):
#     if not DetailUser.objects.filter(user=request.user).exists():
#         DetailUser.objects.create(user=request.user)
#         userdetail = DetailUser.objects.get(user=request.user)
#     else:
#         userdetail = DetailUser.objects.get(user=request.user)
#     # print(userdetail)
#     # userdetail = get_object_or_404(DetailUser, user=request.user)
#     if request.method == 'GET':
#         serializer = UserDetailSerializer(userdetail)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = UserDetailSerializer(userdetail, data=request.data, partial=True)
#         print('확인')
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)