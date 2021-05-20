from django.shortcuts import render


def index_view(request):
    return render(request, "pages/index.html", context={})


def docs_view(request):
    return render(request, "pages/docs.html", context={})
