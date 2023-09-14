from django.shortcuts import render

infos = []

def first(request):
    if request.GET.get("infos"):
        infos.append(request.GET.get("infos"))
        context = {
            'infos' : infos
        }
    else:
        context = {
            "infos": infos
        }
    return render(request, "articles/first.html", context)


def second(request):
    if request.GET.get("infos"):
        infos.append(request.GET.get("infos"))
        context = {
            'infos' : infos
        }
    else:
        context = {
            "infos": infos
        }
    return render(request, "articles/second.html", context)


def third(request):
    if request.GET.get("infos"):
        infos.append(request.GET.get("infos"))
        context = {
            'infos' : infos
        }
    else:
        context = {
            "infos": infos
        }
    return render(request, "articles/third.html", context)

