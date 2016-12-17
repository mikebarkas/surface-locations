from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'index': 'index'})


def about(request):
    content = 'The page is a Django project used for learning.'
    return render(request, 'basic_pages/about.html', {'context': content})
