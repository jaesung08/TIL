from django.shortcuts import render



def food(request):
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    context = {
        "foods" : food,
    }
    return render(request, "articles/food.html", context)


def drink(request):
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    context = {
        "drinks" : drink
    }
    return render(request, "articles/drink.html", context)


def receipt(request):
    total = ["cider","coke","miranda","fanta", "eye of finetree","피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    menu = request.GET.get("order")
    if menu in total:
        context = {
            "order" : menu,
        }
    else:
        context = {
            "order" : "",
            "menu" : menu,
        }
    return render(request, 'articles/receipt.html', context)