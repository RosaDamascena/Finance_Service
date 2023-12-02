from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from django.core.serializers import serialize
from .models import *
from .serializers import *
import requests
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
# -----------csv------------
import pandas as pd
import csv
import json
import pprint

API_KEY = "8fbfa11f9a3138d46e386c74e602fbd0"

# -------------------- 정기 예금 조회 --------------------

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, BasicAuthentication])
def deposit_products(request):
  # ---------------------API-------------------
  URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

  params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
  response = requests.get(URL, params=params).json()
  
  # ---------------------- baseList csv------------------
  # deposit_products_path = 'bank_products/data/deposit_products_baseList.csv'
  
  # response = []
  # with open(deposit_products_path, 'r', encoding='utf-8-sig') as file:
  #   csv_reader = csv.DictReader(file)
  #   for row in csv_reader:
  #     cleaned_row = {key: value.replace('\n', '') for key, value in row.items()}
  #     response.append(dict(cleaned_row))
      
  #   # pprint.pprint(response)

  # ---------------------- optionList csv-------------------
  # deposit_products_path = 'bank_products/data/deposit_products_optionList.csv'

  # response2 = []
  # with open(deposit_products_path, 'r', encoding='utf-8-sig') as file:
  #   csv_reader = csv.DictReader(file)
  #   for row in csv_reader:
  #     cleaned_row = {key: value.replace('\n', '') for key, value in row.items()}
  #     response2.append(dict(cleaned_row))

  #   # pprint.pprint(response2)
  # --------------------------------------------
  
  for d_product in response['result']['baseList']:  # API
  # for d_product in response:
    fin_prdt_cd = d_product['fin_prdt_cd']
    if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
      save_data = {
        'fin_prdt_cd': d_product.get('fin_prdt_cd'),
        'fin_co_no': d_product.get('fin_co_no'),
        'kor_co_nm': d_product.get('kor_co_nm'),
        'fin_prdt_nm': d_product.get('fin_prdt_nm'),
        'join_deny': d_product.get('join_deny'),
        'join_member': d_product.get('join_member'),
        'join_way': d_product.get('join_way'),
        'etc_note': d_product.get('etc_note'),
        'spcl_cnd': d_product.get('spcl_cnd'),
        'mtrt_int': d_product.get('mtrt_int'),
        'max_limit': d_product.get('max_limit'),
        'dcls_strt_day': d_product.get('dcls_strt_day'),
        'dcls_end_day': d_product.get('dcls_end_day'),
        # 'join_user' : d_product.get('join_user'),
        # 'like_user' : d_product.get('like_user'),
      }
      
      serializer = DepositProductsSerializer(data=save_data)
      if serializer.is_valid(raise_exception=True):
        product = serializer.save()
        
    else:
      product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

    for d_option in response['result']['optionList']:  # API
      # for d_option in response2:
      if fin_prdt_cd == d_option['fin_prdt_cd']:
        save_data2 = {
            'fin_prdt_cd': d_option.get('fin_prdt_cd'),               
            'intr_rate_type_nm': d_option.get('intr_rate_type_nm'),  
            'intr_rate': d_option.get('intr_rate'),  
            'intr_rate2': d_option.get('intr_rate2'),
            'save_trm': d_option.get('save_trm'),  
        }
          # if save_data2['intr_rate'] is None: # API
        if save_data2['intr_rate'] is None:
            # null 값 처리 
          save_data2['intr_rate'] = -1
        if save_data2['intr_rate2'] is None:
          save_data2['intr_rate2'] = -1
        serializer2 = DepositOptionsSerializer(data=save_data2)
        if serializer2.is_valid(raise_exception=True):
          # 48번째줄에서 저장해둔 product값을 db에 저장할 때, 같이 넘겨준다. 
          serializer2.save(product=product)
    
    # 상품과 옵션 한 번에 보내기        
    # deposit_products_list = []
    # baseList = response['result']['baseList']
    # optionList = response['result']['optionList']
    
    # for product in baseList:
    #   dict_product = {}
    #   dict_product2 = {}
    #   intr_rate_type_nm = ''
    #   for option in optionList:
    #     if not intr_rate_type_nm:
    #       intr_rate_type_nm = option['intr_rate_type_nm']
    #     if product['fin_prdt_cd'] == option['fin_prdt_cd']:
    #       dict_product[option['save_trm']] = option['intr_rate']
    #       dict_product2[option['save_trm']] = option['intr_rate2']

    #   trm = ['6', '12', '24', '36']
    #   for v in trm:
    #       if v not in dict_product.keys():
    #           dict_product[v] = 0
    #           dict_product2[v] = 0

    #   product['intr_rate_type_nm'] = intr_rate_type_nm
    #   product['intr_rate'] = dict_product
    #   product['intr_rate2'] = dict_product2
    #   deposit_products_list.append(product)  
    
    deposit_products_list = []
    baseList = response['result']['baseList']
    optionList = response['result']['optionList']

    for product in baseList:
        dict_product = {}
        intr_rate_type_nm = ''
        for option in optionList:
            if not intr_rate_type_nm:
                intr_rate_type_nm = option['intr_rate_type_nm']
            if product['fin_prdt_cd'] == option['fin_prdt_cd']:
                dict_product[option['save_trm']] = {
                    'intr_rate': option.get('intr_rate', 0),
                    'intr_rate2': option.get('intr_rate2', 0)
                }

        trm = ['6', '12', '24', '36']
        for v in trm:
            if v not in dict_product.keys():
                dict_product[v] = {
                    'intr_rate': 0,
                    'intr_rate2': 0
                }

        product['intr_rate_type_nm'] = intr_rate_type_nm
        product['rates'] = dict_product
        deposit_products_list.append(product)


  return Response(deposit_products_list) 

  # return JsonResponse({'response' : deposit_products_list})

