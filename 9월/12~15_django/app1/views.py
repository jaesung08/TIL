from django.shortcuts import render
import random

def index(request):
    context = {
        'name' : 'Jane',
    }
    # 렌더 함수에 세번째 인자는 반드시 딕셔너리이어야한다.
    return render(request, "articles/index.html", context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    # name_data = request.GET.get("query")
    # if name_data:
    #     context = {
    #         "names" : name_data,
    #     }
    #     print(name_data)
    return render(request, "articles/search.html")
    # else:
    #     return render(request, "articles/search.html")

def throw(request):
    return render(request, 'articles/throw.html')

# context에 저장후 catch 템플릿에 출력
def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)