from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length= 30 , required=False, help_text="필요 시 닉네임을 설정하시오.")
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # field는 기존 field + 닉네임까지 추가
        fields = UserCreationForm.Meta.fields + ('nickname', )

class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(max_length= 30 , required=False, )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'nickname', )