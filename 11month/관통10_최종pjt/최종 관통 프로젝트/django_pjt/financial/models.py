from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    RESTRICTION_CHOICES = (
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한')
    )
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField()      # 금융 회사 명
    fin_prdt_nm = models.TextField()    # 금융 상풍명
    etc_note = models.TextField()       # 금융 상품 설명(기타 유의사항)
    join_deny = models.IntegerField(choices=RESTRICTION_CHOICES, default=1)   # 가입제한
    join_member = models.TextField()    # 가입대상
    join_way = models.TextField()       # 가입방법
    spcl_cnd = models.TextField()       # 우대조건
    mtrt_int = models.TextField()       # 만기 후 이자율
    max_limit = models.IntegerField(null=True)   # 최고한도
    

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)  # 외래키(DepositProducts 클래스 참조)
    fin_prdt_cd = models.TextField()                        # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명
    intr_rate =models.FloatField(default= -1)                          # 저축금리
    intr_rate2 = models.FloatField()                        # 최고우대금리
    save_trm = models.IntegerField()                        # 저축기간( 단위: 개월)
    
    
    
    
class SavingProducts(models.Model):
    RESTRICTION_CHOICES = (
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한')
    )
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField()      # 금융 회사 명
    fin_prdt_nm = models.TextField()    # 금융 상풍명
    etc_note = models.TextField()       # 금융 상품 설명(기타 유의사항)
    join_deny = models.IntegerField(choices=RESTRICTION_CHOICES, default=1)   # 가입제한
    join_member = models.TextField()    # 가입대상
    join_way = models.TextField()       # 가입방법
    spcl_cnd = models.TextField()       # 우대조건
    mtrt_int = models.TextField()       # 만기 후 이자율
    max_limit = models.IntegerField(null=True)   # 최고한도

    
class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)  # 외래키(DepositProducts 클래스 참조)
    fin_prdt_cd = models.TextField()                        # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명
    intr_rate =models.FloatField(default= -1)                          # 저축금리
    intr_rate2 = models.FloatField()                        # 최고우대금리
    save_trm = models.IntegerField()                        # 저축기간( 단위: 개월)