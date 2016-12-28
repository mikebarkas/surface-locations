from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .models import Location
from .forms import StateSelectForm
from location_data.us_states import state_abbreviation_and_name


class StateSelect(FormView):
    form_class = StateSelectForm
    template_name = 'location/state_select.html'

    def form_valid(self, form):
        return (redirect('/state/' + form.cleaned_data['states'].lower()))


def city_list(request, state):
    city_data = Location.objects.filter(state=state.upper()).order_by('city').distinct('city')

    paginator = Paginator(city_data, 20)
    page = request.GET.get('page')

    try:
        cities = paginator.page(page)
    except PageNotAnInteger:
        cities = paginator.page(1)
    except EmptyPage:
        cities = paginator.page(paginator.num_pages)

    context = {
        'cities': cities,
        'city_count': len(city_data),
        'state': state_abbreviation_and_name(state),
    }

    return render(request, 'location/city_list.html', context)


def city_detail(request, state, city):
    state = state.upper()
    city = city.upper().replace('-', ' ')

    context = {
        'state': state,
        'city': city,
        'city_data': Location.objects.filter(state=state,city=city)
    }

    return render(request, 'location/city_detail.html', context)
