from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreation
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인한 사용자가 들어오면 ??
    if request.user.is_authenticated:
        return redirect("boards:index")

    # Method가 GET일때와 POST일때
    # 실제 회원 가입 진행
    if request.method == 'POST':
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            # 저장 및 자동 로그인 
            user = form.save()
            auth_login(request, user)
            return redirect("boards:index")

    # GET: 회원가입 페이지 보여주기    
    else:
        form =CustomUserCreation()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인한 사용자가 들어오면 ??
    if request.user.is_authenticated:
        return redirect("boards:index")

    # Method가 GET일때와 POST일때
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 자동 로그인 
            auth_login(request, form.get_user())
            return redirect("boards:index")

    # GET    
    else:
        form =AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)


# 세션 데이터 삭제하기 => POST 요청
@require_POST
def logout(request):
    # 로그인 된 사용자만 로그아웃
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("boards:index")


def profile(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    # user = request.user
    context = {
        'person' : person
    }
    return render(request, 'accounts/profile.html', context)


# @login_required
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        you = User.objects.get(pk=user_pk)
        me = request.user
        if you != me:
            if you.followers.filter(pk=request.user.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect("accounts:profile", you.pk)
    return redirect("accounts:login")