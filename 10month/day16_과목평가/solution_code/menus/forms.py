from django import forms
from .models import Menu, Review


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
    
    def __str__(self):
        return self.name


class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput, label='댓글 :')
    class Meta:
        model = Review
        fields = ['content',]