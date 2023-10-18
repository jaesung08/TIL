from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

#  render는 페이지를 만드는 것. redirect는 해당 주소로 다시 요청을 보내는 것.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입
            user = form.save()
            # 로그인 후 리다이렉트
            auth_login(request, user)
            return redirect("shop:index")
    else:
        form =CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)



def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("shop:index")

    else:
        form =AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)



def logout(request):
    auth_logout(request)
    return redirect("shop:index")


from django.db.models import Sum
def profile(request, user_pk):
    user = request.user
    all_price = user.cart.all().aggregate(Sum("price"))
    context={
        "all_price": round(all_price['price__sum'])
    }
    return render(request, "accounts/profile.html",context)

