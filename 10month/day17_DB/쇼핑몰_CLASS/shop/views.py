from django.shortcuts import render, redirect
import requests
from .models import Product
# Create your views here.
is_saved = False

def index(request):
    url = 'https://fakestoreapi.com/products'
    response = requests.get(url)
    products = response.json()
    #반복하면서 데이터베이스에 저장
    for product in products:
        # 이미 저장된 상품이면 pass
        if Product.objects.filter(title=product['title']).exists():
            continue
        title = product['title']
        description = product['description']
        price = int(product['price'])*1300
        image = product['image']
        Product.objects.create(
            title=title,
            description=description,
            price=price,
            image=image,
        )
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'shop/index.html', context)


def addcart(request, product_pk):
    product = Product.objects.get(id=product_pk)
    user = request.user
    if user.is_authenticated:
        # 이미 장바구니에 있는 상품이라면, 장바구니에서 제거
        # if product in user.cart.all(): # 밑에 코드가 더 성능이 좋음
        if user.cart.filter(pk=product.pk).exists():
            user.cart.remove(product)
        # 장바구니에 없다면 추가 
        else:
            user.cart.add(product)
        
        return redirect('shop:index')
    else:
        
        return render(request, "accounts/login.html")
    

