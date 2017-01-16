from django.shortcuts import render

from location_data.us_states import us_states


def index(request):
    return render(request, 'index.html', {'index': 'index'})


def about(request):
    context = {
       'content': 'The page is a Django project used for learning.',
       'us_states': us_states()
    }
    return render(request, 'basic_pages/about.html', context)
