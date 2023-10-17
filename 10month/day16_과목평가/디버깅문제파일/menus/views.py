from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import MenuForm, ReviewForm
from .models import Menu, Review


def index(request):
    menu_list = Menu.objects.all()
    context = {
        'menu_list': menu_list,
    }
    return render(request, 'menus/index.html', context)


# 문제 06. 글 작성을 위한 입력창이 나타나지 않음
# Todo : 화면에 Menu 생성을 위해 사용자 입력 요소들이 나올 수 있도록 수정 필요
@login_required
def create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect('menus:detail', menu.pk)
    else:
        form = MenuForm()

    context = {
        'form': form,
    }
    return render(request, 'menus/create.html')


def detail(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    review_form = ReviewForm()
    context = {
        'menu': menu,
        'review_form': review_form,
        'review_list': menu.review_set.all(),
    }
    return render(request, 'menus/detail.html', context)


@login_required
def edit(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menus:detail', menu_pk)
    else:
        form = MenuForm(instance=menu)

    context = {
        'form': form,
        'menu': menu,
    }
    return render(request, 'menus/edit.html', context)
    

# 문제 07. 댓글 유효성 검사 실패시 모든 댓글이 사라지는 현상
# Todo : 댓글의 유효성 검사가 실패해도, 
#        에러 메세지와 모든 댓글이 보여질 수 있도록 수정 필요
@login_required
def review_create(request, menu_pk):
    if request.method == 'POST':
        menu = Menu.objects.get(pk=menu_pk)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.menu = menu
            review.author = request.user
            review.save()
            return redirect('menus:detail', menu_pk)
    
    context = {
        'menu': menu,
        'review_form': review_form,
    }
    return render(request, 'menus/detail.html', context)


@login_required
def review_delete(request, menu_pk, review_pk):
    if request.method == 'POST':
        review = Review.objects.get(pk=review_pk)
        review.delete()
    return redirect('menus:detail', menu_pk)


# 서술형을 위한 임시 함수이므로 수정하지 마세요.
def menu_recipe(request):
    context = {
        'recipe': 'Top Secret Recipe',
    }
    return render(request, 'menus/recipe.html', context)