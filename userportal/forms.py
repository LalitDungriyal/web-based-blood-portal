from django.forms import ModelForm
from django import forms 
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model=profile
        fields='__all__'
        exclude=['user']
