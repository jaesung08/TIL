from django.contrib import admin
from .models import Article
# Register your models here.

# Article 을 등록
admin.site.register(Article)

# CRUD Create, Read, Update, Delete
# 데이터베이스에서 데이터를 처리하는 4가지 기본 작업