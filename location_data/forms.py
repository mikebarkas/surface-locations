from django import forms

from .us_states import us_states


class StateSelectForm(forms.Form):
    states = forms.ChoiceField(
        choices=us_states(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class CitySearchForm(forms.Form):
    cities = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'city-search'})
    )
