from django.db import models
from django.conf import settings

# ------------------ 정기 예금(Deposit) --------------------

# 정기 예금 상품 정보
class DepositProducts(models.Model):
  fin_prdt_cd = models.TextField(unique=True)
  fin_co_no = models.TextField()
  kor_co_nm = models.TextField()
  fin_prdt_nm = models.TextField()
  join_deny = models.IntegerField(blank=True, null=True)
  join_member = models.TextField(blank=True, null=True)
  join_way =  models.TextField(blank=True, null=True)
  etc_note = models.TextField(blank=True, null=True)
  spcl_cnd = models.TextField(blank=True, null=True)
  mtrt_int = models.TextField(blank=True, null=True)
  dcls_strt_day = models.IntegerField(blank=True, null=True)
  # 찜한 유저
  like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_depositproducts')
  # # 가입한 유저
  join_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_depositproducts')


# 정기 예금 옵션 정보
class DepositProductOptions(models.Model):
  product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
  fin_prdt_cd = models.TextField()
  intr_rate_type_nm = models.TextField(max_length=100)
  intr_rate = models.FloatField(default=-1,null=True,blank=True)
  intr_rate2 = models.FloatField(default=-1,null=True,blank=True)
  save_trm = models.FloatField()
  
# ------------------ 적금(Savings) --------------------

# 적금 상품 정보
class SavingsProducts(models.Model):
  fin_prdt_cd = models.TextField(unique=True)
  fin_co_no = models.TextField()
  kor_co_nm = models.TextField()
  fin_prdt_nm = models.TextField()
  join_deny = models.IntegerField(blank=True, null=True)
  join_member = models.TextField(blank=True, null=True)
  join_way =  models.TextField(blank=True, null=True)
  etc_note = models.TextField(blank=True, null=True)
  spcl_cnd = models.TextField(blank=True, null=True)
  mtrt_int = models.TextField(blank=True, null=True)
  dcls_strt_day = models.IntegerField(blank=True, null=True)
  # 찜한 유저
  like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_savingsproducts')
  # # 가입한 유저
  join_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_savingsproducts')

# 적금 옵션 정보
class SavingsProductsOptions(models.Model):
  product = models.ForeignKey(SavingsProducts, on_delete=models.CASCADE)
  fin_prdt_cd = models.TextField()
  intr_rate_type_nm = models.TextField(max_length=100)
  intr_rate = models.FloatField(default=-1,null=True,blank=True)
  intr_rate2 = models.FloatField(default=-1,null=True,blank=True)
  save_trm = models.FloatField()
  rsrv_type_nm = models.TextField()


# ---------- 찜하기 기능 ----------

# # 정기 예금 찜하기
# class LikeDepositProducts(models.Model):
#   user_id = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_deposit_products')
#   fin_prdt_cd = models.TextField()
  
#   # 적금 찜하기
# class LikeSavingsProducts(models.Model):
#   user_id = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='liked_savings_products')
#   fin_prdt_cd = models.TextField()
  
  
# ----------------- 댓글 기능 ------------------

# 정기 예금 댓글
class DP_Comment(models.Model):
  article = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
# 적금 댓글
class SP_Comment(models.Model):
  article = models.ForeignKey(SavingsProducts, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
