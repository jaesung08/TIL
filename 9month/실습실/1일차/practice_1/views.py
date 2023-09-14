from django.shortcuts import render
from . import data
# Create your views here.
# data.fruit_list

def fruit(request):
    fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
    hate = ["사과","구아바"]
    
    content = {
        "fruit_list" : fruit_list,
        "hate" : hate,
    }
    
    return render(request, "articles/fruit.html", content)