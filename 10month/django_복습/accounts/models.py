# django 가 사용하는 default User 모델 기반으로 개발을 할거다
# 그래서 상속을 받음
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# 앞으로 필드 수정등의 추가적인 작업을 하기 위해 
# 상속을 받아서 정의
class User(AbstractUser):
    nickname = models.CharField(max_length=50, null=True)
    
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
