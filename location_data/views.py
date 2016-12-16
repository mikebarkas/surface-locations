from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Location
from .forms import state_select_form


def state(request):
    if request.method == 'POST':
        form = state_select_form(request.POST)
        if form.is_valid():
          return HttpResponseRedirect('/state/' + form.cleaned_data['states'])
    else:
        return render(request, 'location/state.html', {'form': state_select_form()})


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