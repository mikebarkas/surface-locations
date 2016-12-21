from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from .models import Location
from .forms import StateSelectForm
from .us_states import us_states


def state_select(request):
    if request.method == 'POST':
        form = StateSelectForm(request.POST)
        if form.is_valid():
            return redirect('/state/' + form.cleaned_data['states'].lower())

    else:
        form = StateSelectForm()

    return render(request, 'location/state_select.html', {'form': form})


def city_list(request, state):
    state_name = [(s[0], s[1]) for s in us_states() if s[0] == state.upper()]
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
        'state': state_name[0],
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