# -------------------------------------- 적금 조회 ---------------------------------------------------

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, BasicAuthentication])
def savings_products(request):
  # ---------------------API-------------------
  URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

  params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : '1'
    }
  response = requests.get(URL, params=params).json()
  
  # ---------------------- baseList csv------------------
  # deposit_products_path = 'bank_products/data/savings_products_baseList.csv'
  
  # response = []
  # with open(deposit_products_path, 'r', encoding='utf-8-sig') as file:
  #   csv_reader = csv.DictReader(file)
  #   for row in csv_reader:
  #     cleaned_row = {key: value.replace('\n', '') for key, value in row.items()}
  #     response.append(dict(cleaned_row))
      
  #   # pprint.pprint(response)

  # ---------------------- optionLit csv-------------------
  # deposit_products_path = 'bank_products/data/savings_products_optionList.csv'

  # response2 = []
  # with open(deposit_products_path, 'r', encoding='utf-8-sig') as file:
  #   csv_reader = csv.DictReader(file)
  #   for row in csv_reader:
  #     cleaned_row = {key: value.replace('\n', '') for key, value in row.items()}
  #     response2.append(dict(cleaned_row))

  #   # pprint.pprint(response2)
  # --------------------------------------------
  
  for s_product in response['result']['baseList']:  # API
  # for s_product in response:
    fin_prdt_cd = s_product['fin_prdt_cd']
    if not SavingsProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
      save_data = {
        'fin_prdt_cd': s_product.get('fin_prdt_cd'),
        'fin_co_no': s_product.get('fin_co_no'),
        'kor_co_nm': s_product.get('kor_co_nm'),
        'fin_prdt_nm': s_product.get('fin_prdt_nm'),
        'join_deny': s_product.get('join_deny'),
        'join_member': s_product.get('join_member'),
        'join_way': s_product.get('join_way'),
        'etc_note': s_product.get('etc_note'),
        'spcl_cnd': s_product.get('spcl_cnd'),
        'mtrt_int': s_product.get('mtrt_int'),
        'max_limit': s_product.get('max_limit'),
        'dcls_strt_day': s_product.get('dcls_strt_day'),
        'dcls_end_day': s_product.get('dcls_end_day'),
        # 'join_user' : s_product.get('join_user'),
        # 'like_user' : s_product.get('like_user'),
      }
      
      serializer = SavingsProductsSerializer(data=save_data)
      if serializer.is_valid(raise_exception=True):
        product = serializer.save()
        
    else:
      product = SavingsProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

    for s_option in response['result']['optionList']:  # API
      # for s_option in response2:
      if fin_prdt_cd == s_option['fin_prdt_cd']:
        save_data2 = {
            'fin_prdt_cd': s_option.get('fin_prdt_cd'),               
            'intr_rate_type_nm': s_option.get('intr_rate_type_nm'),  
            'intr_rate': s_option.get('intr_rate'),  
            'intr_rate2': s_option.get('intr_rate2'),
            'save_trm': s_option.get('save_trm'),  
            'rsrv_type_nm': s_option.get('rsrv_type_nm'), 
          }
          # if save_data2['intr_rate'] is None: # API
        if save_data2['intr_rate'] is None:
            # null 값 처리 
          save_data2['intr_rate'] = -1
        if save_data2['intr_rate2'] is None:
            # null 값 처리 
          save_data2['intr_rate2'] = -1
        if save_data2['rsrv_type_nm'] is None:
            # null 값 처리 
          save_data2['rsrv_type_nm'] = -1
        serializer2 = SavingsOptionsSerializer(data=save_data2)
        if serializer2.is_valid(raise_exception=True):
          # 48번째줄에서 저장해둔 product값을 db에 저장할 때, 같이 넘겨준다. 
          serializer2.save(product=product)
            
    # # 상품과 옵션 한 번에 보내기        
    # savings_products_list = []
    # baseList = response['result']['baseList']
    # optionList = response['result']['optionList']
    
    # for product in baseList:
    #   dict_product = {}
    #   dict_product1 = {}
    #   dict_product2 = {}
    #   dict_product3 = {}
    #   intr_rate_type_nm = ''
    #   for option in optionList:
    #     if product['fin_prdt_cd'] == option['fin_prdt_cd']:
    #       if not intr_rate_type_nm:
    #         intr_rate_type_nm = option['intr_rate_type_nm']
    #       if option['rsrv_type_nm'] == '자유적립식':
    #         dict_product[option['save_trm']] = option['intr_rate']
    #         dict_product1[option['save_trm']] = option['intr_rate2']
    #       if option['rsrv_type_nm'] == '정액적립식':
    #         dict_product2[option['save_trm']] =  option['intr_rate']
    #         dict_product3[option['save_trm']] =  option['intr_rate2']
    #   trm = ['6', '12', '24', '36']
    #   for v in trm:
    #       if v not in dict_product.keys():
    #           dict_product[v] = 0
    #       if v not in dict_product1.keys():
    #           dict_product1[v] = 0
    #       if v not in dict_product2.keys():
    #           dict_product2[v] = 0
    #       if v not in dict_product3.keys():
    #           dict_product3[v] = 0

    #   free = {}
    #   fixed = {}
    #   free['intr_rate'] =  dict_product
    #   free['intr_rate2'] = dict_product1
    #   fixed['intr_rate'] =  dict_product2
    #   fixed['intr_rate2'] = dict_product3
    #   product['intr_rate_type_nm'] = intr_rate_type_nm
    #   product['자유적립식'] = free
    #   product['정액적립식'] = fixed
      
    #   savings_products_list.append(product)  
    
    savings_products_list = []
    baseList = response['result']['baseList']
    optionList = response['result']['optionList']

    for product in baseList:
        dict_product = {}
        intr_rate_type_nm = ''
        for option in optionList:
            if product['fin_prdt_cd'] == option['fin_prdt_cd']:
                if not intr_rate_type_nm:
                    intr_rate_type_nm = option['intr_rate_type_nm']
                if option['rsrv_type_nm'] == '자유적립식':
                    if '자유적립식' not in dict_product:
                        dict_product['자유적립식'] = {}
                    dict_product['자유적립식'][option['save_trm']] = {
                        'intr_rate': option.get('intr_rate', 0),
                        'intr_rate2': option.get('intr_rate2', 0)
                    }
                if option['rsrv_type_nm'] == '정액적립식':
                    if '정액적립식' not in dict_product:
                        dict_product['정액적립식'] = {}
                    dict_product['정액적립식'][option['save_trm']] = {
                        'intr_rate': option.get('intr_rate', 0),
                        'intr_rate2': option.get('intr_rate2', 0)
                    }

        trm = ['6', '12', '24', '36']
        for v in trm:
            if '자유적립식' not in dict_product:
                dict_product['자유적립식'] = {}
            if v not in dict_product['자유적립식'].keys():
                dict_product['자유적립식'][v] = {
                    'intr_rate': 0,
                    'intr_rate2': 0
                }
            if '정액적립식' not in dict_product:
                dict_product['정액적립식'] = {}
            if v not in dict_product['정액적립식'].keys():
                dict_product['정액적립식'][v] = {
                    'intr_rate': 0,
                    'intr_rate2': 0
                }

        product['intr_rate_type_nm'] = intr_rate_type_nm
        product.update(dict_product)
        savings_products_list.append(product)


  return Response(savings_products_list) 
  # return JsonResponse({'response' : savings_products_list})



