import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CreateCityForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter the name of the city")

    def clean_renewal_date(self):
        data = self.cleaned_data['name']
        return data
