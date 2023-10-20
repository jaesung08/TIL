from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# # model 선택 세가지 방법
# 1. 직접 가져오기 - > 권장 X
# from .models import User
# 2. settings에 설정된 모델 가져오기
# from django.contrib import settings  # model = settings.AUTH_USER_MODEL
# => 문자열 => models.py 에 작성할 때는 문자열로 적는게 좋다
# 3. get_user_model 메서드 활용
# from django.contrib.auth import get_user_model

class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # settings.AUTH_USER_MODEL
        model = get_user_model()
        # fields = '__all__'
        
        # fields = UserCreationForm.Meta.fields
        # Meta안에 넣음으로서 필드 형식 가져오기 