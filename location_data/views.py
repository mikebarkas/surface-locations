from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import FormView
from django.http import JsonResponse

from .models import Location
from .forms import StateSelectForm, CitySearchForm
from location_data.us_states import state_abbreviation_and_name


class StateSelect(FormView):
    form_class = StateSelectForm
    template_name = 'location/state_select.html'

    def form_valid(self, form):
        return redirect('/state/' + form.cleaned_data['states'].lower())


class CitySearch(FormView):
    form_class = CitySearchForm
    template_name = 'location/city_search.html'

    def form_valid(self, form):
        city, state = form.cleaned_data['cities'].split(', ')
        return redirect('/state/' + state.lower() + '/' + city.lower().replace(' ', '-'))


def city_list(request, state):
    city_data = get_list_or_404(Location.objects.cities_by_state(state))

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
        'city_data': get_list_or_404(Location.objects.city(state, city)),
    }

    return render(request, 'location/city_detail.html', context)


def api_json(request):
    selected_state = request.GET.get('state', 'fl')
    query_set = Location.objects.filter(state=selected_state.upper()).values('population', 'zipcode')[:20]

    return JsonResponse({'results':  list(query_set)})


def api_city_search(request):
    search_city = request.GET.get('term', 'charlotte')

    query_set = Location.objects.filter(city__icontains=search_city).values('city', 'state').distinct()
    result_list = [city['city'] + ', ' + city['state'] for city in query_set]

    return JsonResponse(result_list, safe=False)
