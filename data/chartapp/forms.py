from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from . models import *

class CountryDataForm(forms.ModelForm):
    class Meta:
        model=CounterData
        fields ='__all__'

