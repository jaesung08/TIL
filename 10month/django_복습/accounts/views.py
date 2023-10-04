from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):

    return render(request, "accounts/index.html")


# 1. 로그인 페이지를 보여줘야 한다. : HTTP GET Method
# 2. 실제 로그인 로직 : HTTP POST Method
# 구분을 뭘로 하는가 ? 
def login(request):
    # 실제 로그인 로직 : POST
    if request.method == 'POST':    
        form = AuthenticationForm(request, request.POST)
        # form 에 담긴 데이터가 유효하다면
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")

    
    # 로그인 페이지 : GET
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("accounts:index")