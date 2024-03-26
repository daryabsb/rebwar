
from django import forms
from django.utils.translation import gettext_lazy as _

class XActionForm(forms.Form):
    action = forms.ChoiceField(
        label=_("Action:"),
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
        )
    select_across = forms.BooleanField(
        label="",
        required=False,
        initial=0,
        widget=forms.HiddenInput({"class": "select-across"}),
    )