from django import forms

from .us_states import us_states


class StateSelectForm(forms.Form):
    states = forms.ChoiceField(
        choices=us_states(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