# ----------- 정기 예금, 적금 단일 조회 -----------
  # path('deposit_products/<str:deposit_product_id>/', views.deposit_products_detail),
  # path('savings_products/<str:savings_product_id>/', views.savings_products_detail),

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, BasicAuthentication])
def deposit_products_detail(request, deposit_product_id):
  product = DepositProducts.objects.get(fin_prdt_cd=deposit_product_id)
  serializer = DepositProductsSerializer(product)
  # print(serializer.data)
  return JsonResponse(serializer.data)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication, BasicAuthentication])
def savings_products_detail(request, savings_product_id):
  product = SavingsProducts.objects.get(fin_prdt_cd=savings_product_id)
  serializer = SavingsProductsSerializer(product)
  # print(serializer.data)
  return JsonResponse(serializer.data)

# ----------- 정기 예금, 적금 찜하기 -----------
  # path('deposit_products/<str:deposit_product_id>/like/', views.deposit_products_like),
  # path('savings_products/<str:savings_product_id>/like/', views.savings_products_like),


@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def deposit_products_like(request, deposit_product_id):
  data = False
  product = DepositProducts.objects.get(fin_prdt_cd=deposit_product_id)
  if request.method == 'POST':
    if request.user in product.like_user.all():
      product.like_user.remove(request.user)
      data = False
    else:
      product.like_user.add(request.user)
      data = True
    return Response(data, status=status.HTTP_200_OK)
  elif request.method == 'GET':
    count_dp_like = product.like_user.count()
    return Response({'count': count_dp_like})
  

