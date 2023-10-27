from django.db import models
from django.contrib.auth.models import AbstractUser

# # django가 기본적으로 user모델을
# # 왜 덮어써야 하는가?
# # 1. 장고의 권장사항
# # 2. 커스텀 하기 위해서
# class User(AbstractUser):
#     pass
#     # 내가 원하는 추가적인 필드를 사용
    