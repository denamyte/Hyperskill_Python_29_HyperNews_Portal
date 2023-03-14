from django.shortcuts import render


def coming(request):
    return render(request, 'news/index.html')
