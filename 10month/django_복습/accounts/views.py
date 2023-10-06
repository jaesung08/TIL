from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required 

# # Create your views here.
# def index(request):

#     return render(request, "articles/index.html")


# 1. 로그인 페이지를 보여줘야 한다. : HTTP GET Method
# 2. 실제 로그인 로직 : HTTP POST Method
# 구분을 뭘로 하는가 ? 
def login(request):
    # 실제 로그인 로직 : POST
    if request.method == 'POST':    
        form = AuthenticationForm(request, request.POST)
        # form 에 담긴 데이터가 유효하다면
        if form.is_valid():
            # 로그인 (세션 데이터 생성)
            auth_login(request, form.get_user())
            # next 데이터가 있을 경우
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            
            return redirect("articles:index")

    
    # 로그인 페이지 : GET
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("articles:index")



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
    request.user.delete()
    # auth_logout(request)
    return redirect('articles:index')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        # form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)



def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # form = PasswordChagneForm(user = request.user, data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context={
        'form' : form,
    }
    return render(request, 'articles/change_password.html', context)


def information(request):
    
    return render(request, "accounts/information.html")