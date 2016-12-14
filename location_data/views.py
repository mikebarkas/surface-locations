from django.shortcuts import render

from .models import Location


def state(request):
    data = 'Placeholder page content.'
    return render(request, 'location/state.html', {'data': data})

def city_list(request, state):
    city_list = Location.objects.filter(state=state.upper())
    return render(request, 'location/city_list.html', {'cities': city_list})
