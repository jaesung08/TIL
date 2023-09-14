from django.shortcuts import render

def calculation(request):
    return render(request, "articles/calculation.html")


def result(request):
    first_num = request.GET.get("first_num")
    second_num = request.GET.get("second_num")
    multiply  = int(first_num) * int(second_num)
    minous = int(first_num) - int(second_num)
    if second_num != "0":
        divsion = int(first_num)/int(second_num)
    else:
        divsion = 0
    context = {
        'first' : first_num,
        'second' : second_num,
        'multiply' : multiply,
        'minous' : minous,
        'division' : divsion,
    }
    return render(request, "articles/result.html", context)