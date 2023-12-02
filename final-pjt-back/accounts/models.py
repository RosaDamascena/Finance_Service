from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class User(AbstractUser):
    GENDER_CHOICES = (
        ('남성', '남성'),
        ('여성', '여성'),)
    
    INTEREST_CHOICES = (
        ('내집마련', '내집마련'),
        ('재태크', '재태크'),
        ('신혼여행', '신혼여행'),
        ('출산', '출산'),
    )

    BANK_CHOICES = (
        ('우리은행','우리은행'),
        ('한국스탠다드차타드은행','한국스탠다드차타드은행'),
        ('대구은행','대구은행'),
        ('부산은행','부산은행'),
        ('광주은행','광주은행'),
        ('제주은행','제주은행'),
        ('전북은행','전북은행'),
        ('경남은행','경남은행'),
        ('중소기업은행','중소기업은행'),
        ('한국산업은행','한국산업은행'),
        ('국민은행','국민은행'),
        ('신한은행','신한은행'),
        ('농협은행','농협은행'),
        ('하나은행','하나은행'),
        ('수협은행','수협은행'),
        ('카카오뱅크','주식회사 카카오뱅크'),
        ('주식회사 케이뱅크','주식회사 케이뱅크'),
        ('토스뱅크 주식회사','토스뱅크 주식회사'),
        ('기타','기타')
    )    
    # username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    nickname = models.CharField(max_length=254, unique=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    birthday = models.CharField(max_length=8, null=True, blank=True)
    interest = models.CharField(max_length=10, choices=INTEREST_CHOICES)
    married_period = models.IntegerField(null=True, blank=True)
    saving_target_period = models.IntegerField(null=True, blank=True)
    main_bank = models.CharField(max_length=15,choices=BANK_CHOICES)
    
    # 배우자 필드 추가
    couple_nickname = models.CharField(max_length=254, null=True, blank=True)
    couple_birthday = models.CharField(max_length=8, null=True, blank=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "username"
    def __str__(self): 
        return self.username



# 회원가입은 되지만, 데이터가 정상적으로 저장되지 않는 오류를
# 해결하기 위해서 Adapter를 커스터마이징 해야한다.
# 기본적으로 사용하는 DefaultAccountAdapter를 상속받아,
# 우리가 수정이 필요한 save_user 함수만 오버라이딩 하면 쉽게 사용 가능

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        
        data = form.cleaned_data
        # 기존 필드
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")

        # 추가한 필드
    # nickname = models.CharField(max_length=25, unique=True)
    # address = models.CharField(max_length=255, null=True, blank=True, unique=True)
    # gender = models.CharField(max_length=3, choices=GENDER_CHOICES)
    # birthday = models.CharField(max_length=8, null=True, blank=True)
    # interest = models.CharField(max_length=3, choices=INTEREST_CHOICES)
    # married_period = models.IntegerField(null=True, blank=True)
    # saving_target_period = models.IntegerField(null=True, blank=True)
    # main_bank = models.CharField(max_length=10, null=True, blank=True)
    
        nickname = data.get("nickname")
        address = data.get("address")
        gender = data.get("gender")
        birthday = data.get("birthday")
        interest = data.get("interest")
        married_period = data.get("married_period")
        saving_target_period = data.get("saving_target_period")
        main_bank = data.get("main_bank")
        couple_nickname = data.get("couple_nickname")
        couple_birthday = data.get("couple_birthday")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        
        if last_name:
            user_field(user, "last_name", last_name)
        
        # 추가한 필드 
        if nickname:
            user_field(user, "nickname", nickname)
        if address:
            user_field(user, "address", address)
        if gender:
            user_field(user, "gender", gender)
        if birthday:
            user_field(user, "birthday", birthday)
        if interest:
            user_field(user, "interest", interest)

        # Integer필드는 이렇게 해야 함
        if married_period:
            user.married_period = married_period     
        if saving_target_period:
            user.saving_target_period = saving_target_period
        
        if main_bank:
            user_field(user, "main_bank", main_bank)

        if couple_nickname:
            user_field(user, "couple_nickname", couple_nickname)
        if couple_birthday:
            user_field(user, "couple_birthday", couple_birthday)

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user