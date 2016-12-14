from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Location


def state(request):
    data = 'Placeholder page content.'
    return render(request, 'location/state.html', {'data': data})

def city_list(request, state):
    city_data = Location.objects.filter(state=state.upper())
    paginator = Paginator(city_data, 15)
    page = request.GET.get('page')

    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        cities = paginator.page(1)
    except EmptyPage:
        cities = paginator.page(paginator.num_pages)

    return render(request, 'location/city_list.html', {'cities': cities})
