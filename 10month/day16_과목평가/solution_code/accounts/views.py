from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomUserChangeForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('menus:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# 문제 02. 로그아웃 동작이 정상적으로 되지 않고 에러 발생
# Todo : 정상적으로 로그아웃이 가능하도록 수정 필요
@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('accounts:login')
    return redirect('menus:index')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# 문제 03. 수정할 수 있는 항목의 제한이 필요함
# Todo : 수정할 수 있는 항목은 email, last_name, first_name 만 가능하도록 수정 필요
@login_required
def edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/edit.html', context)


@login_required
def password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('menus:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


# 문제 04. 회원 탈퇴가 정상적으로 되지 않음
# Todo : 정상적인 회원탈퇴가 이루어 지도록 수정 필요
@login_required
def resign(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
        return redirect('accounts:login')
    return redirect('accounts:profile')