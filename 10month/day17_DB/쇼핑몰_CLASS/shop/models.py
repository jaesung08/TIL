from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    # 이미지 URL을 저장
    image = models.URLField()
    # 장바구니 기능을 위한 외래키 설정
    # product : user = N : M
    # related_name : 역참조시 사용할 이름
    # 원래는 Product_set
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cart', blank=True)