from django.urls import path
from . import views

app_name = 'bank_products'
urlpatterns = [
    
# ----------------- 유저가 찜한 상품 ---------------
  path('user/liked_deposit_products/', views.user_liked_deposit_products),
  path('user/liked_savings_products/', views.user_liked_savings_products),
# ----------- 정기 예금, 적금 데이터 저장, 조회 -----------
  path('deposit_products/', views.deposit_products),
  path('savings_products/', views.savings_products),
  

# ----------- 정기 예금, 적금 단일 조회 -----------
  path('deposit_products/<str:deposit_product_id>/', views.deposit_products_detail),
  path('savings_products/<str:savings_product_id>/', views.savings_products_detail),
  
  
# ----------- 정기 예금, 적금 찜하기 -----------
  path('deposit_products/<str:deposit_product_id>/like/', views.deposit_products_like),
  path('savings_products/<str:savings_product_id>/like/', views.savings_products_like),
  
# --------------- 정기 예금, 적금 찜한 상품 조회 -------------
  path('liked_products/<str:username>/', views.user_liked_products),
  
  
# # ------------ 정기 예금, 적금 가입하기 -------------  
#   path('deposit_products/<str:deposit_product_id>/join/', views.deposit_products_join),
#   path('savings_products/<str:savings_product_id>/join/', views.savings_products_join),
# # ----------------- 유저가 가입한 상품 ---------------
#   path('user/joined_deposit_products/', views.user_joined_deposit_products),
#   path('user/joined_savings_products/', views.user_joined_savings_products),  
  
  
# ----------- 정기 예금, 적금 댓글 생성 -----------
  path('deposit_products/<str:deposit_product_id>/comments/', views.DP_comment_create),
  path('savings_products/<str:savings_product_id>/comments/', views.SP_comment_create),
# ----------- 정기 예금, 적금 댓글 조회/수정/삭제 -----------
  path('deposit_products/<str:deposit_product_id>/comments/<int:comment_id>/', views.DP_comment_controller),
  path('savings_products/<str:savings_product_id>/comments/<int:comment_id>/', views.SP_comment_controller),


  
  

  
]

