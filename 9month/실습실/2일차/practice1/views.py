from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if thing in product_price:
        result = product_price[thing]*cnt
    else:
        result = 0
    context = {
        "thing" : thing,
        "cnt" : cnt,
        "result" : result,
    }
    return render(request, "articles/price.html", context)
