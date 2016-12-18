from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect

from .models import Location
from .forms import StateSelectForm


def state_select(request):
    if request.method == 'POST':
        form = StateSelectForm(request.POST)
        if form.is_valid():
            return redirect('/state/' + form.cleaned_data['states'])

    else:
        form = StateSelectForm()

    return render(request, 'location/state_select.html', {'form': form})


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
