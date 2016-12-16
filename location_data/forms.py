from django import forms

from .us_states import us_states

class state_select_form(forms.Form):
    states = forms.ChoiceField(
        choices = us_states(),
        widget = forms.Select(attrs = {'class':'form-control'})
    )
