from django.shortcuts import render

# Create your views here.

def detail(request,num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail/html', context)

def greeting(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/greeting.html', context)