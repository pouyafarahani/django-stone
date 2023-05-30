from django import forms

from .models import AboutModel


class AboutForms(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = '__all__'
