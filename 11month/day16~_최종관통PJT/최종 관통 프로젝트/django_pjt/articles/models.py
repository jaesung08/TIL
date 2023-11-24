from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # 첨부한 사진 media/post_photo에 업로드
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True) # User,
    
    # admin 사이트에서 Post 객체를 title로 표시
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
      return self.comment
  