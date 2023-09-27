from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    abc = Article.objects.all()
    content = {
        "articles": abc
    }
    return render(request, "articles/index.html", content)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    form = ArticleForm
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)

# GET방식 : 특정 리소스 조회(보안성 필요X)
# POST방식 : 특정 리소스 변경(보안성 필요)
# => Token 확인 : DB에 조작을 가하는 요청은 반드시 인증 수단 필요

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article(title = title, content = content)
    # article.save()

    
    # return render(request, 'articles/create.html')
    # return redirect('articles:detail', article.pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사 후 유효한 경우만 save
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm()
    # GET방식일 때
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)




def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')



# def edit(request, pk):
#     article = Article.objects.get(pk = pk)
#     form = ArticleForm(instance= article)
#     context = {
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)



def update(request, pk):
    article = Article.objects.get(pk = pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()

    # UPDATE
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance= article,)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # EDIT(GET방식)
    else: 
        form = ArticleForm(instance= article)
    context = {
            'article' : article,
            'form' : form,
    }
    return render(request, 'articles/edit.html', context)


