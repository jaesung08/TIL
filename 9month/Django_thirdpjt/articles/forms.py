# form : 사용자로부터 데이터를 받기위해 활용하는 방법

from django import forms
from .models import Article

# form 과 modelform과의 차이 => DB
# form : DB에 저장 X (로그인)
# ModelForm : DB에 저장 O (게시글, 회원가입)

# # forms
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# modelform
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 모델에 있는 모든 필드를 이 폼에서 사용하겠다.
        fields = '__all__'