@api_view(['POST', 'GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def savings_products_like(request, savings_product_id):
  data2 = False
  product = SavingsProducts.objects.get(fin_prdt_cd=savings_product_id)
  if request.method == 'POST':
    if request.user in product.like_user.all():
      product.like_user.remove(request.user)
      data2 = False
    else:
      product.like_user.add(request.user)
      data2 = True
    return Response(data2, status=status.HTTP_200_OK)
  elif request.method == 'GET':
    count_sp_like = product.like_user.count()
    return Response({'count': count_sp_like})


# --------------- 유저가 정기 예금, 적금 찜한 상품 조회 -------------
  # path('liked_products/<str:username>/', views.user_liked_products),

@api_view(['GET'])
def user_liked_products(request, username):
  user = get_object_or_404(User, username=username)
  liked_dp = user.liked_depositproducts.all()
  liked_sp = user.liked_savingsproducts.all()
  serialize_dp = DepositProductsSerializer(liked_dp, many = True)
  serialize_sp = SavingsProductsSerializer(liked_sp, many = True)
  d1 = []
  d2 = []
  for dp_p in serialize_dp.data:
    dp_option = DepositProductOptions.objects.filter(fin_prdt_cd=dp_p['fin_prdt_cd']).values()
    dp_p['optionList'] = list(dp_option)
    d1.append(dp_p)

  for sp_p in serialize_sp.data:
    sp_option = SavingsProductsOptions.objects.filter(fin_prdt_cd=sp_p['fin_prdt_cd']).values()
    sp_p['optionList'] = list(sp_option)
    d2.append(sp_p)

  return Response({
    'liked_depositproducts' : d1,
    'liked_savingsproducts' : d2,
  })

# ----------------- 유저가 찜한 상품 ---------------
  # path('user/liked_deposit_products/', views.user_liked_deposit_products),
  # path('user/liked_savings_products/', views.user_liked_savings_products),

@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def user_liked_deposit_products(request):
  liked_products = request.user.liked_depositproducts.all()
  serializer = DepositProductsSerializer(liked_products, many=True)
    
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def user_liked_savings_products(request):
  liked_products = request.user.liked_savingsproducts.all()
  serializer = SavingsProductsSerializer(liked_products, many=True)
    
  return Response(serializer.data, status=status.HTTP_200_OK)

#  ----------- 정기 예금, 적금 가입하기 -----------
#   path('deposit_products/<str:deposit_product_id>/join/', views.deposit_products_join),
#   path('savings_products/<str:savings_product_id>/join/', views.savings_products_join),

@api_view(['POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def deposit_products_join(request, deposit_product_id):
  product = DepositProducts.objects.get(fin_prdt_cd=deposit_product_id)
  if request.user in product.join_user.all():
    product.join_user.remove(request.user)
  else:
    product.join_user.add(request.user)
  return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def savings_products_join(request, deposit_product_id):
  product = SavingsProducts.objects.get(fin_prdt_cd=deposit_product_id)
  if request.user in product.join_user.all():
    product.join_user.remove(request.user)
  else:
    product.join_user.add(request.user)
  return Response(status=status.HTTP_200_OK)


# ----------------- 유저가 가입한 상품 ---------------
  # path('user/joined_deposit_products/', views.user_joined_deposit_products),
  # path('user/joined_savings_products/', views.user_joined_savings_products),


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def user_joined_deposit_products(request):
  joined_products = request.user.joined_depositproducts.all()
  serializer = DepositProductsSerializer(joined_products, many=True)
    
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def user_joined_savings_products(request):
  joined_products = request.user.joined_savingsproducts.all()
  serializer = SavingsProductsSerializer(joined_products, many=True)
    
  return Response(serializer.data, status=status.HTTP_200_OK)

# --------------- 정기 예금, 적금 댓글 생성 -------------------
  # path('deposit_products/<str:deposit_product_id>/comments/', views.DP_comment_create),
  # path('deposit_products/<str:savings_product_id>/comments/', views.SP_comment_create),
# --------------- 정기 예금, 적금 댓글 조회/수정/삭제 -----------
  # path('deposit_products/<str:deposit_product_id>/comments/<int:comment_pk>', views.DP_comment_controller),
  # path('deposit_products/<str:savings_product_id>/comments/<int:comment_pk>', views.SP_comment_controller),
# ------------------------- DP_Comment --------------------------------

# 생성

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def DP_comment_create(request, deposit_product_id):
  # product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
  product = DepositProducts.objects.get(fin_prdt_cd=deposit_product_id)
  if request.method == 'GET':
    comments = DP_Comment.objects.filter(article=product)
    serializer = DP_CommentSerializer(comments, many=True)
    return Response(serializer.data)
  if request.method == 'POST':
    serializer = DP_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user, article=product)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

#  조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def DP_comment_controller(request, deposit_product_id, comment_id):
    comment = get_object_or_404(DP_Comment, id=comment_id)
    if request.method == 'GET':
        serializer = DP_CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DP_CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# ------------------------- SP_Comment --------------------------------

# 생성
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def SP_comment_create(request, savings_product_id):
  product = SavingsProducts.objects.get(fin_prdt_cd=savings_product_id)
  if request.method == 'GET':
    comments = SP_Comment.objects.filter(article=product)
    serializer = SP_CommentSerializer(comments, many=True)
    return Response(serializer.data)
  if request.method == 'POST':
    serializer = SP_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user,article=product)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


#  조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
def SP_comment_controller(request, savings_product_id, comment_pk): 
    comment = get_object_or_404(SP_Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = SP_CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = SP_CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
